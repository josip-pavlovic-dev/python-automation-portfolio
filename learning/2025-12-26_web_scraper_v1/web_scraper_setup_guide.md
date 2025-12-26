---
type: setup_guide
topic: Web Scraper v1 — Detaljni Setup Vodič (Dan 8)
date: 2025-12-26
duration: 6 hours
linked_to: 2025-12-26_web_scraper_v1
---

# 🕷️ Web Scraper Setup Vodič — Sve 4 Faze (Dan 8)

**OVO JE GLAVNI MATERIJAL ZA DAN 8** — Prati sve korake po redu!

---

## 📑 Sadržaj

-   **FAZA 1 (1.5h)** — Requests + BeautifulSoup osnove sa REPL primerom
-   **FAZA 2 (1.5h)** — Project struktura i setup
-   **FAZA 3 (2h)** — Scraper core funkcije
-   **FAZA 4 (2h)** — Testing setup

---

# FAZA 1: Requests + BeautifulSoup Osnove (1.5h)

## Korak 1.1: Instalacija (5 min)

```bash
# Kreiraj venv ako već nije kreiran
cd projects/01-web-scraper
python -m venv venv

# Aktiviraj venv
source venv/bin/activate  # Linux/Mac
# ILI (Windows)
venv\Scripts\activate

# Instaliraj libraryje
pip install requests beautifulsoup4 pytest pytest-cov pytest-mock

# Proveri instalaciju
python3 -c "import requests; import bs4; print('OK')"
# Output: OK
```

## Korak 1.2: GET Zahtev — REPL Praksa (20 min)

Otvori REPL i eksperimentiraj:

```bash
python3
```

### Test 1: Osnovna Zahtev

```python
>>> import requests
>>>
>>> # GET zahtev ka httpbin.org (fake server za testing)
>>> response = requests.get("https://httpbin.org/html")
>>> print(f"Status: {response.status_code}")
Status: 200
>>>
>>> # Proveri da li je HTML
>>> print(type(response.text))
<class 'str'>
>>>
>>> # Prikazi prvih 100 karaktera
>>> print(response.text[:100])
<!DOCTYPE html>
<html>
  <head>
    <title>Herman Melville — Moby-Dick</title>
  </head>
```

**Checkout:** Dobio si HTML kao string! ✅

### Test 2: Headers i Status Kod

```python
>>>
>>> # Pogledaj status kod
>>> print(response.status_code)
200
>>>
>>> # Pogledaj headers
>>> print(response.headers["content-type"])
text/html; charset=utf-8
>>>
>>> # Pogledaj URL (može biti drugačit zbog redirect-a)
>>> print(response.url)
https://httpbin.org/html
```

**Checkpoint:** Status kod je 200 (OK). ✅

### Test 3: Error Handling

```python
>>>
>>> # Zahtev ka nepostoječoj stranici
>>> r2 = requests.get("https://httpbin.org/status/404")
>>> print(r2.status_code)
404
>>>
>>> # Baci grešku ako status nije OK
>>> try:
...     r2.raise_for_status()
... except requests.HTTPError as e:
...     print(f"Error: {e}")
...
Error: 404 Client Error: Not Found for url: https://httpbin.org/status/404
>>>
>>> # Timeout test
>>> import time
>>> r3 = requests.get("https://httpbin.org/delay/10", timeout=2)
# Trebalo bi da baci Timeout grešku...
```

**Checkpoint:** Error handling radi! ✅

## Korak 1.3: BeautifulSoup Parsing — REPL Praksa (20 min)

```python
>>>
>>> from bs4 import BeautifulSoup
>>>
>>> # HTML koji ćemo parsirati
>>> html = """
... <html>
... <head><title>Test</title></head>
... <body>
...     <div class="container">
...         <h1>Naslov</h1>
...         <p class="intro">Uvod tekst</p>
...         <p>Obični paragraf</p>
...         <a href="https://example.com">Link</a>
...     </div>
... </body>
... </html>
... """
>>>
>>> # Parse HTML
>>> soup = BeautifulSoup(html, "html.parser")
>>> print(type(soup))
<class 'bs4.BeautifulSoup'>
```

### Test 1: Osnovna Selekcija

```python
>>>
>>> # Pronađi prvi <h1>
>>> h1 = soup.select_one("h1")
>>> print(h1)
<h1>Naslov</h1>
>>>
>>> # Ekstraktuj tekst
>>> text = h1.get_text()
>>> print(text)
Naslov
```

### Test 2: CSS Selektori

