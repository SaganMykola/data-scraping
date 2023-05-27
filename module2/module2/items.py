# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Module2Item(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()
    stores = scrapy.Field()
    prices = scrapy.Field()
