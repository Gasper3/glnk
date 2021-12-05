from rest_framework import serializers

from .models import Url


class UrlSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    url = serializers.URLField()
    short_url = serializers.ReadOnlyField()

    def create(self, validated_data: dict):
        ip_address = self.get_ip_address_from_request()
        user_agent = self.get_user_agent_from_request()

        url, created = Url.objects.get_or_create(**validated_data, defaults={
            "short_url": Url.objects.generate_short_url(),
            "ip_address": ip_address,
            "user_agent": user_agent
        })
        return url

    def get_ip_address_from_request(self):
        request = self.context.get("request")

        if request and hasattr(request, "META"):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                return x_forwarded_for.split(',')[0]
            else:
                return request.META.get('REMOTE_ADDR')

    def get_user_agent_from_request(self):
        request = self.context.get("request")

        if request and hasattr(request, "META"):
            return request.META.get('HTTP_USER_AGENT')
