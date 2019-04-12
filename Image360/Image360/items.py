# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Image360Item(scrapy.Item):

    collection = 'images'
    id = scrapy.Field()
    image_urls = scrapy.Field()
    title = scrapy.Field()
    thumb = scrapy.Field()
