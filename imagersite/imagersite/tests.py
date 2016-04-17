from django.test import Client, TestCase
from django.conf import settings

HOME = '/'
REGISTER = '/accounts/'
LOGIN = '/login'
LOGOUT = '/logout/'
USER = settings.AUTH_USER_MODEL


class UnauthenticatedUser(TestCase):
    """Create unauth user for testing."""

    def setUp(self):
        """Setup unauth user."""
        client = Client()
        self.home = client.get(HOME)

    def test_no_user_in_db(self):
        """No user i db."""
        self.assertFalse(USER.objects.count())
