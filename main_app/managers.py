from django.db import models
import string
import random
from django.conf import settings

class UrlManager(models.Manager):
    def generate_short_url(self):
        letters = string.ascii_letters
        short_url = ''.join(random.choice(letters) for i in range(settings.SHORT_URL_SIZE))
        return short_url
