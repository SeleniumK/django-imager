from __future__ import unicode_literals
from django.shortcuts import render
from imager_images.models import Photo
from django.contrib.staticfiles import finders
from django.http import HttpResponseRedirect


DEFAULT_IMAGE = finders.find('css/images/default-image')
PROFILE = '/profile/'


def home_page(request, *args, **kwargs):
    if request.user.is_authenticated:
        return HttpResponseRedirect(PROFILE)
    try:
        image = Photo.objects.filter(published="public").order_by("?")[0]
    except IndexError:
        image = DEFAULT_IMAGE
    return render(request, 'home.html', context={'image': image})
