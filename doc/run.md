# Dirinfo
Run all listed commands from m7011e-project/

# Start RabbitMQ
RUN `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management`

# Start main server / apigate
RUN `python src/webserver/manage.py runserver`

# Start auth service
RUN `python src/services/auth/manage.py runserver`

# Start product service
RUN `python src/services/ProductService/manage.py runserver`