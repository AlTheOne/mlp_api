from rest_framework import serializers

from staticPageApp.models import Page

class PageSerializer(serializers.ModelSerializer):
    """Display all entries"""
    class Meta:
        model = Page
        fields = (
            'title',
            'slug',
            'seo_description',
            'content'
        )