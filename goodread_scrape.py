import scrapy

class GoodReadsSpider(scrapy.Spider):
    name="GoodReads"

    def start_requests(self):
        url = 'https://www.goodreads.com/quotes?page=1'
        # urls = [
        #     'https://www.goodreads.com/quotes?page=1',
        #     'https://www.goodreads.com/quotes?page=2',
        #     'https://www.goodreads.com/quotes?page=3',
        #     'https://www.goodreads.com/quotes?page=4',
        #     'https://www.goodreads.com/quotes?page=5',
        #     'https://www.goodreads.com/quotes?page=6',
        #     'https://www.goodreads.com/quotes?page=7',
        #     'https://www.goodreads.com/quotes?page=8',
        #     'https://www.goodreads.com/quotes?page=9',
        #     'https://www.goodreads.com/quotes?page=10',
        #     'https://www.goodreads.com/quotes?page=11',
        #     'https://www.goodreads.com/quotes?page=12'
        # ]

        # for url in urls:
        #     yield scrapy.Requests(url=url, callback=self.parse)
    
    def parse(self, response):
        for quote in response.selector.xpath("//div[@class='quote']"):
            yield {
                'text' : quote.xpath("//div[@class='quoteText')/text()[1]").extract_first(),
                'author': quote.xpath("//div[@class='quoteText')/child::a/text()").extract_first(),
                'tags': quote.xpath("//div[@class='grey']/text()[1]").extract_first(),
            }
        # pagenumber = response.url.split("=")[1]
        # _file="{0}.html".format(pagenumber)

        # with open(_file, "wb") as f:
        #     f.write(response.body)