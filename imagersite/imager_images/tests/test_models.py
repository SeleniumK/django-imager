from django.test import TestCase
# from django.db.models.fields.files import ImageFieldFile
from imager_images.models import Photo, Album
from imager_profile.tests import UserFactory
from datetime import timezone, datetime
import factory


class AlbumFactory(factory.django.DjangoModelFactory):
    """Create Test Albums Factory."""

    class Meta():
        """Model is Album."""

        model = Album


class PhotoFactory(factory.django.DjangoModelFactory):
    """Create Test Photo Factory."""

    class Meta():
        """Model is photo."""

        model = Photo


class SingleAlbumAndPhotoTestCase(TestCase):
    """Asserts that a single User's Photos and Albums work as expected."""

    def setUp(self):
        """Set Up Testing Environment."""
        self.maithrika = UserFactory.create(
            username="maithrika"
        )
        self.vacation = AlbumFactory.create(
            user=self.maithrika,
            title="Vacation",
            description="Album of pics",
            published="public"
        )
        self.selfie = PhotoFactory.create(
            title="selfie",
            user=self.maithrika,
            description="just a picture",
            published="public"
        )

    def test_user_in_db(self):
        """Assert User has primary key."""
        self.assertTrue(self.maithrika.pk)

    def test_photo_in_db(self):
        """Assert User has primary key."""
        self.assertTrue(self.selfie.pk)

    def test_album_in_db(self):
        """Assert User has primary key."""
        self.assertTrue(self.vacation.pk)

    def test_album_attributes(self):
        """Assert Album has necessary attributes."""
        album = self.vacation
        self.assertEqual(album.user, self.maithrika)
        self.assertEqual(album.title, "Vacation")
        self.assertEqual(album.description, "Album of pics")
        self.assertEqual(album.published, "public")
        self.assertIsNone(album.date_published)

    def test_album_datetimes(self):
        """Assert album's datetime fields are datetime."""
        self.assertGreater(datetime.now(timezone.utc), self.vacation.date_uploaded)
        self.assertGreater(datetime.now(timezone.utc), self.vacation.date_modified)

    def test_user_album(self):
        """Assert album is in User.albums."""
        self.assertIn(self.vacation, self.maithrika.albums.all())

    def test_album_in_album(self):
        """Assert album in album collection."""
        self.assertIn(self.vacation, Album.objects.all())

    def test_album_type(self):
        """Assert created album is type Album."""
        self.assertIsInstance(self.vacation, Album)

    def test_user_album_type(self):
        """Assert items in user.albums are type Album."""
        self.assertIsInstance(self.maithrika.albums.all()[0], Album)

    def test_album_in_users_album_list(self):
        """Assert album in user's albums."""
        self.assertIn(self.vacation, self.maithrika.albums.all())

    def test_no_album_cover(self):
        """Assert album has no cover by default."""
        self.assertIsNone(self.vacation.cover)

    def test_photo_user_photos(self):
        """Assert that photo exists in users photos."""
        self.assertIn(self.selfie, self.maithrika.photos.all())

    def test_user_photos_in_photos(self):
        """Assert user photos in Photos."""
        self.assertIn(self.selfie, Photo.objects.all())

    def test_add_photo_to_album_albumaware(self):
        """Assert that adding a photo to an album adds that photo to album.photos."""
        self.assertNotIn(self.selfie, self.vacation.photos.all())
        self.vacation.photos.add(self.selfie)
        self.assertIn(self.selfie, self.vacation.photos.all())

    def test_add_photo_to_album_photoaware(self):
        """Assert that once photo is added to album, that album is in Photo.albums."""
        self.assertNotIn(self.vacation, self.selfie.albums.all())
        self.vacation.photos.add(self.selfie)
        self.assertIn(self.vacation, self.selfie.albums.all())

    def test_add_album_to_photo_albumaware(self):
        """Assert that adding an album to a photo adds that photo to album.photos."""
        self.assertNotIn(self.selfie, self.vacation.photos.all())
        self.selfie.albums.add(self.vacation)
        self.assertIn(self.selfie, self.vacation.photos.all())

    def test_add_album_to_photo_photoaware(self):
        """Assert that once album is added to photo, that album is in Photo.albums."""
        self.assertNotIn(self.vacation, self.selfie.albums.all())
        self.selfie.albums.add(self.vacation)
        self.assertIn(self.vacation, self.selfie.albums.all())

    def test_add_cover(self):
        """Assert that cover can be added to album."""
        self.vacation.photos.add(self.selfie)
        self.vacation.cover = self.selfie
        self.assertEqual(self.selfie, self.vacation.cover)

