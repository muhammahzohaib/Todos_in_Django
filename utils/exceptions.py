from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import OperationalError


class BaseAPIException(Exception):
    """
    Base exception for all custom application exceptions.
    Every custom exception in the project should inherit from this class.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "A server error occurred."

    def __init__(self, detail=None, status_code=None):
        # Use the provided message, otherwise use the default message.
        self.detail = detail or self.default_detail

        # Allow overriding the default HTTP status code.
        if status_code is not None:
            self.status_code = status_code


def project_exception_handler(exc, context):
    """
    Global exception handler for the entire project.

    Every exception raised inside DRF views reaches this function.
    It converts Python/Django exceptions into standardized API responses.
    """

    # Let DRF handle its built-in exceptions first
    response = exception_handler(exc, context)

    # ------------------------------------------------------------------
    # 1. Handle all custom project exceptions
    # ------------------------------------------------------------------
    if isinstance(exc, BaseAPIException):
        return Response(
            {"detail": exc.detail},
            status=exc.status_code
        )

    # ------------------------------------------------------------------
    # 2. Handle missing database records
    # Example:
    # Todo.objects.get(id=5, user=request.user)
    # raises Todo.DoesNotExist
    # ------------------------------------------------------------------
    if exc.__class__.__name__ == "DoesNotExist":
        return Response(
            {
                "detail": "The requested resource does not exist or access is restricted."
            },
            status=status.HTTP_404_NOT_FOUND
        )

    # ------------------------------------------------------------------
    # 3. Handle database connection failures
    # Example:
    # MySQL/PostgreSQL server is offline.
    # ------------------------------------------------------------------
    if isinstance(exc, OperationalError):
        return Response(
            {
                "detail": "Database infrastructure is currently offline."
            },
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )

    # ------------------------------------------------------------------
    # 4. Format DRF validation errors into a consistent response
    # Example:
    #
    # {
    #     "title": ["This field is required."]
    # }
    #
    # becomes
    #
    # {
    #     "detail": "Validation failed.",
    #     "errors": [
    #         {
    #             "field": "title",
    #             "message": "This field is required."
    #         }
    #     ]
    # }
    # ------------------------------------------------------------------
    if response is not None and response.status_code == status.HTTP_400_BAD_REQUEST:

        formatted_errors = [
            {
                "field": field_name,
                "message": error_message[0]
                if isinstance(error_message, list)
                else error_message
            }
            for field_name, error_message in response.data.items()
        ]

        response.data = {
            "detail": "Validation failed.",
            "errors": formatted_errors
        }

    # ------------------------------------------------------------------
    # 5. Catch every unexpected exception
    # Examples:
    # AttributeError
    # TypeError
    # KeyError
    # NameError
    # ------------------------------------------------------------------
    if response is None:
        return Response(
            {
                "detail": "An unexpected system error occurred."
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response