from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from account.api.views import AuthAPIView, RegisterAPIView

urlpatterns = [
    # Api authentication view
    path('auth/', AuthAPIView.as_view()),
    # Api register
    path('register/', RegisterAPIView.as_view()),
    # Api obtain token
    path('auth/jwt/', obtain_jwt_token),
    # Api refresh token
    path('auth/jwt/refresh/', refresh_jwt_token),
]
