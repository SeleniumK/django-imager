from django.shortcuts import render
from django.contrib.auth.decorators import login_required

LIBRARY_TEMPLATE = 'library.html'


@login_required(login_url='/login')
def Library(request, *args, **kwargs):
    """Authenticated User Profile."""
    albums = request.user.albums.all()
    photos = request.user.photos.all()
    return render(
        request,
        LIBRARY_TEMPLATE,
        context={'albums': albums, 'photos': photos})
