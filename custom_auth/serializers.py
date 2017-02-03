from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomSystemUser

class UserCatSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = User
        fields = ( 'username', 'id', )
        
class CustomSystemUserSerializer( serializers.ModelSerializer ) :
    user = UserCatSerializer( many = False )
    class Meta :
        model = CustomSystemUser
        fields = ( 'id', 'user', )