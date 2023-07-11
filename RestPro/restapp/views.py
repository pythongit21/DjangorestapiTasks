from django.shortcuts import render
from .models import Task
from .Serializers import TaskSerializers, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

# Import necessary modules and models

# Viewset for Task model
class TaskViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)  # Set permission classes to only allow authenticated users
    queryset = Task.objects.all().order_by('-date_add')  # Retrieve all tasks and order by date added
    serializer_class = TaskSerializers  # Use the TaskSerializers for serialization

# Viewset for retrieving due tasks
class DueTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_add').filter(completed=False)  # Retrieve all tasks that are not completed and order by date added
    serializer_class = TaskSerializers  # Use the TaskSerializers for serialization

# View for creating a new user
class CreateUserView(CreateAPIView):
    model = get_user_model()  # Set the model to the active user model in the project
    permission_classes = (AllowAny,)  # Allow any user to create a new user
    serializer_class = UserSerializer  # Use the UserSerializer for serialization

# Viewset for retrieving completed tasks
class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_add').filter(completed=True)  # Retrieve all tasks that are completed and order by date added
    serializer_class = TaskSerializers  # Use the TaskSerializers for serialization
