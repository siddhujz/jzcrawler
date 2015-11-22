#import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from jzcrawler.items import JzcrawlerItem

class UiowaSpider(CrawlSpider):
    name = "UiowaSpider"
    allowed_domains = ["uiowa.edu"]
    start_urls = ["http://www.uiowa.edu"]
    rules = (
        Rule(SgmlLinkExtractor(allow=('.*.uiowa.edu', )),
             callback="parse_items",
             follow=True),
    )

    def parse_items(self, response):
        selector = Selector(response)
        anchorItems = selector.xpath('//a/@href')
        items = []
        for anchorItem in anchorItems:
            aItem = JzcrawlerItem()
            aItem["depth"] = response.meta["depth"]
            aItem["title"] = selector.xpath('//title/text()').extract()
            aItem["fromUrl"] = response.url
            aItem["toUrl"] = anchorItem.extract()
            items.append(aItem)
        return(items)
