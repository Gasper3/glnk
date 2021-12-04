from django.urls import path

from .views import CreateShortUrl, RetrieveUrl, index

urlpatterns = [
    path("", index),
    path("url", CreateShortUrl.as_view(), name="create-url"),
    path("<str:short_url>", RetrieveUrl.as_view(), name="get-url"),
]
