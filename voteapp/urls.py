from django.urls import path
from . import views

urlpatterns = [
    path('postcategories/', views.PostCategoryListAPIView.as_view(), name="postcats"),
    path('postcategories/<int:pk>/', views.PostCategoryRetrieveAPIView.as_view(), name="postcat_detail"),
    path('weeklypost/', views.WeeklyPostListAPIView.as_view(), name="weeklyposts"),
    path('weeklywinners/', views.WeeklyWinnerListAPIView.as_view(), name="weeklywinners"),
]