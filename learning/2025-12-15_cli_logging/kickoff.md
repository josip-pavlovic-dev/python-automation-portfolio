---
type: kickoff
topic: CLI + Logging + JSON/CSV — Detaljni Hourly Schedule
date: 2025-12-15
linked_to: 2025-12-15_cli_logging
language: bilingual
status: active
difficulty: beginner-intermediate
estimated_time: 48 hours (6 dana × 8h)
---

# 📅 CLI + Logging + JSON/CSV — KICKOFF (Detaljni Plan)

**Trajanje:** 48 sati (6 dana po 8h)
**Cilj:** Savladaj argparse, logging, JSON/CSV obradu za automation projekte

---

## 🗓️ DAN 1 (8h) — LOGGING FUNDAMENTALS

### **08:00-09:00 | Teorija: Logging Osnove**

-   [ ] Pročitaj [L08_logging_osnove](../../scratch/theory/published/L08_logging_osnove_logger_handler_formatter,_nivoi,_izbegavanje_duplih_handlera.md)
-   [ ] Razumevanje hijerarhije: Logger → Handler → Formatter
-   [ ] Nivoi logovanja: DEBUG (10), INFO (20), WARNING (30), ERROR (40), CRITICAL (50)

**Ishod:**

-   Razumeš zašto je logging bolji od `print()`
-   Znaš kada koristiti koji nivo

---

### **09:00-10:30 | FAZA 1.1-1.2: BasicConfig + Custom Format**

