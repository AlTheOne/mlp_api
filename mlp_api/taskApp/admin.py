from django.contrib import admin

# Register your models here.
from .models import Task, LabelTask, StatusTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ("title", "task_project_active", "task_project")

admin.site.register(LabelTask)
admin.site.register(StatusTask)