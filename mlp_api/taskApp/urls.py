from rest_framework import routers
from taskApp.views import TaskViewSet

router = routers.SimpleRouter()
router.register(r'task', TaskViewSet)

urlpatterns = router.urls