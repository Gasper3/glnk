from django.db import models
import string
import random

class UrlManager(models.Manager):
    def generate_short_url(self):
        letters = string.ascii_letters
        short_url = ''.join(random.choice(letters) for i in range(5))
        return short_url
