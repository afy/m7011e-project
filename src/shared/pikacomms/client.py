import pika
import time
import warnings
from . import protocol

class PikaClient:
    def __init__(self, name="Client", log_params = False):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')
        self.client_name = name
        self.log_params = log_params


    def call(self, key: str, func: str, params: dict, reply=protocol.NO_REPLY) -> None:  
        self.channel.basic_publish(
            exchange ='',
            routing_key = key, 
            body = protocol.parseToNet(params, key, func, reply)
        )
        log_msg = f"Sent func {func} with {params} to " if self.log_info else "Sent data to "
        log_msg += f"{key}"
        self.log(log_msg)


    def log(self, m: str):
        print(f" [{self.client_name} {time.strftime('%H:%M:%S', time.localtime())}] " + m)
        
        
    def close(self):
        warnings.warn("Connection has been closed manually")
        self.connection.close()