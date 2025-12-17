# 🎯 Potrebna Baza — Python Automatizacija

**Pitanje:** "Koja je to baza potrebna kako bih mogao lagodnije i sigurnije učiti u prve projekte?"

**Trebaju ti ČETIRI nivoa znanja:**

```
1. TERMINAL (da radiš sa fajlovima)
2. PYTHON CORE (da razumeš što se dešava)
3. STANDARD LIBRARY (csv, json, pathlib, logging)
4. ONE FRAMEWORK (requests + beautifulsoup)
```

**Ostatak = Kombinovanje gornjeg sa projektima.**

---

## TIER 1: MUST-HAVE (Ne možeš bez toga)

### ✅ Terminal Skills | Osnove

-   [ ] Navigacija: `pwd`, `cd`, `ls`
-   [ ] Rad sa fajlovima: `mkdir`, `touch`, `rm`, `cp`
-   [ ] Čitanje: `cat`, `head`, `tail`, `less`
-   [ ] Pretraga: `grep`, `find`
-   [ ] Pipes: `|`, redirecting: `>`, `>>`

**Zašto?** Skripte rade sa fajlovima. Bez terminala, gubiš vreme.

**Test:** Mogu li da nađem sve `.csv` fajlove u projektu sa `find`?

```bash
find . -name "*.csv"
```

---

### ✅ Python Core | Osnove

-   [ ] Types: `str`, `int`, `list`, `dict`, `None`
-   [ ] Type hints: `def func(x: int) -> str:`
-   [ ] Control flow: `if`, `for`, `while`
-   [ ] Functions: `def`, `return`, default args
-   [ ] Error handling: `try`, `except`, `finally`
-   [ ] OOP basics: `class`, `__init__`, methods

**Zašto?** Bez toga, čitaš kod kao da je hijeroglif.

**Test:** Mogu li da razumem svaki red u `csv_cleaner.py`?

---

### ✅ CSV Module | Osnove

-   [ ] `csv.reader` i `csv.writer`
-   [ ] **Dialect** - recept za format
-   [ ] **Sniffer** - detektuj format
-   [ ] **csv.excel** - fallback
-   [ ] `newline=""` - parametar
-   [ ] `encoding="utf-8"` - parametar

**Zašto?** CSV je osnova za sve automatizacije. Ako ne razumeš csv.Dialect, gubiš vreme.

**Test:** Mogu li da napravim `detect_dialect()` bez guglovanja?

---

## TIER 2: VERY USEFUL (Trebaće ti brzo)

### ✅ File I/O

-   [ ] `open()` vs context manager `with`
-   [ ] `Path` iz `pathlib` vs `os.path`
-   [ ] `Path.read_text()`, `Path.write_text()`

**Zašto?** Skripte manipulišu fajlovima. Path je modern i bolji.

**Test:** Mogu li da zamenim `open()` sa `Path().read_text()`?

---

### ✅ JSON Module

-   [ ] `json.load()`, `json.dump()`
-   [ ] JSON struktura = Python dict
-   [ ] UTF-8 sa specijalnim znacima

**Zašto?** Web API-ji vraćaju JSON. Trebate ga čitati.

**Test:** Mogu li da konvertujem CSV → JSON?

---

### ✅ Logging Module

-   [ ] `logging.basicConfig()`
-   [ ] Levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`
-   [ ] Formatiranje sa `%(levelname)s`

**Zašto?** Print nije dovoljno. Production kod koristi logging.

**Test:** Mogu li da dodam logging u `csv_cleaner.py`?

---

### ✅ Git Basics

-   [ ] `git init`, `git clone`
-   [ ] `git add`, `git commit`, `git push`
-   [ ] `git status`, `git log`

**Zašto?** Trebate verzionisati kod. Kasnije CI/CD.

**Test:** Mogu li da commitujem kod sa porukama?

---

## TIER 3: SOON (Trebaje ti u nedelji-dve)

### ✅ Requests Library | Osnove

-   [ ] `requests.get()`
-   [ ] Status codes
-   [ ] JSON response
-   [ ] Error handling

**Zašto?** Web scraping koristi Requests.

---

### ✅ BeautifulSoup

-   [ ] Instalacija
-   [ ] `BeautifulSoup()` parser
-   [ ] `.find()`, `.find_all()`, `.select()`
-   [ ] CSS selectors

**Zašto?** Trebate parsirati HTML.

---

### ✅ Pytest

-   [ ] `def test_()` konvencija
-   [ ] `assert`
-   [ ] Running: `pytest -v`

**Zašto?** Production kod ima testove.

---

## TIER 4: LATER (Bonus)

### ❌ NE TREBAĆE TI SADA

-   Pandas (čekaj dok ne znaš csv.DictReader)
-   Async (čekaj dok ne znaš requests)
-   Databases (čekaj dok ne znaš JSON)
-   Machine Learning (🚀 Kasnije!)

---

# 📊 VIZUELNO: Šta radiš kada

```
DAN 1-2: Terminal + Git setup
   └─→ Mogu da radim sa fajlovima iz terminala

