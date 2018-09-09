# -*- coding: utf-8 -*-
import scrapy


class MoviesSpiderSpider(scrapy.Spider):
    name = 'movies_spider'
    start_urls = ['http://gomovies.cool/movie/filter']

    def parse(self, response):
        contents = response.xpath('//div[@class="ml-item"]')
        for content in contents:
            print (content.xpath('.//a/@href').extract_first())
        pass
