from rest_framework import serializers

from staticPageApp.models import Page

class StaticPageAppCreateView(serializers.ModelSerializer):
    """Create new page"""
    class Meta:
        model = Page
        fields = (
            'title',
            'slug',
            'seo_description',
            'content'
        )

class StaticPageAppSerializer(serializers.ModelSerializer):
    """Display all entries"""
    class Meta:
        model = Page
        fields = (
            'title',
            'slug',
            'seo_description',
            'content'
        )

class StaticPageAppDetailView(serializers.ModelSerializer):
    """Detailed display of the page on request slug"""
    class Meta:
        model = Page
        fields = (
            'title',
            'seo_description',
            'content'
        )
