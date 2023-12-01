from django.urls import path

from mini_blog.views.blogger import profile

urlpatterns = (
    [
        path("", profile.IndexView.as_view(), name="index"),
    ],
    "profile",
)
