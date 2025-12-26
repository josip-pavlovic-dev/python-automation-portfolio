---
type: cheatsheet
topic: Web Scraping — Requests + BeautifulSoup
date: 2025-12-26
linked_to: 2025-12-26_web_scraper_v1
language: bilingual
status: ready
difficulty: beginner-intermediate
---

# 🕷️ Cheatsheet: Web Scraping — Requests + BeautifulSoup

## ✅ Ključni koncepti

-   **HTTP Request** | Zahtev do web servera (GET, POST)
-   **HTTP Status Code** | Odgovор servera (200=OK, 404=NotFound, 500=Error)
-   **HTML** | Markup jezik za web stranice
-   **CSS Selector** | Način da pronađeš elemente u HTML-u (`.class`, `#id`, `tag`)
-   **DOM (Document Object Model)** | Struktura HTML-a kao stablo
-   **User-Agent** | String koji govori serveru šta si ti (browser ili bot)
-   **Timeout** | Maksimalno vreme čekanja na odgovor (izbjegavanje vešanja)
-   **Response Object** | Objekat koji sadrži response sa servera

---

## 🌐 Requests Osnove

### GET zahtev (Najčešće korišćeno)

```python
import requests

# Osnovna verzija
response = requests.get("https://example.com")
print(response.status_code)  # 200, 404, 500, itd.
print(response.text)         # HTML kao string
print(response.content)      # HTML kao bytes

# Sa timeout-om (izbegni vešanje)
response = requests.get("https://example.com", timeout=5)

# Sa custom headers (neko vreme je User-Agent obavezna)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get("https://example.com", headers=headers)

# Sa parametrima (URL query string)
params = {"q": "python", "page": 1}
response = requests.get("https://example.com/search", params=params)
# URL postaje: https://example.com/search?q=python&page=1
```

### Čitanje Odgovora

```python
response = requests.get("https://example.com")

# Status code
print(response.status_code)  # int: 200, 404, 500, itd.

# HTML tekst
html = response.text  # str: Unicode, moze imati znakove kao š, ž, đ
html_bytes = response.content  # bytes

# Headers
print(response.headers["content-type"])  # "text/html; charset=utf-8"

# Encoding
print(response.encoding)  # "utf-8"

# URL (nakon redirects)
print(response.url)  # https://example.com (može biti drugačit od original URL)
```

### Error Handling

```python
import requests
from requests.exceptions import (
    RequestException,      # Bazna greška
    Timeout,              # Timeout
    ConnectionError,      # Veza ne mogu
    HTTPError,            # HTTP greška (4xx, 5xx)
)

def fetch_page(url: str) -> str:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Baci grešku ako je 4xx ili 5xx
        return response.text
    except Timeout:
        print(f"Timeout: {url}")
        raise
    except ConnectionError:
        print(f"Connection error: {url}")
        raise
    except HTTPError as e:
        print(f"HTTP error {e.response.status_code}: {url}")
        raise
    except RequestException as e:
        print(f"Request failed: {e}")
        raise
```

### Česti Status Kodovi

```
200 OK                    ✅ Sve je dobro
301/302 Redirect         ⏭️  Stranica je pomerena (requests je automatski prati)
304 Not Modified         💾 Sadržaj nije promenjen od zadnjeg puta
400 Bad Request          ❌ Tvoj zahtev je loš (pogrešni parametri)
401 Unauthorized         🔒 Trebja autentifikacija
403 Forbidden            🚫 Nemaš pristup
404 Not Found            ❌ Stranica ne postoji
429 Too Many Requests    ⏰ Previše zahteva (rate limit)
500 Internal Server Error ⚠️  Server greška
503 Service Unavailable  🔧 Server je u održavanju
```

---

## 🍜 BeautifulSoup Osnove

### Parsiranje HTML-a

```python
from bs4 import BeautifulSoup

html = """
<html>
<body>
    <h1>Naslov</h1>
    <div class="container">
        <p>Paragraf 1</p>
        <p>Paragraf 2</p>
    </div>
    <a href="https://example.com" id="link1">Link</a>
</body>
</html>
"""

# Kreiraj soup objekat
soup = BeautifulSoup(html, "html.parser")
# "html.parser" je parser koji koristi Python (ne treba lxml ili html5lib)
```

### CSS Selektori (Najčešće korišćeno)

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

# Pronađi PRVI element
element = soup.select_one("h1")  # <h1>
element = soup.select_one(".container")  # class="container"
element = soup.select_one("#link1")  # id="link1"

