from celery import shared_task
from .coinmarketcap import CoinMarketCapScraper
from .models import ScrapingTask

@shared_task
def scrape_single_coin(coin, job_id):
    scraper = CoinMarketCapScraper()
    try:
        result = scraper.scrape_coin(coin)
        task = ScrapingTask.objects.get(coin=coin, job__job_id=job_id)
        task.output = result
        task.save()
    except Exception as e:
        task = ScrapingTask.objects.get(coin=coin, job__job_id=job_id)
        task.output = {'error': str(e)}
        task.save()