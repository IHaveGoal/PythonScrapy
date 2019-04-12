# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request,FormRequest
from ZhiHu.items import ZhihuItem
from scrapy.selector import Selector


class ZhSpider(CrawlSpider):
    name = 'ZH'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/question/\d+#.*?'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/question/\d+'), callback='parse_item', follow=True),
    )

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2125.111 Safari/537.36",
        "Referer": "http://www.zhihu.com/"
    }

    def start_requests(self):
        return [Request('http://www.zhihu.com/login',meta={'cookiejar':1},callback=self.post_login)]

    def post_login(self,response):
        print('Prepring Login')
        xsrf = response.xpath('//input[@name="_xsrf"]/@@value').extract()[0]
        print(xsrf)

        return [FormRequest('http://www.zhihu.com/login',meta={'cookiejar':response.meta['cookiejar']},
    headers=self.headers,formdata={'_xsrf':xsrf,'email':'1043260502@qq.com','password':'151880308zrq'},
    callback=self.after_login,dont_filter=True)]

    def after_login(self,response):
        yield self.make_requests_from_url(url)


    def parse_item(self, response):
        problem = Selector(response)
        item = ZhihuItem()
        item['url'] = response.url
        item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        print(item['name'])
        item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        item['answer'] = problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        return item