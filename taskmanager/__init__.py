from django.apps import AppConfig
import uuid

class TaskmanagerConfig(AppConfig):
    name = 'taskmanager'

    def ready(self):
        from .models import ScrapingJob, DEFAULT_JOB_ID
        if not ScrapingJob.objects.filter(job_id=DEFAULT_JOB_ID).exists():
            ScrapingJob.objects.create(job_id=DEFAULT_JOB_ID, status='Default')