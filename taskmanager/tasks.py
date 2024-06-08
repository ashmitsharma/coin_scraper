from celery import shared_task
from .models import ScrapingTask
import logging
from .scraper import CoinMarketCapScraper

logger = logging.getLogger(__name__)


@shared_task
def scrape_single_coin(job_id, coin):
    scraper = CoinMarketCapScraper()
    try:
        logger.info(f"Starting task for job_id: {job_id}, coin: {coin}")
        result = scraper.scrape_coin(coin)
        task = ScrapingTask.objects.get(job_id=job_id, coin=coin)
        task.status = 'Completed'
        task.result = result
        task.save()
        logger.info(f"Completed task for job_id: {job_id}, coin: {coin}")
    except Exception as e:
        logger.error(f"Error in task for job_id: {job_id}, coin: {coin} - {e}")
        raise e
