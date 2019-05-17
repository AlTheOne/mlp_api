from rest_framework import serializers

from taskApp.models import Task

class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'title',
            'task_project',
            'task_status',
            'task_label',
            'date_of_updated'
        )


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
