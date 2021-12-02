from django.urls import path

from .views import CreateShortUrl, RetrieveUrl, index

urlpatterns = [
    path("", index),
    path("url", CreateShortUrl.as_view()),
    path("<str:short_url>", RetrieveUrl.as_view()),
]
