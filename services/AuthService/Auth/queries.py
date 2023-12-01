from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def create_user(body: dict):
    params = body['params']
    id = params['id']
    username = params['username']
    password = params['password']
    email = params['email']

    user = User.objects.create_user(id=id, username=username, password=password, email=email)
    user.save()

    token = Token.objects.create(user_id = id)

    return token.key


def test_create_user():
    body = {
        "params": {'id':4, 'username':'nagat4', 'password':'thisismypassword', 'email':'testemail4@hotmail.com'},
        "routing-key": "",
        "function": "",
        "reply": {
            "corr-id": "",
            "reply-to": ""
        }
    }
    create_user(body)


def login(body: dict):
    params = body['params']
    username = params['username']
    password = params['password']
    user = authenticate(username=username, password=password)
    # token = Token.objects.get(username=username)
    if user is not None:
        print(user)
        return "Authenticated"
    else:
        print("None")
        return None