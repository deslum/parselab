# Scrapy settings for hh_crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'hh_crawl'

SPIDER_MODULES = ['hh_crawl.spiders']
NEWSPIDER_MODULE = 'hh_crawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'

DOWNLOAD_DELAY = 2

DOWNLOADER_MIDDLEWARES = [
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware',
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware',
    'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware',
    'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware'
]

COOKIES_DEBUG = False
REDIRECT_ENABLED = True
REDIRECT_MAX_TIMES = 10


DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'UTF-8,*;q=0.5',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language' : 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'
}