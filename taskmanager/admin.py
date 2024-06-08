from django.contrib import admin
from .models import ScrapingTask

@admin.register(ScrapingTask)
class ScrapingTaskAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'coin', 'status', 'created_at', 'updated_at')
    search_fields = ('job_id', 'coin')
    list_filter = ('status', 'created_at')
