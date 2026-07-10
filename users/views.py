from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    RegisterSerializer,
    LoginSerializer
)

from .services import AuthService


class RegisterAPIView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True) # we can generate the custom error

        tokens = AuthService.register_user(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"]
        )

        return Response(
            {
                "message": "Registered successfully.",
                "tokens": tokens
            },
            status=status.HTTP_201_CREATED
        )


class LoginAPIView(APIView):

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        tokens = AuthService.login_user(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"]
        )

        return Response(
            {
                "message": "Logged in successfully.",
                "tokens": tokens
            },
            status=status.HTTP_200_OK
        )