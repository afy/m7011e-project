from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate


# Creates a user in the auth_user table and adds the user to the 'user' group in the auth_user_groups table
# Arguments    : Dictionary (Structure can be found in shared/pikacomms/protocol.py)
# Return value : A token key of type string
def createUser(body: dict):
    params = body['params']
    id = params['id']
    username = params['username']
    password = params['password']
    email = params['email']

    user = User.objects.create_user(id=id, username=username, password=password, email=email)
    user.save()

    addToGroup(user_id=id, group_name="user")

    token = Token.objects.create(user_id = id)

    return {"Token":token.key, "Group":"user"}



# Authenticates a user against the user table using username and password
# Arguments    : Dictionary (Structure can be found in shared/pikacomms/protocol.py)
# Return value : A dictionary containing a token key and the group the user belongs to
def login(body: dict):
    params = body['params']
    username = params['username']
    password = params['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        user_id = User.objects.get(username=username).pk
        token = Token.objects.get(user_id=user_id)
        user_group = getUserGroup(user_id=user_id)
        return {"Token":token.key, "Group":user_group}

    else:
        return None
    
# Needs to check that the token used to make the request belongs to an admin or superuser
def deleteUser(user_id):
    pass



# Verifies a token against the token table in the database
# Arguments    : A string containing a token key
# Return value :  True (if token exists in Token table) or raises PermissionDenied error
def tokenAuthentication(token_key):
    try :
        token = Token.objects.get(key=token_key)
        return True
    
    except Token.DoesNotExist:
        raise PermissionDenied({"message: Invalid token"})



# Creates a new group
# Argument : Name of the group
def createGroups(group_name):
    new_group = Group.objects.create(name=group_name)
    new_group.save()




# Adds an existing user to an existing group
# Arguments: 
#    user_id    : user id of an existing user
#    group_name : name of an existing group
def addToGroup(user_id, group_name):
    try:
        user = User.objects.get(id = user_id)
        group = Group.objects.get(name=group_name)

        user.groups.add(group)

    except User.DoesNotExist:
        raise PermissionDenied({"mwssage: Invalid user id"})
    
    except Group.DoesNotExist:
        raise PermissionDenied({"message: Invalid Group"})
    



# Fetches the group the corresponding user belongs to 
# Arguments    : user id of an existing user
# Return value : Returns a string conaining the name of the group the user belongs to or raises an error
def getUserGroup(user_id):
    try: 
        user = User.objects.get(id=user_id)

        user_group = user.groups.get(user=user_id)
        print("User group is : ",user_group)
        return user_group
    
    except User.DoesNotExist:
        raise PermissionDenied({"message : Invalid user id"})
    
    except Group.DoesNotExist:
        raise PermissionDenied({"message : User does not belong to a group"})
    





 # -------------------Tests------------------

def testCreateUser():
    body = {
        "params": {'id':4, 'username':'nagat4', 'password':'thisismypassword', 'email':'testemail4@hotmail.com'},
        "routing-key": "",
        "function": "",
        "reply": {
            "corr-id": "",
            "reply-to": ""
        }
    }
    createUser(body)


def testLogin():
    body = {
        "params": {'id':4, 'username':'nagat4', 'password':'thisismypassword', 'email':'testemail4@hotmail.com'},
        "routing-key": "",
        "function": "",
        "reply": {
            "corr-id": "",
            "reply-to": ""
        }
    }
    login(body)