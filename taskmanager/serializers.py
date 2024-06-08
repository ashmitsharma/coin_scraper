from rest_framework import serializers

class StartScrapingSerializer(serializers.Serializer):
    coins = serializers.ListField(
        child=serializers.CharField(max_length=10)
    )