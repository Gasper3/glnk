from rest_framework import generics

from .models import Url
from .serializers import UrlSerializer


class ShortUrlViewSet(generics.RetrieveAPIView, generics.CreateAPIView):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
    lookup_field = 'short_url'
