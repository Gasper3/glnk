from rest_framework import serializers
from .models import Url

class UrlSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    url = serializers.CharField()
    short_url = serializers.CharField()
