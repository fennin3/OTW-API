from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Story(models.Model):
    video = models.FileField(upload_to="stories/")
    date_time_uploaded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")