from .models import Task  # Import the Task model
from rest_framework import serializers  # Import the serializers module from Django REST Framework
from django.contrib.auth import get_user_model  # Import the get_user_model function

# Define a serializer for user data
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Create a write-only field for the password

    def create(self, validated_data):
        # Method for creating a new user

        # Create a new user instance with the validated username
        user = get_user_model().objects.create(username=validated_data['username'])

        # Set the password for the user instance
        user.set_password(validated_data['password'])

        # Save the user instance
        user.save()

        # Return the created user instance
        return user

    class Meta:
        model = get_user_model()  # Specify the model for the serializer

        fields = ['username', 'password']  # Specify the fields to be included in the serialized representation


# Define a serializer for task data
class TaskSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)  # Create an image field

    class Meta:
        model = Task  # Specify the model for the serializer

        fields = ['id', 'task_name', 'task_desc', 'completed', 'date_add', 'image']
        # Specify the fields to be included in the serialized representation


