from rest_framework import routers
from staticPageApp.views import PageViewSet

router = routers.SimpleRouter()
router.register(r'page', PageViewSet)

urlpatterns = router.urls