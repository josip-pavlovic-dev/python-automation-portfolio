---
type: qa_reference
date: 2025-12-26
day: 8/14
topic: Web Scraper v1 — Q&A i Česte Greške
---

# 💬 DAN 8 — Q&A i Česte Greške

Ako su ti ova pitanja pala na pamet, odgovori su ovde! 👇

---

## 🌐 REQUESTS PITANJA

### Q: Šta je razlika između `response.text` i `response.content`?

**A:**

```python
response.text      # Unicode string (čitljiv HTML)
response.content   # Raw bytes (binarna representation)

# Za HTML parsing, uvek koristi response.text
soup = BeautifulSoup(response.text, "html.parser")  # ✅
```

---

### Q: Šta znači status kod 404, 500, 200?

**A:**

```
200 — OK, sve je dobro ✅
404 — Page not found ❌
500 — Server error ⚠️
403 — Forbidden (access denied) 🔒
401 — Unauthorized (trebja login) 🔐

# Koristi raise_for_status() da automatski baci greške
response.raise_for_status()  # Baca HTTPError ako je 4xx ili 5xx
```

---

### Q: Zašto server odbija moj zahtev sa 403 Forbidden?

**A:** Server misli da si bot. Rešenje:

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
response = requests.get(url, headers=headers)  # ✅
```

---

### Q: Šta je timeout i zašto mi je važan?

**A:** Ako server ne odgovara, script čeka zauvek. Timeout sprečava to:

```python
# LOŠE: Čeka zauvek ako server ne odgovara
response = requests.get(url)

# DOBRO: Čeka maksimalno 5 sekundi
response = requests.get(url, timeout=5)  # Baca Timeout ako prođe 5s

# Hvati timeout
try:
    response = requests.get(url, timeout=5)
except requests.Timeout:
    print("Server je spora, prekinuo sam zahtev")
```

---

### Q: Kako da testira zahtev bez pravog servera?

**A:** Koristi `unittest.mock.patch`:

```python
from unittest.mock import patch, Mock

@patch("requests.get")
def test_fetch_page(mock_get):
    # Kreiraj mock response
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.text = "<html>...</html>"
    mock_get.return_value = mock_resp

    # Sada requests.get() vraća tvoj mock
    html = fetch_page("https://example.com")
    assert len(html) > 0
```

---

## 🍜 BEAUTIFULSOUP PITANJA

### Q: Kako da pronađem element po CSS selektor-u?

**A:**

```python
soup = BeautifulSoup(html, "html.parser")

# Pronađi PRVI element
element = soup.select_one(".class-name")    # Class
element = soup.select_one("#id-name")       # ID
element = soup.select_one("div")            # Tag

# Pronađi SVE elemente
elements = soup.select(".class-name")       # List od svih
```

---

### Q: `soup.select_one()` vraća None, šta to znači?

**A:** Element sa tim selektor-om ne postoji:

```python
element = soup.select_one(".nonexistent")  # None

# LOŠE: Ovo će pucati
text = element.get_text()  # AttributeError!

# DOBRO: Proveri prvo
if element:
    text = element.get_text()
else:
    print("Element not found")
```

---

### Q: Kako da izvlačim tekst iz HTML-a bez HTML tagova?

**A:**

```python
element = soup.select_one("h1")

# get_text() uklanja tagove
text = element.get_text()  # "My Title   \n   "
text = element.get_text(strip=True)  # "My Title" ✅
```

---

### Q: Šta je razlika između `select()` i `select_one()`?

**A:**

```python
soup.select_one("p")      # Pronađi PRVI <p>, vraća Element ili None
soup.select("p")          # Pronađi SVE <p>, vraća list
```

---

### Q: Kako da iterujem kroz sve elemente?

**A:**

```python
for p in soup.select("p"):
    text = p.get_text(strip=True)
    print(text)

# Sa indeksom
for i, p in enumerate(soup.select("p")):
    print(f"P#{i}: {text}")
```

---

### Q: Kako da pronađem element sa specifičnim atributom?

**A:**

```python
# Sve <a> tagove sa href atributom
links = soup.select("a[href]")

