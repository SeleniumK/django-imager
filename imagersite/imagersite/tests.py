"""Tests for project level urls and views."""
from __future__ import unicode_literals
from django.contrib.staticfiles import finders
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.conf import settings
from imager_images.tests.test_models import PhotoFactory, AlbumFactory
import factory

HOME = '/'
REGISTER = '/accounts/register/'
LOGIN = '/login'
LOGOUT = '/logout'
DEFAULT_IMAGE = finders.find('static/imagersite/images/default-image.jpg')


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

    def test_default_image(self):
        """Test default image shows up."""
        img_path = self.home.context['image']
        self.assertEqual(img_path, DEFAULT_IMAGE)


class AuthenticatedUser(TestCase):
    """Logged in user tests."""

    def setUp(self):
        """Setup for logged in user."""
        self.user = User.objects.create_user(username='dz', password='secret')
        self.auth_user = Client()
        self.unauth_user = Client()
        self.auth_user.login(username='dz', password='secret')
        self.photo1 = PhotoFactory.create(
            title='selfie',
            user=self.user,
            description='just a picture',
            published='public'
        )
        # self.photo2 = PhotoFactory.create(
        #     title='sweet',
        #     user=self.user,
        #     description='its a pic',
        #     published='public'
        # )

    def test_auth_user_image_view(self):
        """Test to see you only see your pics."""
        user_id = self.user.id
        photo_id = self.photo1.id
        response = self.auth_user.get('/images/photos/{}/{}'.format(user_id, photo_id))
        self.assertEqual(response.status_code, 200)

    def test_unauth_user_image_view(self):
        """Test restrict unauth users."""
        user_id = self.user.id
        photo_id = self.photo1.id
        response = self.unauth_user.get('/images/photos/{}/{}'.format(user_id, photo_id))
        self.assertEqual(response.status_code, 401)
