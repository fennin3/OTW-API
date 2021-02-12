from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import PostCategorySerializer, WeeklyPostMainSerializer, WeeklyWinnerSerializer
from rest_framework.response import Response
from .models import PostCategory, WeeklyPost, WeeklyWinner

class PostCategoryListAPIView(APIView):
    def get(self, request):
        postcats = PostCategory.objects.all()
        data = PostCategorySerializer(postcats, many=True).data
        return Response(data)

class PostCategoryRetrieveAPIView(APIView):
    def get(self, request, pk):
        postcat = get_object_or_404(PostCategory,pk=pk)
        data = PostCategorySerializer(postcat).data
        return Response(data)


class WeeklyPostListAPIView(APIView):
    def get(self, request):
        posts = WeeklyPost.objects.all()
        data = WeeklyPostMainSerializer(posts, many=True).data
        return Response(data)

class WeeklyWinnerListAPIView(APIView):
    def get(self, request):
        winners = WeeklyWinner.objects.all()
        data = WeeklyWinnerSerializer(winners , many=True).data
        return Response(data)


