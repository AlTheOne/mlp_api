from rest_framework import serializers
from projectApp.models import Project, Tag, Status


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'slug')
        extra_kwargs = {
            'title': {'validators': []},
            'slug': {'validators': []}
        }

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('title', )
        extra_kwargs = {'title': {'validators': []}}

class ProjectSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'

    # Validation of relational fields:

    def validate_status(self, status_data):
        title = status_data['title']
        if not Status.objects.filter(title=title).exists():
            issue = "Status '%s' doesn't exist." % title
            raise serializers.ValidationError(issue)

        return status_data

    def validate_tags(self, tag_data_list):
        wrong_tags = []

        for tag_data in tag_data_list:
            title, slug = tag_data.values()
            if not Tag.objects.filter(title=title, slug=slug).exists():
                wrong_tags.append(title)

        if not wrong_tags:
            return tag_data_list

        issue = "Problem with next tags: '%s'" % ", ".join(wrong_tags)
        raise serializers.ValidationError(issue)

    # Setting write methods explicitly:

    def create(self, validated_data):
        status_data = validated_data.pop('status')
        tags_data = validated_data.pop('tags')

        status = Status.objects.get(**status_data)
        tags = [Tag.objects.get(**td) for td in tags_data]

        project = Project.objects.create(**validated_data, status=status)
        project.tags.set(tags)
        return project

    def update(self, instance, validated_data):
        status_data = validated_data.pop('status')
        tags_data = validated_data.pop('tags')

        status = Status.objects.get(**status_data)
        tags = [Tag.objects.get(**td) for td in tags_data]

        instance.status = status
        instance.tags.set(tags)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        updated_fields = ['status'] + list(validated_data.keys())
        instance.save(update_fields=updated_fields)
        return instance
