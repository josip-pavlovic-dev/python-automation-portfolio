---
type: daily_kickoff
date: 2025-12-26
day: 8/14
topic: Web Scraper v1 — Setup & Foundation
duration: 8 hours
status: 🔴 ACTIVE
---

# 🔴 DAN 8 KICKOFF — Web Scraper v1: Setup & Foundation

**Dobar dan, Jole! 👋**

Sada počinjеš sa najzanimljivijim delom — **Web Scraper projektom!**

---

## 📊 Vremenska Raspodela Dana (8h)

```
09:00 — Kickoff + Setup (15 min)
09:15 — FAZA 1: Requests + BeautifulSoup (1.5h)
         ├─ Instalacija
         ├─ GET zahteve
         ├─ HTML parsing
         └─ REPL praksa
10:45 — Pauza (15 min)

11:00 — FAZA 2: Project Setup (1.5h)
         ├─ Struktura direktorijuma
         ├─ config.py
         ├─ requirements.txt
         └─ Git setup

12:30 — Ručak (30 min)

13:00 — FAZA 3: Scraper Core (2h)
         ├─ scraper.py osnova
         ├─ fetch_page(url)
         ├─ Headers + timeout
         └─ Error handling

15:00 — Pauza (15 min)

15:15 — FAZA 4: Testing Setup (2h)
         ├─ conftest.py fixtures
         ├─ test_scraper_basics.py
         ├─ Mock testovi
         └─ Coverage check

17:15 — Finalizacija (15 min)
         ├─ Rekapitulacija
         ├─ Checklist
         └─ Git commit

17:30 — DAN 8 DONE ✅
```

---

## 🎯 Tri Linije Dana

### Linija 1️⃣ — "Želim da razumem šta se dešava"

👉 **Za tebe:**

-   Čitaj README.md (Overview)
-   Čitaj cheatsheet.md (Requests + BeautifulSoup osnove)
-   Prati web_scraper_setup_guide.md **korak po korak**
-   Radi REPL primere
-   Piši testove

---

### Linija 2️⃣ — "Samo mi reši zadatak"

👉 **Za tebe:**

-   Preskoči teoriju
-   Idi direktno na web_scraper_setup_guide.md
-   Ispratи sve korake
-   Uradi testove
-   Komit

---

### Linija 3️⃣ — "Imam iskustvo, samo mi reči šta trebam"

👉 **Za tebe:**

-   Koristi tasks.md kao checklist
-   Pogledaj cheatsheet.md za reference
-   Piši code prema specifikaciji
-   Testiraj

---

## 🏗️ Tri Filara Dana 8

### Pilar 1: Instalacija + Osnove (1.5h)

**Šta učiš:**

```python
import requests
response = requests.get("https://example.com")
print(response.status_code)  # 200

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.select("h1")
```

**Rezultat:** Možeš da:

-   ✅ Napraviš GET zahtev
-   ✅ Proveiraš status kod
-   ✅ Parsiraš HTML sa CSS selektorima
-   ✅ Ekstraktuješ tekst iz HTML-a

---

### Pilar 2: Struktura Projekta (1.5h)

**Šta kreirаš:**

```
projects/01-web-scraper/
├── config.py          # Settings (URL, headers, timeout)
├── scraper.py         # Main logika
├── requirements.txt   # pip freeze
├── tests/
│   ├── conftest.py    # Fixtures
│   └── test_scraper_basics.py
├── logs/
│   └── app.log
├── output/
│   └── sample.csv
└── README.md
```

**Rezultat:** Struktura je profesionalna i skalabilna.

---

### Pilar 3: Scraper Core + Tests (3.5h)

**Šta kreirаš:**

```python
# scraper.py
def fetch_page(url: str, timeout: int = 5) -> str:
    """Fetch HTML sa error handling."""

# tests/test_scraper_basics.py
def test_fetch_page_with_valid_url(mock_response):
    """Test fetch_page sa mock-om."""
```

**Rezultat:**

-   ✅ Scraper je testabilan
-   ✅ Svaka funkcija ima test
-   ✅ Coverage >70%

---

## 🎓 Kako Koristiš Materijal Danas?

### ✅ Jednostavna Formula

```
1. Otvori web_scraper_setup_guide.md
2. Prati FAZU 1, 2, 3, 4 redom
3. Svaki primer radi u REPL-u
4. Ako ne razumeš nešto:
   → Čitaj relevant sekciju iz cheatsheet.md
5. Posle svake faze:
   → Proveri tasks.md checklist
6. Na kraju:
   → Git commit "Day 8: Web Scraper Setup"
```

---

## 🚨 Česte Greške (Izbegni!)

### ❌ LOŠE: Preskakanje instalacije

```bash
# LOŠE
python3 -c "import requests"  # Verovatno će pucati

# DOBRO
source venv/bin/activate
pip install requests beautifulsoup4
```

---

### ❌ LOŠE: Ne kreiraj config.py

