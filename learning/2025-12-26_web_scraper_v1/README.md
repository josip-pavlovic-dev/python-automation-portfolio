# 🕷️ WEB SCRAPER v1 — Dan 8: Setup & Foundation

**Datum:** 26. Decembar 2025
**Status:** 🔴 AKTIVNO (Dan 8/14)
**Trajanje:** 8 sati
**Prethodni Dan:** ✅ Dan 6-7 (Pathlib + Testing + Error Handling Complete)

---

## 🎯 Šta Radiš Danas (Dan 8)?

Danas kreirate **foundation** za Web Scraper projekat. Ovo je **SETUP DAN** — ne scrape-ovanja još, već infrastrukture!

### Očekivani Rezultat na Kraju Dana

```
projects/01-web-scraper/
├── venv/                          # Virtual environment
├── config.py                       # Konfiguracija
├── scraper.py                      # Main scraper (prazna struktura)
├── requirements.txt                # Dependencies
├── tests/
│   ├── __init__.py
│   ├── conftest.py                 # Pytest fixtures
│   └── test_scraper_basics.py      # Prvi testovi
├── logs/
│   └── app.log                      # Log fajl
├── output/
│   └── sample.csv                   # Output primer
└── README.md                        # Project dokumentacija

✅ Sve je verzionovano u Git
✅ Svi testovi prolaze
✅ Struktura je proizvodna
✅ Logovanje je konfigurisano
```

---

## 📚 Šta Ćeš Naučiti?

### 1. **HTTP Requests osnove** (1h)

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)  # 200
print(response.text)         # HTML sadržaj
```

### 2. **HTML Parsing sa BeautifulSoup** (1h)

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
titles = soup.select("h1")  # CSS selektori
```

### 3. **Project Setup i Struktura** (2h)

```
Šta kreiramo:
- config.py sa settings (URL, headers, timeout)
- scraper.py sa basic funkcijama
- tests/ sa test fixtures
- Logging konfiguracija
```

### 4. **Error Handling pri Scraping-u** (2h)

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Baci grešku ako je 404/500
except requests.RequestException as e:
    logger.error(f"Request failed: {e}")
```

### 5. **REPL Praksa + Testiranje** (2h)

```bash
# Pokrenite REPL i eksperimentirajte
python3
>>> from scraper import fetch_page
>>> html = fetch_page("https://example.com")
>>> print(len(html))
```

---

## 🗺️ Struktura Učenja Dana 8

### FAZA 1 (1.5h) — Requests + BeautifulSoup Osnove

-   ✅ Instalacija libraryja
-   ✅ GET request-i
-   ✅ HTML parsing sa CSS selektorima
-   ✅ REPL praksa

### FAZA 2 (1.5h) — Project Setup

-   ✅ Kreiranje `projects/01-web-scraper` strukture
-   ✅ config.py sa settings-ima
-   ✅ requirements.txt sa zavisnostima
-   ✅ Git inicijalizacija

### FAZA 3 (2h) — Scraper Osnova

-   ✅ `scraper.py` sa `fetch_page(url)` funkcijom
-   ✅ User-Agent headers
-   ✅ Error handling
-   ✅ Logging

### FAZA 4 (2h) — Testing Setup

-   ✅ `conftest.py` sa fixtures-ima
-   ✅ Mock test stranice
-   ✅ Prvi `test_scraper_basics.py` testovi
-   ✅ Coverage proveravanja

---

## 📖 Kako Koristiš Materijal?

### 1️⃣ **Započni sa kickoff.md** (5 min)

-   Brz pregled timeline-a
-   Šta trebš ako zaglavim

### 2️⃣ **Čitaj cheatsheet.md** (30 min)

-   Requests dokumentacija
-   BeautifulSoup CSS selektori
-   Error handling patterns

### 3️⃣ **Prati web_scraper_setup_guide.md** (6h)

-   **GLAVNI MATERIJAL** — korak po korak vežbe
-   REPL primeri
-   Često ponovljeni kodovi

### 4️⃣ **Koristi tasks.md** (Tokom dana)

-   Checklist šta treba da završiš
-   Checkpoint-i

### 5️⃣ **Ako Zaglavim → chatlog.md**

-   Česta pitanja
-   Rešenja za česte greške

---

## 🔗 Povezivanja sa Prethodnim Danima

| Dan         | Što Si Naučio                 | Kako Se Koristi Danas            |
| ----------- | ----------------------------- | -------------------------------- |
| **Dan 5**   | Type Annotations (TypedDict)  | `class ScrapedItem(TypedDict):`  |
| **Dan 6**   | Pathlib (`Path`, `mkdir`)     | `Path("output") / "data.csv"`    |
| **Dan 7**   | Pytest (`tmp_path`, `caplog`) | `test_scraper_basics.py` testovi |
| **Dan 6-7** | Error Handling                | Try/except u scraper-u           |
| **Dan 1-4** | CSV + Logging + CLI           | Sačuvaj u CSV, loguj, CLI args   |

---

## ⚡ Quick Reference

### Instalacija Dependencies

```bash
cd projects/01-web-scraper
python -m venv venv
source venv/bin/activate
pip install requests beautifulsoup4 pytest pytest-cov
pip freeze > requirements.txt
```

### Testiranje

```bash
pytest tests/test_scraper_basics.py -v
pytest --cov=scraper --cov-report=term-missing
```

### REPL Praksa

```bash
source venv/bin/activate
python3

