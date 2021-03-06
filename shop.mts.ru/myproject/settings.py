# -*- coding: utf-8 -*-

# Scrapy settings for mycrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'my_crawler'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['myproject.spiders']
NEWSPIDER_MODULE = 'myproject.spiders'
USER_AGENT = 'Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1 FirePHP/0.6'
ITEM_PIPELINES = ['myproject.pipelines.MtsPipeline']

CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 0.2
