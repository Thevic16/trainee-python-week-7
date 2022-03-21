from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from account.api.permissions import AnonPermissionOnly
from account.api.serializers import UserRegisterSerializer
from account.models import MyUser

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class AuthAPIView(APIView):
    permission_classes = [AnonPermissionOnly]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'},
                            status=400)
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = jwt_response_payload_handler(token, user, request=request)
        return Response(response)


class RegisterAPIView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonPermissionOnly]
