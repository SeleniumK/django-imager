from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.views.generic.edit import UpdateView
from .models import ImagerProfile

PROFILE_TEMPLATE = 'profile.html'


@login_required(login_url='/login')
def Profile(request, *args, **kwargs):
    """Authenticated User Profile."""
    return render(request, PROFILE_TEMPLATE)


def edit_user_profile(request):
    """Edit user profile."""
    current_user = User.objects.get(pk=request.user.id)
    current_profile = current_user.profile
    if request.method == 'POST':
        form2 = EditUser(request.POST, instance=current_user)
        form1 = EditProfile(request.POST, instance=current_profile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return render(request, 'profile.html')
    else:
        form2 = EditUser(instance=current_user)
        form1 = EditProfile(instance=current_profile)
    return render(request, 'edit_profile.html', {'form1': form1, 'form2': form2})


class EditUser(ModelForm):
    """Edit user form."""

    class Meta:
        """Meta."""

        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class EditProfile(ModelForm):
    """Edit profile form."""

    class Meta:
        """Meta."""

        model = ImagerProfile
        fields = ['location', 'camera_type']





