from django.test import TestCase, Client
from django.conf import settings
from django.contrib.auth.models import User
from imager_images.models import Photo
from django.contrib.staticfiles import finders


DEFAULT_PIC = finders.find('css/images/default-image.jpg')
HOME = '/'
SIGNUP = '/accounts/register/'


class NoUsers(TestCase):
    """Views with no users in db."""

    def setUp(self):
        """Setup Unauthenticated User Tests."""
        c = Client()
        self.home_response = c.get(HOME)
        self.home_context = self.home_response.context[0]
        self.signup_response = c.get(SIGNUP)

    def test_no_users(self):
        """Assert site created with no default users."""
        self.assertFalse(User.objects.count())

    def test_no_pictures(self):
        """Assert site created with no user photos."""
        self.assertFalse(Photo.objects.count())

    def test_home_view_response_code(self):
        """Assert that visiting home returns a 200 response code."""
        self.assertEquals(self.home_response.status_code, 200)

    def test_home_view_template(self):
        """Assert all templates are hit for home view."""
        templates = self.home_response.templates
        self.assertEquals(templates[0].name, 'home.html')
        self.assertEquals(templates[1].name, 'base.html')
        self.assertEquals(len(templates), 2)

    def test_home_view_no_context(self):
        """Assert that no image context is passed when no there are no photos."""
        img_file = self.home_response.context['image']
        self.assertEquals(img_file, DEFAULT_PIC)

    def test_signup_routing_OK(self):
        """Assert that navigating to signup page returns a 200 response code."""
        self.assertEquals(self.signup_response.status_code, 200)


class UnauthenticatedUser(TestCase):
    """Views for unauthenticated users."""

    def setUp(self):
        pass

    def test_home_view_random_photo(self):
        """Assert that, if available, a random user photo appears on home."""
        pass



class AuthenticatedUser(TestCase):
    """Views for authenticated users."""

    pass
