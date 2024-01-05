import pika
import time
import warnings
import uuid
from . import protocol

class PikaClient:
    def __init__(self, name="Client", log_params = False ):
        self.client_name = name
        self.log_params = log_params
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None


    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body


    def call(self, key: str, func: str, params: dict, reply=protocol.NO_REPLY) -> None:  
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key=key,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=protocol.parseToNet(params, key, func, reply))
        self.connection.process_data_events(time_limit=None)

        log_msg = f"Sent func {func} with {params} to " if self.log_params else "Sent data to "
        log_msg += f"{key}"
        self.log(log_msg)
        
        return {"a":protocol.parseFromNet(self.response)}



    def log(self, m: str):
        print(f" [{self.client_name} {time.strftime('%H:%M:%S', time.localtime())}] " + m)
        
        
    def close(self):
        warnings.warn("Connection has been closed manually")
        self.connection.close()