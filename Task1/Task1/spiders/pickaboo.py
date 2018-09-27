# -*- coding: utf-8 -*-
import scrapy
from Task1.items import Task1Item

class PickabooSpider(scrapy.Spider):
    name = "pickaboo_old"
    allowed_domains = ["pickaboo.com"]
    start_urls = ['https://www.pickaboo.com/']

    def parse(self, response):
        urls_categories = response.xpath('//h5/a/@href').extract()
        for url in urls_categories:
            yield scrapy.Request(url=url, callback=self.parse_categories)


    def parse_categories(self, response):
        urls_items = response.xpath('//a[@class="product-image"]/@href').extract()	
        for url_indiv in urls_items:
            yield scrapy.Request(url=url_indiv, callback=self.parse_items)

        # follow next page link
        next_page_url = response.xpath('//a[@class="next i-next" and @title="Next"]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse_categories)

    def parse_items(self, response):
	#initialize with fields from Task1Item
        item = Task1Item()
	#add to items[key] in python dict structure
        item['title'] = response.xpath('//h1[@class="product-productname"]/text()').extract_first()
        item['product_url'] = response.url
        list = response.xpath('//span[@itemprop="title"]/text()').extract()
        item['category'] = ""
        if len(list) > 1: #more than one catagories is available so number 2 is very close to required catagory
            item['category'] = response.xpath('//span[@itemprop="title"]/text()')[1].extract()
        item['img_url'] = response.xpath('//*[@id="owl-demo"]//img/@src').extract_first() #[0].extract()
        item['price'] = response.xpath('//span[@class="price" and @itemprop="price"]/@content').extract_first()
        item['discounted'] = response.xpath('//strong[@style="font-size:18px;"]/text()').extract()
        item['sku'] = response.xpath('//th[contains(text(), "SKU")]/following-sibling::td/text()').extract() #Stock Keeping Unit -- a unique id 
        yield item
