# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapperlist.items import ScrapperlistItem
from scrapy.http import Request



class HeartrateSpider(scrapy.Spider):
    name = 'heartrate'
    allowed_domains = ['liveyoursport.com']
    start_urls = ['https://www.liveyoursport.com/fitness-technology/']

    def parse(self, response):
    	#print (response)
		product_name = response.xpath("//a[@class='pname']/text()").extract()
		print (product_name)
		#for title in product_name:
		#	yield {'Product Name' : title}
