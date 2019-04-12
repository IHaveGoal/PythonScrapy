import pymongo

class MongoPipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        #MongoDB的ip和数据库名
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    #借助from_crawler实现在初始化之前对settings参数调用
    @classmethod
    def from_crawler(cls,crawler):
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


from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class ImPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        url = item['image_urls']
        #下载链接的图片
        yield Request(url)

    def file_path(self,request,response=None,info=None):
        #借助url定义文件名
        url = request.url
        file_name = url.split('/')[-1]
        print(file_name)
        return file_name

    def item_completed(self,results,item,info):
        #确认图片下载完成
        image_path = [x['path'] for ok,x in results if ok]
        if not image_path:
            raise DropItem('Image Download Faild')
        yield item