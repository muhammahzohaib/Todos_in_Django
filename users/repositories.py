from django.contrib.auth import get_user_model

User = get_user_model() #User Model store user data 

class UserRepository:
    @staticmethod
    def create_user(username, password ):
        return User.objects.create_user(username=username, password=password)

    @staticmethod
    def exists(username):
        return User.objects.filter(username=username).exists()