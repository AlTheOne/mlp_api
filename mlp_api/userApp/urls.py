from django.urls import include, path
from rest_framework import routers
from userApp.views import UserViewSet, AccountActivationViewSet


router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'account-activation', AccountActivationViewSet, 'account-activation')

urlpatterns = router.urls
