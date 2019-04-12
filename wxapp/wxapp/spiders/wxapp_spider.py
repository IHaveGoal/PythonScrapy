# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem

class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+/article-.+\.html'), callback="parse_detail", follow=False),
    )


    def parse_detail(self,response):

        title = response.xpath("//h1[@class='ph']/text()").extract()[0]
        author_time = response.xpath('//p[@class="authors"]')
        author = author_time.xpath('./a/text()').extract()[0]
        time = author_time.xpath('.//span/text()').extract()[0]
        print(title,author,time)
        contents = response.xpath('//td[@id="article_content"]//text()').extract()
        # print(content)
        mh_content=''.join(contents)
        # for content in contents:
        #     if content is not None:
        #         mh_content += str(content).strip()

        item = WxappItem(title=title,author=author,time=time,mh_content=mh_content)

        yield item