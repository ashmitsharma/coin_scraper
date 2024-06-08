import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StartScrapingSerializer
from .tasks import scrape_single_coin
from .models import ScrapingTask

class StartScrapingView(APIView):
    def post(self, request):
        serializer = StartScrapingSerializer(data=request.data)
        if serializer.is_valid():
            coins = serializer.validated_data['coins']
            job_id = str(uuid.uuid4())
            for coin in coins:
                ScrapingTask.objects.create(job_id=job_id, coin=coin, status='Pending')
                scrape_single_coin.delay(job_id, coin)
            return Response({"job_id": job_id}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        tasks = ScrapingTask.objects.filter(job_id=job_id)
        results = [
            {
                "coin": task.coin,
                "status": task.status,
                "result": task.result
            }
            for task in tasks
        ]
        return Response({"job_id": job_id, "tasks": results}, status=status.HTTP_200_OK)