-   [ ] Otvori Python REPL
-   [ ] `cli_logging_complete_exercises.md` → [FAZA 1.1](cli_logging_complete_exercises.md#11-basicconfig--najjednostavnije-logovanje)
-   [ ] Eksperimentiši sa različitim nivoima
-   [ ] `cli_logging_complete_exercises.md` → [FAZA 1.2](cli_logging_complete_exercises.md#12-custom-format--bolje-poruke)
-   [ ] Kreiraj custom format sa `%(asctime)s`, `%(levelname)s`, `%(name)s`

**Output:**

```python
2025-12-15 09:45:23 | INFO     | my_app | Aplikacija pokrenuta
```

---

### **10:30-10:45 | ☕ PAUZA**

---

### **10:45-12:00 | FAZA 1.3: Logovanje u Fajl + Console**

-   [ ] Kreiraj `sandbox/basics/cli_logging_practice/scripts/log_to_file.py`
-   [ ] `cli_logging_complete_exercises.md` → [FAZA 1.3](cli_logging_complete_exercises.md#13-logovanje-u-fajl--console)
-   [ ] Implementiraj StreamHandler (console) + FileHandler (fajl)
-   [ ] Postavi različite nivoe: Console (INFO+), File (DEBUG+)
-   [ ] Testiraj: `python3 scripts/log_to_file.py`
-   [ ] Proveri: `cat logs/app.log`

**Checkpoint:**

-   Logovi se prikazuju u terminalu I zapisuju u fajl

---

### **12:00-13:00 | 🍽️ RUČAK**

---

### **13:00-14:30 | FAZA 1.4-1.5: Duplicate Handlers + Propagation**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 1.4](cli_logging_complete_exercises.md#14-izbegavanje-duplikata-handlera)
-   [ ] Kreiraj `scripts/duplicate_problem.py` — demonstracija problema
-   [ ] Kreiraj fixed verziju sa `if not logger.handlers:`
-   [ ] `cli_logging_complete_exercises.md` → [FAZA 1.5](cli_logging_complete_exercises.md#15-logger-hijerarhija-i-propagation)
-   [ ] Eksperimentiraj sa parent/child logger-ima
-   [ ] Testiraj `logger.propagate = False`

**Isход:**

-   Izbegavaš duple poruke
-   Razumeš logger hijerarhiju

---

### **14:30-14:45 | ☕ PAUZA**

---

### **14:45-16:30 | FAZA 1.6: RotatingFileHandler**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 1.6](cli_logging_complete_exercises.md#16-rotatingfilehandler--za-production)
-   [ ] Kreiraj `scripts/rotating_log.py`
-   [ ] Postavi `maxBytes=1_000` (1KB za demo)
-   [ ] Generiši 100+ logova da vidiš rotaciju
-   [ ] Proveri: `ls -lh logs/` (trebalo bi: rotating.log, rotating.log.1, rotating.log.2, rotating.log.3)

**Checkpoint:**

-   Log fajlovi se automatski rotiraju

---

### **16:30-17:00 | Praksa: Reusable Logger**

-   [ ] Kreiraj `sandbox/basics/my_logger.py` sa funkcijom `setup_logger(name, level, log_dir)`
-   [ ] Omogući console + rotating file handler
-   [ ] Testiraj import u drugim skriptama

**Dan 1 Output:**

```python
from my_logger import setup_logger

logger = setup_logger("my_app", "DEBUG", Path("logs"))
logger.info("Hello from reusable logger!")
```

---

### **17:00-17:30 | Dan 1 Wrap-Up**

-   [ ] Commituj napredak: `git add learning/2025-12-15_cli_logging sandbox/basics/ && git commit -m "Dan 1: Logging fundamentals complete"`
-   [ ] Update `tasks.md` checklist
-   [ ] Zapiši pitanja u `chatlog.md`

---

## 🗓️ DAN 2 (8h) — ARGPARSE CLI

### **08:00-09:00 | Teorija: Argparse**

-   [ ] Pročitaj [L11_cli_sa_argparse](../../scratch/theory/published/L11_cli_sa_argparse_argumenti,_flagovi,_validacija,_exit_kodovi.md)
-   [ ] Razumevanje pozicionih vs opcionih argumenata
-   [ ] Boolean flagovi, choices, nargs
-   [ ] Exit kodovi (0 = uspeh, 1+ = greška)

---

### **09:00-10:30 | FAZA 2.1-2.2: Basic Parser + Opcioni Argumenti**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 2.1](cli_logging_complete_exercises.md#21-osnovni-parser)
-   [ ] Kreiraj `scripts/basic_cli.py`
-   [ ] Implementiraj pozicioni argument (name, age)
-   [ ] Testiraj `--help`
-   [ ] `cli_logging_complete_exercises.md` → [FAZA 2.2](cli_logging_complete_exercises.md#22-opcioni-argumenti-i-default-values)
-   [ ] Kreiraj `scripts/optional_cli.py`
-   [ ] Dodaj `--output`, `--limit` sa default vrednostima

**Checkpoint:**

```bash
python3 scripts/optional_cli.py data/users.csv --output results.txt --limit 5
```

---

### **10:30-10:45 | ☕ PAUZA**

---

### **10:45-12:00 | FAZA 2.3-2.4: Boolean Flagovi + Choices**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 2.3](cli_logging_complete_exercises.md#23-boolean-flagovi-actionstore_true)
-   [ ] Kreiraj `scripts/flags_cli.py`
-   [ ] Implementiraj `--verbose`, `--dry-run`, `--quiet`
-   [ ] Testiraj kombinacije flagova
-   [ ] `cli_logging_complete_exercises.md` → [FAZA 2.4](cli_logging_complete_exercises.md#24-choices--ograničene-opcije)
-   [ ] Kreiraj `scripts/choices_cli.py`
-   [ ] Ograniči format na `["json", "csv", "xml"]`
-   [ ] Testiraj sa nevalidnom opcijom (trebalo bi da dobije error)

---

### **12:00-13:00 | 🍽️ RUČAK**

---

### **13:00-14:30 | FAZA 2.5-2.6: nargs + Subparsers**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 2.5](cli_logging_complete_exercises.md#25-nargs--više-argumenata)
-   [ ] Kreiraj `scripts/nargs_cli.py`
-   [ ] Implementiraj `nargs="+"` za fajlove
-   [ ] `cli_logging_complete_exercises.md` → [FAZA 2.6](cli_logging_complete_exercises.md#26-subparsers--git-style-commands)
-   [ ] Kreiraj `scripts/subcommands_cli.py`
-   [ ] Implementiraj subkomande: `list`, `search`, `export`

**Checkpoint:**

```bash
python3 scripts/subcommands_cli.py list /tmp -r --verbose
python3 scripts/subcommands_cli.py export --format csv -o results.csv
```

---

### **14:30-14:45 | ☕ PAUZA**

---

### **14:45-16:30 | FAZA 2.7: Exit Kodovi**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 2.7](cli_logging_complete_exercises.md#27-exit-kodovi--sysexit)
-   [ ] Kreiraj `scripts/exit_codes.py`
-   [ ] Implementiraj proveru postojanja fajla
-   [ ] Vrati različite exit kodove (0, 1, 2)
-   [ ] Testiraj: `echo "Exit kod: $?"`

---

### **16:30-17:00 | Praksa: file_reporter.py**

-   [ ] Kreiraj `sandbox/basics/file_reporter.py` CLI alat
-   [ ] Argumenti: `path`, `--pattern`, `--min-size`, `--verbose`
-   [ ] Lista fajlova sa filterima
-   [ ] Prikaži ukupan broj i zbirnu veličinu

---

### **17:00-17:30 | Dan 2 Wrap-Up**

-   [ ] Commit: `git commit -m "Dan 2: Argparse CLI complete"`
-   [ ] Update `tasks.md`

---

## 🗓️ DAN 3 (8h) — JSON I CSV

### **08:00-09:00 | Teorija: JSON i CSV**

-   [ ] Pročitaj [L13_json_i_csv](../../scratch/theory/published/L13_json_i_csv_čitanje_pisanje,_validacija,_rad_sa_većim_fajlovima.md)
-   [ ] JSON: `json.load/dump`, `ensure_ascii=False`
-   [ ] CSV: `DictReader/DictWriter`, `newline=""`

---

### **09:00-10:30 | FAZA 3.1-3.2: JSON Osnove**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 3.1](cli_logging_complete_exercises.md#31-json--osnove)
-   [ ] Python REPL: Eksperimentiši sa `json.dumps/loads`
-   [ ] `cli_logging_complete_exercises.md` → [FAZA 3.2](cli_logging_complete_exercises.md#32-json-sa-fajlovima)
-   [ ] Kreiraj `scripts/json_file_ops.py`
-   [ ] Zapiši i učitaj JSON sa `ensure_ascii=False`

---

### **10:30-10:45 | ☕ PAUZA**

---

### **10:45-12:00 | FAZA 3.3: JSON Error Handling**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 3.3](cli_logging_complete_exercises.md#33-json-error-handling)
-   [ ] Kreiraj `scripts/json_errors.py`
-   [ ] Testiraj sa nevalidnim JSON-om
-   [ ] Implementiraj `try/except JSONDecodeError`
-   [ ] Prikaži liniju i kolonu greške

---

### **12:00-13:00 | 🍽️ RUČAK**

---

### **13:00-14:30 | FAZA 3.4-3.5: CSV Osnove + DictReader/Writer**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 3.4](cli_logging_complete_exercises.md#34-csv--osnove-csvreaderwriter)
-   [ ] Kreiraj `scripts/csv_basic.py`
-   [ ] Koristi `csv.reader/writer` (lista redova)
-   [ ] `cli_logging_complete_exercises.md` → [FAZA 3.5](cli_logging_complete_exercises.md#35-csv-dictreaderwriter--bolja-opcija)
-   [ ] Kreiraj `scripts/csv_dict.py`
-   [ ] Refaktoriši sa `DictReader/DictWriter` (dict redova)

**Checkpoint:**

-   Razumeš razliku između `reader` (lista) i `DictReader` (dict)

---

### **14:30-14:45 | ☕ PAUZA**

---

### **14:45-16:30 | FAZA 3.6-3.7: CSV ↔ JSON Konverzija**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 3.6](cli_logging_complete_exercises.md#36-csv--json-konverzija)
-   [ ] Kreiraj `scripts/csv_to_json.py`
-   [ ] Konvertuj `data/users.csv` → `data/users_from_csv.json`
-   [ ] `cli_logging_complete_exercises.md` → [FAZA 3.7](cli_logging_complete_exercises.md#37-json--csv-konverzija)
-   [ ] Kreiraj `scripts/json_to_csv.py`
-   [ ] Konvertuj nazad → `data/users_from_json.csv`

**Checkpoint:**

```bash
cat data/users_from_csv.json
cat data/users_from_json.csv
```

---

### **16:30-17:00 | Praksa: Validacija**

-   [ ] Dodaj validaciju u `csv_to_json.py` (obavezne kolone)
-   [ ] Dodaj validaciju u `json_to_csv.py` (proveri da je lista)
-   [ ] Testiraj sa nevalidnim podacima

---

### **17:00-17:30 | Dan 3 Wrap-Up**

-   [ ] Commit: `git commit -m "Dan 3: JSON i CSV complete"`
-   [ ] Update `tasks.md`

---

## 🗓️ DAN 4 (8h) — INTEGRISANI PROJEKAT

### **08:00-10:30 | FAZA 4.1: data_converter.py (Deo 1)**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 4.1](cli_logging_complete_exercises.md#41-cli-alat-sa-logging-i-jsoncsv)
-   [ ] Kreiraj `scripts/data_converter.py`
-   [ ] Implementiraj `setup_logging()` funkciju (console + rotating file)
-   [ ] Implementiraj `csv_to_json()` funkciju
-   [ ] Dodaj argparse subparsers za `csv2json` i `json2csv`

---

### **10:30-10:45 | ☕ PAUZA**

---

### **10:45-12:00 | FAZA 4.1: data_converter.py (Deo 2)**

-   [ ] Implementiraj `json_to_csv()` funkciju
-   [ ] Dodaj error handling (`try/except`)
-   [ ] Dodaj `--log-level` opciju (DEBUG/INFO/WARNING/ERROR)
-   [ ] Testiraj:
    ```bash
    python3 scripts/data_converter.py csv2json data/users.csv data/test.json
    python3 scripts/data_converter.py json2csv data/test.json data/test.csv --log-level DEBUG
    ```

**Checkpoint:**

-   Funkcionalan CLI alat sa svim konceptima (argparse + logging + JSON/CSV)

---

### **12:00-13:00 | 🍽️ RUČAK**

---

### **13:00-14:30 | FAZA 4.2: Filtriranje**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 4.2](cli_logging_complete_exercises.md#42-dodaj-validaciju-i-filtriranje)
-   [ ] Dodaj `filter_csv()` funkciju
-   [ ] Implementiraj `--min-age` filter
-   [ ] Dodaj `filter` subcommand
-   [ ] Testiraj: `python3 scripts/data_converter.py filter data/users.csv data/filtered.csv --min-age 30`

---

### **14:30-14:45 | ☕ PAUZA**

---

### **14:45-17:00 | Refaktorisanje scraper.py**

-   [ ] Otvori `projects/01-web-scraper/scraper.py`
-   [ ] Dodaj argparse:
    -   `--url` (URL za scraping)
    -   `--output` (Output fajl)
    -   `--format` (json/csv)
    -   `--log-level` (DEBUG/INFO/WARNING)
-   [ ] Integriši logging (console + rotating file u `logs/`)
-   [ ] Dodaj JSON/CSV output
-   [ ] Testiraj sa različitim argumentima

**Checkpoint:**

```bash
cd ~/code/python-automation-lab/python-automation-portfolio/projects/01-web-scraper
python3 scraper.py --url "https://quotes.toscrape.com" --output quotes.json --format json --log-level INFO
cat logs/scraper.log
```

---

### **17:00-17:30 | Dan 4 Wrap-Up**

-   [ ] Commit: `git commit -m "Dan 4: Integrisani projekat + scraper refaktoring"`
-   [ ] Update `tasks.md`

---

## 🗓️ DAN 5 (8h) — PYTEST TESTIRANJE

### **08:00-09:00 | Teorija: Pytest**

-   [ ] Pročitaj [L14_pytest_osnove](../../scratch/theory/published/L14_pytest_osnove_struktura_testova,_fixture,_parametrize,_caplog.md)
-   [ ] Instalacija: `pip install pytest`
-   [ ] Osnovna struktura testa
-   [ ] Fixtures: `tmp_path`, `caplog`

---

### **09:00-10:30 | FAZA 5.1-5.2: JSON Testovi**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 5.1-5.2](cli_logging_complete_exercises.md#51-instalacija-pytest)
-   [ ] Kreiraj `tests/test_json_ops.py`
-   [ ] Implementiraj `test_load_json_valid()` sa `tmp_path`
-   [ ] Implementiraj `test_load_json_invalid()` sa `pytest.raises`
-   [ ] Pokreni: `pytest tests/test_json_ops.py -v`

---

### **10:30-10:45 | ☕ PAUZA**

---

### **10:45-12:00 | FAZA 5.3: CLI Parsing Testovi**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 5.3](cli_logging_complete_exercises.md#53-testiranje-cli-argumenta)
-   [ ] Kreiraj `tests/test_cli_parsing.py`
-   [ ] Testiraj default vrednosti
-   [ ] Testiraj custom vrednosti
-   [ ] Testiraj nevalidne choices
-   [ ] Pokreni: `pytest tests/test_cli_parsing.py -v`

---

### **12:00-13:00 | 🍽️ RUČAK**

---

### **13:00-14:30 | FAZA 5.4: Logging Testovi sa caplog**

-   [ ] `cli_logging_complete_exercises.md` → [FAZA 5.4](cli_logging_complete_exercises.md#54-testiranje-logging-a-caplog-fixture)
-   [ ] Kreiraj `tests/test_logging.py`
-   [ ] Implementiraj `test_logging_info()` sa `caplog`
-   [ ] Implementiraj `test_logging_warnings()`
-   [ ] Implementiraj `test_logging_debug()`
-   [ ] Pokreni: `pytest tests/test_logging.py -v`

---

### **14:30-14:45 | ☕ PAUZA**

---

### **14:45-17:00 | Testovi za scraper.py**

-   [ ] Kreiraj `projects/01-web-scraper/tests/test_scraper.py`
-   [ ] Testiraj argparse parsing
-   [ ] Testiraj logging sa `caplog`
-   [ ] Testiraj JSON/CSV output sa `tmp_path`
-   [ ] Pokreni: `cd projects/01-web-scraper && pytest tests/ -v`

---

### **17:00-17:30 | Dan 5 Wrap-Up**

-   [ ] Commit: `git commit -m "Dan 5: Pytest testovi complete"`
-   [ ] Update `tasks.md`

---

## 🗓️ DAN 6 (8h) — BONUS + PRAKSA

### **08:00-09:00 | BONUS FAZA: Pathlib Osnove**

-   [ ] `cli_logging_complete_exercises.md` → [BONUS FAZA](cli_logging_complete_exercises.md#-bonus-faza-pathlib-30-45-min)
-   [ ] Path objekti umesto stringova
-   [ ] `Path.cwd()`, `Path.home()`, `Path() / "folder" / "file"`
-   [ ] `.exists()`, `.is_file()`, `.is_dir()`
-   [ ] `.name`, `.stem`, `.suffix`, `.parent`

---

### **09:00-10:30 | Pathlib Glob Patterns**

-   [ ] `.glob("*.csv")` — svi CSV u folderu
-   [ ] `.rglob("*.json")` — rekurzivna pretraga
-   [ ] `.iterdir()` — lista sadržaja
-   [ ] Kreiraj `utils/file_utils.py` sa helper funkcijama:
    -   `find_files(pattern: str, root: Path) -> list[Path]`
    -   `get_file_info(path: Path) -> dict`

---

### **10:30-10:45 | ☕ PAUZA**

---

### **10:45-12:00 | Kreiranje Utility Modula**

-   [ ] Kreiraj `utils/logging_utils.py`
    -   `setup_logger(name, level, log_dir)` — reusable logging setup
-   [ ] Kreiraj `utils/file_utils.py`
    -   Path helperi, glob functions
-   [ ] Kreiraj `utils/data_utils.py`
    -   `load_json(path)`, `save_json(data, path)`
    -   `load_csv(path)`, `save_csv(data, path)`
    -   `csv_to_json_convert(input, output)`
    -   `json_to_csv_convert(input, output)`

---

### **12:00-13:00 | 🍽️ RUČAK**

---

### **13:00-17:00 | REPL Slobodna Praksa**

-   [ ] Vrati se na vežbe koje su ti bile nejasne
-   [ ] Re-implementiraj neke skripte bez gledanja u vežbe
-   [ ] Eksperimentiši sa kombinacijama (CLI + Logging + JSON)
-   [ ] Dodaj features u `data_converter.py` (npr. `--verbose` flag koji prikazuje svaki red)
-   [ ] Kreiraj novi CLI alat po svom izboru

**Ideje za praksu:**

-   `file_analyzer.py` — analizira fajlove u folderu (broj, veličina, tipovi)
-   `json_merge.py` — spaja više JSON fajlova
-   `csv_validator.py` — validira CSV strukturu
-   `log_analyzer.py` — parsira log fajlove i prikazuje statistiku

---

### **17:00-17:30 | Dan 6 & Finalni Wrap-Up**

-   [ ] Commit: `git commit -m "Dan 6: Pathlib + utility modules + slobodna praksa"`
-   [ ] Update `tasks.md` — označi sve kao završeno ✅
-   [ ] Popuni `summary.md` — šta si naučio, šta ti je bilo teško, šta sledeće
-   [ ] Update `chatlog.md` — finalna pitanja ili beleške

---

## ✅ CHECKLIST — Da Li Si Završio?

### Dan 1: Logging

-   [ ] Razumeš nivoe logovanja (DEBUG, INFO, WARNING, ERROR, CRITICAL)
-   [ ] Konfigurišeš logging u konzolu + fajl
-   [ ] Izbegavaš duplicate handlere
-   [ ] Koristiš RotatingFileHandler

### Dan 2: Argparse

-   [ ] Kreiraš CLI sa pozicionim i opcionim argumentima
-   [ ] Koristiš boolean flagove i choices
-   [ ] Implementiraš subparsers
-   [ ] Vraćaš exit kodove

### Dan 3: JSON/CSV

-   [ ] Čitaš/pišeš JSON sa `ensure_ascii=False`
-   [ ] Koristiš `DictReader/DictWriter`
-   [ ] Konvertuješ CSV↔JSON
-   [ ] Validiraš podatke

### Dan 4: Integrisani Projekat

-   [ ] Kreirao `data_converter.py` CLI alat
-   [ ] Refaktoriše `scraper.py` sa CLI + logging

### Dan 5: Pytest

-   [ ] Pišeš testove sa fixtures
-   [ ] Testiš CLI parsing
-   [ ] Testiš logging sa `caplog`

### Dan 6: Bonus

-   [ ] Koristiš Path objekte i glob patterns
-   [ ] Kreiraš reusable utility module

---

## 🎯 SLEDEĆI KORACI (Nakon 6 Dana)

1. **Pređi na Dan 6-7:** HTTP requests + BeautifulSoup4 (web scraping)
2. **Finalizuj `projects/01-web-scraper/`** sa svim featuresima
3. **Kreiraj novi projekat:** CSV processor, log analyzer, ili API wrapper

---

**SREĆNO!** 🚀
Ovaj plan je ambiciozan ali strukturiran. Radi u svom tempu i ne preskači korake!
