"""Permissions file."""
from rest_framework import permissions


class IsOwnerAndReadOnly(permissions.BasePermission):
    """Allow only users to see their photos."""

    def has_object_permission(self, request, view, obj):
        """Allow only GET requests from logged in user."""
        return request.method in permissions.SAFE_METHODS and obj.owner == request.user

