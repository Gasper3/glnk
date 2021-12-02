from django.http import response
from rest_framework import generics

from .models import Url
from .serializers import UrlSerializer


def index(request):
    return response.HttpResponse()


class RetrieveUrl(generics.RetrieveAPIView):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
    lookup_field = 'short_url'

class CreateShortUrl(generics.CreateAPIView):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
