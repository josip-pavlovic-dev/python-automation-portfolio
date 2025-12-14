---
type: tasklist
linked_to: python-automation-portfolio
status: in_progress
date: 2025-12-14
topic: csv_basics_day01
---

# 📋 Task List — 2025-12-14

## 🔢 Top Priorities

-   [ ] REPL warm-up: `csv.reader` / `DictReader` / `DictWriter`, `newline=""`, delimiter, encoding error.
-   [ ] Dodati `load_csv` / `write_csv` u sandbox/basics/python_refresh.py (Path + DictReader/DictWriter).
-   [ ] Implementirati CSV Cleaner v0 u sandbox/basics/csv_cleaner.py (trim whitespace, normalize delimiter to comma, drop prazne redove, statistika).
-   [ ] Pokrenuti scraper u projects/01-web-scraper i proveriti output/scraped_quotes.csv (prvih 5 redova).
-   [ ] README kratka dopuna + git commit.

## 🧪 Test & Validation Tasks

-   [ ] `load_csv` vraća listu dict-ova; `write_csv` kreira fajl sa očekivanim headerima.
-   [ ] CSV Cleaner v0: izlaz nema leading/trailing whitespace; broj redova ulaz/izlaz/skiplovano ispisan.
-   [ ] Scraper se izvršava bez greške; fajl postoji u output/ i ima 20 redova (očekivano za 2 strane).

## 📌 Optional / Stretch Goals

-   [ ] Jednostavan pytest za CSV Cleaner (trim + skip praznih).
-   [ ] Dodati Path u scraper za output putanje.
-   [ ] Rainbow CSV kratak test (column stats) na clean.csv.
