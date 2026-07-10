from utils.exceptions import BaseAPIException
from rest_framework import status

class UsernameAlreadyExistsException(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "A user with that username already exists."

class InvalidCredentialsException(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Invalid username or password."