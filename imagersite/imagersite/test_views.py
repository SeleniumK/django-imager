from __future__ import unicode_literals
from django.test import TestCase, Client
from django.contrib.auth.models import User
from imager_images.models import Photo
from django.contrib.staticfiles import finders
from imager_images.tests.test_models import PhotoFactory


DEFAULT_PIC = finders.find('css/images/default-image.jpg')
HOME = '/'
SIGNUP = '/accounts/register/'
LIBRARY = '/images/library'
PROFILE = '/profile/'
LOGOUT = '/accounts/logout/?next=/'


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
        self.unauth_user = Client()
        self.user = User.objects.create_user(username='dz', password='secret')
        self.home_response = c.get(HOME)
        self.profile_response = c.get(PROFILE)
        self.library_response = c.get(LIBRARY)
        self.logout_response = c.get(LOGOUT)
        self.photo1 = PhotoFactory.create(
            title='selfie',
            user=self.user,
            description='just a picture',
            published='public'
        )

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

    def test_logout(self):
        """Test logout can be reached."""
        self.assertEqual(self.logout_response.status_code, 302)

    def test_unauth_user_image_view(self):
        """Test restrict unauth users."""
        user_id = self.user.id
        photo_id = self.photo1.id
        response = self.unauth_user.get('/images/photos/{}/{}'.format(user_id, photo_id))
        self.assertEqual(response.status_code, 401)


class AuthenticatedUser(TestCase):
    """Test views for authenticated users."""

    def setUp(self):
        """Set up authenticated users."""
        self.user = User.objects.create_user(username='dz', password='secret')
        self.auth_user = Client()
        self.auth_user.login(username='dz', password='secret')
        self.profile_response = self.auth_user.get(PROFILE)
        self.library_response = self.auth_user.get(LIBRARY)
        self.photo1 = PhotoFactory.create(
            title='selfie',
            user=self.user,
            description='just a picture',
            published='public'
        )

    # def test_landing_page_authenticated(self):
    #     """Assert landing page for authenticated users is profile page."""
    #     self.assertEquals(self.home_response, 200)

    # def test_landing_profile(self):
    #     templates = self.home_response.templates
    #     self.assertEquals(templates[0].name, 'profile.html')

    def test_access_to_profile(self):
        """Assert authenticated user can access profile."""
        self.assertEquals(self.profile_response.status_code, 200)

    def test_access_to_library(self):
        """Assert authenticated user can access library."""
        self.assertEquals(self.library_response.status_code, 200)

    def test_profile_shows_user_info(self):
        """Assert profile shows authenticated user's info."""
        pass
        # self.assertEquals(self.user.username,

    def test_library_shows_user_info(self):
        """Assert library shows authenticated user's info."""
        pass

    def test_auth_user_image_view(self):
        """Test to see you only see your pics."""
        user_id = self.user.id
        photo_id = self.photo1.id
        response = self.auth_user.get('/images/photos/{}/{}'.format(user_id, photo_id))
        self.assertEqual(response.status_code, 200)


