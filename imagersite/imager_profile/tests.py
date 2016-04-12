from __future__ import unicode_literals
from django.test import TestCase
from django.conf import settings
import factory
from faker import Faker


class UserFactory(factory.django.DjangoModelFactory):
    """Create a Test User Factory."""

    class Meta:
        """Meta: This docstring is sponsered by pep8."""

        model = settings.AUTH_USER_MODEL

