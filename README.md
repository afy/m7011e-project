# M7011E Design of Dynamic Web Systems - Project
This repo contains our work on a microservice-based django web server + web client. The project itself is a typical e-shop platform, with support for orders, cart management, role-based access, and more. The base project is provided in the `webserver` folder, where `.../eshop/` is the independent web client and `.../apigate/` provides the API gateway. <br/>
<br/>

The services can be found as separate django projects in the `services/` folder. All additional project documentation is provided in the documentation folder `doc/`.

## Stack
- Web server + microservices: Django w. REST framework
- RabbitMQ library: Pika
- Frontend: Basic HTML/CSS/JS

<br/>

Pip requirements can be found in the `config/requirements.txt` file.

## Running project
A full documentation on deployment will be provided in the documentation folder.

# Authors
- Klas Norling, `https://github.com/Klas-Norling`
- Warsay Maharena, `https://github.com/WarsayMaharena`
- Hannes Furhoff, `https://github.com/afy`