from rest_framework import routers
from .views import TaskViewSet
from projectApp.views import ProjectViewSet

router = routers.SimpleRouter()
router.register(r'task', TaskViewSet)
router.register(r'task/project', ProjectViewSet)

urlpatterns = router.urls