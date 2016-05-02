from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Custom permission to only allow owners of object to edit."""

    def has_object_permission(self, request, view, obj):
        """Check object permissions against the request's user."""
        return obj.user == request.user
