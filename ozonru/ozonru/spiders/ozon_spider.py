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
            # Rule(SgmlLinkExtractor(allow=('\/vacancy\/\d+$'),deny = ('\/area_switcher\?backUrl\=\/vacancy\/\d+')),callback='parser'),
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
      # vacancy  = hxs.xpath("//div[@class='b-vacancy-custom g-round']/h1[@class='title b-vacancy-title']/text()").extract()
      # company  = hxs.xpath("//div[@class='companyname']/a/text()").extract()
      # price    = hxs.xpath("//div[@class='l-paddings']/text()").extract()[3]
      # city     = hxs.xpath("//div[@class='l-paddings']/text()").extract()[4]
      # exp      = hxs.xpath("//div[@class='l-paddings']/text()").extract()[5]
      # vacancy1 = vacancy[0].encode('utf-8')
      # company1 = company[0].encode('utf-8')
      # writer   = csv.writer(open('price.csv', 'a'), lineterminator='\n')
      # writer.writerow([vacancy1,company1, price.encode('utf-8'),city.encode('utf-8'),exp.encode('utf-8')])