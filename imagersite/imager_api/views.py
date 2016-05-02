from rest_framework import viewsets, permissions
from imager_api.serializers import PhotoSerializer, AlbumSerializer
from imager_api.permissions import IsOwner
from imager_images.models import Photo, Album


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    """Provides list and detail actions for Photo view."""

    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        """Get photos owned by current user."""
        return Photo.objects.filter(user=self.request.user)


class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    """Provides list and detail actions for Album view."""

    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        """Get albums owned by current user."""
        return Album.objects.filter(user=self.request.user)
