# Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости.
# Для парсинга использовать XPath. Структура данных должна содержать:

# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.
# Сложить собранные новости в БД


from datetime import datetime, timedelta
from lxml import html
import requests

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError as dke


client = MongoClient('127.0.0.1', 27017)
db = client['yandex_news']
news_db = db.news

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
url = "https://yandex.ru/news/"
response = requests.get(url)
dom = html.fromstring(response.text)

items = dom.xpath("//article")

all_news = []

for item in items:
    news = {}
    source_name = item.xpath(".//a[@class='mg-card__source-link']/text()")
    name = item.xpath(".//h2[@class='mg-card__title']/text()")
    link = item.xpath(".//a[@class='mg-card__link']/@href")
    data = item.xpath(".//span[@class='mg-card-source__time']/text()")
    if len(data[0]) == 5:
        data = str( datetime.now().date()) + ' ' + data[0]
    elif 'вчера' in data[0]:
        yesterday = datetime.now().date() - timedelta(days=1)
        data = str(yesterday) + data[0]
    else:
        data = data[0]
    news['source_name'] = source_name[0]
    news['name'] = name[0]
    news['link'] = link[0]
    news['data'] = data

    if len(list(news_db.find({'link': link[0]}))) == 0:
        try:
            news_db.insert_one(news)
        except dke:
            pass
