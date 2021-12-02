from rest_framework import serializers
from .models import Url

class UrlSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    url = serializers.CharField()
    short_url = serializers.ReadOnlyField()

    def create(self, validated_data: dict):
        url = Url()
        url.url = validated_data.get("url")
        url.short_url = Url.objects.generate_short_url()
        url.save()

        return url
