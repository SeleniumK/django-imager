from django.conf.urls import url
from .views import Profile, edit_user_profile

urlpatterns = [
    url(r'^$', Profile, name="profile"),
    url(r'^edit/', edit_user_profile, name="edit")
]
