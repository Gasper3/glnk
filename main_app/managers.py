import random
import string

from django.conf import settings
from django.db import models


class UrlManager(models.Manager):
    def generate_short_url(self):
        letters = string.ascii_letters
        while True:
            short_url = ''.join(random.choice(letters) for _ in range(settings.SHORT_URL_SIZE))
            if not self.filter(short_url=short_url):
                break
        return short_url
