import pika
from . import protocol

class PikaClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')


    def call(self, key : str, data : dict) -> dict:  
        self.channel.basic_publish(
            exchange ='',
            routing_key = key, 
            body = protocol.parseToNet(data)
        )
        print(" [x] Sent " + data)
        

    def close(self):
        self.connection.close()