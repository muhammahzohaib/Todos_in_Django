# Create your models here.
from django.db import models
from django.conf import settings
class Todo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='todos',#We use related_name to access all todos that belong to a user.
        default=1
    )
    title = models.CharField(max_length=512)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
        # ordering = ['-created_at']  # Newest items appear first

    def __str__(self):
        return self.title

