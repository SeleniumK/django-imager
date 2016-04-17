from __future__ import unicode_literals
from django.shortcuts import render
from imager_images.models import Photo
from django.conf import settings


def home_page(request, *args, **kwargs):
    try:
        image = Photo.objects.filter(published="public").order_by("?")[0]
    except IndexError:
        image = None
    return render(request, 'home.html', context={'image': image})
