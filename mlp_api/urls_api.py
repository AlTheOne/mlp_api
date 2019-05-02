from rest_framework import routers

from projectApp.urls import router as projectApp_router

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