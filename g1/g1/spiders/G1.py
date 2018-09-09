# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class G1Spider(scrapy.Spider):
    name = 'G1'
    start_urls = ['https://g1.globo.com/busca/?q=bolsonario']

    def parse(self, response):
        contents = response.xpath('//section[@class="container"]')
        for content in contents:
            result_content = content.xpath(
                './/div[@class="results results--"]')
            result_content_div = result_content.xpath(
                './/div[@class="results__content"]')
            result_content_div_2 = result_content_div.xpath(
                './/ul[@class="results__list"]')
            lis = result_content_div_2.xpath(
                './/li[@class="widget widget--card widget--info"]')
            for li in lis:
                img = li.xpath('.//img/@src').extract()
                next_link = li.xpath(
                    './/div[@class="widget--info__text-container"]')
                next_link = next_link.xpath('.//a/@href').extract()               
                teste=next_link[0].split('//')[1]               
                yield scrapy.Request('http://'+teste,self.get_urls)

        pass

    def get_urls(self,response):    
        result_body = response.xpath('//script/text()').extract()[0]
        result_body=result_body[result_body.find('(')+2 : result_body.find(')')-1]
        yield scrapy.Request(result_body,self.url_parsed)
      
    def url_parsed(self,response):    
        contents = response.xpath('//body[@class="multicontent"]')
        if len(contents)>0:
            article=contents.xpath('.//div[@class="mc-article-body"]')
            textarea_=article.xpath('.//div[@class="mc-column content-text active-extra-styles active-capital-letter"]')
            textarea = textarea_.xpath('.//p[@class="content-text__container theme-color-primary-first-letter"]').extract()
            soup = BeautifulSoup(textarea[0],'html.parser')
            text1=soup.get_text()
