from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import OperationalError

class BaseAPIException(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "A server error occurred."

    def __init__(self, detail=None, status_code=None): # Constructor
        self.detail = detail or self.default_detail
        if status_code is not None:
            self.status_code = status_code

def project_exception_handler(exc, context):  #This function catches every exception from every API
    response = exception_handler(exc, context) #if normal exceptions
# context contains information about where the exception happened.  like TodoAPIView.
    # 1. Handle our custom App-Specific exceptions cleanly  
    if isinstance(exc, BaseAPIException): #is this exception of a child BaseAPIException   
        return Response({"detail": exc.detail}, status=exc.status_code)

    # 2. Convert standard Django Object Lookups globally to custom 404
    if exc.__class__.__name__ == 'DoesNotExist':   # query to 1, But Todo 1 belongs to Ali, not Zohaib.
        return Response(
            {"detail": "The requested resource does not exist or access is restricted."},
            status=status.HTTP_404_NOT_FOUND
        )

    # 3. Handle System/Database Crashes
    if isinstance(exc, OperationalError):
        return Response(
            {"detail": "Database infrastructure is currently offline."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )

    # 4. Standardize DRF validation messages (Bad Requests)
    if response is not None and response.status_code == status.HTTP_400_BAD_REQUEST:  
        custom_errors = [
            {
                "field": field, # title or complete 
                "message": msg[0] 
                if isinstance(msg, list)
                 else msg
                 
            }
            for field, msg in response.data.items()
        ]
        response.data = {"detail": "Validation failed.", "errors": custom_errors}

    # 5. Global Unhandled Python/Django Fallback
    if response is None:
        return Response(
            {"detail": "An unexpected system error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response