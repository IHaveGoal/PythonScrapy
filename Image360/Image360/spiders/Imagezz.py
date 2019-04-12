# -*- coding: utf-8 -*-
import scrapy,json
from urllib import parse
from Image360.items import Image360Item

class ImagezzSpider(scrapy.Spider):
    name = 'Imagezz'
    allowed_domains = ['image.so.com']

    def start_requests(self):
        base_url = 'http://image.so.com/zj?'
        data = {'ch':'photography','listtype':'new'}
        for page in range(1,2):
            data['sn'] = page * 30
            parmas = parse.urlencode(data)
            url = base_url + parmas
            yield scrapy.Request(url,callback=self.parse)


    def parse(self, response):

        result = json.loads(response.text)
        for image in result.get('list'):
            item = Image360Item()
            item['id'] = image.get('id')
            item['image_urls'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')

            yield item