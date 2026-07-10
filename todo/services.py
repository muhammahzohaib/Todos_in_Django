# services.py
from .repositories import TodoRepository

class TodoService:

    @classmethod
    def get_todo(cls, pk, user):
        return TodoRepository.get_by_id_and_user(pk, user)

    @classmethod
    def list_todos(cls, user):
        return TodoRepository.get_all_by_user(user)

    @classmethod
    def create_todo(cls, user, validated_data):
        return TodoRepository.create(user, validated_data)

    @classmethod
    def update_todo(cls, pk, user, validated_data):
        todo = TodoRepository.get_by_id_and_user(pk, user)
        return TodoRepository.update(todo, validated_data)

    @classmethod
    def delete_todo(cls, pk, user):
        todo = TodoRepository.get_by_id_and_user(pk, user)
        TodoRepository.delete(todo)