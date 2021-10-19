# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class Lesson6Pipeline:
    def __init__ (self):
        mongo_client = MongoClient('localhost', 27017)
        self.mongo_base = mongo_client.books

    def process_item(self, item, spider):

        if item['new_price'] == '':
            del item['new_price']

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        print()
        return item
