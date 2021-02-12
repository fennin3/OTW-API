from django.contrib import admin
from .models import WeeklyPost, Rating, PostCategory, WeeklyWinner

admin.site.register(WeeklyPost)
admin.site.register(Rating)
admin.site.register(PostCategory)
admin.site.register(WeeklyWinner)

