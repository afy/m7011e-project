import pika
import protocol

class PikaClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')


    def send(self, key, data):  
        self.channel.basic_publish(
            exchange ='',
            routing_key = key, 
            body = protocol.parseToNet(data)
        )
        
        print(" [x] Sent " + data)
        

    def close(self):
        self.connection.close()