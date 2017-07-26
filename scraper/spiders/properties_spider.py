import scrapy
from scraper.items import Property
from scrapy.loader import ItemLoader

class QuotesSpider(scrapy.Spider):
    name = "properties"

    def start_requests(self):
        urls = [
            'http://www.domimmo.com/martinique/vente/maison/34-schoelcher/page/1',
            'http://www.domimmo.com/martinique/vente/maison/34-schoelcher/page/2',
            'http://www.domimmo.com/martinique/vente/maison/34-schoelcher/page/3'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for prop in response.css('ul.e46 li.e47'):
            l = ItemLoader(item=Property(), selector=prop)
            l.add_css('id', 'a::attr(href)')
            l.add_css('img', 'img::attr(src)')
            l.add_css('title', 'div.e58 b')
            l.add_css('date', 'div.e52')
            l.add_css('price', 'div.e59')
            l.add_css('description', 'div.e61')
            #l.add_value('last_updated', 'today') # you can also use literal values
            yield l.load_item()
            # yield {
            #     'id': prop.css('a::attr(href)').extract_first(),
            #     'img': prop.css('img::attr(src)').extract_first(),
            #     'title': prop.css('div.e58 b::text').extract_first(),
            #     'date': prop.css('div.e52::text').extract_first(),
            #     'price': prop.css('div.e59::text').extract_first(),
            #     'description': prop.css('div.e61::text').extract_first()
            # }
