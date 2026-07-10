

from rest_framework.views import APIView # class that allow to build REST API end points, give control on get(), post(), delete(),put() functions
from rest_framework.response import Response # send response 
from rest_framework import status  #showing Http status
from rest_framework.permissions import IsAuthenticated

from .repositories import TodoRepository
from .serializers import TodoSerializer
from .exceptions import MissingPrimaryKeyException

# With Authentication Code: Separates user spaces cleanly 
class TodoAPIView(APIView):
    # This line locks the door. Only requests passing a valid JWT token can come inside this view.
    permission_classes = [IsAuthenticated] # UNCHANGED: To protect endpoints with JWT authentication 
    # 1. READ (List all or Retrieve one)
    def get(self, request, pk=None):  # self is the current object of the class
        if pk is not None:  # if Primary_key is provided in the URL
            # If the ID doesn't exist or isn't owned by this user, Django raises 'DoesNotExist'.
            # Our global project handler intercepts it and safely outputs a clean 404 response. # REMOVED_TRY_EXCEPT
            todo = TodoRepository.get_by_id_and_user(pk, request.user) 
            
            # If found, serialize it and return it
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Any unexpected database drops or OperationalError are caught mid-air globally. # REMOVED_TRY_EXCEPT
        todos = TodoRepository.get_all_by_user(request.user) 
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. CREATE
    def post(self, request):
        serializer = TodoSerializer(data=request.data) #serialize the date , e.g title, datatype present,valid()
        
        # 'raise_exception=True' automatically halts execution and hands 400 Bad Request 
        # validation layout rendering over to our global utils handler if the data is wrong.
        # serializer.is_valid(raise_exception=Truf)
        if not serializer.is_valid():
            return Response({
                "myerror" : serializer.errors,
                "Status Code" : 400
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Pass request.user so the repository can stamp this user's unique ID on the new row.
        new_todo = TodoRepository.create(request.user, serializer.validated_data) 
        output_serializer = TodoSerializer(new_todo) #database returns the newly created Todo object 
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    # 3. UPDATE
    def put(self, request, pk=None):
        if pk is None:
            raise MissingPrimaryKeyException()
            # return Response({"detail": "Method PUT not allowed without ID."}, status=status.HTTP_400_BAD_REQUEST)
            
        # Ownership lookup is verified transparently. DoesNotExist falls back to global 404. # REMOVED_TRY_EXCEPT
        todo = TodoRepository.get_by_id_and_user(pk, request.user) 
            
        serializer = TodoSerializer(data=request.data) #serialize the date , e.g title, datatype present,valid()
        
        # Automatically handles bad data parsing and returns error structure globally. # MODIFIED
        if not serializer.is_valid():
            return Response ({
                "myCustomError"  : serializer.errors,
                "Status Code" : 400
            }, status=status.HTTP_400_BAD_REQUEST)


        
        updated_todo = TodoRepository.update(todo, serializer.validated_data)
        output_serializer = TodoSerializer(updated_todo) # convert to json 
        return Response(output_serializer.data, status=status.HTTP_200_OK)

    # 4. DELETE
    def delete(self, request, pk=None):
        if pk is None:
            raise MissingPrimaryKeyException()
            # return Response({"detail": "Method DELETE not allowed without ID."}, status=status.HTTP_400_BAD_REQUEST)
            
        # Enforces isolation lookup; unauthorized attempts trigger the 404 catch pipeline automatically. # REMOVED_TRY_EXCEPT
        todo = TodoRepository.get_by_id_and_user(pk, request.user) 
            
        TodoRepository.delete(todo)
        return Response(status=status.HTTP_204_NO_CONTENT)
    