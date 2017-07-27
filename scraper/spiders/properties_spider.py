import re
import scrapy
from scraper.items import Property
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class QuotesSpider(CrawlSpider):
    name = "properties"

    allowed_domains = ["domimmo.com"]
    start_urls = (
        'http://www.domimmo.com/martinique/vente/appartement/34-schoelcher',
    )

    rules = (

        # Extract links
        # and follow links from them (since no callback means follow=True by default).
        #Rule(LinkExtractor(allow=('appartement', ), )),
        # Rule(LinkExtractor(allow=('maison', ), )),
        #Rule(LinkExtractor(allow=('terrain', ), )),
        #Rule(LinkExtractor(allow=('34-schoelcher', ), )),
        #Rule(LinkExtractor(allow=('6-fort-de-france', ), )),

        # Extract links and parse them with the spider's method parse_page
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//li[@class="kdpli kdpnext"]')), callback='parse_start_url', follow= True),

    )

    #rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//li[@class="kdpnext"]/a/@href',)), callback="parse", follow= True),)


    # def start_requests(self):
    #     urls = [
    #         'http://www.domimmo.com/martinique/vente/maison/34-schoelcher/page/1',
    #         'http://www.domimmo.com/martinique/vente/maison/34-schoelcher/page/2',
    #         'http://www.domimmo.com/martinique/vente/maison/34-schoelcher/page/3'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse_start_url(self, response):
        for prop in response.css('ul.e46 li.e47'):
            l = ItemLoader(item=Property(), selector=prop)
            l.add_css('link', 'a::attr(href)')
            l.add_css('img', 'img::attr(src)')
            l.add_css('cat', 'span.e55 b::text')
            l.add_css('code', 'span.e56 b::text')
            l.add_css('city', 'span.e57 b::text')
            l.add_css('title', 'div.e58 b::text')
            l.add_css('date', 'div.e52::text')
            l.add_css('price', 'div.e59::text')
            l.add_css('description', 'div.e61::text')
            ref = prop.css('a::attr(href)').extract_first()
            m = re.search('(?<=\/)\d+', ref)
            l.add_value('myid', m.group(0))
            #l.add_value('last_updated', 'today') # you can also use literal values
            yield l.load_item()

    #def parse(self, response)
    #    for prop in response.css('ul.e46 li.e47'):
            # yield {
            #     'id': prop.css('a::attr(href)').extract_first(),
            #     'img': prop.css('img::attr(src)').extract_first(),
            #     'title': prop.css('div.e58 b::text').extract_first(),
            #     'date': prop.css('div.e52::text').extract_first(),
            #     'price': prop.css('div.e59::text').extract_first(),
            #     'description': prop.css('div.e61::text').extract_first()
            # }
