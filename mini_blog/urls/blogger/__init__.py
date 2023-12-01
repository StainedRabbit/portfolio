from django.urls import include, path

from .profile import urlpatterns as profile_urlpatterns

urlpatterns = (
    [
        path("profile/", include(profile_urlpatterns)),
    ],
    "blogger",
)