```python
>>>
>>> # Svi <p> tagovi
>>> paragraphs = soup.select("p")
>>> print(len(paragraphs))
2
>>>
>>> # Prvi <p> sa class="intro"
>>> intro = soup.select_one("p.intro")
>>> print(intro.get_text())
Uvod tekst
```

### Test 3: Atributi

```python
>>>
>>> # Link element
>>> link = soup.select_one("a")
>>> print(link)
<a href="https://example.com">Link</a>
>>>
>>> # Ekstraktuj href atribut
>>> href = link.get("href")
>>> print(href)
https://example.com
>>>
>>> # Sve atribute
>>> print(link.attrs)
{'href': 'https://example.com'}
```

### Test 4: Iteracija

```python
>>>
>>> # Iteracija kroz sve <p> tagove
>>> for p in soup.select("p"):
...     print(f"Text: {p.get_text()}")
...
Text: Uvod tekst
Text: Obični paragraf
>>>
>>> # Svi textovi sa strip=True (uklanja whitespace)
>>> for p in soup.select("p"):
...     print(f"Text: '{p.get_text(strip=True)}'")
...
Text: 'Uvod tekst'
Text: 'Obični paragraf'
```

**Checkpoint:** BeautifulSoup selekcija radi! ✅

## Korak 1.4: Kombinovani Primer — REPL Praksa (20 min)

```python
>>>
>>> # Fetch pravi HTML sa httpbin.org
>>> import requests
>>> from bs4 import BeautifulSoup
>>>
>>> response = requests.get("https://httpbin.org/html")
>>> soup = BeautifulSoup(response.text, "html.parser")
>>>
>>> # Pronađi <h1> tagove
>>> titles = soup.select("h1")
>>> print(f"Found {len(titles)} titles")
Found 1
>>>
>>> # Ekstraktuj prvi naslov
>>> title = soup.select_one("h1")
>>> print(f"Title: {title.get_text()}")
Title: Herman Melville — Moby-Dick
>>>
>>> # Pronađi sve <p> tagove i ispiši samo prvo 50 karaktera
>>> paragraphs = soup.select("p")
>>> for i, p in enumerate(paragraphs[:3]):
...     text = p.get_text(strip=True)[:50]
...     print(f"P{i}: {text}")
...
P0: Call me Ishmael. Some years ago—never mind
P1: There is now your insular city of the Manhat
P2: Circumambulate the city of a dreamy Sabbat
```

**Checkpoint:** Kompletan flow radi — fetch + parse + extract! ✅

---

# FAZA 2: Project Struktura i Setup (1.5h)

## Korak 2.1: Kreiraj Direktorijume (5 min)

```bash
# Uvek si u /projects/01-web-scraper
cd projects/01-web-scraper

# Kreiraj strukture
mkdir -p tests logs output

# Kreiraj fajlove
touch config.py scraper.py tests/__init__.py tests/conftest.py tests/test_scraper_basics.py

# Proveri strukturu
tree -L 2
# Output:
# .
# ├── config.py
# ├── scraper.py
# ├── tests/
# │   ├── __init__.py
# │   ├── conftest.py
# │   └── test_scraper_basics.py
# ├── logs/
# ├── output/
# └── venv/
```

## Korak 2.2: Kreiraj config.py (20 min)

Ovo je korak gde definiše sve Settings na jednom mestu:

```python
# projects/01-web-scraper/config.py
"""
Konfiguracija za Web Scraper.
Svi settings su na jednom mestu za laku menjitost.
"""

from pathlib import Path
from typing import Final

# Putanje
PROJECT_ROOT: Final[Path] = Path(__file__).parent
LOGS_DIR: Final[Path] = PROJECT_ROOT / "logs"
OUTPUT_DIR: Final[Path] = PROJECT_ROOT / "output"

# Kreiraj direktorijume ako ne postoje
LOGS_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# HTTP settings
BASE_URL: Final[str] = "https://httpbin.org"  # Test URL
REQUEST_TIMEOUT: Final[int] = 5  # sekundi
HEADERS: Final[dict[str, str]] = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Logging settings
LOG_FILE: Final[Path] = LOGS_DIR / "app.log"
LOG_LEVEL: Final[str] = "INFO"
LOG_FORMAT: Final[str] = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"

# CSV settings
CSV_OUTPUT: Final[Path] = OUTPUT_DIR / "scraped_data.csv"
CSV_ENCODING: Final[str] = "utf-8"

if __name__ == "__main__":
    # Test config
    print(f"PROJECT_ROOT: {PROJECT_ROOT}")
    print(f"LOGS_DIR: {LOGS_DIR}")
    print(f"OUTPUT_DIR: {OUTPUT_DIR}")
    print(f"BASE_URL: {BASE_URL}")
    print(f"All settings are correctly configured!")
```

