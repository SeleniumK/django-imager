from imager_images.models import Photo, Album
from rest_framework import serializers


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """Representation of Photos."""

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        """Meta."""

        model = Photo
        fields = (
            'user', 'img_file', 'title', 'description', 'date_uploaded',
            'date_modified', 'date_published', 'published',
        )


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """Representation of Albums."""

    id = serializers.HyperlinkedRelatedField(view_name='album-detail', read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    cover = serializers.HyperlinkedRelatedField(view_name='photo-detail', read_only=True)
    photos = serializers.HyperlinkedRelatedField(many=True, view_name='photo-detail', read_only=True)

    class Meta:
        """Meta."""

        model = Album
        fields = (
            'user', 'id', 'title', 'photos', 'cover', 'description', 'date_uploaded',
            'date_modified', 'date_published', 'published'
        )