```python
# LOŠE: URL-ovi hardkodirani
def scrape():
    r = requests.get("https://example.com/page")

# DOBRO: config.py
CONFIG = {"BASE_URL": "https://example.com"}
def scrape():
    r = requests.get(CONFIG["BASE_URL"] + "/page")
```

---

### ❌ LOŠE: Ne testiraj

```python
# LOŠE: Nema testova
# DOBRO
def test_fetch_page_returns_string():
    result = fetch_page("https://httpbin.org/html")
    assert isinstance(result, str)
```

---

### ❌ LOŠE: Nema error handling-a

```python
# LOŠE: Ako server ne odgovara?
response = requests.get(url)
soup = BeautifulSoup(response.text)

# DOBRO: Handluj greške
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.RequestException as e:
    logger.error(f"Failed: {e}")
    raise
```

---

## 💪 Motivacija

Primetio sam da si brz sa učenjem. Dan 5 (Type Annotations) je bio teško, ali si ga proslavio! Isti pristup koristi za Dan 8:

1. **Pročitaj** sve pre nego počneš
2. **Praktisuй** u REPL-u
3. **Piši testove** od početka
4. **Komituй** na kraju

**Rezultat?** Profesionalni Web Scraper koji možeš da pokazuješ poslodavcima! 🎉

---

## 🎯 Šta je Uspeh Za Dan 8?

Ako na kraju dana **OVO SVE** možeš da uradi:

```python
# 1. Instalacija
source venv/bin/activate
python3

# 2. Requests
>>> import requests
>>> r = requests.get("https://httpbin.org/html")
>>> print(r.status_code)
200

# 3. BeautifulSoup
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(r.text, "html.parser")
>>> print(len(soup.select("p")))
42

# 4. Scraper
>>> from scraper import fetch_page
>>> html = fetch_page("https://httpbin.org/html")
>>> print(len(html) > 0)
True

# 5. Testovi
$ pytest tests/ -v
tests/test_scraper_basics.py::test_fetch_page_returns_string PASSED
tests/test_scraper_basics.py::test_fetch_page_handles_error PASSED
...
4 passed in 0.23s
```

---

## 🚀 Ako Brzo Završiš?

Dodatne aktivnosti:

1. **Eksperimenti sa CSS selektorima** — try `soup.select()` na različitim URL-ovima
2. **Dodaj retry logiku** — pokušaj zahtev 3x pre nego odustaneš
3. **Testiraj sa user-agent stringu** — vidi kako serveri reaguju
4. **Kreiraj conftest.py mock fixture** — practice za Dan 9

---

## 📞 Ako Zaglavim Duže od 15 Minuta?

### 1️⃣ Proveri cheatsheet.md

Verovatan odgovor je tamo. Primer:

-   "Kako da proverim status kod?" → cheatsheet.md sekcija "Status Codes"

### 2️⃣ Pogledaj chatlog.md

Česte greške su već tu.

### 3️⃣ Pitaj AI sa greškom

Kopi-paста grešku + kod → dobićeš odgovor u 30 sekundi

---

## ⏰ Vremenske Preporuke Po Fazi

| Faza         | Vreme | Aktivnost      | Rezultat           |
| ------------ | ----- | -------------- | ------------------ |
| 1            | 1.5h  | Requests + BS4 | Znam osnove        |
| 2            | 1.5h  | Project setup  | Struktura je jasna |
| 3            | 2h    | Scraper core   | fetch_page() radi  |
| 4            | 2h    | Testing        | 4+ testova prolaze |
| Finalizacija | 15min | Git + review   | Spreman za Dan 9   |

---

## ✅ Pre Nego Počneš — Provera Stanja

Ponovi od mene: "Završio sam Dan 6-7 (Pathlib + Testing) i razumem:"

-   [ ] `Path` operacije
-   [ ] Pytest fixtures (`tmp_path`)
-   [ ] Error handling (`try/except`)
-   [ ] `logging` modul
-   [ ] TypedDict za podatke
-   [ ] Type hints sa `->` return type

Ako je sve ✅ → **Spreman si! 🚀**

---

## 📖 Redosled Materijala Danas

1. ✅ **Sada:** Ovo (kickoff.md) — 5 min
2. → **Sledeće:** [cheatsheet.md](./cheatsheet.md) — 30 min
3. → **GLAVNO:** [web_scraper_setup_guide.md](./web_scraper_setup_guide.md) — 6h (prati sve FAZE)
4. → **Reference:** [tasks.md](./tasks.md) — tokom dana
5. → **Q&A:** [chatlog.md](./chatlog.md) — ako zaglavim

---

## 🎉 Finalna Poruka

> "Today you start building something real. By the end of the day, you'll have a professional Web Scraper project structure with tests, logging, and proper error handling. Same discipline as Day 5 (Type Annotations), same results. Let's go! 💪"

---

**Na putu! 🚀**

**Sledeća stvar:** Otvori [cheatsheet.md](./cheatsheet.md) i počni sa Requests osnove.

---
