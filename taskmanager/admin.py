from django.contrib import admin
from .models import ScrapingJob, ScrapingTask

class ScrapingTaskInline(admin.TabularInline):
    model = ScrapingTask
    extra = 0
    readonly_fields = ('coin', 'output', 'created_at')

@admin.register(ScrapingJob)
class ScrapingJobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'created_at')
    search_fields = ('job_id',)
    readonly_fields = ('job_id', 'created_at')
    inlines = [ScrapingTaskInline]

@admin.register(ScrapingTask)
class ScrapingTaskAdmin(admin.ModelAdmin):
    list_display = ('job', 'coin', 'created_at')
    search_fields = ('coin', 'job__job_id')
    readonly_fields = ('job', 'coin', 'output', 'created_at')
    list_filter = ('coin', 'created_at')