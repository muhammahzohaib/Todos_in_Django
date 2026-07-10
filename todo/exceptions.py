from utils.exceptions import BaseAPIException
from rest_framework import status

# class WorkspaceLimitExceededException(BaseAPIException):
#     status_code = status.HTTP_400_BAD_REQUEST
#     default_detail = "Free tier limit reached. You cannot create more than 20 tasks."

# class TaskDeadlinePastException(BaseAPIException):
#     status_code = status.HTTP_400_BAD_REQUEST


#     default_detail = "Cannot set or update a task deadline to a past date."




class MissingPrimaryKeyException(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Method not allowed without ID."