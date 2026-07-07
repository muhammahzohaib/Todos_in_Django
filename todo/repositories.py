from .models import Todo

class TodoRepository:
    @staticmethod
    def get_all():
        return Todo.objects.all()

    @staticmethod
    def get_by_id(todo_id):
        try:
            return Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return None

    @staticmethod
    def create(data):
        return Todo.objects.create(
            title=data['title'],
            completed=data.get('completed', False)
        )

    @staticmethod
    def update(todo_instance, data):
        todo_instance.title = data.get('title', todo_instance.title)
        todo_instance.completed = data.get('completed', todo_instance.completed)
        todo_instance.save()
        return todo_instance

    @staticmethod
    def delete(todo_instance):
        todo_instance.delete()