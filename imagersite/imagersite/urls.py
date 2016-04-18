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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .views import home_page, photo_view
from imager_profile.views import Profile
from imager_images.views import Library
from .views import home_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name="home_page"),
    url(r'^profile/$', Profile, name="profile"),
    url(r'^images/library$', Library, name='library'),
    url(r'^login$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^images/photos/(?P<user_id>[0-9]+)/(?P<photo_id>[0-9]+)', photo_view, name='photo_view')
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
