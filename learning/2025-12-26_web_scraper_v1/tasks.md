---
type: checklist
date: 2025-12-26
day: 8/14
topic: Web Scraper v1 — Daily Checklist
---

# ✅ DAN 8 — CHECKLIST

Koristi ovo za tracking napretka tokom dana. Zaokruži šta završiš!

---

## FAZA 1: Requests + BeautifulSoup Osnove (1.5h)

### Instalacija + Setup (15 min)

-   [ ] Aktiviran `venv` (`source venv/bin/activate`)
-   [ ] Instaliran `requests` (`pip install requests`)
-   [ ] Instaliran `beautifulsoup4` (`pip install beautifulsoup4`)
-   [ ] Instaliran `pytest pytest-cov pytest-mock` za testove

### Requests REPL Praksa (30 min)

-   [ ] GET zahtev radi: `requests.get("https://httpbin.org/html")`
-   [ ] Status kod je 200: `response.status_code == 200`
-   [ ] HTML je string: `type(response.text) == str`
-   [ ] Headers su dostupni: `response.headers`
-   [ ] URL je dostupan: `response.url`

### BeautifulSoup REPL Praksa (30 min)

-   [ ] BeautifulSoup import radi: `from bs4 import BeautifulSoup`
-   [ ] Parsing HTML radi: `soup = BeautifulSoup(html, "html.parser")`
-   [ ] `select_one()` radi: `soup.select_one("h1")`
-   [ ] `select()` radi: `soup.select("p")`
-   [ ] `get_text()` radi: `h1.get_text(strip=True)`
-   [ ] Atributi rade: `link.get("href")`
-   [ ] Iteracija radi: `for p in soup.select("p")`

### Kombinovani Primer (15 min)

-   [ ] `fetch_page()` + `parse_html()` flow radi u REPL-u
-   [ ] `extract_titles()` vraća títlove
-   [ ] Logging radi (loguje se u console)

---

## FAZA 2: Project Struktura i Setup (1.5h)

### Direktorijumi i Fajlovi (10 min)

-   [ ] Direktorijumi kreirani: `tests/`, `logs/`, `output/`
-   [ ] Fajlovi kreirani: `config.py`, `scraper.py`, `tests/__init__.py`, `tests/conftest.py`, `tests/test_scraper_basics.py`

### config.py (20 min)

-   [ ] `config.py` ima `PROJECT_ROOT`, `LOGS_DIR`, `OUTPUT_DIR`
-   [ ] `config.py` ima `BASE_URL`, `REQUEST_TIMEOUT`, `HEADERS`
-   [ ] `config.py` ima `LOG_FILE`, `LOG_LEVEL`, `LOG_FORMAT`
-   [ ] Direktorijumi se kreiraju sa `mkdir(exist_ok=True)`
-   [ ] `config.py` se može importovati: `from config import PROJECT_ROOT`

### requirements.txt (10 min)

-   [ ] `requirements.txt` je generiisan sa `pip freeze > requirements.txt`
-   [ ] Sadrži `requests`, `beautifulsoup4`, `pytest`

### Git Setup (10 min)

-   [ ] `.gitignore` je kreiran sa `venv/`, `__pycache__/`, `*.pyc`, `logs/*.log`, itd.
-   [ ] Git je inicijalizovan: `git init`
-   [ ] Fajlovi su dodati: `git add config.py requirements.txt`
-   [ ] Commit je napravljen: `git commit -m "Initial setup"`

---

## FAZA 3: Scraper Core Funkcije (2h)

### scraper.py — Struktura (15 min)

-   [ ] `scraper.py` ima `FetchError` i `ScraperError` exception klase
-   [ ] `fetch_page(url)` funkcija je definisana
-   [ ] `parse_html(html)` funkcija je definisana
-   [ ] `extract_titles(html)` funkcija je definisana

### scraper.py — fetch_page() (45 min)

-   [ ] `fetch_page()` primenjuje `requests.get()` sa `timeout`
-   [ ] `fetch_page()` primenjuje `headers` iz `config.py`
-   [ ] `fetch_page()` ima `response.raise_for_status()`
-   [ ] `fetch_page()` hvata `requests.Timeout` i baca `FetchError`
-   [ ] `fetch_page()` hvata `requests.ConnectionError` i baca `FetchError`
-   [ ] `fetch_page()` hvata `requests.HTTPError` i baca `FetchError`
-   [ ] `fetch_page()` vraća HTML kao string
-   [ ] `fetch_page()` loguje sve korake

### scraper.py — parse_html() i extract_titles() (30 min)

-   [ ] `parse_html()` vraća `BeautifulSoup` objekat
-   [ ] `extract_titles()` koristi `soup.select("h1")`
-   [ ] `extract_titles()` vraća listu stringova
-   [ ] `extract_titles()` strip-uje whitespace
-   [ ] `extract_titles()` loguje broj pronađenih títlova

### Testiranje u REPL-u (30 min)

-   [ ] `from scraper import fetch_page` radi
-   [ ] `html = fetch_page("https://httpbin.org/html")` radi
-   [ ] `len(html) > 0` je `True`
-   [ ] `from scraper import extract_titles` radi
-   [ ] `titles = extract_titles(html)` radi
-   [ ] `len(titles) > 0` je `True`

