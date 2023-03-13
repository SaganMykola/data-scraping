import scrapy
from lab2.items import Lab2Item


class UnivCssSpider(scrapy.Spider):
    name = "univ_css"
    allowed_domains = ["univ.kiev.ua"]
    start_urls = ["http://www.univ.kiev.ua/ua/departments"]

    def parse(self, response):
        subdiv_list = response.css('div.b-references').css('.b-references__item')

        for subdiv in subdiv_list:
            name = subdiv.css('a.b-references__link::text').get()
            url = subdiv.css('a.b-references__link::attr(href)').get()
            yield Lab2Item(
                name=name,
                url=url
            )