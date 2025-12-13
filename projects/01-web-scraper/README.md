# Web Scraper Tool

Scrapes quotes from https://quotes.toscrape.com and saves them to JSON or CSV. Built as part of the Python Automation Portfolio.

## Quickstart

```bash
# From repo root
cd projects/01-web-scraper
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run with defaults from config.py
python scraper.py --format json --out output/scraped_quotes.json

# Or target a single URL and emit CSV
python scraper.py --url https://quotes.toscrape.com/ --format csv --out output/quotes.csv
```

## What it does

-   Fetches one or more pages defined in config.py (or via --url)
-   Parses quotes, authors, and tags with BeautifulSoup
-   Writes JSON (default) or CSV
-   Logs to console and to logs/scraper.log with rotation

## Files

-   scraper.py — CLI and scraper logic
-   config.py — default URLs, headers, timeouts, output path
-   requirements.txt — minimal deps
-   tests/ — pytest unit tests
-   logs/ — rotating logs
-   output/ — scraped data

## Testing

```bash
# From this folder with venv active
python -m pytest
```

## Next steps

-   Add pagination support
-   Add retry/backoff and HTTP error handling strategies
-   Add CLI flag for delay between requests
-   Parameterize output directory
