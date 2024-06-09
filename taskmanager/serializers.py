from rest_framework import serializers
from .models import ScrapingJob, ScrapingTask

class ScrapingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapingTask
        fields = ('coin', 'output')

class ScrapingJobSerializer(serializers.ModelSerializer):
    tasks = ScrapingTaskSerializer(many=True, read_only=True)

    class Meta:
        model = ScrapingJob
        fields = '__all__'

class StartScrapingSerializer(serializers.Serializer):
    coins = serializers.ListField(
        child=serializers.CharField(max_length=10),
        allow_empty=False,
        help_text="List of coin acronyms to scrape"
    )

    def validate_coins(self, value):
        for coin in value:
            if not isinstance(coin, str):
                raise serializers.ValidationError("Each coin must be a string.")
        return value