from django.contrib import admin
from groupProjectApp.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass