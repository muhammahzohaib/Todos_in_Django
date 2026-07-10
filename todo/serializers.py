from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:  #it is responsible for the Which data table(model) is  responsible for converting the JSON response / save time / Control 
        model = Todo
        fields = ['id', 'title', 'completed', 'created_at', 'updated_at','user_id']  # or use thr "__all__" for all thr datatype
        read_only_fields = ['id', 'created_at', 'updated_at', 'user_id']


