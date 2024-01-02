import pika
import typing
from . import protocol


class PikaServer:
    def __init__(self, _queue : str, _lookup : dict):
        self.queue = _queue
        self.function_lookup = _lookup
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = connection.channel()
        self.channel.queue_declare(queue = self.queue)
        self.channel.basic_qos(prefetch_count = 1)
        self.channel.basic_consume(queue = self.queue, on_message_callback = self.handle)
        

    def startListening(self):
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()
        

    def onInvalidLookup(self):
        print("Invalid request")


    def handle(self, ch, method, props, body):
        body = protocol.parseFromNet(body)
        if body["function"] in self.function_lookup:
            data = self.function_lookup[body["function"]](body)
            response = protocol.parseToNet(data)
            ch.basic_publish(
                exchange='',
                routing_key = props.reply_to,
                properties = pika.BasicProperties(correlation_id = props.correlation_id),
                body = response
            )
            ch.basic_ack(delivery_tag = method.delivery_tag)
        else:
            self.onInvalidLookup()
