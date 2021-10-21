# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def clear_price(value):
    try:
        cleared_value = int(value)
        return cleared_value
    except:
        return value

class LeroyparseItem(scrapy.Item):


    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(clear_price), output_processor=TakeFirst())
    _id = scrapy.Field()
    images = scrapy.Field()
    characters_list = scrapy.Field()
    values_list = scrapy.Field()
