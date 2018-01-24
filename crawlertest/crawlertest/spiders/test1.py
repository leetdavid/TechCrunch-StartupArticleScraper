# -*- coding: utf-8 -*-
import scrapy
from crawlertest.items import CrawlertestItem

class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['techcrunch.com']
    start_urls = ['https://techcrunch.com/startups/']

    number = 2

    def parse(self, response):

        if response.status - 400 == 4 or self.number == 50:
            return

        for link in response.xpath("//h2[@class='post-title']/a/@href").extract():
            articleRequest = scrapy.Request(url=link, callback=self.articleParser)
            yield articleRequest


        nextUrl = self.start_urls[0] + 'page/' + str(self.number) + '/'
        self.number += 1
        nextPageReq = scrapy.Request(url=nextUrl, callback=self.parse)
        yield nextPageReq

    def articleParser(self, response):
        title = response.css("header.article-header h1::text").extract_first()
        content = "\n".join((response.css("div.article-entry").xpath("./p//text() | .//li//text()").extract())).replace('\n', ' ')
        item = CrawlertestItem()
        item['title'] = title
        item['text'] = content
        return item