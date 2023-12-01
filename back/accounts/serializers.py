from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 
            'username', 
            'email', 
            'deposit_option_list',
            'saving_option_list', 
            'nick_name', 
            'age',
            'money',
            'salary']
        read_only_fields = ('username',)
        