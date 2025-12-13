# DAY 01: Python Automation Kickoff 🚀

**Datum:** 13. decembar 2025.
**Fokus:** Python Refresh + Web Scraper Projekt -START
**Vreme:** 8-10 sati intenzivnog rada
**Energija:** SVE ILI NIŠTA! 💪

---

## 🎯 Cilj Dana

**Do kraja danas:**

1. ✅ Repo kreiran i inicijalizovan
2. ✅ Python okruženje konfigurisano
3. ✅ Prvi scraper kod napisan (basic verzija)
4. ✅ Prvo testiranje u terminalu - radi!
5. ✅ Prvi commit na GitHub
6. ✅ Python ritam uspostavljen - sećaš se sintakse!

**Ovo NIJE teorija.** Danas ODMAH kodiš. Ako negde zaglaviš, AI je tu u VS Code-u!

---

## 📋 Struktura Dana (10h verzija)

### BLOK 1: Setup + Python Refresh (09:00-11:00) - 2h

**Zadatak 1.1: Python Environment Setup (30min)**

```bash
# Proveri Python verziju
python3 --version  # Očekujem 3.10+

# Kreiraj virtual environment za projekat
cd ~/code/python-automation-lab/python-automation-portfolio/projects/01-web-scraper
python3 -m venv venv

# Aktiviraj okruženje
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip
```

**Zadatak 1.2: Instaliraj Dependencies (10min)**

```bash
# Osnovne biblioteke za web scraping
pip install requests beautifulsoup4 pandas lxml

# Snimi requirements
pip freeze > requirements.txt
```

**Zadatak 1.3: Python Syntax Refresh - Hands-On! (1h 20min)**

Otvori novi fajl: `python_refresh.py`

```python
# 1. VARIABLES & TYPES (10min)
# =========================
name = "Jole"
age = 30  # pretpostavljam :)
is_motivated = True
skills = ["Python", "automation", "problem-solving"]

print(f"Ime: {name}, Godina: {age}")
print(f"Skills: {', '.join(skills)}")

# 2. FUNCTIONS (15min)
# ====================
def greet(name):
    """Pozdravlja korisnika."""
    return f"Hello, {name}! Ready to scrape! 🕷️"

def calculate_discount(price, discount_percent):
    """Računa cenu sa popustom."""
    discount = price * (discount_percent / 100)
    return price - discount

# Testiranje
print(greet("Jole"))
print(f"Cena sa popustom: {calculate_discount(100, 20)} EUR")

# 3. LISTS & LOOPS (20min)
# =========================
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

# For petlja
for url in urls:
    print(f"Scraping: {url}")

# List comprehension (Python način!)
urls_upper = [url.upper() for url in urls]
print(urls_upper)

# 4. DICTIONARIES (20min)
# =======================
product = {
    "name": "Laptop",
    "price": 1200,
    "brand": "Dell",
    "in_stock": True
}

# Pristup vrednostima
print(f"Proizvod: {product['name']}, Cena: {product['price']} EUR")

# Iteracija kroz dictionary
for key, value in product.items():
    print(f"{key}: {value}")

# Lista dictionaries (tipičan scraping output!)
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75}
]

for product in products:
    print(f"{product['name']}: €{product['price']}")

# 5. FILE OPERATIONS (15min)
# ===========================
# Pisanje u fajl
with open("test_output.txt", "w") as f:
    f.write("Hello from Python!\n")
    f.write("Web scraping is awesome!\n")

# Čitanje iz fajla
with open("test_output.txt", "r") as f:
    content = f.read()
    print(content)

# CSV operacije (biće ti jako potrebno!)
import csv

data = [
    ["Name", "Price", "Brand"],
    ["Laptop", "1200", "Dell"],
    ["Mouse", "25", "Logitech"]
]

with open("test_products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV fajl kreiran!")
```

**ZADATAK:** Otvori `python_refresh.py`, pokreni kod sekciju po sekciju. Promeni vrednosti, eksperimentuši!

```bash
python python_refresh.py
```

---

### BLOK 2: Web Scraping Basics (11:15-13:15) - 2h

**Zadatak 2.1: Requests Biblioteka (30min)**

Kreiraj novi fajl: `test_requests.py`

