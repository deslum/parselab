# encoding=utf-8
__author__ = 'remedy'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import FormRequest, Request
from hh_crawl.items import PersonItem
import hh_crawl.auth_conf as auth

class HHSpider(CrawlSpider):
    name = 'hh.ru'
    allowed_domains = ['spb.hh.ru']
    #start_urls = ['http://samara.hh.ru/resumesearch/result?a=1783&items=20&cur=USD&profArea=1&edu=0&page=1']
    start_urls = ['http://spb.hh.ru/resumesearch/result?a=89&from=CLUSTER_SPECIALIZATION&cur=USD&profArea=1&edu=0&s=1.50']
    rules = [
        Rule(SgmlLinkExtractor(
            allow=['/resumesearch/'],
            restrict_xpaths=["//div[@class='b-pager m-pager_left-pager HH-Pager']/ul/li"]), follow=True ),
        Rule(SgmlLinkExtractor(allow=['/resume/\w+']), 'parse_person')
    ]

    def start_requests(self):
        return [Request('http://hh.ru/',
                        callback=self.send_logon,
                        errback=self.send_logon,
                        dont_filter=True)]

    def send_logon(self, response):
        return FormRequest.from_response(response,
                                          formdata={
                                              'username': auth.username,
                                              'password': auth.password
                                          }, formnumber=0, callback=self.parse_site)

    def parse_site(self, responce):
        return [Request(self.start_urls[0], callback=self.parse)]


    def parse_person(self, response):
        x = HtmlXPathSelector(response)

        p = PersonItem()
        p['full_name'] = x.select("//div[@class='resume__personal__name']/text()").extract()
        p['vacancy'] = x.select("//div[@class='resume__position__title']/text()").extract()
        p['money'] = x.select("//div[@class='resume__position__salary']/text()").extract()
        p['birth_date'] = x.select("//meta[@itemprop='birthDate']/@content").extract()
        p['last_hh_change_date'] = x.select("//span[@class='resume__updated']/text()").extract()
        p['phone'] = x.select("//span[@class='resume__contacts__phone__number']/text()").extract()
        p['email'] = x.select("//span[@itemprop='email']/text()").extract()
        p['link'] = response.url
        p['payment_required'] = x.select("//div[@class='resume__achtung']").extract()

        return p



