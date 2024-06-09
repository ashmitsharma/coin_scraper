from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StartScrapingSerializer, ScrapingJobSerializer, ScrapingTaskSerializer
from .models import ScrapingJob, ScrapingTask
from .tasks import scrape_single_coin

class StartScrapingView(APIView):
    def post(self, request):
        coins = request.data.get("coins", [])
        # Check if all elements in the list are strings
        if not all(isinstance(coin, str) for coin in coins):
            return Response({"error": "All coins should be strings"}, status=status.HTTP_400_BAD_REQUEST)
        # Check if any coin name is empty
        if any(not coin.strip() for coin in coins):
            return Response({"error": "Coin names cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = StartScrapingSerializer(data=request.data)
        if serializer.is_valid():
            coins = serializer.validated_data['coins']
            job = ScrapingJob.objects.create()
            for coin in coins:
                ScrapingTask.objects.create(job=job, coin=coin)
                scrape_single_coin.delay(coin, str(job.job_id))  # Pass job_id as a string
            return Response({"job_id": job.job_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        try:
            job = ScrapingJob.objects.get(job_id=job_id)
            tasks = ScrapingTask.objects.filter(job=job)
            task_serializer = ScrapingTaskSerializer(tasks, many=True)
            return Response({
                "job_id": job_id,
                "tasks": task_serializer.data
            })
        except ScrapingJob.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
