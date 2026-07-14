from .repositories import TodoRepository


class TodoService:

    @staticmethod
    def get_todo(todo_id, current_user):
        return TodoRepository.get_by_id_and_user( todo_id, current_user )

    @staticmethod
    def list_todos(current_user):
        return TodoRepository.get_all_by_user(current_user)

    @staticmethod
    def create_todo(current_user, todo_payload):
        return TodoRepository.create(current_user,todo_payload)

    @staticmethod
    def update_todo(todo_id, current_user, updated_data):
        todo_record = TodoRepository.get_by_id_and_user(todo_id, current_user
        )

        return TodoRepository.update(todo_record, updated_data )

    @staticmethod
    def delete_todo(todo_id, current_user):
        todo_record = TodoRepository.get_by_id_and_user(todo_id,  current_user )

        TodoRepository.delete(todo_record)