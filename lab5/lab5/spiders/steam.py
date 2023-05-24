import scrapy
from bs4 import BeautifulSoup
from lab5.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from lab5.items import Lab5Item
import time

class Lab5Spider(scrapy.Spider):
    name = "steam"
    allowed_domains = ["store.steampowered.com"]
    start_urls = ["https://store.steampowered.com/"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10
            )

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        steamList = soup.find_all("a", class_="tab_item")
        for steam in steamList:
            if steam:
                name = steam.find("div", class_="tab_item_name").find(string=True, recursive=False).strip()
                url = steam.get("href")
                image_url = steam.find("img").get("src")
                yield Lab5Item(
                        name = name,
                        url = url,
                        image_url = [image_url]
                    )
