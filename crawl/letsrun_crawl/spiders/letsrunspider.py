import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from letsrun_crawl.items import LetsrunPostItem
from itertools import izip
import re


class LetsRunSpider(CrawlSpider):
    name = 'LetsRunSpider'
    allowed_domains = ['letsrun.com']
    start_urls = ['http://www.letsrun.com/forum']

    rules = (
        # Rule(LinkExtractor(allow=('letsrun.com/forum',),
        #                    deny=(
        #                        'letsrun.com/forum/post',
        #                        'letsrun.com/forum/forum.php?board=1',
        #                        'letsrun.com/forum/report',
        #                        )
        # )),
        # Rule(LinkExtractor(allow=('letsrun.com/forum/flat_read.php?',)),
        #      callback='parse_post')
        Rule(SgmlLinkExtractor(
            allow=('forum/flat_read.php',)),
            callback='parse_posts',
            follow=True
        ),
    )

    def parse_posts(self, response):
        items = []

        posts = response.xpath('//*[@class="post"]')
        post_ids = response.xpath('//ul/a/@name').extract()
        thread = re.findall('thread=([0-9]+)', response.url)[0]
        assert len(post_ids) == len(posts)
        for post, id in izip(posts, post_ids):
            item = LetsrunPostItem()
            item['thread_id'] = thread
            item['post_id'] = id

            item['post_author'] = post.xpath(
                './/*[@class="author"]//text()').extract()

            item["post_text"] = post.xpath(
                './/span[contains(@id, "intelliTXT")]//text()').extract()

            item['subject'] = post.xpath(
                './/span[contains(@class, "subject_line")]//text()').extract()

            item['timestamp'] = post.xpath(
                './/span[contains(@class, "timestamp")]//text()').extract()

            items.append(item)
        return items
