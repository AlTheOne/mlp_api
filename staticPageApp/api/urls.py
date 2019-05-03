from django.urls import path, re_path

from .views import (
    StaticPageAppListView,
    StaticPageAppCreateView,
    StaticPageAppDetailView
)

urlpatterns = [
    path('', StaticPageAppListView.as_view(), name='list'),
    path('create', StaticPageAppCreateView.as_view(), name='create'),
    re_path('(?P<slug>[\w-]+)/', StaticPageAppDetailView.as_view(), name='detail')
]