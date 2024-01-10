import binascii
import os

from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate


# Creates a user in the auth_user table and adds the user to the 'user' group in the auth_user_groups table
# Arguments: 
#    id        : nonexisting id
#    username  : username of the user
#    password  : password of the user
#    email     : email of nonexisting user
# Return value : A dictionary containing a token key and the group the user belongs to
def createUser(id, username, password, email):
    user = User.objects.create_user(id=id, username=username, password=password, email=email)
    user.save()

    addToGroup(user_id=id, group_name="user")

    token = Token.objects.create(user_id = id)

    return {"Token":token.key, "Group":"user"}
    


# Authenticates a user against the user table using username and password
# Arguments: 
#    username  : username of an existing user
#    password  : password of an existing user
# Return value : A dictionary containing a token key and the group the user belongs to
def login(username, password):
    user = authenticate(username=username, password=password)

    if user is not None:
        user_id = User.objects.get(username=username).pk
        token = Token.objects.get(user_id=user_id)
        group = getUserGroup(user_id=user_id)
        return {"Token":token.key, "Group":group}

    else:
        return None
    


# Checks the group of the user the token_key belongs to. If group is admin or superuser, deletes user with id=user_id
# Arguments: 
#    token_key : token key of an superuser or admin
#    user_id   : user id of an existing user
def deleteUser(token_key, user_id):
    try:
        token = Token.objects.get(key=token_key)
        user = User.objects.get(username=token.user)

        if user.is_staff == 0 or user.is_superuser == 0:
            raise PermissionDenied({"message : Access level insufficient"})
        
        else: 
            user = User.objects.get(pk=user_id)
            user.delete()

    except Token.DoesNotExist:
        raise PermissionDenied({"message: Invalid token"})
    
    except User.DoesNotExist:
        raise PermissionDenied({"message : Invalid user id"})
    


# Changes password of an existing user
# Arguments:
#    user_id : id of an existing user
#    password : password of the user with id=user_id
#    new_password : new password of the user with id=user_id
def updateUser(user_id, password, new_password):
    try:
        username = User.objects.get(id=user_id).username
        auth = authenticate(username=username, password=password)

        if auth is not None:
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()
        else:
            raise PermissionDenied({"message : User credentials invalid"})

    except User.DoesNotExist:
        raise PermissionDenied({"message : Invalid user id"})



# Verifies a token against the token table in the database
# Arguments    : A string containing a token key
# Return value :  True (if token exists in Token table) or raises PermissionDenied error
def tokenAuthentication(token_key):
    try :
        token = Token.objects.get(key=token_key)
        group = getUserGroup(user_id=token.user_id)
        return {"groups":group}
    
    except Token.DoesNotExist:
        raise PermissionDenied({"message: Invalid token"})
    

# Creates a token for an existing user
# Argument : Name of an existing user
def createToken(user_id):
    token = Token.objects.create(user_id = user_id)
    token.save()


# Note : changes the primary key of the authtoken table
# Genreates a new token key for an existing user with key=token_key
# Argument : token key of an existing user
"""
def updateToken(token_key):
    try:
        new_token = binascii.hexlify(os.urandom(20)).decode()

        Token.objects.filter(key=token_key).update(key=new_token)

    except Token.DoesNotExist:
        raise PermissionDenied({"message : Invalid token"})
"""




# Creates a new group
# Argument : Name of the group
def createGroups(group_name):
    new_group = Group.objects.create(name=group_name)
    new_group.save()


# Deletes an existing group
# Argument : Name of an existing group
def deleteGroups(group_name):
    try:
        group = Group.objects.get(name=group_name)
        group.delete()
    
    except Group.DoesNotExist:
        raise PermissionDenied(["message : Invalid group name"])


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
    
