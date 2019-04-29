from rest_framework import serializers
from projectApp.models import Project, Tag, Status


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'slug')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('title', )


class ProjectListSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            'title',
            'slug',
            'preview',
            'short_description',
            'date_of_updated',
            'status',
            'tags'
        )

class ProjectSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            'title',
            'slug',
            'preview',
            'short_description',
            'full_description',
            'number_of_people',
            'date_of_updated',
            'date_of_end',
            'status',
            'tags'
        )