### Testiranje config.py u REPL-u:

```bash
python3
```

```python
>>> from config import PROJECT_ROOT, LOGS_DIR, BASE_URL
>>> print(f"Root: {PROJECT_ROOT}")
Root: /home/jole-pavlovic-dev/code/python-automation-lab/python-automation-portfolio/projects/01-web-scraper
>>> print(f"Logs dir: {LOGS_DIR}")
Logs dir: /home/jole-pavlovic-dev/code/python-automation-lab/python-automation-portfolio/projects/01-web-scraper/logs
>>> print(f"Base URL: {BASE_URL}")
Base URL: https://httpbin.org
```

**Checkpoint:** Config je učitan! ✅

## Korak 2.3: Kreiraj requirements.txt (10 min)

```bash
# Aktiviraj venv ako nije aktiviran
source venv/bin/activate

# Generiši requirements.txt
pip freeze > requirements.txt

# Proveri sadržaj (trebalo bi da sadrži requests, beautifulsoup4, pytest)
cat requirements.txt | grep -E "requests|beautifulsoup|pytest"
```

**Checkbox:** requirements.txt je kreiiran! ✅

## Korak 2.4: Git Setup (15 min)

```bash
# Inicijalizuj git (ako već nije)
git init

# Kreiraj .gitignore
cat > .gitignore << 'EOF'
venv/
__pycache__/
*.pyc
.pytest_cache/
htmlcov/
.coverage
*.egg-info/
dist/
build/
.env
.DS_Store
logs/*.log
output/*.csv
EOF

# Add fajlove
git add config.py requirements.txt .gitignore

# Commit
git commit -m "Day 8: Web Scraper initial setup"
```

**Checkpoint:** Git je konfiguriran! ✅

---

# FAZA 3: Scraper Core Funkcije (2h)

## Korak 3.1: Kreiraj scraper.py — fetch_page() (30 min)

Sada kreiramo main logiku scraper-a:

```python
# projects/01-web-scraper/scraper.py
"""
Web Scraper core funkcije.
- fetch_page(url) — Fetch HTML sa error handling-om
- parse_items(html) — Parse items iz HTML-a
"""

import logging
from typing import Optional
import requests
from bs4 import BeautifulSoup

from config import HEADERS, REQUEST_TIMEOUT

logger = logging.getLogger(__name__)


class ScraperError(Exception):
    """Base greška za scraper."""
    pass


class FetchError(ScraperError):
    """Greška pri fetch-ovanju HTML-a."""
    pass


def fetch_page(url: str, timeout: int = REQUEST_TIMEOUT) -> str:
    """
    Fetch HTML sadržaj sa date URL-e.

    Args:
        url: URL za fetch
        timeout: Timeout u sekundama

    Returns:
        HTML sadržaj kao string

    Raises:
        FetchError: Ako zahtev ne uspe
    """
    try:
        logger.info(f"Fetching: {url}")

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=timeout
        )

        # Baci grešku ako je 4xx ili 5xx
        response.raise_for_status()

        logger.info(f"Success: {url} (status: {response.status_code})")
        return response.text

    except requests.Timeout as e:
        logger.error(f"Timeout za {url} ({timeout}s)")
        raise FetchError(f"Timeout: {url}") from e

    except requests.ConnectionError as e:
        logger.error(f"Connection error za {url}")
        raise FetchError(f"Connection error: {url}") from e

    except requests.HTTPError as e:
        logger.error(f"HTTP error {e.response.status_code} za {url}")
        raise FetchError(f"HTTP {e.response.status_code}: {url}") from e

    except requests.RequestException as e:
        logger.error(f"Request failed: {url} - {e}")
        raise FetchError(f"Request failed: {url}") from e


def parse_html(html: str) -> BeautifulSoup:
    """
    Parse HTML string u BeautifulSoup objekat.

    Args:
        html: HTML string

    Returns:
        BeautifulSoup objekat
    """
    return BeautifulSoup(html, "html.parser")


def extract_titles(html: str) -> list[str]:
    """
    Primer: Ekstraktuj sve <h1> naslov iz HTML-a.

    Args:
        html: HTML string

    Returns:
        Lista naslov-a
    """
    soup = parse_html(html)
    titles = []

    for h1 in soup.select("h1"):
        title = h1.get_text(strip=True)
        if title:
            titles.append(title)

    logger.info(f"Extracted {len(titles)} titles")
    return titles


if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    # Test
    try:
        html = fetch_page("https://httpbin.org/html")
        titles = extract_titles(html)
        print(f"Found {len(titles)} titles")
        for title in titles:
            print(f"  - {title}")
    except FetchError as e:
        print(f"Error: {e}")
```

