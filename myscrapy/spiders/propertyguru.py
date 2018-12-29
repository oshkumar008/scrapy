# -*- coding: utf-8 -*-
import scrapy


class PropertyguruSpider(scrapy.Spider):
    name = 'propertyguru'
    allowed_domains = ['www.propertyguru.com.sg']
    start_urls = ['https://www.propertyguru.com.sg/']

    def parse(self, response):
        return response
