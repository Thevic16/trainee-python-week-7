from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from account.api.views import AuthView

urlpatterns = [
    # Api obtain token
    path('auth/jwt/', obtain_jwt_token),
    # Api refresh token
    path('auth/jwt/refresh/', refresh_jwt_token),
    # Api view
    path('', AuthView.as_view()),
]
