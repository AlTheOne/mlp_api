from django.urls import include, path
from rest_framework import routers
from groupProjectApp.views import GroupViewSet

router = routers.SimpleRouter()
router.register(r'(?P<project_slug>[A-Za-z0-9]+)', GroupViewSet, basename='group')

urlpatterns = router.urls