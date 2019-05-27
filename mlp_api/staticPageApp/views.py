from rest_framework import viewsets
from staticPageApp.models import Page
from staticPageApp.serializers import PageSerializer

from rest_framework import permissions


class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Page.objects.filter(is_activate=True)
    serializer_class = PageSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'