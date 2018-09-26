# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Task1Item(scrapy.Item):
	title = scrapy.Field()
	product_url = scrapy.Field()
	category = scrapy.Field()
	img_url = scrapy.Field()
	#image_urls = scrapy.Field()
	price = scrapy.Field()
	discounted = scrapy.Field()
	sku = scrapy.Field()