# Sve <a> tagove sa href="#"
links = soup.select("a[href='#']")

# Sve <img> tagove sa alt atributom
imgs = soup.select("img[alt]")
```

---

### Q: Kako da pronađem HTML strukturu za CSS selektor?

**A:** Koristi browser Dev Tools:

```
1. Desni-klik na element → "Inspect"
2. Pogledaj HTML strukturu
3. Koristi CSS selektor da ga pronađeš

Primer:
<div class="product">
    <h2 class="title">Product Name</h2>  ← Target
</div>

CSS selektor: div.product > h2.title
soup.select_one("div.product > h2.title")
```

---

## 🧪 PYTEST PITANJA

### Q: Šta je fixture?

**A:** Reusable test data ili setup:

```python
@pytest.fixture
def mock_html():
    """Vraća mock HTML za testove."""
    return "<h1>Test</h1>"

def test_example(mock_html):  # mock_html je automatski injected
    assert "<h1>" in mock_html
```

---

### Q: Kako da testiram exception-e?

**A:**

```python
from scraper import FetchError

def test_fetch_page_raises_error():
    with pytest.raises(FetchError):
        fetch_page("https://invalid-url.xyz")
```

---

### Q: Šta je `caplog` i kako da ga koristim?

**A:** `caplog` hvata logging output:

```python
def test_logging(caplog):
    fetch_page("https://example.com")

    # Proveri da je nešto loguvano
    assert "Fetching" in caplog.text
    assert "Success" in caplog.text

    # Proveri log level
    assert "INFO" in caplog.text
```

---

### Q: Kako da pokrenem samo jedan test?

**A:**

```bash
# Pokreni samo jedan test
pytest tests/test_scraper_basics.py::test_fetch_page_with_valid_url -v

# Pokreni samo TestFetchPage klasu
pytest tests/test_scraper_basics.py::TestFetchPage -v

# Pokreni testove koji sadrže "timeout"
pytest -k "timeout" -v
```

---

### Q: Kako da vidim šta se dešava u testu?

**A:**

```bash
# Pokreni sa -s flagi (prikaži print output)
pytest tests/ -s

# U testu: dodaj print statement
def test_example(mock_html):
    print(f"HTML length: {len(mock_html)}")  # Videće se sa -s
    assert len(mock_html) > 0
```

---

## 📁 PROJECT STRUKTURA PITANJA

### Q: Gde trebalo je da bude `config.py`?

**A:**

```
projects/01-web-scraper/
├── config.py                    ← OVDE (root direktorijum)
├── scraper.py
├── tests/
├── logs/
└── output/
```

---

### Q: Šta trebalo je da bude u `requirements.txt`?

**A:**

```
requests
beautifulsoup4
pytest
pytest-cov
pytest-mock
```

Generiši sa:

```bash
pip freeze > requirements.txt
```

---

### Q: Gde trebalo je da bude `__init__.py` u `tests/`?

**A:**

```
tests/
├── __init__.py              ← Prazan fajl (marker da je package)
├── conftest.py
└── test_scraper_basics.py
```

`__init__.py` može biti prazan, samo signalizira da je `tests/` Python package.

---

## 🔴 ČESTE GREŠKE

### Greška 1: "ModuleNotFoundError: No module named 'requests'"

**Problem:** requests nije instaliran

**Rešenje:**

```bash
pip install requests
```

---

### Greška 2: "AttributeError: 'NoneType' object has no attribute 'get_text'"

**Problem:** `select_one()` vrataje `None`:

```python
# LOŠE
element = soup.select_one(".nonexistent")
text = element.get_text()  # None nema get_text() metod!

# DOBRO
element = soup.select_one(".nonexistent")
if element:
    text = element.get_text()
else:
    text = "Not found"
```

---

### Greška 3: "ConnectionError: Failed to establish a new connection"

**Problem:** Server nije dostupan ili nema interneta

**Rešenje:**

```python
try:
    response = requests.get(url, timeout=5)
except requests.ConnectionError:
    print("Connection failed, using mock data")
    html = "<h1>Mock</h1>"  # Fallback
