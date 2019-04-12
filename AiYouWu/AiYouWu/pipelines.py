# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from AiYouWu.settings import IMAGES_STORE
from scrapy.http import Request
import os

class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for img_url in item['img_urls']:
            referer = 'https://www.meitulu.com/img.html?img='+img_url
            headers = {'Referer':referer}
            yield Request(img_url,headers=headers,meta={'mid_data':item['title']})


    def file_path(self, request, response=None, info=None):
        title = request.meta['mid_data']
        img_path = os.path.join(IMAGES_STORE,title)
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        name = request.url.split('/')[-1]
        img_path = os.path.join(img_path,name)
        print(img_path)
        return img_path
