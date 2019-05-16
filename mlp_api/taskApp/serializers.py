from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'task_project', 'date_of_updated', 'task_label')
        depth = 4