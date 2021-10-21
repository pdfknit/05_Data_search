# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lesson6Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    authors = scrapy.Field()
    reg_price = scrapy.Field()
    new_price = scrapy.Field()
    rating = scrapy.Field()
    link = scrapy.Field()
    _id = scrapy.Field()
