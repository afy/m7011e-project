import pika#chu
import typing
import time
from collections.abc import Callable
from . import protocol


class CannotCreatePikaServerException(Exception):
    pass


class GenericPikaServerException(Exception):
    pass


class PikaServerLookup:
    def __init__(self):
        self.lookup = {}

    # Add new function to lookup
    def add(self, func_name:str, func_ref:Callable, required_groups:list = None, required_args:list = None):
        self.lookup[func_name] = {"ref": func_ref, "required-groups": required_groups, "required-args": required_args}


    # Check if function exists
    def func_exists(self, func_name: str) -> bool: 
        return func_name in self.lookup
    

    # Check if group requirements are met
    def required_groups_met(self, func_name:str, body:dict) -> bool:
        if not self.func_exists(func_name):
            raise GenericPikaServerException("Function does not exist.")
        if not "required-groups" in self.lookup[func_name]:
            raise GenericPikaServerException("Malformed lookup table; no required groups stored.")
        
        # Verify groups return T/F
        req = self.lookup[func_name]["required-groups"]
        if req == None: return True
        if not "user-validation" in body or body["user-validation"] == None: return False
        if not "groups" in body["user-validation"]: return False 

        for req_group in req:
            if not req_group in body["user-validation"]["groups"]:
                return False
        return True


    # Check if param requirements pass
    def required_args_met(self, func_name:str, params:dict) -> bool:
        if not self.func_exists(func_name):
            raise GenericPikaServerException("Function does not exist.")
        if not "required-args" in self.lookup[func_name]:
            raise GenericPikaServerException("Malformed lookup table; no args stored.")
        
        # Verify args are met; return T/F
        req = self.lookup[func_name]["required-args"]
        if req == None: return True
        for arg in req:
            if not (arg[0] in params and type(params[arg[0]] == arg[1])):
                return False
        return True


    # Return function callabe
    def get_func(self, func_name:str) -> Callable:
        if not self.func_exists(func_name):
            raise GenericPikaServerException("Function does not exist.")
        if not "ref" in self.lookup[func_name]:
            raise GenericPikaServerException("Malformed lookup table; no func stored.")
        return self.lookup[func_name]["ref"]


class PikaServer:
    def __init__(self, _queue:str, _lookup:PikaServerLookup, _name:str="Server"):
        if type(_lookup) != PikaServerLookup:
            raise CannotCreatePikaServerException("Please use lookup of type PikaServerLookup.")

        self.server_name = _name
        self.queue = _queue
        self.lookup = _lookup
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672, heartbeat = 0)
        )
        self.channel = connection.channel()
        self.channel.queue_delete(queue = self.queue) # Clear old queue
        self.channel.queue_declare(queue = self.queue)
        self.channel.basic_qos(prefetch_count = 1)
        self.channel.basic_consume(queue = self.queue, on_message_callback = self.handle)
        self.log("Initialized pikaserver")
        

    def log(self, m:str):
        print(f" [{self.server_name} {time.strftime('%H:%M:%S', time.localtime())}] " + m)


    def startListening(self):
        self.log("Listening..")
        self.channel.start_consuming()


    def handle(self, ch, method, props, body):       
        body = protocol.parseFromNet(body)
        response = None
        if body == None: 
            self.log(f"In message handler: Invalid parsing; skipping message. Full message: {body}")
            response = protocol.parseToError("Invalid parsing")
        
        elif not self.lookup.func_exists(body["function"]):
            self.log(f"In message handler: Function {body['function']} does not exist in lookup.")
            response = protocol.parseToError("Function does not exist")
        
        elif not self.lookup.required_args_met(body["function"], body["params"]):
            self.log(f"In message handler: Required args are not met: {body['params']}")
            response = protocol.parseToError("Required args not met")

        elif not self.lookup.required_groups_met(body["function"], body):
            self.log(f"In message handler: Required groups are not met")
            print("body received in pikaserver : ", body)
            print("function recived in pikaserver: ", body["function"])
            response = protocol.parseToError("Required groups not met")
        
        if response == None:
            try:
                return_value = self.lookup.get_func(body["function"])(body)
                response = protocol.parseToNet({"return": return_value}, "func-return", None, None)
            except Exception as e:
                self.log(f"In message handler: Something went wrong during function call.\n{e}")
                response = protocol.parseToError("Something went wrong during function call")
  
        ch.basic_publish(
                exchange='',
                routing_key = props.reply_to,
                properties = pika.BasicProperties(correlation_id = props.correlation_id),
                body = response
        )
        ch.basic_ack(delivery_tag = method.delivery_tag)