### Testiranje scraper.py u REPL-u:

```bash
python3
```

```python
>>> from scraper import fetch_page, extract_titles
>>>
>>> # Fetch HTML
>>> html = fetch_page("https://httpbin.org/html")
>>> print(len(html))
3741
>>>
>>> # Extract titles
>>> titles = extract_titles(html)
>>> print(f"Found {len(titles)} titles")
Found 1
>>> print(f"Title: {titles[0]}")
Title: Herman Melville — Moby-Dick
```

**Checkpoint:** fetch_page() i parse_titles() rade! ✅

## Korak 3.2: Logging Setup (30 min)

Dodaj logging u main delu scraper.py:

```python
# Dodaj ovo na kraju scraper.py (nakon funkcija)

# ============================================================================
# LOGGING SETUP
# ============================================================================

import logging
from config import LOG_FILE, LOG_LEVEL, LOG_FORMAT

def setup_logging():
    """Setupuj logging sa file + console output."""

    # Kreiraj logger
    logger = logging.getLogger(__name__)
    logger.setLevel(LOG_LEVEL)

    # File handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Inicijalizuj logging
logger = setup_logging()
```

### Testiranje logging-a:

```bash
python3
```

```python
>>> from scraper import fetch_page, logger
>>>
>>> # Pozovi funkciju koja loguje
>>> html = fetch_page("https://httpbin.org/html")
INFO:scraper:Fetching: https://httpbin.org/html
INFO:scraper:Success: https://httpbin.org/html (status: 200)
>>>
>>> # Proveri log fajl
>>> ! tail -5 logs/app.log
2025-12-26 12:34:56,123 | scraper | INFO | Fetching: https://httpbin.org/html
2025-12-26 12:34:57,456 | scraper | INFO | Success: https://httpbin.org/html (status: 200)
```

**Checkpoint:** Logging je konfigurisan! ✅

---

# FAZA 4: Testing Setup (2h)

## Korak 4.1: Kreiraj conftest.py sa Fixtures-ima (30 min)

```python
# projects/01-web-scraper/tests/conftest.py
"""
Pytest fixtures za Web Scraper testove.
"""

import pytest
from pathlib import Path
from unittest.mock import Mock
from bs4 import BeautifulSoup

# Mock HTML za testiranje
MOCK_HTML = """
<html>
<head><title>Test Page</title></head>
<body>
    <h1>Herman Melville — Moby-Dick</h1>
    <p class="intro">Test introduction text</p>
    <div class="item">
        <a href="/item1">Item 1</a>
        <span class="price">$10.99</span>
    </div>
    <div class="item">
        <a href="/item2">Item 2</a>
        <span class="price">$20.50</span>
    </div>
</body>
</html>
"""

@pytest.fixture
def mock_html() -> str:
    """Vrati mock HTML."""
    return MOCK_HTML

@pytest.fixture
def mock_soup(mock_html: str) -> BeautifulSoup:
    """Vrati parsiran mock HTML kao BeautifulSoup."""
    return BeautifulSoup(mock_html, "html.parser")

@pytest.fixture
def mock_response():
    """Vrati mock requests.Response objekat."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.text = MOCK_HTML
    mock_resp.headers = {"content-type": "text/html"}
    mock_resp.url = "https://example.com"
    return mock_resp

@pytest.fixture
def mock_response_404():
    """Vrati mock 404 response."""
    mock_resp = Mock()
    mock_resp.status_code = 404
    mock_resp.raise_for_status.side_effect = Exception("404 Not Found")
    return mock_resp

@pytest.fixture
def tmp_csv_file(tmp_path: Path) -> Path:
    """Kreiraj privremenu CSV datoteku."""
    csv_file = tmp_path / "test_output.csv"
    csv_file.write_text("title,price\nItem1,10.99\nItem2,20.50\n")
    return csv_file
```

**Checkpoint:** Fixtures su kreirane! ✅

## Korak 4.2: Kreiraj test_scraper_basics.py (60 min)

