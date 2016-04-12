from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings

PUBLISHED_OPTIONS = (
    ("private", "private"),
    ("shared", "shared"),
    ("public", "public"),
)


@python_2_unicode_compatible
class Album(models.Model):
    """Create Album Model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="albums",
        on_delete=models.CASCADE,
    )
    cover = models.ForeignKey(
        "Photo",
        null=True,
        related_name="albums_covered"
    )
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=120)
    photos = models.ManyToManyField(
        "Photo",
        null=True,
        related_name="albums",
        symmetrical=False
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True)
    published = models.CharField(max_length=10, choices=PUBLISHED_OPTIONS)

    def __str__(self):
        """Return String Representation of Album."""
        return "{}: Album belonging to {}".format(self.title, self.user)

    def __repr__(self):
        """Return Console Representation of Album."""
        return "Title: {} User: {} NumPhotos: {} CoverPhoto: {}".format(
            self.title, self.user, self.photos.count(), self.cover.title
        )


@python_2_unicode_compatible
class Photo(models.Model):
    """Create Photo Model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='photos',
        on_delete=models.CASCADE,
    )
    file = models.ImageField(upload_to='user_photos')
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=120)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True)
    published = models.CharField(max_length=10, choices=PUBLISHED_OPTIONS)

    def __str__(self):
        """Return String Representation of Album."""
        return "{}: Photo belonging to {}".format(self.title, self.user)

    def __repr__(self):
        """Return Console Representation of Album."""
        return "Title: {} User: {} Albums: {} Uploaded On: {}".format(
            self.title, self.user, self.albums.all(), self.date_uploaded
        )
