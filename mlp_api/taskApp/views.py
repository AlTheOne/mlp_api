<<<<<<< HEAD
from rest_framework import viewsets

# Create your views here.
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> e1470c48924e3ba85afc1090e5f80190ec5708fd
