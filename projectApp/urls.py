from django.urls import include, path
from rest_framework import routers
from projectApp.views import ProjectViewSet


router = routers.SimpleRouter()
router.register(r'project', ProjectViewSet)

urlpatterns = router.urls