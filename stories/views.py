from stories.serializers import StoriesSerializer
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from .models import Story
from rest_framework.response import Response


class StoriesCreateListView(ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoriesSerializer

@api_view(['GET'])
def retriev_user_stories(request, id):
    user_stories = Story.objects.filter(user__id=id)
    data = StoriesSerializer(user_stories,many=True).data
    return Response({"my_stories":data})
