from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import OperationalError

class BaseAPIException(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "A server error occurred."

    def __init__(self, detail=None, status_code=None):
        self.detail = detail or self.default_detail
        if status_code is not None:
            self.status_code = status_code

def project_exception_handler(exc, context):
    """The master catch-net for the whole project."""
    response = exception_handler(exc, context)

    # 1. Catch our app-specific custom exceptions
    if isinstance(exc, BaseAPIException):
        return Response({"detail": exc.detail}, status=exc.status_code)

    # 2. Catch Django Object Lookups (DoesNotExist) globally
    if exc.__class__.__name__ == 'DoesNotExist':
        return Response(
            {"detail": "The requested item does not exist or access is restricted."},
            status=status.HTTP_404_NOT_FOUND
        )

    # 3. Catch Database Failures (MySQL down)
    if isinstance(exc, OperationalError):
        return Response(
            {"detail": "Database infrastructure is currently offline."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )

    # 4. Standardize validation responses (Bad Requests)
    if response is not None and response.status_code == status.HTTP_400_BAD_REQUEST:
        custom_errors = [
            {"field": field, "message": msg[0] if isinstance(msg, list) else msg}
            for field, msg in response.data.items()
        ]
        response.data = {"detail": "Validation failed.", "errors": custom_errors}

    # 5. Ultimate Fallback Safeguard
    if response is None:
        return Response(
            {"detail": "An unexpected system error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response