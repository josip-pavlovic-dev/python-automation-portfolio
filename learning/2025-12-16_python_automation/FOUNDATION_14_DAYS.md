# 🏗️ FOUNDATION — 14 Dana Priprema za Python Automatizaciju

**Status:** Master Plan za sistensku pripremu
**Cilj:** Jača teoretska osnova pre nego što kreneš sa projektima
**Rezultat:** Samstalno kodiranje bez "osećaja nesigurnosti"

---

## 🎯 PROBLEM KOJI REŠAVAMO

```
❌ Trenutno stanje:
"Imam osećaj da mi treba jača teorijska osnova"
"Stalno imam potrebu da tražim pomoć"
"Ne mogu da počnem samostalno"

✅ Stanje posle 14 dana:
"Mogu da pročitam kod i razumejem šta se dešava"
"Mogu da pišem osnovne skripte bez guglovanja"
"Znam šta su moje slabe tačke i kako da ih pojačam"
```

---

## 🧱 FUNDAMENTALNI SLOJEVI (Piramida učenja)

```
         ┌─────────────────────┐
         │   PROJECTS (veb)    │  ← Nedelja 3-4: Web scraping
         │   AUTOMATION (real) │
         ├─────────────────────┤
         │  FRAMEWORKS (csv)   │  ← Nedelja 2-3: csv, json, pathlib
         │  LIBRARIES & MODULES│
         ├─────────────────────┤
         │  PYTHON CORE (OOP)  │  ← Nedelja 1-2: klase, tipovi, errors
         │  FUNDAMENTALS       │
         ├─────────────────────┤
         │   LINUX BASICS      │  ← OSNOVA: terminalni, git, paths
         │   TERMINAL & GIT    │
         └─────────────────────┘
```

**Lekcija:** Ako ti nedostaje neka osnova, sve iznad pada! 💥

---

## 📋 SPECIFIČNA BAZA POTREBNA ZA PYTHON AUTOMATIZACIJU

### Nivo 1: LINUX & TERMINAL (Fundamentals) — Dan 1-2

**Šta moraš znati:**

#### 1.1 Terminal Basics

-   [ ] `pwd`, `ls`, `cd` - navigacija
-   [ ] `mkdir`, `touch`, `rm` - kreiranje/brisanje
-   [ ] `cat`, `less`, `head`, `tail` - čitanje fajlova
-   [ ] `grep`, `find` - pretraga
-   [ ] Pipes: `|` i redirecting: `>`, `>>`
-   [ ] Running scripts: `python script.py` vs `./script.sh`

**Zašto?** Automatizacija = Često radiš sa fajlovima iz terminala

---

#### 1.2 Git Basics

-   [ ] `git init`, `git clone`
-   [ ] `git add`, `git commit`, `git push`
-   [ ] `git status`, `git log`
-   [ ] `.gitignore`

**Zašto?** Trebate verzionisati kod, a kasnije koristiš CI/CD

---

#### 1.3 File Paths & Permissions

-   [ ] Absolute vs relative paths
-   [ ] `chmod` - dozvole (`755`, `644`)
-   [ ] Environment variables: `echo $PATH`
-   [ ] Virtual environments: `venv`

**Zašto?** Skripte se pokošavaju sa različitih lokacija + permissions

---

### Nivo 2: PYTHON CORE (Fundamentals) — Dan 2-4

**Šta moraš znati:**

#### 2.1 Types & Type Hints

-   [ ] `int`, `str`, `float`, `bool`, `None`
-   [ ] `list`, `tuple`, `dict`, `set`
-   [ ] Type hints: `def func(x: int) -> str:`
-   [ ] Generic types: `list[str]`, `dict[str, int]`

**Test:** Mogu li da napišem `def read_csv(path: str) -> list[dict[str, str]]:`?

---

#### 2.2 Control Flow & Functions

-   [ ] `if`, `elif`, `else`
-   [ ] `for`, `while` loops
-   [ ] `break`, `continue`, `pass`
-   [ ] Funkcije sa `return`, default args, `*args`, `**kwargs`
-   [ ] List comprehensions: `[x*2 for x in range(10)]`

**Test:** Mogu li da napravim filter sa list comprehension?

---

#### 2.3 Error Handling

-   [ ] `try`, `except`, `finally`
-   [ ] Built-in exceptions: `ValueError`, `TypeError`, `KeyError`
-   [ ] `raise Exception("msg")`
-   [ ] Custom exceptions

**Test:** Mogu li da napravim function koja hvata encoding error?

---

#### 2.4 OOP Basics

-   [ ] `class` definicija
-   [ ] `__init__`, `self`
-   [ ] Methods i properties
-   [ ] Inheritance: `class Child(Parent):`
-   [ ] `@property`, `@staticmethod`, `@classmethod`

