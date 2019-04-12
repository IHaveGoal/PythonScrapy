# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,Spider
from urllib.request import quote
from TaoSelenium.items import TaoseleniumItem


class TaobaoSpider(scrapy.Spider):
    name = 'Taobao'
    allowed_domains = ['www.taobao.com']
    base_url = 'http://www.taobao.com/seacher?q='

    def start_requests(self):
        for keyword in self.settings.get('KETWORDS'):
            for page in range(1,self.settings.get('MAX_PAGE')+1):
                url = self.base_url + quote(keyword)
                yield Request(url, callback=self.parse, meta={'page':page}, dont_filter=True)


    def parse(self, response):
        products = response.xpath()
        fro product in products:
        item = TaoseleniumItem()
