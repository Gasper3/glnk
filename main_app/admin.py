from django.contrib import admin

from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    fields = ("url", "short_url", "ip_address", "user_agent")
    list_display = ("url", "ip_address", "user_agent")
