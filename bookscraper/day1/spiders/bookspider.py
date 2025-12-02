import scrapy
from day1.items import BookItem

class BookSpider(scrapy.Spider):
    name = "Books"
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.css("article.product_pod h3 a::attr(href)").getall()

        for book in books:
            yield response.follow(book, callback=self.parse_book)

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        item = BookItem()

        item['title'] = response.css(".product_main h1::text").get()
        item['price'] = response.css("p.price_color::text").get()
        item['category'] = response.css("ul.breadcrumb li a::text").getall()[2]

        description = response.css("#product_description ~ p::text").get()
        item['description'] = description.strip() if description else ""

        yield item   # ✔ FIXED
