import scrapy
from lab3.items import Lab3Item


class UnivXpathSpider(scrapy.Spider):
    name = "univ_xpath"
    allowed_domains = ["univ.kiev.ua"]
    start_urls = ["http://www.univ.kiev.ua/ua/departments"]

    def parse(self, response):
        subdiv_list = response.xpath('//div[contains(@class, "b-references")]').xpath('.//li[contains(@class, "b-references")]')

        for subdiv in subdiv_list:
            name = subdiv.xpath('.//a[contains(@class, "b-references__link")]/text()').get()
            url = subdiv.xpath('.//a[contains(@class, "b-references__link")]/@href').get()
            yield Lab3Item(
                name=name,
                url=url
            )