**Test:** Mogu li da napravim `class CSVReader` sa metodama?

---

### Nivo 3: PYTHON MODULES (Standard Library) — Dan 4-7

**Šta moraš znati:**

#### 3.1 File I/O

-   [ ] `open()`, `read()`, `write()`, `readlines()`
-   [ ] Context manager: `with` statement
-   [ ] `pathlib.Path` vs `os.path`

---

#### 3.2 CSV Module (TVOJ FOKUS)

-   [ ] `csv.reader`, `csv.writer`
-   [ ] `csv.DictReader`, `csv.DictWriter`
-   [ ] **Dialect, Sniffer, csv.excel** ← U `csv_repl_exercises.md`
-   [ ] `newline=""`, `encoding="utf-8"`

---

#### 3.3 JSON Module

-   [ ] `json.load()`, `json.dump()`
-   [ ] JSON struktura vs Python dict
-   [ ] UTF-8 encoding sa specijalnim znacima

---

#### 3.4 Pathlib Module

-   [ ] `Path()` - better than `os.path`
-   [ ] `Path.read_text()`, `Path.write_text()`
-   [ ] `Path.glob()`, `Path.iterdir()`
-   [ ] `Path.exists()`, `Path.mkdir()`

---

#### 3.5 Logging Module

-   [ ] `logging.basicConfig()`
-   [ ] Levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`
-   [ ] Formatiranje sa `%(levelname)s`

---

#### 3.6 Datetime Module

-   [ ] `datetime.datetime.now()`
-   [ ] String formatting: `strftime()`, `strptime()`
-   [ ] Timezones (basic)

---

#### 3.7 RE Module (Regex)

-   [ ] `re.search()`, `re.findall()`, `re.sub()`
-   [ ] Basic patterns: `\d`, `\w`, `.*`, `^`, `$`
-   [ ] Character classes: `[a-z]`, `[0-9]`

---

### Nivo 4: FRAMEWORKS & LIBRARIES — Dan 7-10

**Šta moraš znati:**

#### 4.1 Requests Library (Web)

-   [ ] `requests.get()`, `requests.post()`
-   [ ] Status codes: `200`, `404`, `500`
-   [ ] Headers, parameters, timeout
-   [ ] JSON response: `response.json()`

---

#### 4.2 BeautifulSoup (HTML Parsing)

-   [ ] Instalacija: `pip install beautifulsoup4`
-   [ ] `BeautifulSoup(html, "html.parser")`
-   [ ] Finding elements: `.find()`, `.find_all()`, `.select()`
-   [ ] CSS selectors: `.class-name`, `#id`, `element > child`

---

#### 4.3 Pandas (Data Analysis)

-   [ ] `pd.read_csv()` - alternativa csv modulu
-   [ ] DataFrames vs Series
-   [ ] Filtering: `df[df['column'] > 10]`
-   [ ] Grouping: `df.groupby('column').sum()`
-   [ ] Exporting: `df.to_csv()`, `df.to_json()`

---

#### 4.4 Pytest (Testing)

-   [ ] `def test_function():` konvencija
-   [ ] `assert` statement
-   [ ] `pytest.fixture`
-   [ ] Running tests: `pytest -v`

---

### Nivo 5: PROJECTS & REAL WORLD — Dan 10-14

**Šta moraš raditi:**

#### 5.1 Build Your Own: CSV Cleaner

-   [ ] Sve koncepte iz Nivoa 2-3
-   [ ] Input: random CSV (različiti formati)
-   [ ] Output: čist, standardizovan CSV
-   [ ] Add logging, error handling, testing

---

#### 5.2 Build Your Own: Web Scraper

-   [ ] Requests + BeautifulSoup
-   [ ] Snimi HTML → CSV
-   [ ] Error handling za network issues
-   [ ] Implement delay između requestova

---

#### 5.3 Build Your Own: Data Pipeline

-   [ ] Čitaj CSV → Procesiranje → Upiši JSON
-   [ ] Kombinuj csv + json + pathlib + logging

---

## 📅 PLAN ZA NAREDNIH 14 DANA (konkretno)

### Nedelja 1: PYTHON CORE + CSV OSNOVE

**Dan 1-2: Linux & Terminal Osnove**

```
- [ ] REPL exercises: terminal navigation
- [ ] Git init + first commit
- [ ] Razumeti PATH i file permissions
Vremenske: ~4h
```

**Dan 2-3: Python Core Basics**

```
- [ ] Types, functions, control flow
- [ ] OOP: class, __init__, methods
- [ ] Error handling: try/except
Vremenske: ~6h
```

**Dan 3-4: Python CSV Module**

```
- [ ] 📖 csv_repl_exercises.md DEO 1 (2h)
- [ ] 📖 csv_repl_exercises.md DEO 2 (2h)
- [ ] 📖 csv_repl_exercises.md DEO 3 (2h)
- [ ] Own: Napravi variant sa DictReader
Vremenske: ~8h
```

