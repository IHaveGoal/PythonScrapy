# -*- coding: utf-8 -*-
import scrapy
from ROSI.items import RosiItem
from urllib import request

class CrawlSpider(scrapy.Spider):
    name = 'ROSI_spider'
    allowed_domains = ['www.meinvtu123.net']
    start_urls = ['https://www.meinvtu123.net/a/56/32064.html']

    def parse(self, response):

        print(response)
        item = RosiItem()
        title = response.xpath('//div[@class="Title111"]/h3/text()').extract()[-1]
        print(title)
        item['title'] = title
        pic_urls = response.xpath('//div[@class="contenta"]/img/@src').extract()
        print(pic_urls)
        item['image_urls'] = pic_urls
        yield item

        next_urls = response.xpath('//div[@class="page"]/ul/a[last()]/@href').extract()[0]
        if next_urls:
            next_url = request.urljoin(response.url, next_urls)
            print(next_url)
            yield scrapy.Request(next_url,callback=self.parse)