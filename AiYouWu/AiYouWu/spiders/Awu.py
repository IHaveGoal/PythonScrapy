# -*- coding: utf-8 -*-
import scrapy,re
from urllib import request
from AiYouWu.items import AiyouwuItem

class AwuSpider(scrapy.Spider):
    name = 'Awu'
    allowed_domains = ['meitulu.com']

    def start_requests(self):
        for i in range(1,24):
            if i == 1:
                url = 'https://www.meitulu.com/t/aiyouwu/'
            else:
                url = 'https://www.meitulu.com/t/aiyouwu/{}.html'.format(str(i))
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        page_urls = response.xpath('//div[@class="boxs"]/ul/li/a/@href').extract()
        for page_url in page_urls:
            print(page_url)
            yield scrapy.Request(page_url,callback=self.img_parse,dont_filter=True)

    def img_parse(self,response):


        title = response.xpath('//div[@class="weizhi"]//h1/text()').extract()[0]
        title = re.sub('\d+/\d+','',title).strip()
        img_urls = response.xpath('//div[@class="content"]//img/@src').extract()
        print(title,img_urls)
        item = AiyouwuItem(title=title,img_urls=img_urls)
        yield item
        num = response.xpath('//div[@id="pages"]/span/text()').extract()[0]
        if '1' in num:
            next_urls = response.xpath('//div[@id="pages"]/a/@href').extract()[1:-1]
            for next_url in next_urls:
                next_url = request.urljoin(response.url,next_url)
                yield scrapy.Request(next_url,callback=self.img_parse)