DAN 2-4: Python Core
   └─→ Razumem kontrolu toka, tipove, greške

DAN 3-4: CSV + Dialect (TVOJ FOKUS)
   └─→ Mogu da čitam/pišem CSV bilo kog formata

DAN 5-6: Pathlib + File I/O
   └─→ Path je prirodnije od os.path

DAN 6-7: JSON + Logging
   └─→ Mogu da procesuiram API response

DAN 7-8: Pytest
   └─→ Imam testove za svoj kod

DAN 8-10: Requests + BeautifulSoup
   └─→ Mogu da skrapujem web

DAN 10-14: Integration
   └─→ Kombinujem sve u realnim projektima
```

---

## 🎓 KOJA JE RAZLIKA IZMEĐU TIERS?

```python
# TIER 1: Gledaš šta se dešava
for row in csv.reader(f):  # Znam što je csv.reader
    print(row)             # Znam što je print

# TIER 2: Rad postaje elegantniji
with open(file) as f:      # with statement
    data = json.load(f)    # json.load umesto ručnog parsiranja

# TIER 3: Radiš sa web-om
response = requests.get(url)  # Dobuam podatke
soup = BeautifulSoup(response.text)  # Parsiranje

# TIER 4: Samo ako trebaj (ne sada!)
df = pd.read_csv(file)     # Trebaj samo ako radiš sa big data
```

---

## ⚠️ NAJVEĆE GREŠKE KOJU POČETNICI PRAVE

```
❌ GREŠKA 1: Početo sa Pandas
   → Pandas skriva csv.reader
   → Ne razumeš šta se dešava
   → Kasnije si zaglavljen kada trebaj raw CSV

❌ GREŠKA 2: Async na početku
   → Trebaj prvo synchronous code
   → Async = Napredni koncept

❌ GREŠKA 3: Suviše biblioteka
   → Nauče BeautifulSoup, Selenium, Scrapy, ...
   → Zbunjeni koji da koriste
   → Trebaj samo BeautifulSoup na početku

❌ GREŠKA 4: Teorija bez prakse
   → Čitaš dokumentaciju 3 dana
   → Nikada ne pokreneš kod
   → Zaboravaš sve što si pročitao

✅ ISPRAVAN PUT: Praksa sa teorijom
   → 30 min teorije
   → 90 min kodiranja i eksperimentisanja
   → Ponavljanje
