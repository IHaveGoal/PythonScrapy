# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from YouGuo.settings import IMAGES_STORE
from scrapy.http import Request
import os


class ImagesnamePipeline(ImagesPipeline):

    #调用这个函数这要是为了将title传给file_path使用，
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            #在请求img_url前，在请求中带上title参数
            yield Request(image_url,meta={'mid_item':item['title']})

    def file_path(self, request, response=None, info=None):
        #提取出title
        title = request.meta['mid_item']
        print(title)
        #依据title创建文件名
        image_store = os.path.join(IMAGES_STORE,title)
        if not os.path.exists(image_store):
            os.mkdir(image_store)
        #https://pic.meinvtu123.net/tupian/2019/allimg/190321/21133024-1-3B4.jpg
        #使用split('-')切割，提取最后一个作为文件名
        name = request.url.split('-')[-1]
        #构建完整存储路径并且返回
        filename = os.path.join(image_store, name)
        print(filename)

        return filename