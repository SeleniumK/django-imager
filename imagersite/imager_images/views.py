from django.shortcuts import render
from django.contrib.auth.decorators import login_required

LIBRARY_TEMPLATE = 'library.html'


@login_required(login_url='/login')
def Library(request, *args, **kwargs):
    """Authenticated User Profile."""
    return render(request, LIBRARY_TEMPLATE)
