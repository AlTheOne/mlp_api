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

class ProjectSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