### Nedelja 2: MODULES + PATHLIB + TESTING

**Dan 5-6: Pathlib + File I/O**

```
- [ ] REPL: Path vs os.path
- [ ] REPL: Path.read_text(), write_text()
- [ ] REPL: Path.glob() za file search
- [ ] Own: Refaktoruj csv_cleaner da koristi Path umesto str
Vremenske: ~4h
```

**Dan 6-7: JSON + Logging**

```
- [ ] REPL: json.load/dump sa CSV output
- [ ] REPL: logging levels i formatting
- [ ] Own: Dodaj logging u csv_cleaner
Vremenske: ~4h
```

**Dan 7-8: Testing + Pytest**

```
- [ ] REPL: assert i test osnove
- [ ] REPL: pytest.fixture
- [ ] Own: Napravi test_csv_cleaner.py
Vremenske: ~4h
```

### Nedelja 3: WEB SCRAPING + INTEGRATION

**Dan 8-10: Requests + BeautifulSoup**

```
- [ ] REPL: Requests basic API calls
- [ ] REPL: BeautifulSoup HTML parsing
- [ ] Own: Napravi mini web scraper
Vremenske: ~6h
```

**Dan 10-12: Real Project - Web Scraper**

```
- [ ] Kombinuj: requests, bs4, csv, pathlib, logging
- [ ] Output: CSV sa scraped data
- [ ] Add: Error handling, rate limiting
Vremenske: ~6h
```

**Dan 12-14: Consolidation + Advanced**

```
- [ ] Refaktuj `projects/01-web-scraper`
- [ ] Add: Data validation, filtering
- [ ] Add: Async requests (bonus)
- [ ] Dokumentuj: README + docstrings
Vremenske: ~6h
```

---

# 🔍 KAKO DA ZNAŠ DA SI SPREMAN?

**Test sebi nakon 14 dana:**

```python
# ✅ Ako mogu ovo:

# 1. Čitam bilo koji CSV bez panic
csv_path = Path("random_format.csv")
dialect = detect_dialect(csv_path)
rows = read_csv(csv_path, dialect)

# 2. Pišem testove
def test_csv_cleaner():
    assert clean_rows([]) == ([], {"input_rows": 0, ...})

# 3. Gledam kodom od drugih (npr BeautifulSoup) i razumejem
soup = BeautifulSoup(html)
for tag in soup.find_all("a"):  # ← Mogu da objasnim šta se dešava

# 4. Debugiram bez guglovanja
def my_func(data: list[dict]) -> str:
    result = ""
    for item in data:
        result += item["name"] + "\n"  # ← Mogu da vidim šta je loše
    return result

# → SPREMAN SI! 🚀
```

---

# 📚 RESURSI ZA SVAKI NIVO

| Nivo          | Resurs                                                                              | Tip            |
| ------------- | ----------------------------------------------------------------------------------- | -------------- |
| Terminal      | `man ls`, `man grep`                                                                | Built-in       |
| Python Core   | Python official docs                                                                | Free           |
| CSV           | `csv_repl_exercises.md`                                                             | Tvoj materijal |
| Requests      | [requests.readthedocs.io](https://requests.readthedocs.io)                          | Free           |
| BeautifulSoup | [crummy.com/software/BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) | Free           |
| Testing       | [pytest.org](https://pytest.org)                                                    | Free           |

---

# 🎯 ZAKLJUČAK

**Baza koja ti treba = Ova 4 nivoa:**

1. **Terminal & Git** - da radiš sa fajlovima i verzijama
2. **Python Core** - da razumeš šta se dešava
3. **Standard Library** - csv, json, pathlib, logging
4. **One Framework** - Requests + BeautifulSoup za web

**Onda:** Kombinuješ sve zajedno u projektima.

**Najveća greška:** Pokušaj da naučiš Pandas pre nego što razumeš csv.reader i DictReader.

**Tvoj prioritet sada:**

1. ✅ Završi `csv_repl_exercises.md` (DEO 1-3)
2. ✅ Napravi sopstvene vežbe sa Sniffer
3. ✅ Refaktoruj `projects/01-web-scraper`
4. ✅ Tek tada Pandas/Advanced

---

# 💪 Motivacija

```
Sada: "Ne mogu da počnem"
Dana 3: "Poceo sam da razumem csv.Dialect"
Dana 7: "Napisao sam test za csv_cleaner"
Dana 10: "Mogu da skrapujem web bez boja u faci"
Dana 14: "Razumem svoj kod i mogu ga proširiti"
Dana 30: "Kreiram nove projekte bez paničnog guglovanja"
```

**Sistem učenja → Samopouzdanje → Produktivnost**

🚀
