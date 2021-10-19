from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from lesson_6 import settings
from lesson_6.spiders.lab import LabSpider

# from jobparser.spiders.sjru import SjruSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LabSpider)
    # process.crawl(SjruSpider)

    process.start()