---

## FAZA 4: Testing Setup (2h)

### conftest.py (30 min)

-   [ ] `conftest.py` ima `mock_html` fixture
-   [ ] `conftest.py` ima `mock_soup` fixture
-   [ ] `conftest.py` ima `mock_response` fixture
-   [ ] `conftest.py` ima `mock_response_404` fixture
-   [ ] Svi fixtures vraćaju expected tipove

### test_scraper_basics.py — TestFetchPage (30 min)

-   [ ] Test `test_fetch_page_with_valid_url` postoji i prolazi
-   [ ] Test `test_fetch_page_calls_with_correct_params` postoji i prolazi
-   [ ] Test `test_fetch_page_raises_on_timeout` postoji i prolazi
-   [ ] Test `test_fetch_page_raises_on_connection_error` postoji i prolazi
-   [ ] Test `test_fetch_page_raises_on_http_error` postoji i prolazi

### test_scraper_basics.py — TestParseHtml (20 min)

-   [ ] Test `test_parse_html_returns_soup` postoji i prolazi
-   [ ] Test `test_parse_html_handles_empty_string` postoji i prolazi

### test_scraper_basics.py — TestExtractTitles (20 min)

-   [ ] Test `test_extract_titles_with_valid_html` postoji i prolazi
-   [ ] Test `test_extract_titles_with_no_h1` postoji i prolazi
-   [ ] Test `test_extract_titles_with_multiple_h1` postoji i prolazi

### test_scraper_basics.py — Integration & Logging (20 min)

-   [ ] Test `test_fetch_and_parse_flow` postoji i prolazi
-   [ ] Test `test_fetch_page_logs_success` postoji i prolazi (koristi `caplog`)
-   [ ] Test `test_fetch_page_logs_error` postoji i prolazi (koristi `caplog`)

### Pokretanje Testova (15 min)

-   [ ] `pytest tests/test_scraper_basics.py -v` prolazi
-   [ ] Svi testovi su PASSED
-   [ ] Broj testova > 10

### Coverage (10 min)

-   [ ] `pytest --cov=scraper tests/` pokazuje coverage
-   [ ] Coverage za `scraper.py` > 85%
-   [ ] Sve važne linije su pokrivene

---

## FINALIZACIJA (30 min)

### Struktura i Organizacija

-   [ ] Svi fajlovi su na mestu:
    -   [ ] `config.py`
    -   [ ] `scraper.py`
    -   [ ] `requirements.txt`
    -   [ ] `tests/conftest.py`
    -   [ ] `tests/test_scraper_basics.py`
    -   [ ] `logs/` direktorijum postoji
    -   [ ] `output/` direktorijum postoji

### Git Finalizacija

-   [ ] Svi fajlovi su staged: `git add .`
-   [ ] Commit je napravljen: `git commit -m "Day 8: Web Scraper Setup Complete"`
-   [ ] Git log pokazuje commit: `git log --oneline` (vidiš poslednji commit)

### Dokumentacija

-   [ ] README.md je kreiran sa:
    -   [ ] "How to Setup" sekcija
    -   [ ] "How to Run Tests" sekcija
    -   [ ] "Project Structure" sekcija

### Finalni Test

```bash
# Pokreni ovo u terminalu i proveri da sve radi:
source venv/bin/activate
pytest tests/ -v
pytest --cov=scraper tests/
cat logs/app.log | tail -5
```

-   [ ] Svi testovi prolaze ✅
-   [ ] Coverage > 85% ✅
-   [ ] Log fajl ima entries ✅

---

## BONUS (Ako Brzo Završiš)

-   [ ] Dodaj još 3-5 custom testova
-   [ ] Eksperimentiraj sa drugačitim CSS selektorima
-   [ ] Kreiraj mock podatke sa drugačitim struktuama
-   [ ] Dodaj `test_scraper_integration.py` sa end-to-end testom

---

## 🎯 SUMMARY

**Na kraju dana, trebalo bi:**

```bash
# Struktura
projects/01-web-scraper/
├── config.py                          ✅ 20 linija
├── scraper.py                         ✅ 80 linija
├── requirements.txt                   ✅ 10 linija
├── tests/
│   ├── conftest.py                   ✅ 50 linija
│   └── test_scraper_basics.py        ✅ 150 linija
├── logs/
│   └── app.log                        ✅ (autogenerisan)
└── output/

# Testovi
$ pytest tests/ -v
10 passed in 0.45s

# Coverage
$ pytest --cov=scraper tests/
Cover: 90%+

# Git
$ git log --oneline
2e4f8a9 Day 8: Web Scraper Setup Complete
e3a8c1d Initial setup
```

---

## 🎉 ČESTITAM

Ako si sve završio, sada imaš:

✅ Profesionalan Web Scraper projekat
✅ 10+ testova sa 90%+ coverage
✅ Logging sistem
✅ Modularna struktura
✅ Git verzionisano

**Spreman si za Dan 9: Web Scraper Implementation! 🚀**

---
