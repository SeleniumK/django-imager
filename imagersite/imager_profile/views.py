from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from .models import ImagerProfile

PROFILE_TEMPLATE = 'profile.html'


@login_required(login_url='/login')
def Profile(request, *args, **kwargs):
    """Authenticated User Profile."""
    return render(request, PROFILE_TEMPLATE)


class EditProfile(UpdateView):
    """Edit profile."""

    model = ImagerProfile
    fields = ['location', 'camera_type']
    success_url = '/profile/'
    template_name = 'edit_profile.html'

    def get_object(self):
        """Override get_object method."""
        return get_object_or_404(User, pk=self.request.user.id)


