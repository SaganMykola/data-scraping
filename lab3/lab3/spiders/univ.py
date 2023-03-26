import scrapy
from bs4 import BeautifulSoup
from lab3.items import Lab3Item


class UnivSpider(scrapy.Spider):
    name = "univ"
    allowed_domains = ["univ.kiev.ua"]
    start_urls = ["http://www.univ.kiev.ua/ua/departments"]
    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        subdiv_list = soup.find(class_="b-body__holder")
        for li in subdiv_list.find_all("li"):
            a = li.find("a")
            subdiv_name = a.find(string=True, recursive=False)
            subdiv_url = f"http://www.univ.kiev.ua{a.get('href')}"
            #image_urls = f""
            yield Lab3Item(
                name=subdiv_name,
                url=subdiv_url,
                #image_urls=image_urls
            )
