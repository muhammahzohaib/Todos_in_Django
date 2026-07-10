from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #AbstractUser = A ready-made User model that already has username, email, password, first_name, last_name, etc.
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'auth_users'

    def __str__(self):
        return self.username