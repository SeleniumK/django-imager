from __future__ import unicode_literals
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView


def home_page(request, *args, **kwargs):
    foo = 'garbanzobeans'
    return render(request, 'home.html', context={'foo': foo})


class ClassView(TemplateView):
    """Class view for Home.html."""

    template_name = 'home.html'

    def get_context_data(self, id=1):
        """Foo Context for home template."""
        foo = 'garbanzobeans'
        return {'foo': foo}
