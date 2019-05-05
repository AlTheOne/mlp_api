from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_title',
        'slug',
        'is_activate',
        'data_of_updated',
        'data_of_created'
    )
    list_display_links = ('short_title',)
    list_filter = ('is_activate',)
    readonly_fields = ('data_of_updated', 'data_of_created')
    fields = (
        'title',
        'slug',
        'seo_description',
        'content',
        'is_activate',
        ('data_of_updated', 'data_of_created')
    )
    save_on_top = True