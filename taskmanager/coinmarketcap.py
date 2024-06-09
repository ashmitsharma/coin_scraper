import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CoinMarketCapScraper:

    def __init__(self):
        chrome_options = Options()
        # # chrome_options.add_argument("--headless")  # Ensure headless mode
        chrome_options.add_argument("--start-maximized")
        # self.driver = webdriver.Chrome(options=chrome_options)
        self.chrome_options = chrome_options
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)



    def scrape_coin(self, coin):
        url = f'https://coinmarketcap.com/'
        try:
            self.driver.get(url)
        except Exception as e:
            print(f"Failed to load URL: {e}")
            return None

        try:
            # Locate the div with class 'search-input-static' and click it to activate the input field
            time.sleep(3)
            search_div = self.driver.find_element(By.CLASS_NAME, 'search-input-static')
            search_div.click()
        except Exception as e:
            print(f"Failed to find or click search input static: {e}")
            return None

        try:
            # Wait until the input element with class 'desktop-input' appears
            wait = WebDriverWait(self.driver, 10)
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'desktop-input')))
        except Exception as e:
            print(f"Failed to locate desktop input: {e}")
            return None

        try:
            # Enter the search term
            search_input.send_keys(coin)

            # Wait for a short time before pressing Enter (using an explicit wait)
            time.sleep(2)  # Explicitly waiting for 1 second

            # Verify if the correct element contains the search term
            search_input.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Failed during search and verification: {e}")
            return None

        try:
            time.sleep(2)
            data = self.extract_data()
            return data
        except Exception as e:
            print(f"Failed to extract data: {e}")
            return None

    def extract_data(self):
        data = {}

        try:
            price_element = self.driver.find_element(By.CSS_SELECTOR,
                                                'div#section-coin-overview div.gNSoet.flexStart.alignBaseline > span')
            data['price'] = float(price_element.text.replace('$', '').replace(',', ''))
        except Exception as e:
            data['price'] = None
            print(f"Error extracting price: {e}")

        try:
            price_change_element = self.driver.find_element(By.CSS_SELECTOR,
                                                       'div#section-coin-overview p')
            price_change_text = price_change_element.text.split('%')[0].split()[-1]
            data['price_change'] = float(price_change_text)
            if price_change_element.get_attribute('color') == 'red':
                data['price_change'] = -data['price_change']
        except Exception as e:
            data['price_change'] = None
            print(f"Error extracting price change: {e}")

        try:
            market_cap_element = self.driver.find_element(By.CSS_SELECTOR,
                                                     'div#section-coin-stats div:nth-child(1) > div.bwRagp.iWXelA.flexBetween > dd')
            market_cap_text = market_cap_element.text
            market_cap = int(market_cap_text.split('$')[-1].replace(',', ''))
            data['market_cap'] = market_cap
        except Exception as e:
            data['market_cap'] = None
            print(f"Error extracting market cap: {e}")

        try:
            market_cap_rank_element = self.driver.find_element(By.CSS_SELECTOR,
                                                          'div#section-coin-stats div:nth-child(1) > div.bwRagp.iElHRj.BasePopover_base__tgkdS > div > span')
            market_cap_rank_text = market_cap_rank_element.text
            market_cap_rank = int(market_cap_rank_text.replace('#', ''))
            data['market_cap_rank'] = market_cap_rank
        except Exception as e:
            data['market_cap_rank'] = None
            print(f"Error extracting market cap rank: {e}")

        try:
            volume_element = self.driver.find_element(By.CSS_SELECTOR,
                                                 'div#section-coin-stats div:nth-child(2) > div.bwRagp.iWXelA.flexBetween > dd')
            volume_text = volume_element.text
            volume = int(volume_text.split('$')[-1].replace(',', ''))
            data['volume'] = volume
        except Exception as e:
            data['volume'] = None
            print(f"Error extracting volume: {e}")

        try:
            volume_rank_element = self.driver.find_element(By.CSS_SELECTOR,
                                                      'div#section-coin-stats div:nth-child(2) > div.bwRagp.iElHRj.BasePopover_base__tgkdS > div > span')
            volume_rank_text = volume_rank_element.text
            volume_rank = int(volume_rank_text.replace('#', ''))
            data['volume_rank'] = volume_rank
        except Exception as e:
            data['volume_rank'] = None
            print(f"Error extracting volume rank: {e}")

        try:
            volume_change_element = self.driver.find_element(By.CSS_SELECTOR,
                                                        'div#section-coin-stats div:nth-child(3) > div > dd')
            volume_change_text = volume_change_element.text.split('%')[0]
            volume_change = float(volume_change_text)
            data['volume_change'] = volume_change
        except Exception as e:
            data['volume_change'] = None
            print(f"Error extracting volume change: {e}")

        try:
            circulating_supply_element = self.driver.find_element(By.CSS_SELECTOR,
                                                             'div#section-coin-stats div:nth-child(4) > div > dd')
            circulating_supply_text = circulating_supply_element.text.split()[0]
            circulating_supply = int(circulating_supply_text.replace(',', ''))
            data['circulating_supply'] = circulating_supply
        except Exception as e:
            data['circulating_supply'] = None
            print(f"Error extracting circulating supply: {e}")

        try:
            total_supply_element = self.driver.find_element(By.CSS_SELECTOR,
                                                       'div#section-coin-stats div:nth-child(5) > div > dd')
            total_supply_text = total_supply_element.text.split()[0]
            total_supply = int(total_supply_text.replace(',', ''))
            data['total_supply'] = total_supply
        except Exception as e:
            data['total_supply'] = None
            print(f"Error extracting total supply: {e}")

        try:
            diluted_market_cap_element = self.driver.find_element(By.CSS_SELECTOR,
                                                             'div#section-coin-stats div:nth-child(7) > div > dd')
            diluted_market_cap_text = diluted_market_cap_element.text
            diluted_market_cap = int(diluted_market_cap_text.replace('$', '').replace(',', ''))
            data['diluted_market_cap'] = diluted_market_cap
        except Exception as e:
            data['diluted_market_cap'] = None
            print(f"Error extracting diluted market cap: {e}")

        contracts = []
        try:
            contract = {}
            contacts_name_element = self.driver.find_element(By.CSS_SELECTOR, 'div#__next span.dEZnuB')
            contacts_name_text = contacts_name_element.text.replace(':', '')
            contacts_address_element = self.driver.find_element(By.XPATH, '//a[@class="chain-name"]')
            href_value = contacts_address_element.get_attribute('href').split('/')[-1]
            contract['name'] = contacts_name_text
            contract['address'] = href_value
            contracts.append(contract)
            data['contracts'] = contracts
        except Exception as e:
            data['contracts'] = []
            print(f"Error extracting contracts: {e}")

        try:
            official_links = []
            try:
                official_links_element = self.driver.find_element(By.CSS_SELECTOR,
                                                         'div#__next div.cvkYMS.coin-info-links > div:nth-child(2) > div.bwRagp > div')
            except:
                official_links_element = self.driver.find_element(By.CSS_SELECTOR,
                                                          'div#__next div.cvkYMS.coin-info-links > div:nth-child(1) > div.bwRagp > div')
            official_links_a = official_links_element.find_elements(By.TAG_NAME, 'a')
            for official_link in official_links_a:
                link_data = {}
                link_data['name'] = official_link.text
                link_data['link'] = official_link.get_attribute('href')
                official_links.append(link_data)
            data['official_links'] = official_links
        except Exception as e:
            data['official_links'] = []
            print(f"Error extracting official links: {e}")

        try:
            social_links = []
            try:
                social_links_element = self.driver.find_element(By.CSS_SELECTOR,
                                                       'div#__next div.cvkYMS.coin-info-links > div:nth-child(3) > div.bwRagp > div')
            except Exception as e:
                social_links_element = self.driver.find_element(By.CSS_SELECTOR,
                                                                'div#__next div.cvkYMS.coin-info-links > div:nth-child(2) > div.bwRagp > div')

            social_links_a = social_links_element.find_elements(By.TAG_NAME, 'a')
            for social_link in social_links_a:
                link_data = {}
                link_data['name'] = social_link.text
                link_data['url'] = social_link.get_attribute('href')
                social_links.append(link_data)
            data['socials'] = social_links
        except Exception as e:
            data['socials'] = []
            print(f"Error extracting social links: {e}")


        return data

    def quit(self):
        if self.driver:
            self.driver.quit()

    def __del__(self):
        self.driver.quit()
