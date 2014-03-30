from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from tutorial.items import QuestionItem
import pprint

class MininovaSpider(CrawlSpider):

    name = 'uk'
    allowed_domains = ['answers.yahoo.com']
    start_urls = ['https://uk.answers.yahoo.com/?tab=recent&filter=intl']
    rules = [Rule(SgmlLinkExtractor(allow=(r"(.*uk\.answers\.yahoo\.com/question/index\?qid=\w*$)|(.*uk.answers.yahoo.com/?tab=recent&filter=intl&page=.*)")), 'parse_question', follow=True)]

    def parse_question(self, response):
        sel = Selector(response)
        question = QuestionItem()

        # record url of this page
        question['url'] = response.url

        # extract title
        contents = sel.xpath('//h1[re:test(@class, "subject\ inline")]/text()').extract()
        question['title'] = "".join(contents)

        # extract question content
        contents = sel.xpath('//div[re:test(@class, "content\ mb10")]/text()').extract()
        question['question'] = "".join(contents)

        # extract answer content
        contents = sel.xpath('//div[re:test(@class, "content\ mb14")]/text()').extract()
        question['answer'] = "".join(contents)

        
        return question
