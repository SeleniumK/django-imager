from django.shortcuts import render
from rest_framework import renderers
from imager_images.models import Photo, Album
from rest_framework import viewsets
from .permissions import IsOwnerAndReadOnly
from .serializers import PhotoSerializer, AlbumSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    """View all current users photos."""

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated, IsOwnerAndReadOnly)

    def list_photos(self, request, *args, **kwargs):
        """List all photos."""
        self.queryset = self.queryset.filter(user=self.request.user)
        return self.queryset


class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    """View all current users albums."""

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated, IsOwnerAndReadOnly)