```python
# projects/01-web-scraper/tests/test_scraper_basics.py
"""
Osnovni testovi za Web Scraper.
"""

import pytest
from unittest.mock import patch, Mock
from pathlib import Path

from scraper import (
    fetch_page,
    parse_html,
    extract_titles,
    FetchError,
)


class TestFetchPage:
    """Testovi za fetch_page funkciju."""

    @patch("requests.get")
    def test_fetch_page_with_valid_url(self, mock_get, mock_response):
        """Test fetch_page sa validnom URL-om."""
        mock_get.return_value = mock_response

        html = fetch_page("https://example.com")

        assert isinstance(html, str)
        assert len(html) > 0
        assert "test" in html.lower()
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_fetch_page_calls_with_correct_params(self, mock_get, mock_response):
        """Test da fetch_page koristi correct headers i timeout."""
        mock_get.return_value = mock_response

        fetch_page("https://example.com", timeout=10)

        # Proveri da je requests.get pozvan sa timeout
        call_kwargs = mock_get.call_args[1]
        assert call_kwargs["timeout"] == 10
        assert "User-Agent" in call_kwargs["headers"]

    @patch("requests.get")
    def test_fetch_page_raises_on_timeout(self, mock_get):
        """Test da fetch_page baci FetchError na timeout."""
        import requests
        mock_get.side_effect = requests.Timeout("Timeout!")

        with pytest.raises(FetchError):
            fetch_page("https://example.com")

    @patch("requests.get")
    def test_fetch_page_raises_on_connection_error(self, mock_get):
        """Test da fetch_page baci FetchError na connection error."""
        import requests
        mock_get.side_effect = requests.ConnectionError("Connection failed!")

        with pytest.raises(FetchError):
            fetch_page("https://example.com")

    @patch("requests.get")
    def test_fetch_page_raises_on_http_error(self, mock_get, mock_response_404):
        """Test da fetch_page baci FetchError na 404."""
        mock_get.return_value = mock_response_404

        with pytest.raises(FetchError):
            fetch_page("https://example.com")


class TestParseHtml:
    """Testovi za parse_html funkciju."""

    def test_parse_html_returns_soup(self, mock_html):
        """Test da parse_html vraća BeautifulSoup objekat."""
        soup = parse_html(mock_html)

        assert soup is not None
        assert hasattr(soup, "select")
        assert hasattr(soup, "find")

    def test_parse_html_handles_empty_string(self):
        """Test da parse_html radi sa praznom stringom."""
        soup = parse_html("")
        assert soup is not None


class TestExtractTitles:
    """Testovi za extract_titles funkciju."""

    def test_extract_titles_with_valid_html(self, mock_html):
        """Test extract_titles sa validnim HTML-om."""
        titles = extract_titles(mock_html)

        assert isinstance(titles, list)
        assert len(titles) == 1
        assert titles[0] == "Herman Melville — Moby-Dick"

    def test_extract_titles_with_no_h1(self):
        """Test extract_titles kada nema <h1> tagova."""
        html = "<html><body><p>No title</p></body></html>"
        titles = extract_titles(html)

        assert titles == []

    def test_extract_titles_with_multiple_h1(self):
        """Test extract_titles sa više <h1> tagova."""
        html = """
        <html>
        <body>
            <h1>Title 1</h1>
            <h1>Title 2</h1>
            <h1>Title 3</h1>
        </body>
        </html>
        """
        titles = extract_titles(html)

        assert len(titles) == 3
        assert titles == ["Title 1", "Title 2", "Title 3"]


class TestIntegration:
    """Integration testovi (simulacija realnog flow-a)."""

    @patch("requests.get")
    def test_fetch_and_parse_flow(self, mock_get, mock_response):
        """Test kompletan flow: fetch → parse → extract."""
        mock_get.return_value = mock_response

        # Fetch
        html = fetch_page("https://example.com")
        assert len(html) > 0

        # Parse
        soup = parse_html(html)
        assert soup is not None

        # Extract
        titles = extract_titles(html)
        assert len(titles) == 1


# ============================================================================
# LOGGING TESTOVI
# ============================================================================

class TestLogging:
    """Testovi za logging."""

    @patch("requests.get")
    def test_fetch_page_logs_success(self, mock_get, mock_response, caplog):
        """Test da fetch_page loguje uspešan zahtev."""
        mock_get.return_value = mock_response

        fetch_page("https://example.com")

        assert "Fetching" in caplog.text or "Success" in caplog.text

    @patch("requests.get")
    def test_fetch_page_logs_error(self, mock_get, caplog):
        """Test da fetch_page loguje greške."""
        import requests
        mock_get.side_effect = requests.Timeout("Timeout!")

        with pytest.raises(FetchError):
            fetch_page("https://example.com")

        assert "Timeout" in caplog.text or "error" in caplog.text.lower()
```

