from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView
)

from staticPageApp.models import Page
from .serialzers import (
    StaticPageAppSerializer,
    StaticPageAppCreateView,
    StaticPageAppDetailView
)

class StaticPageAppCreateView(CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = StaticPageAppCreateView

class StaticPageAppListView(ListAPIView):
    queryset = Page.objects.all()
    serializer_class = StaticPageAppSerializer

class StaticPageAppDetailView(RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = StaticPageAppDetailView
    lookup_field = 'slug'