```

---

## 💡 SPECIFIČNO ZA TVOJ SLUČAJ

**Čujem:** "Stalno imam osečaj da mi treba jača teorijska osnova"

**Diagnoza:**

1. Verovatno ti nedostaje Python Core (kontrola toka, greške, types)
2. Verovatno ne praktikuješ dovoljno (čitaš > kodiraš)
3. Verovatno ne znaš što je Dialect (prvi put vidim...)

**Rešenje:**

1. ✅ Prvo DEO 1.2-1.5 iz `csv_repl_exercises.md` (Teorija)
2. ✅ Zatim DEO 1.1-1.7 (Praktična vežba - TI kodiraš)
3. ✅ Zatim napravi **svoj** CSV cleaner (Integracija)

**Rezultat:** Iz "treba mi osnova" u "Razumem Dialect!" za 2h.

---

## 📋 14-dnevni plan

### Nedelja 1: OSNOVE + CSV

| Dan | Fokus                                  | Trajanje | Rezultat                      |
| --- | -------------------------------------- | -------- | ----------------------------- |
| 1   | Terminal + Git                         | 2h       | `git init`, prvi commit       |
| 2   | Python Core (types, functions, errors) | 3h       | Razumem Python toka           |
| 3   | CSV Dialect + Sniffer                  | **2h**   | `detect_dialect()` radi       |
| 4   | CSV čitanje/pisanje                    | 2h       | `read_rows()`, `write_rows()` |
| 5   | CSV cleaner integracija                | 2h       | Kompletan `csv_cleaner.py`    |
| 6   | Pathlib + File I/O                     | 2h       | `Path` umesto `os.path`       |
| 7   | JSON + Logging                         | 2h       | Refaktuj sa logging           |

---

### Nedelja 2: MODULES + TESTING

| Dan | Fokus                 | Trajanje | Rezultat                       |
| --- | --------------------- | -------- | ------------------------------ |
| 8   | Pytest osnove         | 2h       | Napravi `test_csv_cleaner.py`  |
| 9   | Error handling        | 2h       | Try/except u skripti           |
| 10  | Requests osnove       | 2h       | `requests.get()` radi          |
| 11  | BeautifulSoup osnove  | 2h       | Mogu da parserium HTML         |
| 12  | Mini scraper projekat | 3h       | Moj prvi scraper               |
| 13  | Integration           | 2h       | Scraper → CSV                  |
| 14  | Consolidation         | 2h       | Refaktuj sve sa best practices |

**UKUPNO:** ~38 sati = Sistem učenja

---

## 🔍 VALIDACIJA: Kako da znaš da si gotov sa svakim TIER?

### TIER 1 ✅

-   [ ] Mogu da nađem `.py` fajl u bilo kom direktorijumu
-   [ ] Mogu da napravim `hello_world.py` i pokrenem ga
-   [ ] Mogu da napravim try/except bez greške
-   [ ] Mogu da razumem tip (str, int, dict, list)

### TIER 2 ✅

-   [ ] Mogu da čitam CSV bilo kog formata sa Sniffer
-   [ ] Mogu da koristim Path umesto os.path
-   [ ] Mogu da konvertujem CSV → JSON
-   [ ] Mogu da dodam logging u skriptu

### TIER 3 ✅

-   [ ] Mogu da dobuam podatke sa API-ja
-   [ ] Mogu da parserium HTML sa BeautifulSoup
-   [ ] Mogu da napravim test sa pytest
-   [ ] Mogu da kombinujem 3 biblioteke zajedno

---

# 🎯 ZAVRŠAK: Šta radiš SADA (sutra)

1. **Otvori:** [`learning/DAY_03_CSV_BASICS.md`](../learning/DAY_03_CSV_BASICS.md)
2. **Pokreni:** FAZA 1 (Setup test fajlova)
3. **Praktikuj:** FAZA 2 (Sniffer eksperimenti)
4. **Kodiraj:** FAZA 3 (detect_dialect funkcija)

**Rezultat:** Sutra razumeš Dialect bez paničnog guglovanja! ✅

---

# 📚 Resursi po TIER

| TIER | Resurs               | Gde                                                                                 |
| ---- | -------------------- | ----------------------------------------------------------------------------------- |
| 1    | Python official docs | [python.org/docs](https://python.org/docs)                                          |
| 1    | Terminal tutorial    | `man ls`, `man grep`                                                                |
| 1    | Our material         | [`csv_repl_exercises.md`](../scratch/repl_sessions/csv_repl_exercises.md)           |
| 2    | Pathlib docs         | [docs.python.org/pathlib](https://docs.python.org/3/library/pathlib.html)           |
| 2    | CSV docs             | [docs.python.org/csv](https://docs.python.org/3/library/csv.html)                   |
| 3    | Requests docs        | [requests.readthedocs.io](https://requests.readthedocs.io)                          |
| 3    | BeautifulSoup        | [crummy.com/software/BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) |
| 3    | Pytest docs          | [pytest.org](https://pytest.org)                                                    |

---

## 💪 MOTIVACIJSKI ZAKLJUČAK

```
SADA:     "Ne razumem Dialect... treba mi osnova..."
SUTRA:    "Pogledaj! Sniffer detektuje sve formate automatski!"
NEDELJA:  "Napisao sam kompletan csv_cleaner sa testovima"
MESECI:      "Mogu da kreiram nove projekte bez paničnog guglovanja"
POLA GODINE:   "Postao sam Python automation engineer"
```

**Razlika?** Sistem učenja + Praksa + Ponavljanje.

**Počni sutra sa DAY_03.** 🚀

---

## 🎬 Ako imaš još pitanja

**P: Treba li mi Pandas sada?**
O: **NE**. Čekaj dok ne znaš csv.DictReader savršeno.

**P: Treba li mi Selenium za scraping?**
O: **NE**. BeautifulSoup je dovoljna na početku.

**P: Treba li mi baza podataka?**
O: **NE**. Čekaj dok ne znaš JSON savršeno.

**P: Treba li mi Docker?**
O: **NE**. Čekaj 3-6 meseci.

**P: Treba li mi asyncio?**
O: **NE**. Nauči synchronous first.

**Lekcija:** Ako se pitate "da li treba X?" - odgovor je verovatno **NE**.

Uči samo ono što ti treba sada. Ostatak dolazi prirodno.

🎯 **Pokreni DAY_03 sutra!**

---
