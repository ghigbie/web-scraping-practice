import scrapy

class GoodReadSpider(scrapy.Spider):
    name ="GoodReads"
    

    def start_requests(self):
        url = 'https://www.goodreads.com/quotes?page=1'


    def parse(self, response):
        for quote in response.selector.xpath("//div[@class='quote']"):
            yield{
                'text' : quote.xpath("//div[@class='quoteText')/text()[1]").extract_first(),
                'author' : quote.xpath("//div[@class='quoteText')/child::a/text()").extract_first(),
                'tag':  quote.xpath("//div[@class='quoteText']/text()[1]").extract_first(),
            }