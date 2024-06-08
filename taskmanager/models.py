from django.db import models

class ScrapingTask(models.Model):
    job_id = models.CharField(max_length=255)
    coin = models.CharField(max_length=10)
    status = models.CharField(max_length=50, default='Pending')
    result = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.coin} - {self.job_id}"
