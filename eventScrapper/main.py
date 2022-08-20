from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from eventScrapper.spiders.mtickets_spider import EventsSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(EventsSpider)
process.start()