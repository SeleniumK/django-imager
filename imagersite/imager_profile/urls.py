from django.conf.urls import url
from .views import Profile

urlpatterns = [
    url(r'^$', Profile, name="profile"),
]
