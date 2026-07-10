# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoSerializer
from .exceptions import MissingPrimaryKeyException
from .services import TodoService

class TodoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # 1. READ (List all or Retrieve one
    def get(self, request, pk=None):
        if pk is not None:
            todo = TodoService.get_todo(pk, request.user)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        todos = TodoService.list_todos(request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. CREATE
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        new_todo = TodoService.create_todo(request.user, serializer.validated_data)
    
        return Response(TodoSerializer(new_todo).data, status=status.HTTP_201_CREATED)

    # 3. UPDATE
    def put(self, request, pk=None):
        if pk is None:
            raise MissingPrimaryKeyException()
            
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        updated_todo = TodoService.update_todo(pk, request.user, serializer.validated_data)
        return Response(TodoSerializer(updated_todo).data, status=status.HTTP_200_OK)

    # 4. DELETE
    def delete(self, request, pk=None):
        if pk is None:
            raise MissingPrimaryKeyException()
            
        TodoService.delete_todo(pk, request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)