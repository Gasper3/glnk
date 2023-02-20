import random
import string

from django.conf import settings


def generate_short_url():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(settings.SHORT_URL_SIZE))
