# -*- coding: utf-8 -*-
import scrapy

class OnePageSpider(scrapy.Spider):
    name = 'one_page'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/egr/']

    def parse(self, response):
    	jobs = response.xpath('//p[@class="result-info"]')
    	
    	for job in jobs:
    		title = job.xpath('a/text()').extract_first()
    		address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
    		urls = job.xpath('a/@href').extract_first()

    		yield {'URL' : urls, 'Title' : title, 'Address' : address}
