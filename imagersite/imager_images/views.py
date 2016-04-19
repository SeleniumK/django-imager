from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.forms import ModelForm
from .models import Photo
from django.views.generic.edit import CreateView

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


def photo_view(request, **kwargs):
    photo_id = kwargs.get('photo_id')
    user = User.objects.filter(id=kwargs.get('user_id')).first()
    image = user.photos.filter(id=photo_id).first()
    if image.published != 'public' or request.user.id != user.id:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'images/photo_view.html', context={'image': image})


class AddPhoto(CreateView):
    """View for form to add new photo."""

    model = Photo
    template_name = 'addphoto.html'
    fields = ["title", "img_file", "description"]
    success_url = 'library'


class AddAlbum(ModelForm):
    """View for form to add new album."""

    pass




















