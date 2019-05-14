from rest_framework import routers

from projectApp.urls import router as projectApp_router
from staticPageApp.urls import router as staticPageApp_router
<<<<<<< HEAD
from taskApp.urls import router as taskApp_router
=======
from userApp.urls import router as userApp_router
>>>>>>> e1470c48924e3ba85afc1090e5f80190ec5708fd

class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method
    for extending url routes from another router.
    """
    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.

        Args:
            router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)

# Include new routers from applications
router = DefaultRouter()
router.extend(projectApp_router)
router.extend(staticPageApp_router)
<<<<<<< HEAD
router.extend(taskApp_router)
=======
router.extend(userApp_router)
>>>>>>> e1470c48924e3ba85afc1090e5f80190ec5708fd
