# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.http import HtmlResponse
from scrapy.pipelines.images import ImagesPipeline

class LeroyparsePipeline:
    def __init__(self):
        mongo_client = MongoClient('localhost', 27017)
        self.mongo_base = mongo_client.leroymerlin


    def process_item(self, item, spider):
        item_character = {}
        for character, value in zip (item['characters_list'], item['values_list']):
            value = value.replace(' ', '').replace('\n', '')
            try:
                value = int(value)
            except:
                try:
                    value = float(value)
                except:
                    pass
            item_character[character] = value
        item['characters_list'] = item_character
        del item['values_list']
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item

class LeroyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['images']:
            for image in item['images']:
                try:
                    yield scrapy.Request(image)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
       item['images'] = [img[1] for img in results if img[0]]
       return item
    # def file_path(self, request, response=None, info=None, *, item=None):
