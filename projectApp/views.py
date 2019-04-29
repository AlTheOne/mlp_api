from rest_framework import viewsets
from projectApp.models import Project
from projectApp.serializers import *


class ProjectListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.filter(is_active=True).order_by('-date_of_created')
    serializer_class = ProjectListSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer

    def get(self, slug):
        queryset = Project.objects.filter(slug=slug, is_active=True)