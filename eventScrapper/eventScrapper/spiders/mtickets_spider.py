import scrapy

class EventsSpider(scrapy.Spider): 
   name = "mtickets_events"

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