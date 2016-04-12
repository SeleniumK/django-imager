from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings

LOCATIONS = (
    ("US", "United States"),
    ("DE", "Germany"),
    ("JP", "Japan"),
    ("FR", "France"),
)


class ActiveProfileManager(models.Manager):
    """Create Model Manager for Active Profiles."""

    def get_queryset(self):
        """Return active users."""
        qs = super(ActiveProfileManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Create Model for User Profile."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        on_delete=models.CASCADE,
    )
    objects = models.Manager()
    active = ActiveProfileManager()
    friends = models.ManyToManyField(
        "self",
        related_name="friend_of",
        symmetrical=False
    )
    location = models.CharField(max_length=2, choices=LOCATIONS)

    def __str__(self):
        """Create Representation Of ImagerProfile."""
        return "{}'s' profile".format(self.user)

    @property
    def is_active(self):
        """Return Boolean Value.

        Indicates if user associated with this profile is active.
        """
        return self._is_active