### Pokretanje Testova:

```bash
# Pokreni sve testove
pytest tests/test_scraper_basics.py -v

# Output trebalo bi da bude nešto kao:
# tests/test_scraper_basics.py::TestFetchPage::test_fetch_page_with_valid_url PASSED
# tests/test_scraper_basics.py::TestFetchPage::test_fetch_page_calls_with_correct_params PASSED
# ...
# 10 passed in 0.45s
```

**Checkpoint:** Svi testovi prolaze! ✅

## Korak 4.3: Coverage Provera (30 min)

```bash
# Pokreni testove sa coverage
pytest --cov=scraper --cov-report=term-missing tests/

# Output:
# Name       Stmts   Miss  Cover   Missing
# ---------------------
# scraper.py    45      5    89%    12-15, 45
# config.py     20      0   100%
# ---------------------
# TOTAL         65      5    92%
```

**Cilj:** Coverage > 85%

```bash
# Ako je coverage niska, pokreni sa detaljima
pytest --cov=scraper --cov-report=html tests/
open htmlcov/index.html  # Pogledaj u browseru
```

**Checkpoint:** Coverage je dobar! ✅

---

## 🎉 FAZA 4 DONE!

Sada bi trebalo:

```bash
# Proveri sve fajlove
ls -la projects/01-web-scraper/

# Struktura
projects/01-web-scraper/
├── config.py                          ✅
├── scraper.py                         ✅
├── requirements.txt                   ✅
├── tests/
│   ├── __init__.py                   ✅
│   ├── conftest.py                   ✅
│   └── test_scraper_basics.py        ✅
├── logs/
│   └── app.log                        ✅
└── output/

# Testovi prolaze
pytest tests/ -v
# → 10+ passed

# Coverage je dobar
pytest --cov=scraper tests/
# → Coverage > 85%

# Logovani su dostupni
cat logs/app.log
```

---

## ✅ Finalni Checklist za Dan 8

```
FAZA 1: Requests + BeautifulSoup
  [ ] Instaliran requests i beautifulsoup4
  [ ] GET zahtev radi u REPL-u
  [ ] HTML parsing radi u REPL-u
  [ ] CSS selektori rade
  [ ] Error handling je testiran

FAZA 2: Project Setup
  [ ] Struktura direktorijuma je kreiirana
  [ ] config.py je kompletan sa svim setting-ima
  [ ] requirements.txt je generiiran
  [ ] .gitignore je kreiran
  [ ] Git commit je napravljen

FAZA 3: Scraper Core
  [ ] scraper.py je kompletan
  [ ] fetch_page() radi sa error handling-om
  [ ] parse_html() radi
  [ ] extract_titles() radi
  [ ] Logging je setup-an

FAZA 4: Testing
  [ ] conftest.py je kompletan sa fixtures-ima
  [ ] test_scraper_basics.py ima 10+ testova
  [ ] Svi testovi prolaze (pytest -v)
  [ ] Coverage > 85%
  [ ] Logging testovi rade (caplog)

FINALIZACIJA:
  [ ] Rekapitulacija šta je napravljeno
  [ ] Git commit "Day 8: Web Scraper Setup Complete"
  [ ] README.md je napravljen sa instrukcije
```

---

## 📞 Ako Zaglavim...

### Problem: "ModuleNotFoundError: No module named 'requests'"

```bash
# Rešenje: Instaliraj
pip install requests beautifulsoup4

# ILI proveri venv
which python3
# Trebalo bi da pokazuje na venv/bin/python3
```

### Problem: "AssertionError: assert 0 == 1" u testovima

```bash
# Debug: Pokreni sa -s flagi
pytest -s tests/test_scraper_basics.py::test_extract_titles_with_valid_html

# Vidi šta se dešava u testu
```

### Problem: "Coverage too low" (<85%)

```bash
# Pronađi šta nije pokriveno
pytest --cov=scraper --cov-report=term-missing tests/

# Dodaj još testova za te linije
```

---

**Sada ide na [tasks.md](./tasks.md) za checklist i potom **GIT COMMIT** na kraju dana!** 🚀

Odličan posao! 💪

---