# Pronađi SVE elemente (vraća list)
elements = soup.select("p")  # Svi <p> tagovi
elements = soup.select(".container p")  # Svi <p> unutar .container
elements = soup.select("a[href]")  # Svi <a> sa href atributom

# Kombinovani selektori
elements = soup.select("div.content > p")  # <p> koji su direktna deca <div class="content">
```

### Ekstraktovanje Vrednosti

```python
soup = BeautifulSoup(html, "html.parser")

# Tekst iz elementa
h1 = soup.select_one("h1")
text = h1.get_text()  # "Naslov"
text = h1.get_text(strip=True)  # "Naslov" (uklanja whitespace)

# Atribut
link = soup.select_one("a")
href = link.get("href")  # "https://example.com"
link_id = link.get("id")  # "link1"

# Sve atribute
attrs = link.attrs  # {"href": "...", "id": "link1"}

# Provera da li atribut postoji
if link.has_attr("href"):
    print("Link ima href")
```

### Iteracija preko Elemenata

```python
soup = BeautifulSoup(html, "html.parser")

# Iteracija kroz sve <p> tagove
for paragraph in soup.select("p"):
    text = paragraph.get_text(strip=True)
    print(f"Paragraf: {text}")

# Output:
# Paragraf: Paragraf 1
# Paragraf: Paragraf 2

# Iteracija sa indeksom
for i, p in enumerate(soup.select("p")):
    print(f"P #{i}: {p.get_text()}")
```

### Struktura Stabla (DOM)

```python
# HTML kao stablo:
# <html>
#   <body>
#     <h1>...</h1>
#     <div class="container">
#       <p>...</p>
#       <p>...</p>
#     </div>
#     <a>...</a>
#   </body>
# </html>

soup = BeautifulSoup(html, "html.parser")

# Pronađi parent
p = soup.select_one("p")
parent = p.parent  # <div class="container">

# Pronađi sve children
div = soup.select_one(".container")
children = div.children  # Generator [<p>, <p>]

# Pronađi sledeći sibling
h1 = soup.select_one("h1")
next_sib = h1.find_next_sibling()  # <div class="container">

# Pronađi sve tagove određenog tipa
all_p = soup.find_all("p")  # Isto kao soup.select("p")
```

---

## 🔍 CSS Selektori — Cheat Sheet

```python
# TAGOVI
soup.select("p")              # Svi <p> tagovi
soup.select("div")            # Svi <div> tagovi

# KLASE
soup.select(".title")         # class="title"
soup.select(".box.red")       # class="box red" (oba)

# ID
soup.select("#main")          # id="main"

# ATRIBUTI
soup.select("a[href]")        # <a> koji imaju href
soup.select("a[href='#']")    # <a href="#">
soup.select("img[alt]")       # <img> koji imaju alt

# KOMBINOVANI
soup.select("div > p")        # <p> direktna deca <div>
soup.select("div p")          # <p> negde unutar <div>
soup.select("div + p")        # <p> odmah posle <div>
soup.select("div ~ p")        # <p> negde posle <div>

# PSEUDO-SELEKTORI
soup.select("p:first-child")  # Prvi <p> koji je dete
soup.select("p:last-child")   # Poslednji <p>
soup.select("p:nth-child(2)") # Drugi <p>
```

---

## 🛠️ Praktična Primena — Kompletan Primer

### Scenario: Scrape Proizvode sa E-commerce Sajta

```python
import requests
from bs4 import BeautifulSoup
import logging
from pathlib import Path
from typing import TypedDict

logger = logging.getLogger(__name__)

class Product(TypedDict):
    title: str
    price: float
    url: str

def fetch_products(url: str) -> list[Product]:
    """Scrape proizvode sa stranice."""
    try:
        # Fetch
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        logger.info(f"Fetched {url} (status: {response.status_code})")

        # Parse
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract
        products = []
        for item in soup.select(".product"):
            try:
                title = item.select_one(".title").get_text(strip=True)
                price_text = item.select_one(".price").get_text(strip=True)
                price = float(price_text.replace("$", ""))  # "$10.99" → 10.99
                url = item.select_one("a").get("href")

                products.append({
                    "title": title,
                    "price": price,
                    "url": url,
                })
            except (AttributeError, ValueError) as e:
                logger.warning(f"Skipped malformed product: {e}")
                continue

        logger.info(f"Extracted {len(products)} products")
        return products

    except requests.RequestException as e:
        logger.error(f"Failed to fetch {url}: {e}")
        raise

