import scrapy
import json
import time
from scrapy.utils.url import canonicalize_url

class BookSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "ROBOTSTXT_OBEY": False,
        "DOWNLOAD_DELAY": 1,
        "CLOSESPIDER_PAGECOUNT": 1000,  # Stop after 1000 pages
    }

    def __init__(self, *args, **kwargs):
        super(BookSpider, self).__init__(*args, **kwargs)
        self.visited_urls = set()  # Track visited URLs
        self.data = []  # Store book data for the web archive
        self.start_time = time.time()  # Start time for crawl

    def parse(self, response):
        # Parse all book links on the current page
        book_links = response.xpath('//h3/a/@href').getall()
        for link in book_links:
            # Make the link absolute
            absolute_link = response.urljoin(link)
            if absolute_link not in self.visited_urls:
                self.visited_urls.add(absolute_link)
                yield scrapy.Request(absolute_link, callback=self.parse_book)

        # Follow pagination links to the next page
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_book(self, response):
        # Extract detailed book data
        title = response.xpath('//h1/text()').get()
        price = response.xpath('//p[@class="price_color"]/text()').get()
        availability = response.xpath('//p[contains(@class, "availability")]/text()').re_first(r'\d+ available')
        category = response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get()
        description = response.xpath('//meta[@name="description"]/@content').get()
        rating = response.xpath('//p[contains(@class, "star-rating")]/@class').re_first(r'star-rating (\w+)')

        # Save data
        self.data.append({
            "title": title,
            "price": price,
            "availability": availability,
            "category": category,
            "description": description.strip() if description else None,
            "rating": rating,
            "url": canonicalize_url(response.url),
        })

    def closed(self, reason):
        end_time = time.time()
        duration = end_time - self.start_time
        self.save_web_archive()
        self.save_statistics(duration)

    def save_web_archive(self):
        # Save all crawled data in JSON format
        with open("web_archive.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)
        self.log("Web archive saved to web_archive.json")

    def save_statistics(self, duration):
        # Save crawl statistics in a text file
        with open("statistics.txt", "w") as stats_file:
            stats_file.write(f"Total URLs Crawled: {len(self.visited_urls)}\n")
            stats_file.write(f"Total Books Extracted: {len(self.data)}\n")
            stats_file.write(f"Duration: {duration / 60:.2f} minutes\n")
            stats_file.write(f"Pages Per Minute: {len(self.visited_urls) / (duration / 60):.2f}\n")
