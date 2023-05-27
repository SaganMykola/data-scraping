import scrapy
from bs4 import BeautifulSoup
from module2.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from module2.items import Module2Item
import time

class Module2Spider(scrapy.Spider):
    name = "ek"
    allowed_domains = ["ek.ua"]
    start_urls = [f"https://ek.ua/ua/list/239/?p={page}" for page in range(1, 376)]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10
            )

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        ekList = soup.find_all("table", class_="model-short-block")
        for ek in ekList:
            name = ek.find("span", class_="u").find(string=True, recursive=False).strip()
            url = ek.find("a").get("href")
            image_url = ek.find("img").get("src")
            stores = []
            prices = []
            for store in ek.find_all("td", class_="model-shop-name"):
                store_names = store.find("u").find(string=True, recursive=False).strip()
                stores.append(store_names)

            for items in ek.find_all("td", class_="model-shop-price"):
                price = items.find("a").find(string=True, recursive=False).strip().replace(" ", "")
                prices.append(price)

            yield Module2Item(
                    name = name,
                    url = f"https://ek.ua/{url}",
                    image_url = [image_url],
                    stores = stores,
                    prices = prices
                )