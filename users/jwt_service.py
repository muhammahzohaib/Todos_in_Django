from rest_framework_simplejwt.tokens import (
    AccessToken,
    RefreshToken
)
from rest_framework_simplejwt.authentication import JWTAuthentication

from .exceptions import InvalidTokenException


class JWTService:

    @staticmethod
    def generate_tokens(user):

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    @staticmethod
    def validate_token(raw_token):

        try:
            return AccessToken(raw_token)

        except Exception:
            raise InvalidTokenException("Access token has expired. Please login again.")
        

    @staticmethod
    def decode_token(validated_token):

        return dict(validated_token)

    @staticmethod
    def get_user(validated_token):

        jwt_authentication = JWTAuthentication()

        return jwt_authentication.get_user(
            validated_token
        )