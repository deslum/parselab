# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from ozonru.items import OzonruItem
import csv
import codecs



class HhSpider(CrawlSpider):
   name = "ozonru" 
   allowed_domains = ["www.ozon.ru"]
   start_urls = ["http://www.ozon.ru/catalog/1137926?page=1"]
   order_id = 1

   rules = (
            Rule(SgmlLinkExtractor(allow=('\/catalog\/1137926\/\?page\=\d+$')),follow='True'),
            Rule(SgmlLinkExtractor(allow=('\/context\/detail\/id\/\d+\/$')),callback='parser'),
            )

   def parse_me(self, hxs, st):    
      return [i.strip() for i in hxs.xpath(st).extract()]



   def parser(self,response):
      hxs = HtmlXPathSelector(response)
      title = hxs.xpath("//div['bCombiningColumn']/div['bContentColumn']/div[@class='bContentBlock']/h1/text()").extract()
      idx = hxs.xpath("//div['bCombiningColumn']/div['bContentColumn']/div[@class='bContentBlock']/div[@class='eDetail_ProductId']/text()").extract()
      authors = hxs.xpath("//div['bCombiningColumn']/div['bContentColumn']/div[@class='bContentBlock']/div[@class='bDetailLogoBlock']/p[@itemprop='author']/a/text()").extract()
      publisher = hxs.xpath("//div['bCombiningColumn']/div['bContentColumn']/div[@class='bContentBlock']/div[@class='bDetailLogoBlock']/p[@itemprop='publisher']/a/text()").extract()
      price = hxs.xpath("//div[@class='bOzonPrice']/span[@class='eOzonPrice_main']/text()").extract()
      if title!=[]:
         title = title[0].encode('utf-8')
         idx = idx[0].encode('utf-8')
         for i in authors:
            author   = csv.writer(open('author.csv', 'a'), lineterminator='\n')
            author.writerow([str(self.order_id), i.encode('utf-8')])
         if publisher!=[]:
            publisher = publisher[0].encode('utf-8')
         else:
            publisher = 'null'
         price = price[0].encode('utf-8')
         writer   = csv.writer(open('books.csv', 'a'), lineterminator='\n')
         writer.writerow([str(self.order_id), title, idx, publisher,price.strip()])
         self.order_id += 1