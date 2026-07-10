from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LoginSerializer 
from .repositories import UserRepository
from .exceptions import UsernameAlreadyExistsException, InvalidCredentialsException

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
    
        if not serializer.is_valid():
            return Response({
                "Custom Error ":serializer.errors,
                "Status ": 404

            }, status=status.HTTP_400_BAD_REQUEST)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        

        # Duplicity Check: Instead of returning a manual Response, we raise our custom domain error.
        if UserRepository.exists(username):
            raise UsernameAlreadyExistsException() #Raise Means Throw the Exception error
        
        user = UserRepository.create_user(username=username, password=password)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "Registered successfully!"
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        # Throws bad requests or missing payload elements up to the centralized interceptor.

        if not  serializer.is_valid():
            return Response ({
                "myerror":serializer.errors," status": 401
            },status=status.HTTP_400_BAD_REQUEST)
        # print('Check : ', str(serializer.errors))
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        # Credentials Verification: Fails directly into the core catch pipeline seamlessly.
        user = authenticate(username=username, password=password)
        if not user:
            raise InvalidCredentialsException()

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "Logged in successfully!"
            # "user" : user
        }, status=status.HTTP_200_OK)