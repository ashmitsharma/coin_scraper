# Coin Scraper Project

This repository contains the code for a Django REST Framework API to scrape cryptocurrency data from CoinMarketCap.

## Description

The project consists of two main components:
- A Django REST Framework API for scraping cryptocurrency data.
- A Celery task manager for executing scraping tasks asynchronously.

## Usage
### API Endpoints
#### Start Scraping
- URL: /api/taskmanager/start_scraping/
- Method: POST
- Description: Initiates scraping for a list of cryptocurrency coins.
```Request Body:
{
    "coins": ["BTC", "ETH", "XRP"]
}
```
 - Response: Returns a job ID for tracking the scraping task.
#### Scraping Status
- URL: /api/taskmanager/scraping_status/<job_id>/
- Method: GET
- Description: Retrieves the current status and data of a scraping job.
- Response:
```{
    "job_id": "d073e585-1638-4052-b9e2-721ac785847f",
    "tasks": [
        {
            "coin": "DUKO",
            "output": {
                "price": 0.004365,
                "price_change": -8.27,
                "market_cap": 42182345,
                "market_cap_rank": 692,
                "volume": 8465258,
                "volume_rank": 380,
                "volume_change": 20.07,
                "circulating_supply": 9663955990,
                "total_supply": 9999609598,
                "diluted_market_cap": 43647445,
                "contracts": [
                    {
                        "name": "Solana ",
                        "address": "HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"
                    }
                ],
                "official_links": [
                    {
                        "name": "Website",
                        "link": "https://dukocoin.com/"
                    }
                ],
                "socials": [
                    {
                        "name": "𝕏\nTwitter",
                        "url": "https://twitter.com/dukocoin"
                    },
                    {
                        "name": "Telegram",
                        "url": "https://t.me/+jlScZmFrQ8g2MDg8"
                    }
                ]
            }
        },
        {
        	 “coin”: “NOT”,
                    “output”: {
        			…
        		 }
            },
            {
        	 “coin”: “GORILLA”,
                    “output”: {
        			…
        		 }
            }
          ]
        }
```

## Screenshots

- Postman screenshot showing a correct POST request to start scraping.
![postman correct request](https://github.com/ashmitsharma/coin_scraper/assets/55889884/1c26f37a-e2a1-49a5-af5a-981d770c05e4)

- Postman screenshot showing a wrong POST request with invalid input.
![Postman Post Request Validation Check](https://github.com/ashmitsharma/coin_scraper/assets/55889884/440631ab-d030-4b1e-8563-1d09e619b04f)

- Postman screenshot showing a GET request to retrieve scraping status.
![postman correct get request](https://github.com/ashmitsharma/coin_scraper/assets/55889884/e8b76bb5-bda7-414a-9ab2-507838a1a84a)

- Admin dashboard screenshot displaying scraping and task tables.
![Admin Dashboard](https://github.com/ashmitsharma/coin_scraper/assets/55889884/158c21fd-cfad-467f-8649-4534c544a507)

- Admin panel screenshot showing the scraping table.
![Admin Scraping Job Table](https://github.com/ashmitsharma/coin_scraper/assets/55889884/e96c1f33-fb6c-4e76-bd4e-4a9d49d097da)

- Admin panel screenshot displaying data in the scraping table.
![Admin Scraping Job Table Data](https://github.com/ashmitsharma/coin_scraper/assets/55889884/022086ed-b3c3-4c72-a6b1-3e245d9a83c1)

- Admin panel screenshot showing the task table.
![Admin Scraping Tasks Table](https://github.com/ashmitsharma/coin_scraper/assets/55889884/025fc4a0-36c8-426e-8912-326a96046aeb)

- Admin panel screenshot displaying data in the task table.
![Admin Scraping Tasks Data](https://github.com/ashmitsharma/coin_scraper/assets/55889884/f2d9f8e6-d6f1-4fcb-8f44-0befe959d1ab)

- Screenshot of a GET request opened in a web browser.
  ![Browser Api Dsta View](https://github.com/ashmitsharma/coin_scraper/assets/55889884/735bad16-0319-42a6-8f78-16539529bcf5)
