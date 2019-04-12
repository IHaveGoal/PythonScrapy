# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib import request
from YouGuo.items import YouguoItem

class YouguozzSpider(CrawlSpider):
    name = 'YouGuozz'
    allowed_domains = ['meinvtu123.net']
    start_urls = ['https://www.meinvtu123.net/a/56/list_56_1.html']
    #使用rules非常简单筛选出页面中下一页链接
    rules = (
        Rule(LinkExtractor(allow=r'.+a/56/list_56_.+\.html')),
        Rule(LinkExtractor(allow=r'.+a/56/\d+\.html'), follow=True, callback='parse_item')
    )

    def parse_item(self, response):

        #提取title，去除空h3
        title = response.xpath('//div[@class="contenta"]/img[1]/@alt').extract()[0]
        print(title)

        pic_urls = response.xpath('//div[@class="contenta"]/img/@src').extract()
        print(pic_urls)
        item = YouguoItem(title=title,image_urls=pic_urls)
        yield item


        next_urls = response.xpath('//div[@class="page"]/ul/a[last()]/@href').extract()[0]
        if next_urls:
            next_url = request.urljoin(response.url, next_urls)
            print(next_url)
            yield scrapy.Request(next_url, callback=self.parse_item)
