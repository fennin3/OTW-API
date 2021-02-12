from django.db.models import fields
from stories.models import Story
from django.contrib.auth import get_user_model
from django.db import models
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','username']


class StoriesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Story
        fields = '__all__'
