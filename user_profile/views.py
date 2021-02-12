from django.shortcuts import render
from .serializers import UserProfileSerializer, UserSerializer

from rest_framework import generics
from .models import UserProfile


class UserProfileRetrieveAndUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    