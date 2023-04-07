import uuid

from config import settings


def generate_short_url() -> str:
    return uuid.uuid4().hex[:settings.short_url_size].upper()
