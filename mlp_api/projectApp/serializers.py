from rest_framework import serializers
from projectApp.models import Project, Technology, Status


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
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
    technologies = TechnologySerializer(many=True)

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

    def validate_technologies(self, tech_data_list):
        wrong_techs = []

        for tech_data in tech_data_list:
            title, slug = tech_data.values()
            if not Technology.objects.filter(title=title, slug=slug).exists():
                wrong_techs.append(title)

        if not wrong_techs:
            return tech_data_list

        issue = "Problem with next techs: '%s'" % ", ".join(wrong_techs)
        raise serializers.ValidationError(issue)

    # Setting write methods explicitly:

    def create(self, validated_data):
        status_data = validated_data.pop('status')
        techs_data = validated_data.pop('technologies')

        status = Status.objects.get(**status_data)
        techs = [Technology.objects.get(**td) for td in techs_data]

        project = Project.objects.create(**validated_data, status=status)
        project.technologies.set(techs)
        return project

    def update(self, instance, validated_data):
        status_data = validated_data.pop('status')
        techs_data = validated_data.pop('technologies')

        status = Status.objects.get(**status_data)
        techs = [Technology.objects.get(**td) for td in techs_data]

        instance.status = status
        instance.technologies.set(techs)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        updated_fields = ['status'] + list(validated_data.keys())
        instance.save(update_fields=updated_fields)
        return instance
