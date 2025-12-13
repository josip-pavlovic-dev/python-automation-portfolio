# Web Scraper Tool | Web Scraping Automation

en: Scrapes quotes from [https://quotes.toscrape.com](https://quotes.toscrape.com) and saves them to `JSON` or `CSV`. Built as part of the Python Automation Portfolio.

sr: Alat za veb skrejping koji prikuplja citate sa [https://quotes.toscrape.com](https://quotes.toscrape.com) i čuva ih u `JSON` ili `CSV` formatu. Napravljeno kao deo Python Automation Portfolio.

## Quickstart | Brzi početak

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

---

## What it does | Šta radi

-   Fetches one or more pages defined in config.py (or via --url) | _Dohvata jednu ili više stranica definisanih u config.py (ili preko --url)_
-   Parses quotes, authors, and tags with BeautifulSoup | _Parsira citate, autore i tagove pomoću BeautifulSoup_
-   Writes JSON (default) or CSV output | _Upisuje izlaz u JSON (podrazumevano) ili CSV_
-   Logs to console and to logs/scraper.log with rotation | _Loguje u konzolu i u logs/scraper.log sa rotacijom_

---

## File structure | Struktura fajlova

-   scraper.py — CLI and scraper logic | _CLI i logika skrejpera_
-   config.py — default URLs, headers, timeouts, output path | _podrazumevani URL-ovi, zaglavlja, vremenska ograničenja, putanja izlaza_
-   requirements.txt — minimal deps | _minimalne zavisnosti_
-   tests/ — pytest unit tests | _pytest jedinicni testovi_
-   logs/ — rotating logs | _rotirajući logovi_
-   output/ — scraped data | _izvučeni podaci_

---

## Testing | Testiranje

```bash
# From this folder with venv active
python -m pytest
```

---

## Next steps | Sledeći koraci

-   Add pagination support | _Dodaj podršku za paginaciju_
-   Add retry/backoff and HTTP error handling strategies | _Dodaj strategije ponovnog pokušaja/odlaganja i rukovanja HTTP greškama_
-   Add CLI flag for delay between requests | _Dodaj CLI zastavicu za kašnjenje između zahteva_
-   Parameterize output directory | _Parametrizuj izlazni direktorijum_

---
