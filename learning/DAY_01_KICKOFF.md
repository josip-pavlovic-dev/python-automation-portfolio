---
Title: DAY 01: Python Automation Kickoff 🚀
Date: December 14, 2025
Duration: 8-10 hours
Slug: day-01-python-automation-kickoff
Tags: day-01,python,automation,setup,environment,basics
Summary: Danas postavljamo okruženje, radimo CSV osnove u REPL-u, pravimo mini CSV Cleaner i pokrećemo web scraper primer.
role: mentor
user: Junior Python Developer
motivation: high
---

# DAY 01: Python Automation Kickoff 🚀

**Datum:** December 14, 2025
**Fokus:** CSV osnove u REPL-u + Python Refresh + Web Scraper primer
**Vreme:** 8-10 sati intenzivnog rada
**Energija:** SVE ILI NIŠTA! 💪

---

## 🎯 Cilj Dana

**Do kraja danas:**

1. ✅ Repo i venv spremni
2. ✅ CSV osnove savladane (reader/dict, delimiter, encoding, newline)
3. ✅ Mini CSV Cleaner v0 napravljen
4. ✅ Web scraper primer pokrenut (quotes.toscrape)
5. ✅ README + commit na GitHub
6. ✅ Python ritam uspostavljen (REPL → skripta → git)

**Ovo NIJE teorija.** Danas ODMAH kodiraš. Ako negde zaglaviš, AI je tu u VS Code-u!

## 📋 Struktura Dana (10h verzija)

### BLOK 1: Setup + CSV REPL Warm-up (09:00-10:30) - 1h 30min

-   Aktiviraj venv u projects/01-web-scraper (već postoji). Ako fali, pokreni task "Setup venv (web-scraper)".
-   U root-u projekta koristi REPL sa relativnim putanjama.
-   Prođi kroz [scratch/repl_sessions/csv_repl_plan.md](scratch/repl_sessions/csv_repl_plan.md) + [scratch/repl_sessions/csv_repl_exercises.md](scratch/repl_sessions/csv_repl_exercises.md):
    -   `csv.reader`, `csv.DictReader/DictWriter`, `newline=""`, `delimiter`, `encoding` error.
    -   Napravi fajlove: sample.csv, out.csv, people.csv.
-   Čekiraj [scratch/repl_sessions/csv_repl_checklist_20_09_2025.md](scratch/repl_sessions/csv_repl_checklist_20_09_2025.md) dok radiš.

### BLOK 2: Mini helper funkcije (10:30-11:30) - 1h

-   Otvori [sandbox/basics/python_refresh.py](sandbox/basics/python_refresh.py).
-   Dodaj funkcije (neka budu kratke, sa Path):
    -   `load_csv(path: Path) -> list[dict[str, str]]` (koristi `DictReader`).
    -   `write_csv(path: Path, rows: list[dict[str, str]], headers: list[str]) -> None` (koristi `DictWriter`).
-   Testiraj ih na fajlovima iz BLOK 1.
-   Kratak eksperimenat: pogrešan delimiter i encoding error.

### BLOK 3: CSV Cleaner v0 (11:45-13:00) - 1h 15min

-   Napravi novi fajl u sandbox/basics (npr. csv_cleaner.py).
-   Sample input (ručno napravi): par ispravnih redova + par sa whitespace, drugačijim delimiterom i praznim vrednostima.
-   Logika:
    -   Učitavanje u listu dict-ova.
    -   Normalizuj delimiter na `,`, trimuj whitespace, odbaci prazne redove.
    -   Sačuvaj u clean.csv.
    -   Ispiši statistiku: redova ulaz/izlaz/skiplovano.
-   (Po želji) jednostavan test: assert dužina izlaza + basic field check.

### 🍔 Pauza (13:00-14:00)

### BLOK 4: Web Scraper Primer (14:00-16:00) - 2h

-   Lokacija: projects/01-web-scraper.
-   Ako nije instalirano: pokreni task "Install deps (web-scraper)".
-   Pregledaj [projects/01-web-scraper/config.py](projects/01-web-scraper/config.py) i [projects/01-web-scraper/scraper.py](projects/01-web-scraper/scraper.py).
-   Pokreni scraper: `source venv/bin/activate && python scraper.py` (ili VS Code task Test/Run).
-   Proveri output/scraped_quotes.csv (prvih 5 redova).
-   Mini refaktor (ako stigneš): ubaci Path za output, dodaj `timeout` i `headers` proveru.

