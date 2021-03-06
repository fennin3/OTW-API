from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

User = get_user_model()

def get_and_authenticate_user(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user


def create_user_account(email,username, password, first_name="",
                        last_name="", **extra_fields):
    user = User.objects.create_user( username =username,
        email=email, password=password, first_name=first_name,
        last_name=last_name, **extra_fields)
    return user