from rest_framework import viewsets
from staticPageApp.models import Page
from staticPageApp.serializers import PageSerializer

class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'