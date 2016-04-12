from django.test import TestCase
from django.db.models.fields.files import ImageFieldFile
from imager_images.models import Photo, Album
from imager_profile.tests import UserFactory
import factory


class AlbumFactory(factory.django.DjangoModelFactory):
    """Create Test Albums Factory."""

    def Meta():
        """Model is Album."""
        model = Album


class PhotoFactory(factory.django.DjangoModelFactory):
    """Create Test Photo Factory."""

    def Meta():
        """Model is photo."""
        model = Photo


class AlbumAndTestCase(TestCase):
    """Asserts that Photos and Albums have access to all correct attributes."""

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
            user=maithrika,
            description="just a picture",
            published="public"
        )

    def test_album_attributes(self):
        """Assert Album has necessary attributes."""
        pass

    def test_user_album(self):
        """Assert album is in User.albums."""
        self.assertIn(self.vacation, self.maithrika.albums)
# create album for user. Assert album in user.album
# assert new album is type album   
# assert user.album is type album
# create album, attach to user, assert user has album
# assert album has no cover by default
# assert album has title
# assert album has description 
# assert album has photos
# assert album has date uploaded
# assert album has date modified
# assert album has date published
# assert album has .published


# create photo for user. Assert photo exists
# create photo, attach to user, assert user has photo
# create photo and album for user, assert photo can be added to album
# create photo for one user, album for another, assert photo must be user's to go in album
# assert user's photo can be made cover of album
# ssert album has cover
# assert cover of album must belong to the same user
