from django.urls.exceptions import NoReverseMatch
from stories.views import StoriesCreateListView, retriev_user_stories
from django.urls import path

urlpatterns = [
    path('create_or_list/', StoriesCreateListView.as_view(), name='create_list_story'),
    path('my_stories/<int:id>', retriev_user_stories, name="my_stories")
]
