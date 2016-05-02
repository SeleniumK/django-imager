from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import home_page
from imager_api import views


router = DefaultRouter()
router.register(r'photo', views.PhotoViewSet, base_name="photo")
router.register(r'album', views.AlbumViewSet, base_name="album")


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name="home_page"),
    url(r'^login$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^images/', include('imager_images.urls')),
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^api/v1/', include(router.urls)),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
