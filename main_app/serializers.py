from rest_framework import serializers

from .models import Url


class UrlSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    url = serializers.CharField()
    short_url = serializers.ReadOnlyField()

    def create(self, validated_data: dict):
        url, created = Url.objects.get_or_create(**validated_data)
        return url
