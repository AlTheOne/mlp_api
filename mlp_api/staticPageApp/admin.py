from django.contrib import admin
from staticPageApp.models import Page, BlockPage


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
        'blocks_content',
        'is_activate',
        ('data_of_updated', 'data_of_created')
    )
    save_on_top = True

    def get_readonly_fields(self, request, obj=None):
        request.user.has_perm('page.readonly_page')
        return self.readonly_fields


@admin.register(BlockPage)
class BlockPageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'data_of_updated',
        'data_of_created'
    )
    list_display_links = ('title',)
    readonly_fields = ('data_of_updated', 'data_of_created')
    fields = (
        'title',
        'content',
        ('data_of_updated', 'data_of_created')
    )