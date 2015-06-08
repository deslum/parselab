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
   start_urls = ["http://www.chipdip.ru/catalog-show/universal-screwdrivers",
                  "http://www.chipdip.ru/catalog-show/ceramic-screwdrivers",
                  "http://www.chipdip.ru/catalog-show/reversible-screwdrivers",
                  "http://www.chipdip.ru/catalog-show/esd-screwdrivers",
                  "http://www.chipdip.ru/catalog-show/torque-screwdrivers",
                  "http://www.chipdip.ru/catalog-show/screwdrivers-with-attachments",
                  "http://www.chipdip.ru/catalog-show/screwdrivers-bits",
                  "http://www.chipdip.ru/catalog-show/screwdrivers-for-mobile-phones",
                  "http://www.chipdip.ru/catalog-show/screwdriver-sets"]

   rules = (
            Rule(SgmlLinkExtractor(allow=('\/catalog-show\/[\w-]+\/\?page=\d+$')),follow='True'),
            Rule(SgmlLinkExtractor(allow=('\/product\/[\d\w-]+\/$')),follow='True', callback='parser',)
            )


   def parser(self,response):
      hxs      =  HtmlXPathSelector(response)
      title    =  hxs.xpath("//div[@class='main-header']/h1[@itemprop='name']/text()").extract()
      art      =  hxs.xpath("//div[@class='product__control']/span[not(@class='product__control-name')]/text()").extract()
      article  =  art[0].encode('utf-8')
      code     =  art[1].encode('utf-8')
      brand    =  hxs.xpath("//div[@class='product__control']/a/text()").extract()
      summary  =  hxs.xpath("//div[contains(@class,'showhide') and contains(@class ,'item_desc')]/p/text()").extract()[0]
      print summary