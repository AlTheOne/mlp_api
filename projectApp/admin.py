from django.contrib import admin
from projectApp.models import Project, Tag, Status

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
