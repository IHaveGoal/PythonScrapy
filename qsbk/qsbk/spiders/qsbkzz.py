# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkzzSpider(scrapy.Spider):
    name = 'qsbkzz'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        print(type(response.body))
        print(type(response.text))
        contents = response.xpath('//div[@id="content-left"]')

        for content in contents:

            author = content.xpath('.//h2/text()').extract()
            print(author)
            neirong = content.xpath('.//div[@class="content"]/span/text()').extract()
            print(neirong)
            item = QsbkItem(author=author,neirong=neirong)
            yield item

            next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract()[0]
            print(next_url)

            if next_url is not None:
                next_url = 'https://www.qiushibaike.com'+next_url
                print(next_url)
                yield  scrapy.Request(next_url,callback=self.parse)
