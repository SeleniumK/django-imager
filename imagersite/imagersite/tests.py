from django.test import Client, TestCase
from django.contrib.auth.models import User

HOME = '/'
REGISTER = '/accounts/register/'
LOGIN = '/login'
LOGOUT = '/logout'


class UnauthenticatedUser(TestCase):
    """Create unauth user for testing."""

    def setUp(self):
        """Setup unauth user."""
        client = Client()
        self.home = client.get(HOME)
        self.login = client.get(LOGIN)
        self.logout = client.get(LOGOUT)
        self.register = client.get(REGISTER)

    def test_no_user_in_db(self):
        """No user i db."""
        self.assertFalse(User.objects.count())

    def test_homepage(self):
        """Test homepage can be reached."""
        self.assertEqual(self.home.status_code, 200)

    def test_login(self):
        """Test login cna be reached."""
        self.assertEqual(self.login.status_code, 200)

    def test_logout(self):
        """Test logout can be reached."""
        self.assertEqual(self.logout.status_code, 200)

    def test_register(self):
        """Test register can be reached."""
        self.assertEqual(self.register.status_code, 200)
