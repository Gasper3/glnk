import random
import string

from django.conf import settings
from django.db import models


class UrlManager(models.Manager):
    def generate_short_url(self):
        letters = string.ascii_letters
        short_url = ''.join(random.choice(letters) for i in range(settings.SHORT_URL_SIZE))
        while self.filter(short_url=short_url):
            short_url = ''.join(random.choice(letters) for i in range(settings.SHORT_URL_SIZE))
        return short_url
