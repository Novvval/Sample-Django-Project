from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PasswordField(serializers.CharField):

    def __init__(self, **kwargs):
        kwargs["style"] = {"input": "password"}
        kwargs.setdefault("write_only", True)
        super().__init__(**kwargs)
        self.validators.append(validate_password)


class CreateUserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)
    password_repeat = PasswordField(required=True)

    class Meta:
        model = User
        fields = ["id", "password", "password_repeat", "username", "first_name", "last_name"]

    def validate(self, attrs: dict):
        if attrs["password"] != attrs["password_repeat"]:
            raise ValidationError("Password must match")
        return attrs

    def create(self, validated_data: dict):
        del validated_data["password_repeat"]
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)


class LoginSerializer(serializers.ModelSerializer):

    password = PasswordField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["password", "username"]

    def create(self, validated_data: dict):
        if not (user := authenticate(
                username=validated_data["username"],
                password=validated_data["password"]
        )):
            raise AuthenticationFailed
        return user
