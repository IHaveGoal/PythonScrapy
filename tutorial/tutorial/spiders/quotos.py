# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class QuotosSpider(scrapy.Spider):
    name = 'quotos'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = TutorialItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tag.tag::text').extract()
            yield item

        next = response.css('.pagger .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url,callback=self.parse)