from django.contrib.auth import authenticate

from .repositories import UserRepository
from .jwt_service import JWTService
from .exceptions import (
    UsernameAlreadyExistsException,
    InvalidCredentialsException
)


class AuthService:

    @staticmethod
    def register_user(username, password):

        if UserRepository.exists(username):
            raise UsernameAlreadyExistsException()

        user = UserRepository.create_user(
            username=username,
            password=password
        )

        return JWTService.generate_tokens(user)

    @staticmethod
    def login_user(username, password):

        user = authenticate(
            username=username,
            password=password
        )

        if not user:
            raise InvalidCredentialsException()

        return JWTService.generate_tokens(user)