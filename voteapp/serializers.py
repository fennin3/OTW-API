from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Rating, WeeklyPost, PostCategory, WeeklyWinner
from user_profile.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

# For General Use

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude =['user']


class UserSerializers(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','first_name','last_name', 'profile']

class WeeklyPostSerializer(serializers.ModelSerializer):
    person =UserSerializers(read_only=True)
    class Meta:
        model = WeeklyPost
        fields = '__all__'

class PostCategorySSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'



# For Post Category



class PostCategorySerializer(serializers.ModelSerializer):
    weekly_posts = WeeklyPostSerializer(many=True, read_only=True)
    class Meta:
        model = PostCategory
        fields = '__all__'




# For Weekly Post


class WeeklyPostMainSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    category = PostCategorySSerializer(read_only=True)
    person = UserSerializers(read_only=True)
    class Meta:
        model = WeeklyPost
        fields = '__all__'



# For WeeklyWinner
class WeeklyPostFWSerializer(serializers.ModelSerializer):
    person =UserSerializers(read_only=True)
    category = PostCategorySSerializer(read_only=True)
    class Meta:
        model = WeeklyPost
        fields = '__all__'

class WeeklyWinnerSerializer(serializers.ModelSerializer):
    post = WeeklyPostFWSerializer(read_only=True)
    class Meta:
        model = WeeklyWinner
        fields = '__all__'
