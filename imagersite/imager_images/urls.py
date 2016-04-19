from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from imager_images.views import Library
from .views import photo_view, AddOrEditAlbum, AddOrEditPhoto
# from .views import photo_view, AddAlbum, AddPhoto, UpdateAlbum


urlpatterns = [
    url(r'^library$', Library, name='library'),
    url(r'^photos/(?P<user_id>[0-9]+)/(?P<photo_id>[0-9]+)', photo_view, name='photo_view'),
    url(r'^albums/add$', login_required(AddOrEditAlbum.as_view()), name='add_album_view'),
    url(r'^albums/(?P<pk>[0-9]+)/edit/$', login_required(AddOrEditAlbum.as_view()), name='edit_album_view'),
    url(r'^photos/add$', login_required(AddOrEditPhoto.as_view()), name='add_photo_view'),
    url(r'^photos/(?P<pk>[0-9]+)/edit/$', login_required(AddOrEditAlbum.as_view()), name='edit_photo_view'),
]
