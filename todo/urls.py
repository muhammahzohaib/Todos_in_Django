# from django.urls import path
# from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView

# urlpatterns = [
#     path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
#     path('todos/<int:pk>/', TodoRetrieveUpdateDestroyView.as_view(), name='todo-detail'),
# ]



from django.urls import path
from .views import TodoAPIView

urlpatterns = [
    # Maps to GET (List) and POST (Create)
    path('', TodoAPIView.as_view(), name='todo-list-create'),
    
    # Maps to GET (Retrieve), PUT (Update), and DELETE (Destroy) by routing the <int:pk>
    path('todos/<int:pk>/', TodoAPIView.as_view(), name='todo-detail'),
]