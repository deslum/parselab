# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from hh.items import HhItem
import csv
import codecs



class HhSpider(CrawlSpider):
   name = "hh" 
   allowed_domains = ["ekaterinburg.hh.ru"]
   start_urls = ["http://ekaterinburg.hh.ru"]

   rules = (
            Rule(SgmlLinkExtractor(allow=('\/catalog$')), follow='True'),
            Rule(SgmlLinkExtractor(allow=('\/catalog\/[\w-]+$', '\/catalog\/[\w-]+\/page-[0-9]+')), follow='True'),
            Rule(SgmlLinkExtractor(allow=('\/vacancy\/\d+$'), deny = ('\/area_switcher\?backUrl\=\/vacancy\/\d+')),callback='parser'),
            )


   def parser(self, response):
      hxs = HtmlXPathSelector(response)
      vacancy  = hxs.xpath("//div[@class='b-vacancy-custom g-round']/h1[@class='title b-vacancy-title']/text()").extract()
      company  = hxs.xpath("//div[@class='companyname']/a/text()").extract()
      price    = hxs.xpath("//div[@class='l-paddings']/text()").extract()[3]
      city     = hxs.xpath("//div[@class='l-paddings']/text()").extract()[4]
      exp      = hxs.xpath("//div[@class='l-paddings']/text()").extract()[5]
      vacancy1 = vacancy[0].encode('utf-8')
      company1 = company[0].encode('utf-8')
      writer   = csv.writer(open('price.csv', 'a'), lineterminator='\n')
      writer.writerow([vacancy1, company1, price.encode('utf-8'), city.encode('utf-8'), exp.encode('utf-8')])