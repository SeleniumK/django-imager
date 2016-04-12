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
        profiles = ImagerProfile.objects.all()
        self.assertIn(self.bob.profile, profiles)
        self.assertIn(self.charlie.profile, profiles)
        self.assertIn(self.disa.profile, profiles)

    def test_user_profile_type(self):
        """Assert when user is created, has profile."""
        self.assertIsInstance(self.bob.profile, ImagerProfile)
        self.assertIsInstance(self.disa.profile, ImagerProfile)
        self.assertIsInstance(self.charlie.profile, ImagerProfile)

    def test_active_user(self):
        """Assert when user is active when created."""
        self.assertTrue(self.bob.is_active)
        self.assertTrue(self.disa.is_active)
        self.assertTrue(self.charlie.is_active)

    def test_unactive_user(self):
        """Assert when user.is_active can be set to false."""
        self.bob.is_active = False
        self.assertFalse(self.bob.is_active)

    def test_user_in_active_list(self):
        """Assert when user is active, in ImagerProfile.active."""
        profiles = ImagerProfile.active.all()
        self.assertIn(self.bob.profile, profiles)
        self.assertIn(self.charlie.profile, profiles)
        self.assertIn(self.disa.profile, profiles)

    def test_user_not_in_active_list(self):
        """Assert when user is not active, not in ImagerProfile.active."""
        self.bob.is_active = False
        self.assertNotIn(self.bob, ImagerProfile.active.all())

    def test_lonely_user(self):
        """Assert when user is created, user has no friends."""
        self.assertFalse(self.bob.profile.friends.all())
        self.assertFalse(self.disa.profile.friends.all())
        self.assertFalse(self.charlie.profile.friends.all())

    def test_friends_single(self):
        """Assert when user is given a friends friend appears in list."""
        self.bob.profile.friends.add(self.disa.profile)
        self.assertIn(self.disa.profile, self.bob.profile.friends.all())

    def test_multiple_friends(self):
        """Assert multiple people can be assigned as user's friends."""
        self.bob.profile.friends.add(self.disa.profile)
        self.charlie.profile.friends.add(self.disa.profile)
        self.assertIn(self.disa.profile, self.bob.profile.friends.all())
        self.assertIn(self.disa.profile, self.charlie.profile.friends.all())

    def test_friend_is_friend_of(self):
        """Assert user's friend can access user using .friend_of."""
        self.bob.profile.friends.add(self.disa.profile)
        self.assertIn(self.bob.profile, self.disa.profile.friend_of.all())

    def test_many_friends_are_friend_of(self):
        """Assert user's multiple friends can all access user using .friend_of."""
        self.bob.profile.friends.add(self.disa.profile)
        self.bob.profile.friends.add(self.charlie.profile)
        self.assertIn(self.bob.profile, self.disa.profile.friend_of.all())
        self.assertIn(self.bob.profile, self.charlie.profile.friend_of.all())

    def test_friend_is_friend_of_multiple(self):
        """Assert user can be friend of multiple other users."""
        self.bob.profile.friends.add(self.disa.profile)
        self.charlie.profile.friends.add(self.disa.profile)
        self.assertIn(self.bob.profile, self.disa.profile.friend_of.all())
        self.assertIn(self.charlie.profile, self.disa.profile.friend_of.all())

    def test_add_location(self):
        """Assert location can be added to a user."""
        self.charlie.profile.location = "US"
        self.assertEqual(self.charlie.profile.location, "US")

    def test_profile_str(self):
        """Assert profiles str method returns string with user's name."""
        self.assertEqual(self.disa.profile.__str__(), "disa's profile")
        self.assertEqual(self.charlie.profile.__str__(), "charlie's profile")
        self.assertEqual(self.bob.profile.__str__(), "bob's profile")

    def test_deleted_profile(self):
        """Assert when user is deleted, profile no longer exists."""
        self.charlie.delete()
        self.assertFalse(ImagerProfile.objects.filter(user__username__exact='charlie'))


