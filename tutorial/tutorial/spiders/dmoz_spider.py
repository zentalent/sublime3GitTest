import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.spiders.Spider):
	name = 'amazon'
	allowed_domains = ['amazon.cn']
	start_urls = [
	'https://www.amazon.com/gp/new-releases/books/',
	]

	def parse(self,response):
		for sel in response.xpath('//ul/li'):
			item = DmozItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('text()').extract()
			yield item
