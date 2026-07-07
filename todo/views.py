# from rest_framework import generics
# from .models import Todo
# from .serializers import TodoSerializer

# # Handles: GET /todos/ and POST /todos/
# class TodoListCreateView(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

# # Handles: GET /todos/:id/, PUT /todos/:id/, and DELETE /todos/:id/
# class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .repositories import TodoRepository
from .serializers import TodoSerializer

class TodoAPIView(APIView):
    
    # 1. READ (List all or Retrieve one)
    def get(self, request, pk=None):
        if pk is not None: # if Primary_key Not Zero  
            todo = TodoRepository.get_by_id(pk)  #
            if not todo:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        todos = TodoRepository.get_all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. CREATE
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            new_todo = TodoRepository.create(serializer.validated_data)
            output_serializer = TodoSerializer(new_todo)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. UPDATE
    def put(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method PUT not allowed without ID."}, status=status.HTTP_400_BAD_REQUEST)
            
        todo = TodoRepository.get_by_id(pk)
        if not todo:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            updated_todo = TodoRepository.update(todo, serializer.validated_data)
            output_serializer = TodoSerializer(updated_todo)
            return Response(output_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 4. DELETE
    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method DELETE not allowed without ID."}, status=status.HTTP_400_BAD_REQUEST)
            
        todo = TodoRepository.get_by_id(pk)
        if not todo:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            
        TodoRepository.delete(todo)
        return Response(status=status.HTTP_204_NO_CONTENT)

