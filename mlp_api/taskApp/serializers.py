from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("title", "task_project_active", "task_current", "task_status", "task_label", "date_of_updated",)