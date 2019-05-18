from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from taskApp.models import Task
from taskApp.serializers import TaskSerializer, TaskListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    TaskViewSet is use for get datas of tasks
    with considering project_slug
    """

    serializer_class = TaskSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.all()
        return queryset

    def list(self, *args, **kwargs):
        queryset = Task.objects.filter(task_project__slug=kwargs.get('project_slug'))
        serializer = TaskListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, project_slug, pk=None):
        task = get_object_or_404(Task, pk=pk, task_project__slug=project_slug)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
