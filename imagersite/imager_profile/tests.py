from __future__ import unicode_literals
from django.test import TestCase
from django.conf import settings
import factory
from imager_profile.models import ImagerProfile


class UserFactory(factory.django.DjangoModelFactory):
    """Create a Test User Factory."""

    class Meta:
        """Meta: This docstring is sponsered by pep8."""

        model = settings.AUTH_USER_MODEL


class UserTestCase(TestCase):
    """Test User and ImagerProfile Models."""

    def setUp(self):
        """Set up environment for Testing Users."""
        self.bob = UserFactory.create(
            username="bob",
            email="lotsa@test.org"
        )
        self.bob.set_password("secret")
        self.disa = UserFactory.create(
            username="disa",
            email="lotsa@test.org"
        )
        self.disa.set_password("secret")
        self.charlie = UserFactory.create(
            username="charlie",
            email="lotsa@test.org"
        )
        self.charlie.set_password("secret")

    def test_user_profile(self):
        """Assert when user is created, has profile."""
        self.assertEqual(list(ImagerProfile.objects.filter(user__username__exact="bob")), [self.bob.profile])
        self.assertEqual(list(ImagerProfile.objects.filter(user__username__exact="disa")), [self.disa.profile])
        self.assertEqual(list(ImagerProfile.objects.filter(user__username__exact="charlie")), [self.charlie.profile])

    def test_user_profile_type(self):
        """Assert when user is created, has profile."""
        self.assertEqual(type(self.bob.profile), ImagerProfile)
        self.assertEqual(type(self.disa.profile), ImagerProfile)
        self.assertEqual(type(self.charlie.profile), ImagerProfile)

    def test_deleted_profile(self):
        """Assert when user is deleted, profile no longer exists."""
        pass

    def test_active_user(self):
        """Assert when user is active when created."""
        pass

    def test_user_in_active_list(self):
        """Assert when user is active, in ImagerProfile.active."""
        pass

    def test_unactive_user(self):
        """Assert when user.is_active can be set to false."""
        pass

    def test_user_not_in_active_list(self):
        """Assert when user is not active, not in ImagerProfile.active."""
        pass

    def test_lonely_user(self):
        """Assert when user is created, user has no friends."""
        pass

    def test_friends_single(self):
        """Assert when user is given a friends friend appears in list."""
        pass

    def test_multiple_friends(self):
        """Assert multiple people can be assigned as user's friends."""
        pass

    def test_friend_is_friend_of(self):
        """Assert user's friend can access user using .friend_of."""
        pass

    def test_many_friends_are_friend_of(self):
        """Assert user's multiple friends can all access user using .friend_of."""
        pass

    def test_friend_is_friend_of_multiple(self):
        """Assert user can be friend of multiple other users."""
        pass

    def test_add_location(self):
        """Assert location can be added to a user."""
        pass

    def test_profile_str(self):
        """Assert profiles str method returns string with user's name."""
        pass
