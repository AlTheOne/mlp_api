from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *

class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    serializer_class = TaskProjectSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.all()
        return queryset

    def list(self, *args, **kwargs):
        # project_slug записывается в словарь **kwargs
        queryset = Task.objects.filter(task_project__slug=kwargs.get('project_slug'))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
