from django.shortcuts import render
from django.contrib.auth.decorators import login_required

PROFILE_TEMPLATE = 'profile.html'


@login_required(login_url='/login')
def Profile(request, *args, **kwargs):
    """Authenticated User Profile."""
    import pdb; pdb.set_trace()
    return render(request, PROFILE_TEMPLATE)
