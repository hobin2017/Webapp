# -*- coding: utf-8 -*-
"""
   The crawl started by making requests to the URLs defined in the start_urls variable. And then it called the default
function 'parse', passing the response object as an argument.
Running script as below:
D:\01PythonFile\basicTest\04Scrapy\Scripts\scrapy.exe  runspider  D:\01PythonFile\basicTest\04Scrapy\official_tutorial1\first_spider.py  -o first_spider_result.json
or
D:\01PythonFile\basicTest\04Scrapy\Scripts\scrapy.exe  runspider  D:\01PythonFile\basicTest\04Scrapy\official_tutorial1\first_spider.py  -o first_spider_result.jl
The first_spider_result.json file will be saved under where the cmd is opened.
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes1"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        """
        :param response:
        :return:
        """
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

