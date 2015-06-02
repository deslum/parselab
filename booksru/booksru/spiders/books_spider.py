# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from booksru.items import BooksruItem
import csv
import codecs



class BooksSpider(CrawlSpider):
   name = "booksru" 
   allowed_domains = ["www.books.ru"]
   start_urls = ["http://www.books.ru/biznes-9000032/?page=1"]
   order_id = 1
   author_id = 1

   rules = (
            Rule(SgmlLinkExtractor(allow=('\/biznes-9000032\/\?page=\d+')), follow='True', callback='parser'),
            )


   def parser(self, response):
      hxs = HtmlXPathSelector(response)
      writer   = csv.writer(open('authors.csv', 'a'), lineterminator='\n')
      for i in hxs.xpath("//td[@class='descr']"):
         authors = i.xpath("p[@class='authors']/a/text()").extract()
         for j in authors:
            writer.writerow([str(self.author_id), j.encode('utf-8')])
         self.author_id += 1
      titles = hxs.xpath("//td[@class='descr']/p[@class='title']/a/text()").extract()
      texts  = hxs.xpath("//td[@class='descr']/p[not(@*)]/text()").extract()
      price  = hxs.xpath("//td[@class='opinions']/p/span/strong/text()").extract()
      stars  = hxs.xpath("//td[@class='opinions']/img/@src").extract()
      alls   = zip(titles, texts, price, stars)
      writer    = csv.writer(open('books.csv', 'a'), lineterminator='\n')
      for title, text, price, star in alls:
         writer.writerow([str(self.order_id), title.encode('utf-8').strip(), text.encode('utf-8').strip(), price, star])
         self.order_id += 1