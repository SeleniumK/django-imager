from __future__ import unicode_literals
from django.shortcuts import render
from imager_images.models import Photo
from django.http import HttpResponse
from django.conf import settings
# TODO: Will need to figure out how to user auth_user_model for views
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.http import HttpResponseRedirect

DEFAULT_IMAGE = finders.find('css/images/default-image')
PROFILE = '/profile/'


def home_page(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(PROFILE)
    try:
        image = Photo.objects.filter(published="public").order_by("?")[0]
    except IndexError:
        image = DEFAULT_IMAGE
    return render(request, 'home.html', context={'image': image})


def photo_view(request, **kwargs):
    photo_id = kwargs.get('photo_id')
    user = User.objects.filter(id=kwargs.get('user_id')).first()
    image = user.photos.filter(id=photo_id).first()
    if image.published != 'public' and request.user.id != user.id:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'images/photo_view.html', context={'image': image})
