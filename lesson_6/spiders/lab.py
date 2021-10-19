# II вариант
# 1) Создать пауков по сбору данных о книгах с сайтов labirint.ru и/или book24.ru
# 2) Каждый паук должен собирать:
# * Ссылку на книгу
# * Наименование книги
# * Автор(ы)
# * Основную цену
# * Цену со скидкой
# * Рейтинг книги
# 3) Собранная информация должна складываться в базу данных



import scrapy
from scrapy.http import HtmlResponse
from lesson_6.items import Lesson6Item


class LabSpider(scrapy.Spider):
    name = 'lab'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/genres/2994/', 'https://www.labirint.ru/best/']

    def parse(self, response:HtmlResponse):
        next_page = response.xpath('//a[@class = "pagination-next__text"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath('//a[@class = "cover"]/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.books_parse)




    def books_parse(self, response:HtmlResponse):
        name = response.xpath('//h1/text()').get()
        authors = response.xpath('//a[@data-event-label = "author"]/@data-event-content').get()
        reg_price = response.xpath('//span[@class = "buying-price-val-number"]/text()').get()
        new_price = ''
        if not reg_price:
            reg_price = response.xpath('//span[@class = "buying-priceold-val-number"]/text()').get()
            new_price = response.xpath('//span[@class = "buying-pricenew-val-number"]/text()').get()
        rating = response.xpath('//div[@id = "rate"]/text()').get()
        link = response.url
        item = Lesson6Item(name=name, authors=authors, reg_price=reg_price, new_price=new_price, rating=rating, link=link)
        yield item

