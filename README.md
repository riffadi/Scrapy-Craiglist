# Scrapy-Craiglist
Scrapy tutorial to build a Craigslist crawler that scrapes engineering jobs in New York.

# Usage
In Terminal or CMD, navigate to the main Scrapy project folder, and run one of the spiders:

## Scraping Craigslist's Engineering Job Titles from One Page
```$ scrapy crawl titles -o job-titles.csv```

## Scraping Craigslist's Engineering Job Titles, Addresses, and URLs from One Page
```$ scrapy crawl jobsone -o job-one-page.csv```

## Scraping Craigslist's Engineering Job Titles, Addresses, and URLs from All Pages
```$ scrapy crawl jobsall -o job-all-pages.csv```

## Scraping Craigslist's Engineering Job Details from Each Job's Web Page
``` $ scrapy crawl jobscontent -o job-all-pages-content.csv```

## Scrapy Tutorial: Craigslist
Check this blog post for the full Scrapy tutorial:

http://python.gotrained.com/scrapy-tutorial-web-scraping-craigslist
