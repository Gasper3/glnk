from django.urls import path

from .views import ShortUrlViewSet

urlpatterns = [
    path("url", ShortUrlViewSet.as_view(), name="create-url"),
    path("<str:short_url>", ShortUrlViewSet.as_view(), name="get-url"),
]
