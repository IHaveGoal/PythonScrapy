# -*- coding: utf-8 -*-

# Scrapy settings for Fang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Fang'

SPIDER_MODULES = ['Fang.spiders']
NEWSPIDER_MODULE = 'Fang.spiders'

ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

DOWNLOADER_MIDDLEWARES = {
   'Fang.middlewares.FangDownloaderMiddleware': 543,
}

# Scrapy-Redis相关配置
# 启用redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 确保所有爬虫共享相同的去重指纹
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 设置redis为RedisPipeline
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# 在redis中保持scrapy-redis用到的队列，停止爬取不会清理redis中的队列，从而可以实现暂停和恢复的功能。
SCHEDULER_PERSIST = True

# 设置连接redis信息
REDIS_HOST = '192.168.199.184'
REDIS_PORT = 6379