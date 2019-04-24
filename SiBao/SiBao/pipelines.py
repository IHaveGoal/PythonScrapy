# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from SiBao.settings import IMAGES_STORE
from scrapy.http import Request
import os

class SiBaoImgpipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img_url in item['img_urls']:
            yield Request(img_url,meta={'mid':item['title']})

    def file_path(self, request, response=None, info=None):
        title = request.meta['mid']
        img_path = os.path.join(IMAGES_STORE, title)
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        name = request.url.split('-')[-1]
        img_path = os.path.join(img_path,name)
        print(img_path)
        return img_path

import pymongo
class Mongopipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    # 借助from_crawler实现在初始化之前对settings参数调用
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self,item,spider):
        #插入数据
        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self,spider):
        #关闭连接
        self.client.close()