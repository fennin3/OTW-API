from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank= True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile_pics/images/')
    institution = models.CharField(max_length=300, blank= True, null=True)
    programme_of_studies = models.CharField(max_length=300, blank= True, null=True)
    level = models.CharField(max_length=20, blank= True, null=True)

