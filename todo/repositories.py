from .models import Todo


class TodoRepository:

    @staticmethod
    def get_all_by_user(current_user):
        return Todo.objects.filter(user=current_user)

    @staticmethod
    def get_by_id_and_user(todo_id, current_user):
        return Todo.objects.get(
            id=todo_id,
            user=current_user
        )

    @staticmethod
    def create(current_user, todo_payload):
        return Todo.objects.create(
            user=current_user,
            **todo_payload
        )

    @staticmethod
    def update(todo_record, updated_data):

        for field_name, new_value in updated_data.items():
            setattr(todo_record, field_name, new_value)

        todo_record.save()

        return todo_record

    @staticmethod
    def delete(todo_record):
        todo_record.delete()
        





# from .models import Todo

# class TodoRepository:
#     @staticmethod
#     def get_all_by_user(user_instance):
#         return Todo.objects.filter(user=user_instance)

#     @staticmethod
#     def get_by_id_and_user(todo_id, user_instance):
#         return Todo.objects.get(id=todo_id, user=user_instance)

#     @staticmethod
#     def create(user_instance, validated_data):
#         return Todo.objects.create(user=user_instance, **validated_data)

#     @staticmethod
#     def update(todo_instance, validated_data):
#         for attr, value in validated_data.items():
#             setattr(todo_instance, attr, value)
#         todo_instance.save()
#         return todo_instance

#     @staticmethod
#     def delete(todo_instance):
#         todo_instance.delete()