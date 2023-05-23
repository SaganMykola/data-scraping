import scrapy
from bs4 import BeautifulSoup
from module_2.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from module_2.items import Module2Item
import time


class EkSpider(scrapy.Spider):
    name = "ek"
    allowed_domains = ["ek.ua"]
    start_urls = [f"https://ek.ua/ua/list/91/"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10
            )


def parse(self, response):
    soup = BeautifulSoup(response.body, "html.parser")
    ekList = soup.find(id="list_form1")
    for ek in ekList:
        if ek:
            url = ek.find(name="a", class_="model-short-title").get("href")
            img_url = ek.find(name="img").get("src")
            store = ek.find(name="a", class_="model-short-title").find(string=True, recursive=False).strip()
            price = ek.find(name="td", class_="model-shop-price").find(string=True, recursive=False).strip()
            yield Module2Item(
                url=url,
                img_url=[img_url],
                store=[store],
                price=[price]
            )