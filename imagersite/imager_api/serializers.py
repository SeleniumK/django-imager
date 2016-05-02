"""Serializers file."""
from rest_framework import serializers
from imager_images.models import Photo, Album


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Photo model."""

    user = serializers.ReadOnlyField(source='user.username')
    img_file = serializers.FileField(use_url=True)

    class Meta:
        """Meta for Photo Serializer."""

        model = Photo
        fields = ['user', 'title', 'description', 'published', 'img_file']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Album model."""

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        """Meta for Alubm model."""

        model = Album
        fields = ['user', 'title', 'published', 'description']
