# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from chipdip.items import ChipdipItem
import csv
import codecs



class HhSpider(CrawlSpider):
   name = "chipdip" 
   allowed_domains = ["www.chipdip.ru"]
   start_urls = ["http://www.chipdip.ru/catalog/screwdrivers/"]
   order_id = 1

   rules = (
            Rule(SgmlLinkExtractor(allow=('\/catalog-show\/[\w-]+\/$')),follow='True'),
            Rule(SgmlLinkExtractor(allow=('\/catalog-show\/[\w-]+\/\?page=\d+$')),follow='True'),
            Rule(SgmlLinkExtractor(allow=('\/product\/[\d\w-]+\/$')),follow='True', callback='parser',)
            )


   def parser(self,response):
      print "OK" 