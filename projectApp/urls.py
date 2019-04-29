from django.urls import include, path
from rest_framework import routers
from projectApp.views import ProjectListViewSet, ProjectViewSet


router = routers.DefaultRouter()
router.register(r'project', ProjectListViewSet)
router.register(r'project/<pk>/$', ProjectViewSet)


urlpatterns = [
    path('', include(router.urls)),
]