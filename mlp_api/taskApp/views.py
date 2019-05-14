from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
from .models import Task
from .serializers import TaskSerializer

# class TaskViewSet(viewsets.ModelViewSet):
#
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.all()
        return queryset

    def list(self, *args, **kwargs):
        queryset = Task.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)