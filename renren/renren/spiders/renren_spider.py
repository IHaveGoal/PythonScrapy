# -*- coding: utf-8 -*-
import scrapy


class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        data = {
            'email': '15313299416',
            'password': '151880308'
        }
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request

    def parse_page(self,response):
        request = scrapy.Request(url='http://www.renren.com/968910325/profile',callback=self.parse_file)
        yield request

    def parse_file(self,response):
        with open('renren.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
