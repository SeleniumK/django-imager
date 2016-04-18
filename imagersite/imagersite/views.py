from __future__ import unicode_literals
from django.shortcuts import render
from imager_images.models import Photo
from django.conf import settings
from django.contrib.staticfiles import finders


DEFAULT_IMAGE = finders.find('css/images/default-image')

def home_page(request, *args, **kwargs):
    try:
        image = Photo.objects.filter(published="public").order_by("?")[0]
    except IndexError:
        image = DEFAULT_IMAGE
    return render(request, 'home.html', context={'image': image})
