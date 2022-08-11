from user.models import Customer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError


class CustomerRegister(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user1 = User.objects.create(**validated_data)
        user1.set_password(password)
        user1.save()
        return user1


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get(
                'request'), username=username, password=password)
            if not user:
                raise serializers.ValidationError(
                    "Unable to Login with provided credentials", code='authorization')
        else:
            raise serializers.ValidationError(
                'Must include "username" and "password".', code='authorization')

        data['user'] = user
        return data
