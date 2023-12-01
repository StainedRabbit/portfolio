from django.urls import include, path

from .blogger import urlpatterns as blogger_urlpatterns

app_name = "mini_blog"

urlpatterns = [
    path("blogger/", include(blogger_urlpatterns)),
]
