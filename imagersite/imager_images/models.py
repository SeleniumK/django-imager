from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import datetime
from django.conf import settings

PUBLISHED_OPTIONS = (
    ("private"),
    ("shared"),
    ("public"),
)


@python_2_unicode_compatible
class Photo(models.Model):
    """Create Photo Model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    file = models.ImageField()
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=120)
    # date_uploaded = models.
    # date_modified = models.
    # date_published = models.
    published = models.CharField(max_length=10, choices=PUBLISHED_OPTIONS)


@python_2_unicode_compatible
class Album(models.Model):
    """Create Album Model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    cover = models.OneToOne()
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=120)
    # date_uploaded = 
    # date_modified = 
    # date_published =
    published = models.CharField(max_length=10, choices=PUBLISHED_OPTIONS)
    photos = models.ManyToManyField(
        Photo,
        related_name="in_album",
        symmetrical=False
    )
