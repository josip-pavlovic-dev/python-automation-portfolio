# DAY 02: CLI + Logging + Tests 🚀

Datum: 14. decembar 2025
Fokus: Argparse (CLI), Logging (file + rotating), Pytest (osnovno)
Vreme: 8–10 sati fokusiranog rada
Energia: Idemo dalje – sistematizacija koda i kvaliteta! 💪

---

## 🎯 Ciljevi Dana

Do kraja dana:

- ✅ Dodati CLI podršku sa `argparse` (ulazi: URL-ovi, output putanja, delay)
- ✅ Uvesti `logging` (console + file, rotating handler, nivo INFO/ERROR)
- ✅ Refaktorisati scraper u klasu `Scraper`
- ✅ Napisati osnovne testove sa `pytest` za parser
- ✅ Ažurirati README (usage sa CLI i logging)
- ✅ Commit + lokalni push (ako želiš)

---

## 🗂️ Kontekst Fajlovi

- projects/01-web-scraper/scraper.py
- projects/01-web-scraper/config.py
- projects/01-web-scraper/tests/test_scraper.py (novi)
- learning/DAILY_KICKOFF_PROMPT.md

---

## ⏱️ Plan Po Blokovima

### BLOK 1 (09:00–11:00): Argparse – CLI Interface (2h)

1. Kreiraj CLI parser u `scraper.py` – minimalna verzija:

```python
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Web Scraper Tool")
    parser.add_argument("--urls", nargs="*", help="List of URLs to scrape")
    parser.add_argument("--output", default="output/scraped_quotes.csv", help="CSV output path")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests (seconds)")
    parser.add_argument("--timeout", type=int, default=10, help="Request timeout (seconds)")
    parser.add_argument("--log", default="logs/scraper.log", help="Log file path")
    parser.add_argument("--level", default="INFO", choices=["DEBUG","INFO","WARNING","ERROR"], help="Log level")
    return parser
```

2. U `main()` koristi parser:

```python
if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    # Pass args to scraper run
```

3. Testiraj u terminalu:

```bash
source venv/bin/activate
python scraper.py --urls https://quotes.toscrape.com/page/1/ https://quotes.toscrape.com/page/2/ --output output/quotes.csv --delay 1 --timeout 10 --level INFO
```

4. Dodaj validaciju: ako `--urls` nije dato, koristi `config.URLS` kao fallback.

---

### BLOK 2 (11:15–13:15): Logging – Console + File + Rotating (2h)

1. Napravi `setup_logger()` u `scraper.py`:

```python
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(log_file: str, level: str = "INFO"):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger("scraper")
    logger.setLevel(getattr(logging, level))

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(getattr(logging, level))
    ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # Rotating file handler
    fh = RotatingFileHandler(log_file, maxBytes=500_000, backupCount=3)
    fh.setLevel(getattr(logging, level))
    fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s"))

    # Avoid duplicate handlers when re-running
    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
```

2. Koristi logger u `fetch_page()` i `parse_quotes()`:

```python
logger.info(f"Fetching: {url}")
logger.error("Failed with status %s", response.status_code)
```

3. Pokretanje:

```bash
python scraper.py --log logs/scraper.log --level INFO
cat logs/scraper.log | head -n 10
```

---

### 🍔 Pauza (13:15–14:15)

Reset – ručak, hodanje, voda.

---

### BLOK 3 (14:15–16:45): Refactor – Class-Based Scraper (2.5h)

1. Napravi klasu:

```python
class Scraper:
    def __init__(self, urls, headers, output_path, timeout, delay, logger):
        self.urls = urls
        self.headers = headers
        self.output_path = output_path
        self.timeout = timeout
        self.delay = delay
        self.logger = logger

    def fetch_page(self, url):
        # use self.logger, self.timeout
        pass

    def parse_quotes(self, html):
        # return list of dicts
        pass

    def run(self):
        # main loop
        pass
```

