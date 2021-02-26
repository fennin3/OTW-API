from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import PostCategorySerializer, WeeklyPostMainSerializer, WeeklyWinnerSerializer
from rest_framework.response import Response
from .models import PostCategory, WeeklyPost, WeeklyWinner
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class PostCategoryListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_class = JSONWebTokenAuthentication
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all()


class PostCategoryRetrieveAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    def get(self, request, pk):
        postcat = get_object_or_404(PostCategory,pk=pk)
        data = PostCategorySerializer(postcat).data
        return Response(data)


class WeeklyPostListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = WeeklyPostMainSerializer
    queryset = WeeklyPost.objects.all()

class WeeklyWinnerListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    def get(self, request):
        winners = WeeklyWinner.objects.all()
        data = WeeklyWinnerSerializer(winners , many=True).data
        return Response(data)



