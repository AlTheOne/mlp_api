from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'title',
            'task_description',
            'task_project',
            'task_current',
            'user',
            'executor',
            'task_status',
            'task_label'
        )