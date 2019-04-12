# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FangItem(scrapy.Item):

    province = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    jushi = scrapy.Field()
    area = scrapy.Field()
    address = scrapy.Field()
    onsale = scrapy.Field()
    origin = scrapy.Field()


