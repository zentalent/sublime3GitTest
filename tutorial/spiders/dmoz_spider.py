#coding=utf-8
import re
import json
from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor as sle
from tutorial.items import DmozItem

class DmozSpider(CrawlSpider):
	name = 'amazon'
	allowed_domains = ['cnblogs.com']
	start_urls = [
	"http://www.cnblogs.com/rwxwsblog/default.html?page=1",
	]

	rules = [
        Rule(sle(allow=("/rwxwsblog/default.html\?page=\d{1,}")), #此处要注意?号的转换，复制过来需要对?号进行转义。
                         follow=True,
                         callback='parse')
    ]
    #print "**********CnblogsSpider**********"

	def parse_item(self, response):
	   #print "-----------------"
	   items = []
	   sel = Selector(response)
	   base_url = get_base_url(response)
	   postTitle = sel.css('div.day div.postTitle')
	   #print "=============length======="
	   postCon = sel.css('div.postCon div.c_b_p_desc')
	   #标题、url和描述的结构是一个松散的结构，后期可以改进
	   for index in range(len(postTitle)):
	       item = CnblogsItem()
	       item['title'] = postTitle[index].css("a").xpath('text()').extract()[0]
	       #print item['title'] + "***************\r\n"
	       item['link'] = postTitle[index].css('a').xpath('@href').extract()[0]
	       item['listUrl'] = base_url
	       item['desc'] = postCon[index].xpath('text()').extract()[0]
	       #print base_url + "********\n"
	       items.append(item)
	       #print repr(item).decode("unicode-escape") + '\n'
	   return items
