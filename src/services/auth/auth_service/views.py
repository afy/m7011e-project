from .queries import *

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from shared.pikacomms.server import PikaServer, PikaServerLookup

lookup = PikaServerLookup() 

# User table CRUD
lookup.add("create-user", createUser, ['', 'user', 'admin', 'superuser'], 
           [('id', int), ('username', str), ('password', str), ('email', str)])

lookup.add("update-user", updateUser, ['user', 'admin', 'superuser'], 
           [('user_id', int), ('password', str), ('new_password', str)])

lookup.add("delete-user", deleteUser, ['admin', 'superuser'],
           [('token_key', str), ('user_id', str)])
# Read


# Other
lookup.add("login", login, ['', 'user', 'admin', 'superuser'], 
           [('username', str), ('password', str)])

lookup.add("token-auth", tokenAuthentication, ['', 'user', 'admin', 'superuser'], 
           [('token_key', str)])

lookup.add("create-token", createToken, ['admin', 'superuser'], 
           [('user_id', str)])

lookup.add("create-groups", createGroups, ['admin', 'superuser'], 
           [('group_name', str)])

lookup.add("delete-groups", deleteGroups, ['admin', 'superuser'], 
           [('group_name', str)])

lookup.add("add-to-group", addToGroup, ['admin', 'superuser'],
           [('user_id', str), ('group_name', str)])


server = PikaServer("auth", lookup, "Authorization Server")
server.startListening()


lookup_OLD = {

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