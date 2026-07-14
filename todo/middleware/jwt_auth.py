from django.contrib.auth import get_user_model

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from users.jwt_service import JWTService

User = get_user_model()


class JwtAuthentication(BaseAuthentication):

    keyword = "Bearer" #auth_schema

    def authenticate(self, request):

        access_token = self.extract_token(request)

        if access_token is None:
            raise AuthenticationFailed(
                "Authentication credentials were not provided."
            )

        validated_token = JWTService.validate_token(
            access_token
        )

        authenticated_user = JWTService.get_user(
            validated_token
        )

        # Same responsibility as IsAuthenticated
        if not authenticated_user.is_authenticated:
            raise AuthenticationFailed(
                "User is not authenticated."
            )

        return (
            authenticated_user,
            validated_token
        )

    def extract_token(self, request):

        authorization_header = request.headers.get(
            "Authorization"
        )

        if authorization_header is None:
            raise AuthenticationFailed(
                "Authentication credentials were not provided."
            )

        try:
            keyword, access_token = authorization_header.split()

        except ValueError:
            raise AuthenticationFailed(
                "Invalid Authorization header."
            )

        if keyword != self.keyword:
            raise AuthenticationFailed(
                "Authorization header must start with Bearer."
            )

        return access_token