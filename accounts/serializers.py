import random

from django.contrib.auth import authenticate
from rest_framework import serializers as srz

from accounts.models import User


class LoginSerializer(srz.Serializer):
    username = srz.CharField()
    password = srz.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise srz.ValidationError("Incorrect Credentials")


class RegisterSerializer(srz.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        otp = random.randint(10000000, 99999999)
        user = User.objects.create_user(
            name=validated_data["email"],
            username=validated_data["email"],
            otp=otp,
            email=validated_data["email"],
            password=validated_data["email"],
        )

        return user


class UserSerializer(srz.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email", "username")


class VerifyEmailSerializer(srz.Serializer):
    email = srz.EmailField()
    otp = srz.CharField()
