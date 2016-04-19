from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Photo, Album
from django.views.generic.edit import CreateView, ModelFormMixin, ProcessFormView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic import UpdateView
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


class AddOrEditContent(SingleObjectTemplateResponseMixin, ModelFormMixin, ProcessFormView):
    template_name = 'forms.html'
    success_url = '/images/library'

    def get_object(self, queryset=None):
        try:
            return super(AddOrEditContent, self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(AddOrEditContent, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """Set user to request user."""
        form.instance.user = self.request.user
        form.instance.date_published = datetime.datetime.now()
        return super(AddOrEditContent, self).form_valid(form)


class AddOrEditPhoto(AddOrEditContent):
    """View to add new Photo."""

    model = Photo
    fields = ["title", "img_file", "description", "published"]


class AddOrEditAlbum(AddOrEditContent):
    """View for form to add new album."""

    model = Album
    fields = ["title", "description", "cover", "photos", "published"]

    def get_form(self, form_class):
        """Set up field querysets."""
        form = super(AddOrEditAlbum, self).get_form(form_class)
        user_photos = Photo.objects.filter(user=self.request.user)
        form.fields['cover'].queryset = user_photos
        form.fields['photos'].queryset = user_photos
        return form

