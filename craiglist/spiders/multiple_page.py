# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class MultiplePageSpider(scrapy.Spider):
    name = 'multiple_page'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/egr/']

    def parse(self, response):
        jobs = response.xpath('//p[@class="result-info"]')
        
        for job in jobs:
        	title = job.xpath('a/text()').extract_first()
        	address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
        	urls = job.xpath('a/@href').extract_first()

        	yield {'URL' : urls, 'Title' : title, 'Address' : address}

        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)

        yield Request(absolute_next_url, callback=self.parse)
