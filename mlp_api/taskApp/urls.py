from rest_framework import routers
from .views import TaskViewSet

router = routers.SimpleRouter()
router.register('task', TaskViewSet, basename='task')
#router.register(r'task/(?P<project_slug>[A-Za-z0-9]+)/$', TaskViewSet, basename='task')


urlpatterns = router.urls