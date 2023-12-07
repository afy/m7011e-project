# Deprecated; delete files

import pika
import json


class ApiGatewayServer:
    def __init__(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='rpc_queue')
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='rpc_queue', on_message_callback=self.on_request)

        print(" [x] Awaiting RPC requests")
        channel.start_consuming()

    def get_product_price(self, name):
        return 15

    def on_request(self, ch, method, props, body):
        n = str(body)

        print(f" [.] fib({n}) loop")
        response = {'price': self.get_product_price(n), 'category': 'PANTS', 'lista':[1,2,3,'dsdsadsa']}

        ch.basic_publish(exchange='',
                        routing_key=props.reply_to,
                        properties=pika.BasicProperties(correlation_id = \
                                                            props.correlation_id),
                        body=json.dumps(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)

