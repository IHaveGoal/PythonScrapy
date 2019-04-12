# -*- coding: utf-8 -*-

# Scrapy settings for Image360 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Image360'

SPIDER_MODULES = ['Image360.spiders']
NEWSPIDER_MODULE = 'Image360.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Image360 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


DOWNLOAD_DELAY = 1

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

ITEM_PIPELINES = {
   'Image360.pipelines.ImPipeline': 300,
   'Image360.pipelines.MongoPipeline': 301,
}
# from Image360.Image360.pipelines import Image360Pipeline

IMAGES_STORE = r'E:\Scrapy'
MONGO_URI = 'localhost'
MONGO_DB = 'images360'

