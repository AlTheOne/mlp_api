from rest_framework import viewsets
from projectApp.models import Project
from projectApp.serializers import ProjectSerializer
from commonApp.permissions import IsAdminUserOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    lookup_field = 'slug'
