from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializers):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_ name', 'email', 'password', 'city']