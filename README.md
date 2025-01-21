# Web Crawler
This assignment implements a web crawler using Scrapy to extract detailed information about books from books.toscrape.com. The crawler navigates through the entire website, fetching information from all available book pages and generating structured data for further analysis.

## Workflow
### 1. Crawler Design

The crawler:

    Starts from the main page (http://books.toscrape.com) as the seed URL.
    Navigates through all pages using pagination links.
    Visits each book's detail page to extract relevant data.
    Ensures no duplicate URLs are crawled by tracking visited pages.

### 2. Data Extraction

The crawler extracts the following details from each book page:

    Title: The name of the book.
    Price: The cost of the book.
    Availability: The stock status of the book.
    Category: The category/genre of the book.
    Description: A brief description of the book.
    Star Rating: The rating of the book (e.g., "One", "Two", "Three" stars).

### 3. Performance Metrics

The crawler tracks:

    Total URLs crawled.
    Total books extracted.
    Crawl duration.
    Pages crawled per minute.

### 4. Visualization

The project generates detailed visualizations for:

    Crawl Speed Over Time: Number of pages crawled per minute.
    Ratio of URLs Crawled: Proportion of successfully extracted books to total URLs.
    Books Extracted vs. URLs Crawled: Comparison of successful data extraction against crawled pages.
    Crawl Completion Percentage: Percentage of successful data extraction.

### Outputs
1. Data Files

    web_archive.json: Contains structured data for all extracted books. Example:
```json
[
    {
        "title": "A Light in the Attic",
        "price": "£51.77",
        "availability": "22 available",
        "category": "Poetry",
        "description": "It's hard to imagine a world without A Light in the Attic...",
        "rating": "Three",
        "url": "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    }
]
```
statistics.txt: Provides crawl statistics. Example:

    Total URLs Crawled: 1000
    Total Books Extracted: 965
    Duration: 20.52 minutes
    Pages Per Minute: 48.74

2. Visualizations

Generated plots for crawl analysis:

    crawl_speed_over_time.png: Crawl speed visualization.
    ratio_of_urls_crawled.png: Pie chart showing crawl completion ratio.
    books_vs_urls_crawled.png: Bar chart comparing crawled URLs and extracted books.
    crawl_completion_percentage.png: Crawl completion percentage.

## Running the Project

### 1. Clone the repository:

`git clone https://github.com/yourusername/book-crawler.git`\
`cd book-crawler`

### 2. Start the Scrapy spider:

`scrapy crawl bookspider `

### 3. Generate visualizations:

  `python3 visualizations.py`

## Outputs:
Extracted data: web_archive.json\
Crawl statistics: statistics.txt\
Visualizations: PNG files in the project directory.

