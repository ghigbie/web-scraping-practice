import scrapy

class GoodReadsSpider(scrapy.Spider)
    name="GoodReads"

    def start_requests(self):
        url = ''
        urls = [

        ]

        for url oin urls:
            yield scrapy.Requests(url=url, callbak=self.parse)