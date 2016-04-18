from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
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
    url(r'^accounts/', include('registration.backends.hmac.urls'))
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
