from rest_framework import routers
from staticPageApp.views import PageViewSet

router = routers.SimpleRouter()
router.register(r'', PageViewSet)

urlpatterns = router.urls