from .models import Todo

class TodoRepository:
    @staticmethod
    def get_all_by_user(user_instance):
        return Todo.objects.filter(user=user_instance)

    @staticmethod
    def get_by_id_and_user(todo_id, user_instance):
        return Todo.objects.get(id=todo_id, user=user_instance)

    @staticmethod
    def create(user_instance, validated_data):
        return Todo.objects.create(user=user_instance, **validated_data)

    @staticmethod
    def update(todo_instance, validated_data):
        for attr, value in validated_data.items():
            setattr(todo_instance, attr, value)
        todo_instance.save()
        return todo_instance

    @staticmethod
    def delete(todo_instance):
        todo_instance.delete()