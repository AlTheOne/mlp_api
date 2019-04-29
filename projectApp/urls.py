from django.urls import include, path
from rest_framework import routers
from projectApp.views import ProjectViewSet


router = routers.DefaultRouter()
router.register(r'project', ProjectViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
