"""Default configuration for the web scraper project."""

URLS = [
    "https://quotes.toscrape.com/page/1/",
    "https://quotes.toscrape.com/page/2/",
]

HEADERS = {
    "User-Agent": "python-automation-portfolio/1.0 (+https://github.com/jole-pavlovic-dev)",
    "Accept-Language": "en-US,en;q=0.9",
}

OUTPUT_PATH = "output/scraped_quotes.json"

REQUEST_TIMEOUT = 15
DELAY_BETWEEN_REQUESTS = 1.0
