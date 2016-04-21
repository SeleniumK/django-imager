from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Photo, Album
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
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
    """Generic Class for View to Edit or Add new Content."""

    template_name = 'forms.html'
    success_url = '/images/library'

    def get_object(self, queryset=None):
        """Get current object, if any."""
        try:
            return super(AddOrEditContent, self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        """If request method is get."""
        self.object = self.get_object()
        return super(AddOrEditContent, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """If request method is post."""
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """If form is valid, set user to request user and update published date."""
        form.instance.user = self.request.user
        form.instance.date_published = datetime.datetime.now()
        return super(AddOrEditContent, self).form_valid(form)


class AddOrEditPhoto(AddOrEditContent):
    """View to add or edit new Photo."""

    model = Photo
    fields = ["title", "img_file", "description", "published"]


class AddOrEditAlbum(AddOrEditContent):
    """View for form to edit existing or add new album."""

    model = Album
    fields = ["title", "description", "cover", "photos", "published"]

    def get_form(self, form_class):
        """Set up field querysets."""
        form = super(AddOrEditAlbum, self).get_form(form_class)
        user_photos = Photo.objects.filter(user=self.request.user)
        form.fields['cover'].queryset = user_photos
        form.fields['photos'].queryset = user_photos
        return form