```python
import requests

# 1. Osnovni GET request
url = "https://httpbin.org/get"
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(f"Content Type: {response.headers['Content-Type']}")
print(f"Response Text:\n{response.text[:200]}...")  # Prva 200 karaktera

# 2. Provera da li je request uspešan
if response.status_code == 200:
    print("✅ Request successful!")
else:
    print(f"❌ Request failed with code {response.status_code}")

# 3. JSON response
url_json = "https://jsonplaceholder.typicode.com/users/1"
response_json = requests.get(url_json)
data = response_json.json()  # Parsiraj JSON

print(f"\nUser Name: {data['name']}")
print(f"Email: {data['email']}")
print(f"City: {data['address']['city']}")

# 4. Custom headers (važno za scraping!)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
response_with_headers = requests.get("https://httpbin.org/headers", headers=headers)
print(f"\nResponse with custom headers:\n{response_with_headers.text[:300]}...")
```

**Pokreni i vidi kako funkcioniše:**

```bash
python test_requests.py
```

**Zadatak 2.2: BeautifulSoup Parsing (1h)**

Kreiraj: `test_beautifulsoup.py`

```python
import requests
from bs4 import BeautifulSoup

# 1. Učitaj HTML stranicu
url = "https://quotes.toscrape.com/"  # Odličan sajt za vežbanje!
response = requests.get(url)
html = response.text

# 2. Parsiraj HTML sa BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# 3. Izvuci naslov stranice
title = soup.find('title')
print(f"Page Title: {title.text}")

# 4. Nađi sve quote tekstove
quotes = soup.find_all('span', class_='text')
print(f"\n📖 Ukupno citata: {len(quotes)}\n")

for i, quote in enumerate(quotes[:5], 1):  # Prvih 5
    print(f"{i}. {quote.text}")

# 5. Izvuci autore
authors = soup.find_all('small', class_='author')
print(f"\n✍️ Autori:\n")

for i, author in enumerate(authors[:5], 1):
    print(f"{i}. {author.text}")

# 6. Struktuirani podaci - PRAVI NAČIN!
quotes_data = []

# Svaki quote je u <div class="quote">
quote_divs = soup.find_all('div', class_='quote')

for quote_div in quote_divs:
    # Izvuci text, author, i tags
    text = quote_div.find('span', class_='text').text
    author = quote_div.find('small', class_='author').text
    tags = [tag.text for tag in quote_div.find_all('a', class_='tag')]

    quotes_data.append({
        'text': text,
        'author': author,
        'tags': ', '.join(tags)
    })

# Prikaži strukturirane podatke
print("\n📊 Strukturirani podaci:\n")
for i, quote in enumerate(quotes_data[:3], 1):
    print(f"{i}.")
    print(f"   Text: {quote['text']}")
    print(f"   Author: {quote['author']}")
    print(f"   Tags: {quote['tags']}\n")

# 7. Export u CSV koristeći pandas
import pandas as pd

df = pd.DataFrame(quotes_data)
df.to_csv('quotes_scraped.csv', index=False, encoding='utf-8')
print("✅ CSV fajl kreiran: quotes_scraped.csv")
```

**Pokreni:**

```bash
python test_beautifulsoup.py
```

**PROVERITE CSV:**

```bash
cat quotes_scraped.csv  # Ili otvori u Excel-u!
```

**Zadatak 2.3: CSS Selectors Deep Dive (30min)**

Dodaj na kraj `test_beautifulsoup.py`:

```python
# CSS SELECTORS - moćniji način!
print("\n🎯 CSS SELECTORS:\n")

# 1. Selektuj po klasi
quotes_css = soup.select('span.text')
print(f"Quotes via CSS selector: {len(quotes_css)}")

# 2. Selektuj po ID (ako postoji)
# container = soup.select_one('#content')  # Primer

# 3. Nested selectors
authors_css = soup.select('div.quote small.author')
print(f"Authors via nested selector: {len(authors_css)}")

# 4. Kombinovani selektori
tags_css = soup.select('div.quote a.tag')
print(f"Tags via selector: {len(tags_css)}")

# 5. Atributi
links = soup.select('a[href]')  # Svi linkovi sa href
print(f"Total links: {len(links)}")
```

---

### 🍔 PAUZA ZA RUČAK (13:15-14:15) - 1h

**NE PRESKAČI!** Mozak treba odmor. Jedi, prošetaj, resetuj se.

---

### BLOK 3: Prvi Pravi Scraper (14:15-17:15) - 3h

