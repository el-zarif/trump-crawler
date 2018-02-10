from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from cnn_scrapy.items import CnnScrapyItem
from scrapy import Request
from newspaper import Article

class CNNSpider(CrawlSpider):
    name = "cnn"
    allowed_domains = ["edition.cnn.com"]
    start_urls = [
        "https://edition.cnn.com/"
    ]
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]
    article_count = 0

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, dont_filter=True)

    # Method for parsing items
    def parse_items(self, response):
        
        # Exit when the count is above or equal 25
        if self.article_count >= 25:
            return

        items = []
        # Download and parse the articles
        article = Article(response.url)
        article.download()
        article.parse()
        title = article.title
        text = article.text

        if 'trump' in title.lower():
            filename = response.url if 'html' in response.url else response.url + '.html'
            filename = filename.replace('/','-')
            with open(filename, 'wb') as f:
                f.write(response.body)
            item = CnnScrapyItem()
            item['url'] = filename
            item['title'] = title
            item['text'] = text
            items.append(item)
            self.article_count += 1

        # Only extract canonicalized and unique links (with respect to the current page)
        if self.article_count < 25:
            links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)

        return items
        


        
