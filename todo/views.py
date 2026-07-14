from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .middleware.jwt_auth import JwtAuthentication

from .serializers import TodoSerializer
from .exceptions import MissingPrimaryKeyException
from .services import TodoService


class TodoAPIView(APIView):
    authentication_classes = [JwtAuthentication] 
    # permission_classes = [IsAuthenticated]

    # 1. READ (List All or Retrieve One)
    def get(self, request, todo_id=None):

        if todo_id is not None:
            todo_record = TodoService.get_todo(
                todo_id,
                request.user
            )

            response_serializer = TodoSerializer(todo_record)

            return Response(
                response_serializer.data, #  pass  object 
                status=status.HTTP_200_OK
            )

        todo_records = TodoService.list_todos(request.user)

        response_serializer = TodoSerializer(
            todo_records,
            many=True
        )

        return Response(
            response_serializer.data,
            status=status.HTTP_200_OK
        )

    # 2. CREATE
    def post(self, request):

        request_serializer = TodoSerializer(
            data=request.data
        )

        request_serializer.is_valid(
            raise_exception=True
        )

        created_todo = TodoService.create_todo(
            request.user,
            request_serializer.validated_data
        )

        response_serializer = TodoSerializer(
            created_todo
        )

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )

    # 3. UPDATE
    def put(self, request, todo_id=None):

        if todo_id is None:
            raise MissingPrimaryKeyException()

        request_serializer = TodoSerializer(
            data=request.data
        )

        request_serializer.is_valid(
            raise_exception=True
        )

        updated_todo = TodoService.update_todo(
            todo_id,
            request.user,
            request_serializer.validated_data
        )

        response_serializer = TodoSerializer(
            updated_todo
        )

        return Response(
            response_serializer.data,
            status=status.HTTP_200_OK
        )

    # 4. DELETE
    def delete(self, request, todo_id=None):

        if todo_id is None:
            raise MissingPrimaryKeyException()

        TodoService.delete_todo(
            todo_id,
            request.user
        )

        return Response(
            {
                "Todo": "Delete Successfully"
            } ,  status=status.HTTP_204_NO_CONTENT
        )