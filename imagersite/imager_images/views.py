from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Photo, Album
from django.views.generic.edit import CreateView
from django.forms import ModelForm
import datetime

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


# class AlbumForm(ModelForm):
#     """Album Form."""

#     class Meta:
#         """Meta."""

#         model = Album
#         fields = ["title", "description", "cover", "photos", "published"]

#     def __init__(self, *args, **kwargs):
#         """Damn you pep8."""
#         super(AlbumForm, self).__init__(self, *args, **kwargs)
#         self.fields['photos'].queryset = Photo.objects.filter(user=self.user)


class AddContent(CreateView):
    """Generic view for form to add new content."""

    template_name = 'forms.html'
    success_url = '/images/library'

    def form_valid(self, form):
        """Set user to request user."""
        form.instance.user = self.request.user
        form.instance.date_published = datetime.datetime.now()
        return super(AddContent, self).form_valid(form)


class AddPhoto(AddContent):
    """View to add new Photo."""

    model = Photo
    fields = ["title", "img_file", "description", "published"]


class AddAlbum(AddContent):
    """View for form to add new album."""

    model = Album
    fields = ["title", "description", "cover", "photos", "published"]

    def get_form(self, form_class):
        form = super(AddAlbum, self).get_form(form_class)
        form.fields['photos'].queryset = Photo.objects.filter(user=self.request.user)
        return form
