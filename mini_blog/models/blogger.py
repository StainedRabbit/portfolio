from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Blogger(AbstractUser):
    about_me = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Blogger")
        verbose_name_plural = _("Bloggers")
        default_related_name = "bloggers"