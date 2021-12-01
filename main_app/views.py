from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins

from .models import Url
from .serializers import UrlSerializer


class RetrieveUrl(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()

    def retrieve(self, request, short_url=None):
        queryset = Url.objects.all()
        url = get_object_or_404(queryset, short_url=short_url)

        serializer = UrlSerializer(url)

        return JsonResponse(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
