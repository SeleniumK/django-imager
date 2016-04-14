"""imagersite URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
# from .views import home_page, ClassView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',
        TemplateView.as_view(template_name='home.html'),
        name="home_page"),  # url contains nothing but slash
    # url(r'^$', ClassView.as_view(), name=home)
    url(r'^accounts/login', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^accounts/', include('registration.backends.hmac.urls'))
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
