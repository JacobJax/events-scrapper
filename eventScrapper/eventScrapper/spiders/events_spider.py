import scrapy
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
from scrapy.utils.log import configure_logging

class MticketsSpider(scrapy.Spider): 
   name = "mtickets"

   start_urls = [
      "https://mtickets.com/events/upcoming"
   ]

   def parse(self, response):
      
      posts = response.css('.search-result-item')
      for post in posts:
         yield {
            'title': post.css('.event-title a strong::text').get(),
            'price': post.css('.search-result-item-price strong::text').get(),
            'link' :post.css('.search-result-item a::attr(href)').get(),
            'time' :post.css('.event-info-about p::text')[1].get()
         }
      
      next_page = response.css('.pagination li a::attr(href)')[1].get()
      if next_page is not None:
         next_page = response.urljoin(next_page)
         yield scrapy.Request(next_page, callback=self.parse)


class TicketsasaSpider(scrapy.Spider): 
   name = "ticketsasa"

   start_urls = [
      "https://www.ticketsasa.com/events"
   ]

   def parse(self, response):
      
      posts = response.css('.tkt-evt')
      for post in posts:
         yield {
            'title': post.css('.evt-info h3 a span::text').get(),
            'time': post.css('.evt-info a::attr(content)')[0].get(),
            'link': f"https://www.ticketsasa.com{post.css('.image::attr(href)').get()}"
         }

configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
   yield runner.crawl(MticketsSpider)
   yield runner.crawl(TicketsasaSpider)
   reactor.stop()

crawl()
reactor.run()