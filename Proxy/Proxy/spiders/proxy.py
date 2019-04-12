# -*- coding: utf-8 -*-
import scrapy
import json

class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        ipaddr = json.loads(response.text)['origin']
        print(ipaddr)
        yield scrapy.Request(self.start_urls[0],dont_filter=True)
