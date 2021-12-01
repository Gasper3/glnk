from django.urls import path
from rest_framework import routers

from .views import RetrieveUrl

urlpatterns = [
    path("<str:short_url>", RetrieveUrl.as_view())
]
