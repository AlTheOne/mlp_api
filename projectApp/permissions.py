from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Allows retrieve API data to any user, and
    create or destroy it only to administrators.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_staff or
            request.method in permissions.SAFE_METHODS
        )
