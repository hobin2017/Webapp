# -*- coding: utf-8 -*-
"""
You must create the project by running this command: scrapy startproject your_project_name
After creating the project,
scrapy crawl quotes
P.S.
My scrapy sits at: D:\01PythonFile\basicTest\04Scrapy\Scripts\scrapy.exe
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # It identifies the Spider and must be unique within a project

    def start_requests(self):
        """
        This function must return an iterable of Requests (scrapy.Request).
        :return:
        """
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        It will be called by scrapy.Request to handle the response.
        :param response: the type is the TextResponse class.
        :return:
        """
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' %page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' %filename)


class QuotesSpider2(scrapy.Spider):
    """
    A shortcut to the start_requests method.
    What is  more, the parse function can extract the information from the web-page.
    """
    name = 'quotes2'  # It identifies the Spider and must be unique within a project
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]

    def parse(self, response):
        """
        It will be called by scrapy.Request to handle the response.
        Compared with the QuotesSpider class, this spider will extract the data by using css() and extract() after we
        analysis the HTML web-page.
        :param response: the type is the TextResponse class.
        :return:
        """
        for quote in response.css('div.quote'):
            yield dict(text=quote.css('span.text::text').extract_first(),
                       author=quote.css('small.author::text').extract_first(),
                       tags=quote.css('div.tags a.tag::text').extract())


class QuotesSpider2_1(scrapy.Spider):
    """
    Compared with the QuotesSpider2 class, this class will crawl the link provided by the current page.
    """
    name = 'quotes2_1'  # It identifies the Spider and must be unique within a project
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
        ]

    def parse(self, response):
        """
        After all contents of current page are extracted, the next page given by the current page is crawled also.
        Compared with the QuotesSpider2_1 class, this class will automatically crawl the link provided by the current page.
        :param response: the type is the TextResponse class.
        :return:
        """
        for quote in response.css('div.quote'):
            yield dict(text=quote.css('span.text::text').extract_first(),
                       author=quote.css('small.author::text').extract_first(),
                       tags=quote.css('div.tags a.tag::text').extract())

        # the first way to crawl next link
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            # the first way to create next requests
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

            # the second way to create next requests
            # yield response.follow(next_page, callback= self.parse)

        # the second way to crawl next link
        for href in response.css('li.next a::attr(href)'):
            # response.follow forms the absolute url automatically.
            yield response.follow(href, callback=self.parse)


