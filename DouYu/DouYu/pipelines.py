# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.images import ImagesPipeline
from DouYu.settings import IMAGES_STORE

class DYImages(ImagesPipeline):


    def file_path(self, request, response=None, info=None):
        # 导入文件地址
        image_store = IMAGES_STORE

        # 提取url中间数字作为图片名。
        name = request.url.split('/')[-1]

        # 自己构建文件地址
        filename = os.path.join(image_store, name)

        print(filename)
        return filename
