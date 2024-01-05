from .queries import *

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from shared.pikacomms.server import PikaServer, PikaServerLookup

def example(body):
    print("Auth")
    return {"test-response-data": 3}, None, None, body["reply"]  

lookup_new = PikaServerLookup() 
lookup_new.add("create_user", example, None)
server = PikaServer("auth", lookup_new, "AuthServer")
server.startListening()


lookup = {

    "create-user": {
        "func": createUser,
        "groups": ["", "user", "admin", "superuser"],
        "required_fields": [("id", int), ("username", str), ("password", str), ("email", str)]
    },

    "login": {
        "func": login,
        "groups": ["", "user", "admin", "superuser"],
        "required_fields": [("username", str), ("password", str)]
    },

    "delete-user": {
        "func": deleteUser,
        "groups": ["admin", "superuser"],
        "required_fields": [("token_key", str), ("user_id", str)]
    },

    "update-user": {
        "func": updateUser,
        "groups": ["user", "admin", "superuser"],
        "required_fields": [("user_id", int), ("password", str), ("new_password", str)]
    },

    "token-auth": {
        "func": tokenAuthentication,
        "groups": ["", "user", "admin", "superuser"],
        "required_fields": [("token_key", str)]
    },

    "create-token": {
        "func": createToken,
        "groups": ["admin", "superuser"],
        "required_fields": [("user_id", str)]
    },

    "create-groups": {
        "func": createGroups,
        "groups": ["admin", "superuser"],
        "required_fields": [("group_name", str)]
    },

    "delete-groups": {
        "func": deleteGroups,
        "groups": ["admin", "superuser"],
        "required_fields": [("group_name", str)]
    },

    "add-to-group": {
        "func": addToGroup,
        "groups": ["admin", "superuser"],
        "required_fields": [("user_id", str), ("group_name", str)]
    },

    "get-user-group": {
        "func": getUserGroup,
        "groups": ["admin", "superuser"],
        "required_fields": [("user_id", str)]
    },
    
}


# Create your views here.