### BLOK 5: README + Git Commit (16:00-17:00) - 1h

-   README dopuni kratkim paragrafom o CSV Cleaner v0 (šta radi, gde se nalazi) i kako pokrenuti scraper.
-   `git status` → `git add .` → `git commit -m "chore: day01 csv foundations and scraper primer"` (ili slična poruka).
-   Ako je repo vezan za GitHub: `git push`.

### BLOK 6: Reflection + Plan Tomorrow (17:00-17:30) - 30min

-   Kratke beleške: šta je bilo jasno, gde je konfuzija (delimiter, newline, encoding, Path?).
-   Upis u DAY_01_SUMMARY.md (može u learning/ ili scratch/notes).
-   Postavi 3 cilja za Day 02 (npr. argparse za scraper, logging u fajl, jednostavni pytest za CSV Cleaner).

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from config import URLS, HEADERS, OUTPUT_DIR, OUTPUT_FILE, REQUEST_TIMEOUT, DELAY_BETWEEN_REQUESTS

def fetch_page(url):
"""
Fetches HTML content from URL.

    Args:
        url (str): Target URL

    Returns:
        str: HTML content or None if failed
    """
    try:
        print(f"📥 Fetching: {url}")
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)

        if response.status_code == 200:
            print(f"✅ Success! Status: {response.status_code}")
            return response.text
        else:
            print(f"❌ Failed! Status: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return None

def parse_quotes(html):
"""
Parses quotes from HTML content.

    Args:
        html (str): HTML content

    Returns:
        list: List of dictionaries with quote data
    """
    soup = BeautifulSoup(html, 'lxml')
    quotes_data = []

    quote_divs = soup.find_all('div', class_='quote')
    print(f"🔍 Found {len(quote_divs)} quotes on this page")

    for quote_div in quote_divs:
        try:
            text = quote_div.find('span', class_='text').text
            author = quote_div.find('small', class_='author').text
            tags = [tag.text for tag in quote_div.find_all('a', class_='tag')]

            quotes_data.append({
                'quote': text,
                'author': author,
                'tags': ', '.join(tags)
            })
        except AttributeError as e:
            print(f"⚠️ Warning: Could not parse quote - {e}")
            continue

    return quotes_data

def save_to_csv(data, output_path):
"""
Saves scraped data to CSV file.

    Args:
        data (list): List of dictionaries
        output_path (str): Path to output CSV file
    """
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"💾 Saved {len(data)} quotes to {output_path}")

def main():
"""
Main scraper logic.
"""
print("🚀 Starting Web Scraper...")
print(f"📋 Target URLs: {len(URLS)}")
print("=" \* 60)

    all_quotes = []

    # Scrape svaki URL
    for i, url in enumerate(URLS, 1):
        print(f"\n[{i}/{len(URLS)}] Processing: {url}")

        html = fetch_page(url)

        if html:
            quotes = parse_quotes(html)
            all_quotes.extend(quotes)
            print(f"✅ Extracted {len(quotes)} quotes")
        else:
            print(f"⚠️ Skipping {url} due to fetch error")

        # Delay između requesta (ne bombarduj server!)
        if i < len(URLS):  # Ne čekaj posle poslednjeg
            print(f"⏳ Waiting {DELAY_BETWEEN_REQUESTS}s before next request...")
            time.sleep(DELAY_BETWEEN_REQUESTS)

    # Sačuvaj rezultate
    print("\n" + "=" * 60)
    print(f"📊 Total quotes scraped: {len(all_quotes)}")

    if all_quotes:
        # Kreiraj output folder ako ne postoji
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        save_to_csv(all_quotes, output_path)

        print(f"✅ Scraping complete! Check: {output_path}")
    else:
        print("❌ No data scraped!")

if **name** == "**main**":
main()

````

**Zadatak 3.4: Testiranje! (20min)**

```bash
# Aktiviraj venv ako nije
source venv/bin/activate

# Pokreni scraper!
python scraper.py
````

**Očekivani output:**

```
🚀 Starting Web Scraper...
📋 Target URLs: 2
============================================================

[1/2] Processing: https://quotes.toscrape.com/page/1/
📥 Fetching: https://quotes.toscrape.com/page/1/
✅ Success! Status: 200
🔍 Found 10 quotes on this page
✅ Extracted 10 quotes
⏳ Waiting 1s before next request...

