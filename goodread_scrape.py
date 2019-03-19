import scrapy

class GoodReadsSpider(scrapy.Spider)
    name="GoodReads"

    def start_requests(self):
        url = ''
        urls = [
            'https://www.goodreads.com/quotes?page=1',
            'https://www.goodreads.com/quotes?page=2',
            'https://www.goodreads.com/quotes?page=3',
            'https://www.goodreads.com/quotes?page=4',
            'https://www.goodreads.com/quotes?page=5',
            'https://www.goodreads.com/quotes?page=6',
            'https://www.goodreads.com/quotes?page=7',
            'https://www.goodreads.com/quotes?page=8',
            'https://www.goodreads.com/quotes?page=9',
            'https://www.goodreads.com/quotes?page=10',
            'https://www.goodreads.com/quotes?page=11',
            'https://www.goodreads.com/quotes?page=12'
        ]

        for url oin urls:
            yield scrapy.Requests(url=url, callback=self.parse)