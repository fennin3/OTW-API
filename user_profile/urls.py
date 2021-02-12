from django.urls import path
from .views import UserProfileRetrieveAndUpdateView


urlpatterns = [
    path('<int:pk>/', UserProfileRetrieveAndUpdateView.as_view(), name='user_profile')
]