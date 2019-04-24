# -*- coding: utf-8 -*-
import scrapy
from SiBao.items import SibaoItem
from urllib import parse

class SbzzSpider(scrapy.Spider):
    name = 'SBzz'
    allowed_domains = ['meinvtu123.net']
    def start_requests(self):
        for i in range(1,7):
            url = 'https://www.meinvtu123.net/a/47/list_47_{}.html'.format(str(i))
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        lis = response.xpath('//ul[@class="wp-list clearfix"]/li')
        for li in lis:
            title = li.xpath('.//a[@target="_blank"]/@title').extract()[0].strip()
            detail_url = li.xpath('.//a[@target="_blank"]/@href').extract()[0]
            print(title,detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'title':title})
            # break

    def parse_detail(self,response):
        title = response.meta['title']
        print(title)
        img_urls = response.xpath('//div[@class="contenta"]/img/@src').extract()
        item = SibaoItem(title=title, img_urls=img_urls)
        yield item

        try:
            next_page = response.xpath('//div[@class="page"]/ul/a[contains(.,"下一页")]/@href').extract()[0]
            next_url = parse.urljoin(response.url, next_page)
            yield scrapy.Request(next_url, callback=self.parse_detail,meta={'title':title})
        except Exception:
            print(self.title,'读取完成')


