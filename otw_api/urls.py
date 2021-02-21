"""otw_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from stories.models import User
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from users.views import UserLoginView
# from rest_framework_simplejwt import views as jwt_views

schema_view = get_swagger_view(title="OTW API Documentation")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('api/userprofile/', include('user_profile.urls')),
    path('api/login/', UserLoginView.as_view(),name="login_"),
    path('api/voteapp/', include('voteapp.urls')),
    path('api/stories/',include('stories.urls')),
    path('api/documentation/', schema_view),

    # JWT URLS
    # path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)