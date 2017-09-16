# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapperlist.items import ScrapperlistItem
from scrapy.http import Request

class HeartrateSpider(scrapy.Spider):
	name = 'heartrate'
	allowed_domains = ['liveyoursport.com']
	start_urls = [
        'https://www.liveyoursport.com/heart-rate-monitors-1/']
    
	def parse(self, response):

		for heartrate in response.css("div.ProductDetails"):
			product_name = heartrate.css("a::text").extract(),
			price = heartrate.css("em::text").extract(),
			product_url = heartrate.css("a::attr(href)").extract(),
			for item in zip(product_name,price,product_url):
				scrap_info = {
				'product_name':item[0],
				'price' : item[1],
				'product_url' : item[2],
				}

			yield scrap_info

		next_page_url = response.css('div.FloatLeft > a::attr(href)').extract_first()
		if next_page_url :
			yield scrapy.Request(url = next_page_url ,callback = self.parse)