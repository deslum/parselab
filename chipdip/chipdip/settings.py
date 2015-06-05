# -*- coding: utf-8 -*-

# Scrapy settings for chipdip project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'chipdip'

SPIDER_MODULES = ['chipdip.spiders']
NEWSPIDER_MODULE = 'chipdip.spiders'

USER_AGENT = 'Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1 FirePHP/0.6'
ITEM_PIPELINES = ['chipdip.pipelines.ChipdipPipeline']
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 0.6


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'chipdip (+http://www.yourdomain.com)'