[2/2] Processing: https://quotes.toscrape.com/page/2/
📥 Fetching: https://quotes.toscrape.com/page/2/
✅ Success! Status: 200
🔍 Found 10 quotes on this page
✅ Extracted 10 quotes

============================================================
📊 Total quotes scraped: 20
💾 Saved 20 quotes to output/scraped_quotes.csv
✅ Scraping complete! Check: output/scraped_quotes.csv
```

**PROVERI CSV:**

```bash
cat output/scraped_quotes.csv | head -n 5
# Ili otvori u Excel/LibreOffice!
```

---

### BLOK 4: README + Git Commit (17:30-19:00) - 1h 30min

**Zadatak 4.1: README.md za Projekat (45min)**

Kreiraj `projects/01-web-scraper/README.md`:

````markdown
# Web Scraper Tool

**Status:** ✅ MVP Complete (Dec 13, 2025)
**Tech Stack:** Python 3.10+, Requests, BeautifulSoup, Pandas

---

## 📖 Description

Flexible web scraping tool that extracts structured data from websites and exports to CSV. Built for freelance clients needing data collection automation.

**Current Implementation:** Quotes scraper (demo)
**Customizable for:** Product listings, job postings, real estate data, competitor analysis

---

## 🚀 Features

-   ✅ Multiple URL scraping
-   ✅ Configurable headers (anti-blocking)
-   ✅ Rate limiting (respectful scraping)
-   ✅ Error handling & logging
-   ✅ CSV export with Pandas
-   ✅ Clean, documented code

---

## 🛠️ Installation

```bash
# Clone repo
git clone <your-repo-url>
cd python-automation-portfolio/projects/01-web-scraper

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```
````

---

## 📦 Dependencies

```
requests==2.31.0
beautifulsoup4==4.12.2
pandas==2.1.4
lxml==5.0.0
```

---

## 💻 Usage

### Basic Usage

```bash
python scraper.py
```

Output saved to `output/scraped_quotes.csv`.

### Customize Target URLs

Edit `config.py`:

```python
URLS = [
    "https://your-target-site.com/page1",
    "https://your-target-site.com/page2",
]
```

### Adjust Settings

```python
# config.py
REQUEST_TIMEOUT = 10  # seconds
DELAY_BETWEEN_REQUESTS = 1  # seconds (be nice to servers!)
OUTPUT_FILE = "your_output.csv"
```

---

## 📂 Project Structure

```
01-web-scraper/
├── scraper.py          # Main scraper logic
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── output/             # Scraped data (CSV files)
├── tests/              # Unit tests (coming soon)
└── venv/               # Virtual environment (not committed)
```

---

## 🧪 Example Output

**CSV Format:**

```csv
quote,author,tags
"The world as we have created it...",Albert Einstein,"change,deep-thoughts,thinking,world"
"It is our choices...",J.K. Rowling,"abilities,choices"
```

---

## 🔧 Customization for Clients

This scraper can be adapted for various use cases:

### E-commerce Price Monitoring

```python
# Parse product listings
def parse_products(html):
    soup = BeautifulSoup(html, 'lxml')
    products = []

    for item in soup.find_all('div', class_='product'):
        name = item.find('h2', class_='title').text
        price = item.find('span', class_='price').text
        products.append({'name': name, 'price': price})

    return products
```

### Job Listings Aggregation

```python
# Parse job postings
def parse_jobs(html):
    soup = BeautifulSoup(html, 'lxml')
    jobs = []

    for job in soup.find_all('div', class_='job-listing'):
        title = job.find('h3').text
        company = job.find('span', class_='company').text
        location = job.find('span', class_='location').text
        jobs.append({'title': title, 'company': company, 'location': location})

    return jobs
```

---

## ⚠️ Legal & Ethical Considerations

-   Always check `robots.txt` before scraping
-   Respect rate limits (don't overload servers)
-   Some websites prohibit scraping in Terms of Service
-   Use scraped data responsibly and legally

**This tool is for educational and legitimate business purposes only.**

---

## 🐛 Troubleshooting

### Issue: "Connection timeout"

**Solution:** Increase `REQUEST_TIMEOUT` in config.py

### Issue: "Status 403 Forbidden"

**Solution:** Update `User-Agent` header in config.py

### Issue: "No data found"

**Solution:** Inspect HTML with DevTools, adjust CSS selectors

---

## 🚀 Future Enhancements

-   [ ] Command-line arguments (argparse)
-   [ ] Selenium support for JavaScript-heavy sites
-   [ ] Proxy rotation
-   [ ] Database export (SQLite/PostgreSQL)
-   [ ] Scheduled scraping (cron jobs)
-   [ ] Email notifications on completion
-   [ ] Unit tests with pytest

---

## 📞 Contact

For custom scraping projects:

**Jole Pavlović**
GitHub: [jole-pavlovic-dev]
Available for freelance work starting January 2026

---

**License:** MIT
**Last Updated:** December 14, 2025

```

