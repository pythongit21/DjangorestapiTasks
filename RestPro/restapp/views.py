from django.shortcuts import render
from .models import Task
from .Serializers import TaskSerializers, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
# from rest_framework.views import APIView

# Create your views here.


class TaskViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('-date_add')
    serializer_class = TaskSerializers

class DueTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_add').filter(completed=False)
    serializer_class = TaskSerializers

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_add').filter(completed=True)
    serializer_class = TaskSerializers
