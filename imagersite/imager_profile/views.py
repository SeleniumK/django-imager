from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Profile(LoginRequiredMixin, TemplateView):
    # template = 
    pass
    # @login_required(login_url='/login')

