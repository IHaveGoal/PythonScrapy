# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from ROSI.settings import IMAGES_STORE
import os

class ImagesnamePipeline(ImagesPipeline):

        # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):

        # 提取url中间数字作为图片名。
        image_store = IMAGES_STORE
        name =  request.url.split('-')[-2] + '.jpg'
        filename = os.path.join(image_store,name)
        print(filename)

        return filename

