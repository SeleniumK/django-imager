from django.conf.urls import url
from .views import Profile, EditProfile

urlpatterns = [
    url(r'^$', Profile, name="profile"),
    url(r'^edit/', EditProfile.as_view(), name="edit")
]
