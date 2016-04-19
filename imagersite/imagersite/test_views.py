from django.test import TestCase, Client
from django.contrib.auth.models import User
from imager_images.models import Photo
from django.contrib.staticfiles import finders


DEFAULT_PIC = finders.find('css/images/default-image.jpg')
HOME = '/'
SIGNUP = '/accounts/register/'
LIBRARY = '/images/library'
PROFILE = '/profile/'


class NoUsers(TestCase):
    """Views with no users in db."""

    def setUp(self):
        """Setup Unauthenticated User Tests."""
        c = Client()
        self.home_response = c.get(HOME)
        self.home_context = self.home_response.context[0]
        self.signup_response = c.get(SIGNUP)
        self.profile_response = c.get(PROFILE)
        self.library_response = c.get(LIBRARY)

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
    """Test views for unauthenticated users."""

    def setUp(self):
        """Set up unauthenticated users."""
        c = Client()
        self.home_response = c.get(HOME)
        self.profile_response = c.get(PROFILE)
        self.library_response = c.get(LIBRARY)

    def test_landing_page(self):
        """Assert that unauthenticated user lands at homepage."""
        templates = self.home_response.templates
        self.assertEquals(templates[0].name, 'home.html')

    # def test_home_view_user_photos(self):
    #     """Assert that landing page photo is a user photo."""
    #     img_file = self.home_response.context['image']
    #     self.assertIn(img_file, Photo.objects.filter(published='public'))

    def test_no_access_to_profile(self):
        """Assert profile page redirects unauthenticated users."""
        self.assertEquals(self.profile_response.status_code, 302)

    def test_no_access_to_library(self):
        """Assert library page redirects unauthenticated users."""
        self.assertEquals(self.library_response.status_code, 302)


class AuthenticatedUser(TestCase):
    """Test views for authenticated users."""

    def setUp(self):
        """Set up authenticated users."""
        c = Client()
        self.home_response = c.get(HOME)

    # def test_landing_page_authenticated(self):
    #     """Assert landing page for authenticated users is profile page."""
    #     self.assertEquals(self.home_response, 200)

    # def test_landing_profile(self):
    #     templates = self.home_response.templates
    #     self.assertEquals(templates[0].name, 'profile.html')


    def test_access_to_profile(self):
        """Assert authenticated user can access profile."""
        pass

    def test_access_to_library(self):
        """Assert authenticated user can access library."""
        pass

    def test_profile_shows_user_info(self):
        """Assert profile shows authenticated user's info."""
        pass

    def test_library_shows_user_info(self):
        """Assert library shows authenticated user's info."""
        pass