```

**Git koraci (kratko podsetnik)**

```bash
git status
git add .
git commit -m "chore: day01 csv foundations and scraper primer"
# ako je povezan remote
git push
```

---

### BLOK 6: Reflection + Plan Tomorrow (17:00-17:30) - 30min

**Zadatak 5.1: Napravi DAY_01_SUMMARY.md**

```markdown
# Day 01 Summary

**Date:** 14. decembar 2025.

## ✅ Completed

-   [x] Venv aktiviran i deps instalirani
-   [x] CSV REPL warm-up (reader/dict, delimiter, encoding, newline)
-   [x] Helper funkcije za CSV read/write (Path + DictReader/DictWriter)
-   [x] CSV Cleaner v0 (trim, delimiter normalize, drop prazne)
-   [x] Web scraper primer pokrenut (quotes.toscrape → CSV)
-   [x] README dopuna + git commit/push

## 📊 Stats

-   Lines of code written: [popuni]
-   Files created/edited: [popuni]
-   Quotes scraped: [popuni]
-   Commits: [popuni]

## 🧠 What I Learned

-   Razlika `csv.reader` vs `DictReader`, važnost `newline=""`
-   Delimiter/encoding greške i kako ih rešiti
-   Path za portabilne putanje
-   Jednostavna ETL logika (učitaj → očisti → upiši)
-   Kako scraper hvata HTML i eksportuje u CSV

## 💪 Challenges

-   [Napiši šta ti je bilo teško]
-   [Gde si zapeo i kako si rešio]

## 🎯 Tomorrow (Day 02)

1. Dodaj argparse za scraper (izbor output fajla, broj strana)
2. Logging u fajl i bolji error handling (requests timeout/retry)
3. Pytest za CSV Cleaner (bar 2 testa: trim + skip praznih)
4. (Optional) Refaktor scraper u klasu
5. (Optional) Rainbow CSV / VS Code upotreba za verifikaciju

## 🗣️ Notes

-   [Tvoje opservacije]
-   [Šta ti se sviđa u Python-u]
-   [Plan za sledeću nedelju]

---

**Energy Level:** [1-10]
**Confidence Level:** [1-10]
**Ready for Day 02:** [YES/NO]
```

---

## 🎉 ČESTITAM

Ako si došao ovde, završio si Day 01! Evo šta si postigao:

✅ **Repo kreiran** - python-automation-portfolio na GitHub-u
✅ **CSV Cleaner v0** - osnovni ETL (čitanje → čišćenje → upis)
✅ **Prvi projekat** - Web Scraper Tool (funkcioniše!)
✅ **Python sintaksa** - osvežena i testirana
✅ **Real code written** - 300+ linija production-ready koda
✅ **Git workflow** - commit + push mastered

---

## 🚀 Šta Dalje?

**Sutra (Day 02):**

-   Dodaj CLI argumente
-   Implementiraj logging
-   Refaktoruj u class-based strukturu
-   Osnovno unit testing

**Sledećih 7 dana:**

-   Week 1: Web Scraper projekt complete (advanced features)
-   Dec 21: Kreni na Project 2 - Excel Automation

**3-Month Goal:**

-   4 portfolio projekta
-   Freelance profiles live (Upwork/Fiverr)
-   Prvi klijent do kraja januara 2026

---

## 💡 Pro Tips

1. **Commit često!** Svaki feature = novi commit
2. **Testiraj u malim koracima** - nemoj pisati 200 linija pa onda testirati
3. **Čitaj error poruke** - Python errors su super informativne!
4. **Pitaj AI** - ako zaglaviš 15+ minuta, pitaj za pomoć
5. **Pravi pauze** - svaka 2h stanke 10-15min

---

**See you tomorrow at 09:00! 🚀**

**ALL OR NOTHING!** 💪
