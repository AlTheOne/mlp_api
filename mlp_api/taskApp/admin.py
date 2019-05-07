from django.contrib import admin

# Register your models here.
from .models import Task, LabelTask, StatusTask

admin.site.register(Task)
admin.site.register(LabelTask)
admin.site.register(StatusTask)