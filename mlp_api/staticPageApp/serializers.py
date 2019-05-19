from rest_framework import serializers

from staticPageApp.models import Page, BlockPage


class BlockPageSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = BlockPage
        fields = (
            'title',
            'content'
        )


class PageSerializer(serializers.ModelSerializer):
    """Display all entries"""
    blocks_content = BlockPageSerializer(many=True)

    class Meta:
        model = Page
        fields = (
            'title',
            'slug',
            'seo_description',
            'blocks_content'
        )