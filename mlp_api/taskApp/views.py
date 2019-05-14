from rest_framework import viewsets

# Create your views here.
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'task_project_id'