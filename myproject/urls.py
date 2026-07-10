
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todo.urls')),  
    path('Auth/', include('users.urls'))
]
