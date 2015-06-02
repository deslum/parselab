# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from letu.items import LetuItem
import csv
import codecs



class LetuSpider(CrawlSpider):
   name = "letu" 
   allowed_domains = ["www.letu.ru"]
   start_urls = ["http://www.letu.ru/parfyumeriya/zhenskaya-parfyumeriya"]
   order_id = 1
   id1 = []

   rules = (
            Rule(SgmlLinkExtractor(allow=('\?q_pageSize=24\&q_docSortOrder=descending\&viewAll=true')),follow='True'),
            Rule(SgmlLinkExtractor(allow=('\/[\w-]+\/\w+\?navAction=push$')), follow='True', callback='go_go'),
            )


   def go_go(self, response):
      hxs = HtmlXPathSelector(response)
      price = []
      for i in hxs.xpath("//td[@class='price']/p[@class='new_price' or @class='price_no_discount']/text()").extract():
         if i!=u'\r\n  ':
            price.append(i.strip())
      writer = csv.writer(open('price.csv', 'a'), lineterminator='\n')
      for x, i in enumerate(hxs.xpath("//td[@class='item']")):
         order = str(self.order_id)
         name = i.xpath("h2/text()").extract()[0].strip()                     
         title = i.xpath("p[@class='description']/text()").extract()[0].strip() 
         article = i.xpath("p[@class='article']/text()").extract()[0].strip()   
         num = price[x]                                                      
         writer.writerow([i.encode('utf-8') for i in [order, name, title, article, num]])
      description = self.parse_me(hxs, "//div[@itemprop='description']/text()")
      features = self.parse_me(hxs, "//div[@id='features']/dl/dd/text()")
      img = self.parse_me(hxs, "//div[@class='atg_store_productImage']/img/@src")
      alls = [str(self.order_id)] + description + features + img
      writer = csv.writer(open('shop.csv', 'a'), lineterminator='\n')
      writer.writerow([i.encode('utf-8') for i in alls])
      self.order_id += 1