```

---

### Greška 4: "Timeout: Failed to establish a new connection"

**Problem:** Server je spora ili je timeout premali

**Rešenje:**

```python
# Povećaj timeout
response = requests.get(url, timeout=10)  # 10 sekundi umesto 5
```

---

### Greška 5: "AssertionError" u testu

**Problem:** Test očekuje nešto, ali dobija drugo

**Rešenje:**

```bash
# Pokreni sa -s da vidiš šta se dešava
pytest -s tests/test_scraper_basics.py::test_extract_titles_with_valid_html

# Ili dodaj debug print
def test_example(mock_html):
    titles = extract_titles(mock_html)
    print(f"Got titles: {titles}")  # Vidiš šta je vraćeno
    assert len(titles) == 1
```

---

### Greška 6: "403 Forbidden" pri zahtevanju

**Problem:** Server odbija zahtev, misli da si bot

**Rešenje:**

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
response = requests.get(url, headers=headers)
```

---

### Greška 7: "venv not activated"

**Problem:** Python ne koristi pakete iz venv-a

**Rešenje:**

```bash
# Aktiviraj venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Proveri (trebalo bi (venv) ispred prompt-a)
which python3
# /path/to/projects/01-web-scraper/venv/bin/python3
```

---

## 💡 SAVETI

### Savet 1: Koristi httpbin.org za testiranje

```python
# Besplatna fake stranica za testiranje
requests.get("https://httpbin.org/html")  # Vraća HTML
requests.get("https://httpbin.org/status/404")  # Vraća 404
requests.get("https://httpbin.org/delay/10")  # Simulira spor server
```

---

### Savet 2: Čuvaj HTML lokalno tokom razvoja

```python
# Prvi put
html = fetch_page("https://real-website.com")
Path("mock_data.html").write_text(html)

# Potom
html = Path("mock_data.html").read_text()  # Brže, bez mrežnog zahteva
```

---

### Savet 3: Koristi `prettify()` za debug-ovanje

```python
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify()[:500])  # Prikaži prvih 500 karaktera lepše formatiranog HTML-a
```

---

### Savet 4: Testiraj različite CSS selektor-e u browser Dev Tools

```
1. Otvori Inspect Element
2. Konsola → Tipaj: $$(".class-name")  # Pronađi sve
3. Vidiš li elemente? Ako da, selektor je dobar
```

---

### Savet 5: Loguj detaljne poruke

```python
logger.info(f"Response status: {response.status_code}")
logger.info(f"Found {len(titles)} titles")
logger.debug(f"HTML length: {len(html)}")  # Debug info
```

---

## 🎓 UČENJA SAMO ZA DAN 8

**Šta si naučio:**

1. ✅ HTTP zahteve sa `requests` libraryjem
2. ✅ HTML parsing sa `BeautifulSoup`
3. ✅ CSS selektor-e
4. ✅ Error handling pri scraping-u
5. ✅ Project struktura (config, tests, logs)
6. ✅ Pytest sa mock-ima
7. ✅ Logging setup
8. ✅ Git verzionisanje

**Šta ćeš naučiti Dan 9:**

-   Više kompleksnih CSS selektor-a
-   Navigacija kroz DOM stablo
-   Pagination (multiple pages)
-   Rate limiting i delay-e
-   Sveobuhvatnije testove

---

## ✨ Ako želiš da pitaš nešto što nije ovde?

Poruka sa:

1. Šta pokušavaš da uradiš?
2. Šta si pokušao?
3. Koja je greška/rezultat?

Primer:

```
"Pokušavam da pronađem sve <div> sa class='product'.
Koristim soup.select('.product') što je vraća listu,
ali želim samo prvi. Probao sam select_one('.product')
ali vraća samo jedan element. Kako da pronađem sve?"

→ Odgovor: select('.product') je ispravno za sve,
   select_one('.product') za prvi. Zavisi šta trebaš.
```

---

**Srećno sa testiranjem! 🎉**

**Sledeće:** Probaj neke od challenge-a u [tasks.md](./tasks.md) ako brzo završiš!

---
