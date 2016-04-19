from django.conf.urls import url
from imager_images.views import Library
from .views import photo_view, AddAlbum, AddPhoto


urlpatterns = [
    url(r'^library$', Library, name='library'),
    url(r'^photos/(?P<user_id>[0-9]+)/(?P<photo_id>[0-9]+)', photo_view, name='photo_view'),
    # url(r'^albums/add$', AddAlbum.as_view(), name='add_album_view'),
    url(r'^photos/add$', AddPhoto.as_view(), name='add_photo_view'),
]
