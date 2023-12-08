from django.shortcuts import render
from .server import PikaServer
from .queries import test_login

test_login()
#test_create_user()

#lookup = {function: 'create_blabla'}
#pika_server = PikaServer(_lookup = lookup)

# Create your views here.
