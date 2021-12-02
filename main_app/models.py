from django.db import models
from .managers import UrlManager


class Url(models.Model):
    url = models.TextField(null=False)
    short_url = models.TextField(unique=True, null=False, max_length=255)
    objects = UrlManager()

class LinkVisits(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE, null=False, related_name="urls")
    ip_address = models.CharField(max_length=15, null=True)
    user_agent = models.CharField(null=True, max_length=255)
