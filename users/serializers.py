from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
#more field required like email, DOB etc
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 150)
    password = serializers.CharField(write_only=True)

# class  Authserializer (serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True) 