**SADA PRAVIŠ PRAVI PROJEKAT!**

**Zadatak 3.1: Projekat Setup (15min)**

Organizuj foldere:

```bash
cd ~/code/python-automation-lab/python-automation-portfolio/projects/01-web-scraper

# Folder struktura:
# 01-web-scraper/
#   ├── scraper.py (glavni kod)
#   ├── config.py (konfiguracija)
#   ├── requirements.txt
#   ├── README.md
#   ├── tests/ (kasnije)
#   └── output/ (gde se čuva CSV)

mkdir -p output tests
```

**Zadatak 3.2: config.py - Best Practice! (10min)**

Kreiraj `config.py`:

```python
"""
Configuration file for web scraper.
"""

# Target websites
URLS = [
    "https://quotes.toscrape.com/page/1/",
    "https://quotes.toscrape.com/page/2/",
]

# Request headers (simuliraj browser)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Output settings
OUTPUT_DIR = "output"
OUTPUT_FILE = "scraped_quotes.csv"

# Request settings
REQUEST_TIMEOUT = 10  # sekunde
DELAY_BETWEEN_REQUESTS = 1  # sekunda (budi pristojan prema serveru!)
```

**Zadatak 3.3: scraper.py - Glavni Kod! (2h 15min)**

Kreiraj `scraper.py`:

```python
"""
Web Scraper Tool - Quotes Scraper
Scrapes quotes from quotes.toscrape.com and saves to CSV.
"""

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
    print("=" * 60)

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


if __name__ == "__main__":
    main()
```

**Zadatak 3.4: Testiranje! (20min)**

```bash
# Aktiviraj venv ako nije
source venv/bin/activate

# Pokreni scraper!
python scraper.py
```

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
**Last Updated:** December 13, 2025

````

**Zadatak 4.2: Git Commit! (30min)**

```bash
# Proveri status
git status

# Dodaj sve fajlove
git add .

# Commit sa opisnom porukom
git commit -m "feat: initialize Python automation portfolio with web scraper MVP

- Add comprehensive README for portfolio
- Implement quotes scraper (requests + BeautifulSoup + pandas)
- Add config.py for easy customization
- Include detailed project README with usage examples
- Setup .gitignore for Python projects
- Create folder structure (projects/, learning/, docs/)

Day 01 complete: scraper tested and working!"

# Vidi commit
git log --oneline -1
````

**Zadatak 4.3: GitHub Push (15min)**

```bash
# Kreiraj novi repo na GitHub (via web ili gh CLI)
# Zatim:

git remote add origin https://github.com/jole-pavlovic-dev/python-automation-portfolio.git
git branch -M main
git push -u origin main
```

---

### BLOK 5: Reflection + Plan Tomorrow (19:00-19:30) - 30min

**Zadatak 5.1: Napravi DAY_01_SUMMARY.md**

```markdown
# Day 01 Summary

**Date:** 13. decembar 2025.

## ✅ Completed

-   [x] Repo kreiran i inicijalizovan
-   [x] Python environment setup (venv)
-   [x] Dependencies installed (requests, beautifulsoup4, pandas)
-   [x] Python syntax refresh (functions, loops, dicts, files)
-   [x] Requests library testing
-   [x] BeautifulSoup testing
-   [x] **PRVI PRAVI SCRAPER NAPISAN I TESTIRAN!** 🎉
-   [x] CSV export funkcioniše
-   [x] README dokumentacija
-   [x] Git commit + push na GitHub

## 📊 Stats

-   Lines of code written: ~300+
-   Files created: 8
-   Quotes scraped: 20
-   Commits: 1 (solid!)

## 🧠 What I Learned

-   Kako funkcioniše requests.get() i response.status_code
-   BeautifulSoup parsing sa find() i find_all()
-   CSS selectors za preciznije selektovanje
-   Pandas DataFrame.to_csv() za export
-   Best practice: config.py za settings
-   Error handling sa try/except blokovima

## 💪 Challenges

-   [Napiši šta ti je bilo teško]
-   [Gde si zapeo i kako si rešio]

## 🎯 Tomorrow (Day 02)

1. Dodaj command-line arguments (argparse)
2. Implementiraj error logging u fajl
3. Refaktoruj kod - napravi scraper class
4. Unit tests sa pytest (osnovni)
5. Selenium setup za JS-heavy sites (optional)

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