# Upotreba
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    products = fetch_products("https://example.com/products")
    for p in products:
        print(f"{p['title']}: ${p['price']}")
```

---

## 🧪 Testiranje sa Mock-ima

```python
import pytest
from unittest.mock import Mock, patch
from scraper import fetch_products

# Mock HTML
MOCK_HTML = """
<div class="product">
    <div class="title">Product 1</div>
    <div class="price">$10.99</div>
    <a href="/p1">Link</a>
</div>
<div class="product">
    <div class="title">Product 2</div>
    <div class="price">$20.50</div>
    <a href="/p2">Link</a>
</div>
"""

@patch("requests.get")
def test_fetch_products(mock_get):
    # Setup mock
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML
    mock_get.return_value = mock_response

    # Test
    products = fetch_products("https://example.com")

    # Assertions
    assert len(products) == 2
    assert products[0]["title"] == "Product 1"
    assert products[0]["price"] == 10.99
    assert products[1]["price"] == 20.50
```

---

## ⚠️ Česti Problemi i Rešenja

### Problem 1: "AttributeError: 'NoneType' object has no attribute..."

```python
# LOŠE: Ne proveraš da li element postoji
price = soup.select_one(".price").get_text()  # Može biti None!

# DOBRO: Proveri prvo
price_element = soup.select_one(".price")
if price_element:
    price = price_element.get_text(strip=True)
else:
    logger.warning("Price not found")
    price = None
```

### Problem 2: "UnicodeDecodeError"

```python
# LOŠE: BeautifulSoup ne zna encoding
soup = BeautifulSoup(response.content, "html.parser")

# DOBRO: Koristi text
soup = BeautifulSoup(response.text, "html.parser")

# ILI napravi soup iz bytes sa specify encoding
soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
```

### Problem 3: Server odbija zahtev (403, 401)

```python
# LOŠE: Nema User-Agent-a, server misli da si bot
response = requests.get("https://example.com")

# DOBRO: Dodaj User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
response = requests.get("https://example.com", headers=headers)
```

### Problem 4: Script se zaglavjuje

```python
# LOŠE: Nema timeout-a, čeka zauvek
response = requests.get(url)

# DOBRO: Postavi timeout
try:
    response = requests.get(url, timeout=5)  # 5 sekundi max
except requests.Timeout:
    print(f"Timeout za {url}")
```

### Problem 5: Nema elementa koji tražiš

```python
# DEBUG: Šta je stvarno u HTML-u?
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify()[:1000])  # Prikaži prvih 1000 karaktera

# DRUGI DEBUG: Proveri CSS selektor
all_divs = soup.select("div.product")  # Postoji li ikoji?
print(f"Found {len(all_divs)} products")

# TREĆI DEBUG: BeautifulSoup navigator
div = soup.select_one("div")  # Pronađi prvi div
print(div.name)  # "div"
print(div.attrs)  # {"class": ["product"]}
```

---

## 🎯 Best Practices

1. **Uvek koristi `timeout`** — izbegni da se script zaglavji
2. **Dodaj User-Agent header** — neki serveri odbijaju bot zahteve
3. **Koristi `get_text(strip=True)`** — uklanja whitespace
4. **Proveri da li element postoji** — `select_one()` može vratiti `None`
5. **Loguj sve zahteve** — debug je lakši sa logovima
6. **Testiraj sa mock-ima** — ne testira real server svaki put
7. **Čitaj response.url** — može biti drugačit zbog redirect-a
8. **Čuvaj HTML lokalno** — dev-ovanje je brže bez mrežnog zahteva

---

## 📚 Reference

-   [Requests Documentation](https://docs.python-requests.org/)
-   [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
-   [CSS Selectors Guide](https://www.w3schools.com/cssref/selectors.asp)
-   [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## 🧪 Testiranje — Quick Reference

```bash
# Instalacija
pip install requests beautifulsoup4 pytest pytest-mock

# Test sa mock-om
pytest test_scraper.py -v

# Test sa real URL (obazrivo!)
pytest test_scraper.py::test_fetch_real_url -v

# Coverage
pytest --cov=scraper test_scraper.py
```

---

**Sada idi na [web_scraper_setup_guide.md](./web_scraper_setup_guide.md) i počni sa FAZA 1! 🚀**
