import scrapy
from scrapy.http import HtmlResponse

from lesson_7.leroyparse.items import LeroyparseItem
from scrapy.loader import ItemLoader


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']


    def __init__(self, query):
        super().__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={query}']


    def parse(self, response:HtmlResponse):
        next_page = response.xpath('//a[@data-qa-pagination-item = "right"]/@href').get() #у меня не получилось e, перестает обрабатывать страницы
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath('//a[@data-qa = "product-image"]/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.leroy_parse)




    def leroy_parse(self, response:HtmlResponse):

        loader = ItemLoader(item=LeroyparseItem(), response=response)
        loader.add_value('link', response.url)
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('price', '//span[@slot = "price"]/text()')
        loader.add_xpath('images', '//source[@media=" only screen and (min-width: 1024px)"]/@data-origin')
        loader.add_xpath('characters_list', '//dt/text()')
        loader.add_xpath('values_list', '//dd[@class="def-list__definition"]/text()')
        print()
        # name = response.xpath('//h1/text()').get()
        # price = response.xpath('//span[@slot = "price"]/text()').get()
        # characters_html = response.xpath('//dl[@class = "def-list"]').getall()
        # images = response.xpath('//source[@media=" only screen and (min-width: 1024px)"]/@data-origin').getall()

        # yield LeroyparseItem(name=name, price=price, link=response.url, images=images)
        yield loader.load_item()