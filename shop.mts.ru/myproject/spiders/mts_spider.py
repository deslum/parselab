# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from myproject.items import MtsItem
import csv
import codecs


class MtsLoader(XPathItemLoader):
    pass

class MtsSpider(CrawlSpider):
   name = "mts" 
   allowed_domains = ["www.shop.mts.ru"]
   start_urls = ["http://www.shop.mts.ru/smartfony/"]

   f = codecs.open('my.txt',encoding='utf-8')
   values_list = [[line.strip() for line in f]][0]
   f.close()

   rules = (
            Rule(SgmlLinkExtractor(allow=('\?PAGEN_1=\d+$')), follow=True),
            Rule(SgmlLinkExtractor(allow=('\w+\/[\w\-.]+.html$')), callback='parse_settings'),
            )

   # def get_values(self,response):
   #    f1 = open('my.txt','a')
   #    hxs = HtmlXPathSelector(response)
   #    assorti = hxs.select("//td[@class='table_left_col gray_char_text vmiddle']/text()").extract()
   #    for i in assorti:
   #       if i not in self.spisok:
   #          print i
   #          self.spisok.append(i)
   #          f1.write(i.encode('utf-8')+'\n')
   #    f1.close()


   def parse_settings(self, response):
      hxs = HtmlXPathSelector(response)
      smart = hxs.select("//div[@id='right_block']/h1/text()").extract()
      price =  hxs.select("//div[@class='price_penel_text']/span/text()").extract()
      assorti = [i.strip() for i in hxs.select("//td[@class='table_left_col gray_char_text vmiddle']/text()").extract()]
      value = hxs.xpath("//td[@class='table_right_col vmiddle']")
      value =[i.xpath('string(.)').extract()[0] for i in value]
      a = smart+price
      sett = dict(zip(assorti,value))
      for i in self.values_list:
         if i in sett:
            a.append(sett[i])
         else:
            a.append('nul')
      writer = csv.writer(open('shop.csv', 'a'), lineterminator='\n')
      writer.writerow([i.encode('utf-8') for i in a])

        
