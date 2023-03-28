import scrapy
from bs4 import BeautifulSoup
from module.items import ModuleItem


class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = [f"https://hotline.ua/ua/av/fotoapparaty/?p={page}" for page in range(1, 5)]

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")

        items = soup.find(name="div", class_="list-body").find_all(class_="list-item")
        for item in items:
            name = item.find(name="a", class_="list-item__title").find(string=True, recursive=False).strip()
            url = item.find(name="a", class_="list-item__title").get("href")
            price = item.find(class_="price__value").find(string=True, recursive=False)
            img_url = item.find(name="img").get("src")

            yield ModuleItem(
                name=name,
                price=price,
                url=url,
                img_url=[f"https://hotline.ua{img_url}"]
            )