# Isprobaj requests
>>> import requests
>>> r = requests.get("https://httpbin.org/html")
>>> print(r.status_code)
200

# Isprobaj BeautifulSoup
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(r.text, "html.parser")
>>> print(soup.prettify()[:200])
```

---

## 🎯 Minimalni Zahtev za Dan 8

**MINIMUM (da bih mogao nastaviti na Dan 9):**

```
1. ✅ Instalisan requests i beautifulsoup4
2. ✅ Kreiran projects/01-web-scraper sa strukturom
3. ✅ config.py sa settings-ima (URL, headers)
4. ✅ scraper.py sa fetch_page(url) funkcijom
5. ✅ test_scraper_basics.py sa 3+ testova
6. ✅ Sve testove prolaze (pytest -v)
7. ✅ Coverage >70%
8. ✅ Git commit sa porukom "Day 8: Web Scraper Setup"
```

---

## 💡 Pro Tips za Dan 8

1. **Koristi `httpbin.org` za testiranje** — fake endpoint za vežbu
2. **Dodaj User-Agent header** — neki serveri odbijaju bot zahteve
3. **Postavi timeout** — izbegni da se script zamrzne
4. **Loguj sve zahteve** — debug je lakši sa logovima
5. **Testiranje sa mock-om** — ne testira pravi server svaki put
6. **Čitaj requests dokumentaciju** — samo 5 minuta ali je korisno

---

## 📞 Support Struktura

### Ako Se Zaglaviš na Requests

```bash
# Proveri status koda
>>> response.status_code
200  # OK
404  # Not found
500  # Server error

# Proveri headers
>>> response.headers
{'content-type': 'text/html; charset=utf-8', ...}

# Proveri sadržaj
>>> response.text[:100]
```

### Ako Se Zaglaviš na BeautifulSoup

```python
# Sve što je u <div class="title">
div = soup.select_one("div.title")

# Sve <a> tagove
links = soup.select("a")

# Tekst iz elementa
text = soup.select_one("h1").get_text(strip=True)
```

### Ako Se Zaglaviš na Pytest

```bash
# Pokreni samo jedan test
pytest tests/test_scraper_basics.py::test_fetch_page_returns_string -v

# Vidi print output
pytest -s tests/test_scraper_basics.py

# Vidi coverage
pytest --cov=scraper tests/
```

---

## 📚 Reference Materijali

**Local Files:**

-   [cheatsheet.md](./cheatsheet.md) — Requests + BeautifulSoup reference
-   [web_scraper_setup_guide.md](./web_scraper_setup_guide.md) — **GLAVNI MATERIJAL**
-   [tasks.md](./tasks.md) — Checklist
-   [chatlog.md](./chatlog.md) — Q&A

**Official Docs:**

-   [Requests Docs](https://docs.python-requests.org/)
-   [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
-   [Pytest Docs](https://docs.pytest.org/)

**Prethodni Materijali:**

-   `learning/2025-12-22_pathlib_advanced/cheatsheet.md` — Pathlib refresh
-   `scratch/docs/cheatsheet_error_handling.md` — Error handling patterns
-   `scratch/docs/cheatsheet_pytest_testing.md` — Pytest fixtures

---

## 🚀 Šta Dolazi Dan 9?

**Dan 9-10:** Web Scraper Implementation

```python
# To će biti tvoj kod na Dan 9:
class Product(TypedDict):
    title: str
    price: float
    url: str

def scrape_products(url: str) -> list[Product]:
    """Scrape proizvode sa CSS selektorima"""
    html = fetch_page(url)
    items = parse_products(html)
    return items
```

---

## ✅ Checklist Pre Nego Počneš

Proveri da li imaš sve od Dana 6-7:

-   [ ] Razumem `Path` operacije (Pathlib)
-   [ ] Mogu da napravim jednostavan test sa `tmp_path`
-   [ ] Znam kako koristiti `pytest.raises()` za greške
-   [ ] Razumem try/except/else/finally
-   [ ] Znam kako da napravim custom exception
-   [ ] Mogu da koristim `logging` modul

Ako je sve ✅, spreman si za Dan 8! 🚀

---

**Status: READY TO START**

**Start Time: Kada god želiš**

**Duration: 8 hours**

**Next: [kickoff.md](./kickoff.md)**

---
