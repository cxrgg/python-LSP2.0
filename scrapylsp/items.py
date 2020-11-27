# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemName(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()

class ItemImage(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    imgUrl = scrapy.Field()