2. `main()` postaje tanki orchestration:

```python
def main():
    args = build_parser().parse_args()
    logger = setup_logger(args.log, args.level)
    urls = args.urls or URLS
    scraper = Scraper(urls, HEADERS, args.output, args.timeout, args.delay, logger)
    scraper.run()
```

3. Testiraj ponovo:

```bash
python scraper.py --urls https://quotes.toscrape.com/page/1/ --delay 0.5 --level DEBUG
```

---

### BLOK 4 (16:45–17:45): Pytest – Osnovni Testovi (1h)

1. Napravi folder `tests/` i fajl `tests/test_scraper.py`:

```python
import pytest
from bs4 import BeautifulSoup
from projects01_web_scraper.scraper import Scraper  # adjust import to your structure

HTML_FIXTURE = """
<html>
  <body>
    <div class="quote">
      <span class="text">Quote 1</span>
      <small class="author">Author 1</small>
      <a class="tag">life</a>
      <a class="tag">wisdom</a>
    </div>
    <div class="quote">
      <span class="text">Quote 2</span>
      <small class="author">Author 2</small>
    </div>
  </body>
</html>
"""

class DummyLogger:
    def info(self, *args, **kwargs):
        pass
    def error(self, *args, **kwargs):
        pass

@pytest.fixture
def scraper():
    return Scraper(urls=[], headers={}, output_path="/tmp/out.csv", timeout=5, delay=0, logger=DummyLogger())

def test_parse_quotes(scraper):
    data = scraper.parse_quotes(HTML_FIXTURE)
    assert len(data) == 2
    assert data[0]["author"] == "Author 1"
    assert "tags" in data[0]
```

2. Pokreni testove:

```bash
pip install pytest
pytest -q
```

3. Dodaj `pytest.ini` (opciono):

```ini
[pytest]
addopts = -q
```

---

### BLOK 5 (17:45–19:00): README + Commit (1h 15min)

1. README dopune:

- Usage primer sa CLI argumentima
- Logging sekcija (gde se logovi čuvaju)
- Tests sekcija (kako pokrenuti)

2. Git workflow:

```bash
git add projects/01-web-scraper scraper.py config.py tests/ learning/DAY_02_KICKOFF.md
git commit -m "feat(day02): add argparse CLI, logging, class-based refactor, and pytest scaffold"
```

---

## 🧩 Zadaci – Checklista

- [ ] Implement `argparse` parser i validacija
- [ ] Napraviti `setup_logger()` sa rotating file handlerom
- [ ] Refaktorisati u `Scraper` klasu (fetch, parse, run)
- [ ] Dodati osnovne `pytest` testove
- [ ] Dopuniti README – usage + logging + tests
- [ ] Commit promene

---

## 🐛 Troubleshooting

- Problem: "ImportError: cannot import Scraper"

  - Rešenje: Proveri PYTHONPATH ili koristi relativne import puteve; pokreći iz root-a.

- Problem: "FileNotFoundError: logs/scraper.log"

  - Rešenje: `os.makedirs(os.path.dirname(log_file), exist_ok=True)` u logger setup-u.

- Problem: "pytest cannot find tests"
  - Rešenje: Uveri se da je folder `tests/` u projektu i da fajl počinje sa `test_`.

---

## 📚 Šta Vežbati Danas

- Napiši 3 varijante CLI-ja: (a) sve preko `config.py`, (b) sve preko argumenata, (c) mešovito.
- Dodaj `--proxy` i `--user-agent` argumente, demonstriraj promenu headera.
- Napravi `--max-pages` argument i implementiraj paginaciju.

---

## 🧠 Mentalni Model

- CLI → reproducibilno pokretanje, lakša integracija.
- Logging → vidljivost, dijagnostika, profesionalno.
- Tests → sigurnost promene, poverenje u refactor.
- Klasa → enkapsulacija i čitljivost.

Idemo jako — kvalitet + brzina! 🚀
