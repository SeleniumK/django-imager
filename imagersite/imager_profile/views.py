from django.shortcuts import render
# from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin

PROFILE_TEMPLATE = 'profile.html'


@login_required(login_url='/login')
def Profile(request, *args, **kwargs):
    """Authenticated User Profile."""
    return render(request, PROFILE_TEMPLATE)

# Create your views here.
# class Profile(LoginRequiredMixin, TemplateView):
    # """Authenticated User Profile."""

    # template = 'profile.html'

    # def authUserProfile(request)
