from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class MininovaSpider(CrawlSpider):

    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = ['http://www.reddit.com/r/leagueoflegends']
    rules = [Rule(SgmlLinkExtractor(unqiue=True), 'parse_torrent')]

    def parse_torrent(self, response):
        sel = Selector(response)
        torrent = TorrentItem()
        torrent['url'] = response.url
        print response.url
        return torrent
