---
type: tasks
topic: CLI + Logging + JSON/CSV — Task Checklist
date: 2025-12-15
linked_to: 2025-12-15_cli_logging
language: bilingual
status: active
---

# ✅ CLI + Logging + JSON/CSV — Task Checklist

**Napomena:** Označi `[x]` kada završiš zadatak. Commit progress svaki dan!

---

## 🔧 PRIPREMA (Pre Početka)

-   [x] Pročitao `README.md` — razumeo pregled modula
-   [x] Pročitao `START_GUIDE.md` — razumeo 48h plan
-   [x] Pročitao `kickoff.md` — razumeo hourly schedule
-   [x] Setup practice environment:
    ```bash
    cd ~/code/python-automation-lab/python-automation-portfolio/sandbox/basics
    mkdir -p cli_logging_practice/{scripts,data,logs,tests}
    ```
-   [ ] Kreirao test podatke (`data/users.csv`, `data/config.json`)
-   [ ] Provera: `ls -lh sandbox/basics/cli_logging_practice/data/`

---

## 📚 DAN 1: LOGGING FUNDAMENTALS

### Teorija

-   [x] Pročitao [L08_logging_osnove](../../scratch/theory/published/L08_logging_osnove_logger_handler_formatter,_nivoi,_izbegavanje_duplih_handlera.md)
-   [x] Razumeo hijerarhiju: Logger → Handler → Formatter
-   [x] Razumeo nivoe: DEBUG (10), INFO (20), WARNING (30), ERROR (40), CRITICAL (50)

---

### FAZA 1.1-1.2: BasicConfig + Custom Format

-   [ ] Otvorio Python REPL
-   [ ] Testirao `logging.basicConfig()` sa različitim nivoima
-   [ ] Kreirao custom format sa `%(asctime)s`, `%(levelname)s`, `%(name)s`
-   [ ] Razumeo format stringove

---

### FAZA 1.3: Logovanje u Fajl + Console

-   [ ] Kreirao `scripts/log_to_file.py`
-   [ ] Implementirao StreamHandler (console, nivo INFO+)
-   [ ] Implementirao FileHandler (fajl, nivo DEBUG+)
-   [ ] Testirao: `python3 scripts/log_to_file.py`
-   [ ] Provera: `cat logs/app.log` — vidiš DEBUG logove

---

### FAZA 1.4-1.5: Duplicate Handlers + Propagation

-   [ ] Kreirao `scripts/duplicate_problem.py` — video problem duplikata
-   [ ] Kreirao fixed verziju sa `if not logger.handlers:`
-   [ ] Eksperimentisao sa parent/child logger-ima
-   [ ] Testirao `logger.propagate = False`

---

### FAZA 1.6: RotatingFileHandler

-   [ ] Kreirao `scripts/rotating_log.py`
-   [ ] Postavio `maxBytes=1_000` (1KB)
-   [ ] Generisao 100+ logova
-   [ ] Provera: `ls -lh logs/` — vidiš rotating.log, rotating.log.1, rotating.log.2, rotating.log.3

---

### Praksa

-   [ ] Kreirao `sandbox/basics/my_logger.py`
-   [ ] Implementirao `setup_logger(name, level, log_dir)` funkciju
-   [ ] Testirao import u drugim skriptama

---

### Dan 1 Wrap-Up

-   [ ] Commit: `git commit -m "Dan 1: Logging fundamentals complete"`
-   [ ] Update ovaj fajl (`tasks.md`)
-   [ ] Zapisao pitanja u `chatlog.md`

---

## 🖥️ DAN 2: ARGPARSE CLI

### Teorija

-   [ ] Pročitao [L11_cli_sa_argparse](../../scratch/theory/published/L11_cli_sa_argparse_argumenti,_flagovi,_validacija,_exit_kodovi.md)
-   [ ] Razumeo pozicione vs opcione argumente
-   [ ] Razumeo boolean flagove, choices, nargs
-   [ ] Razumeo exit kodove (0 = uspeh, 1+ = greška)

### FAZA 2.1-2.2: Basic Parser + Opcioni Argumenti

-   [ ] Kreirao `scripts/basic_cli.py`
-   [ ] Implementirao pozicione argumente (name, age)
-   [ ] Testirao `--help`
-   [ ] Kreirao `scripts/optional_cli.py`
-   [ ] Dodao `--output`, `--limit` sa default-ima
-   [ ] Testirao sa različitim kombinacijama

### FAZA 2.3-2.4: Boolean Flagovi + Choices

-   [ ] Kreirao `scripts/flags_cli.py`
-   [ ] Implementirao `--verbose`, `--dry-run`, `--quiet`
-   [ ] Testirao kombinacije flagova
-   [ ] Kreirao `scripts/choices_cli.py`
-   [ ] Ograničio format na `["json", "csv", "xml"]`
-   [ ] Testirao sa nevalidnom opcijom (dobio error)

### FAZA 2.5-2.6: nargs + Subparsers

-   [ ] Kreirao `scripts/nargs_cli.py`
-   [ ] Implementirao `nargs="+"` za fajlove
-   [ ] Kreirao `scripts/subcommands_cli.py`
-   [ ] Implementirao subkomande: `list`, `search`, `export`
-   [ ] Testirao svaku subkomandu sa `--help`

### FAZA 2.7: Exit Kodovi

-   [ ] Kreirao `scripts/exit_codes.py`
-   [ ] Implementirao proveru postojanja fajla
-   [ ] Vratio različite exit kodove (0, 1, 2)
-   [ ] Testirao: `echo "Exit kod: $?"`

### Praksa

-   [ ] Kreirao `sandbox/basics/file_reporter.py` CLI alat
-   [ ] Implementirao `path`, `--pattern`, `--min-size`, `--verbose`
-   [ ] Testirao sa različitim filterima

### Dan 2 Wrap-Up

-   [ ] Commit: `git commit -m "Dan 2: Argparse CLI complete"`
-   [ ] Update ovaj fajl (`tasks.md`)

---

## 📄 DAN 3: JSON I CSV

### Teorija

-   [ ] Pročitao [L13_json_i_csv](../../scratch/theory/published/L13_json_i_csv_čitanje_pisanje,_validacija,_rad_sa_većim_fajlovima.md)
-   [ ] Razumeo `json.load/dump`, `ensure_ascii=False`
-   [ ] Razumeo `DictReader/DictWriter`, `newline=""`

### FAZA 3.1-3.2: JSON Osnove

-   [ ] Python REPL: Eksperimentisao sa `json.dumps/loads`
-   [ ] Testirao `ensure_ascii=False` sa srpskim znakovima
-   [ ] Kreirao `scripts/json_file_ops.py`
-   [ ] Zapisao i učitao JSON sa `ensure_ascii=False, indent=2`

### FAZA 3.3: JSON Error Handling

-   [ ] Kreirao `scripts/json_errors.py`
-   [ ] Testirao sa nevalidnim JSON-om (dobio `JSONDecodeError`)
-   [ ] Implementirao `try/except JSONDecodeError`
-   [ ] Prikazao liniju i kolonu greške

### FAZA 3.4-3.5: CSV Osnove + DictReader/Writer

-   [ ] Kreirao `scripts/csv_basic.py`
-   [ ] Koristio `csv.reader/writer` (lista redova)
-   [ ] Kreirao `scripts/csv_dict.py`
-   [ ] Refaktorisao sa `DictReader/DictWriter` (dict redova)
-   [ ] Razumeo zašto je `DictReader` čitljiviji

### FAZA 3.6-3.7: CSV ↔ JSON Konverzija

-   [ ] Kreirao `scripts/csv_to_json.py`
-   [ ] Konvertovao `data/users.csv` → `data/users_from_csv.json`
-   [ ] Provera: `cat data/users_from_csv.json`
-   [ ] Kreirao `scripts/json_to_csv.py`
-   [ ] Konvertovao nazad → `data/users_from_json.csv`
-   [ ] Provera: `cat data/users_from_json.csv`

### Praksa: Validacija

-   [ ] Dodao validaciju u `csv_to_json.py` (obavezne kolone)
-   [ ] Dodao validaciju u `json_to_csv.py` (proveri da je lista)
-   [ ] Testirao sa nevalidnim podacima

### Dan 3 Wrap-Up

-   [ ] Commit: `git commit -m "Dan 3: JSON i CSV complete"`
-   [ ] Update ovaj fajl (`tasks.md`)

---

## 🔧 DAN 4: INTEGRISANI PROJEKAT

### FAZA 4.1: data_converter.py (Deo 1)

-   [ ] Kreirao `scripts/data_converter.py`
-   [ ] Implementirao `setup_logging()` (console + rotating file)
-   [ ] Implementirao `csv_to_json()` funkciju
-   [ ] Dodao argparse subparsers za `csv2json` i `json2csv`

### FAZA 4.1: data_converter.py (Deo 2)

-   [ ] Implementirao `json_to_csv()` funkciju
-   [ ] Dodao error handling (`try/except`)
-   [ ] Dodao `--log-level` opciju (DEBUG/INFO/WARNING/ERROR)
-   [ ] Testirao:
    ```bash
    python3 scripts/data_converter.py csv2json data/users.csv data/test.json
    python3 scripts/data_converter.py json2csv data/test.json data/test.csv --log-level DEBUG
    ```
-   [ ] Provera: `cat logs/converter.log` — vidiš sve operacije

### FAZA 4.2: Filtriranje

-   [ ] Dodao `filter_csv()` funkciju
-   [ ] Implementirao `--min-age` filter
-   [ ] Dodao `filter` subcommand
-   [ ] Testirao: `python3 scripts/data_converter.py filter data/users.csv data/filtered.csv --min-age 30`
-   [ ] Provera: `cat data/filtered.csv` — samo redovi sa age >= 30

### Refaktorisanje scraper.py

-   [ ] Otvorio `projects/01-web-scraper/scraper.py`
-   [ ] Dodao argparse:
    -   [ ] `--url` (URL za scraping)
    -   [ ] `--output` (Output fajl)
    -   [ ] `--format` (json/csv)
    -   [ ] `--log-level` (DEBUG/INFO/WARNING)
-   [ ] Integriso logging (console + rotating file u `logs/`)
-   [ ] Dodao JSON/CSV output opcije
-   [ ] Testirao:
    ```bash
    cd ~/code/python-automation-lab/python-automation-portfolio/projects/01-web-scraper
    python3 scraper.py --url "https://quotes.toscrape.com" --output quotes.json --format json --log-level INFO
    ```
-   [ ] Provera: `cat logs/scraper.log`

### Dan 4 Wrap-Up

-   [ ] Commit: `git commit -m "Dan 4: Integrisani projekat + scraper refaktoring"`
-   [ ] Update ovaj fajl (`tasks.md`)

---

## 🧪 DAN 5: PYTEST TESTIRANJE

### Teorija

-   [ ] Pročitao [L14_pytest_osnove](../../scratch/theory/published/L14_pytest_osnove_struktura_testova,_fixture,_parametrize,_caplog.md)
-   [ ] Instalirao pytest: `pip install pytest`
-   [ ] Razumeo osnovnu strukturu testa
-   [ ] Razumeo fixtures: `tmp_path`, `caplog`

### FAZA 5.1-5.2: JSON Testovi

-   [ ] Kreirao `tests/test_json_ops.py`
-   [ ] Implementirao `test_load_json_valid()` sa `tmp_path`
-   [ ] Implementirao `test_load_json_invalid()` sa `pytest.raises`
-   [ ] Implementirao `test_save_json()` sa `tmp_path`
-   [ ] Pokrenuo: `pytest tests/test_json_ops.py -v`
-   [ ] Svi testovi prolaze ✅

### FAZA 5.3: CLI Parsing Testovi

-   [ ] Kreirao `tests/test_cli_parsing.py`
-   [ ] Testirao default vrednosti
-   [ ] Testirao custom vrednosti
-   [ ] Testirao nevalidne choices sa `pytest.raises(SystemExit)`
-   [ ] Pokrenuo: `pytest tests/test_cli_parsing.py -v`

### FAZA 5.4: Logging Testovi sa caplog

-   [ ] Kreirao `tests/test_logging.py`
-   [ ] Implementirao `test_logging_info()` sa `caplog`
-   [ ] Implementirao `test_logging_warnings()`
-   [ ] Implementirao `test_logging_debug()`
-   [ ] Pokrenuo: `pytest tests/test_logging.py -v`

### Testovi za scraper.py

-   [ ] Kreirao `projects/01-web-scraper/tests/test_scraper.py`
-   [ ] Testirao argparse parsing
-   [ ] Testirao logging sa `caplog`
-   [ ] Testirao JSON/CSV output sa `tmp_path`
-   [ ] Pokrenuo: `cd projects/01-web-scraper && pytest tests/ -v`

### Dan 5 Wrap-Up

-   [ ] Commit: `git commit -m "Dan 5: Pytest testovi complete"`
-   [ ] Update ovaj fajl (`tasks.md`)

---

## 🎁 DAN 6: BONUS + PRAKSA

### BONUS FAZA: Pathlib Osnove

-   [ ] Path objekti umesto stringova
-   [ ] `Path.cwd()`, `Path.home()`, `Path() / "folder" / "file"`
-   [ ] `.exists()`, `.is_file()`, `.is_dir()`
-   [ ] `.name`, `.stem`, `.suffix`, `.parent`, `.absolute()`

### Pathlib Glob Patterns

-   [ ] `.glob("*.csv")` — svi CSV u folderu
-   [ ] `.rglob("*.json")` — rekurzivna pretraga
-   [ ] `.iterdir()` — lista sadržaja
-   [ ] Kreirao `utils/file_utils.py` sa helper funkcijama

### Kreiranje Utility Modula

-   [ ] Kreirao `utils/logging_utils.py`:
    -   [ ] `setup_logger(name, level, log_dir)` funkcija
-   [ ] Kreirao `utils/file_utils.py`:
    -   [ ] `find_files(pattern, root)` funkcija
    -   [ ] `get_file_info(path)` funkcija
-   [ ] Kreirao `utils/data_utils.py`:
    -   [ ] `load_json(path)`, `save_json(data, path)`
    -   [ ] `load_csv(path)`, `save_csv(data, path)`
    -   [ ] `csv_to_json_convert(input, output)`
    -   [ ] `json_to_csv_convert(input, output)`

### REPL Slobodna Praksa

-   [ ] Vratio se na vežbe koje su mi bile nejasne
-   [ ] Re-implementirao neke skripte bez gledanja u vežbe
-   [ ] Eksperimentisao sa kombinacijama (CLI + Logging + JSON)
-   [ ] Dodao features u `data_converter.py`
-   [ ] (Bonus) Kreirao novi CLI alat po svom izboru

### Dan 6 Wrap-Up

-   [ ] Commit: `git commit -m "Dan 6: Pathlib + utility modules + slobodna praksa"`
-   [ ] Update ovaj fajl (`tasks.md`)
-   [ ] Popunio `summary.md` — šta sam naučio, šta mi je bilo teško
-   [ ] Update `chatlog.md` — finalna pitanja

---

## ✅ FINALNI CHECKLIST — Da Li Si Završio?

### Logging

-   [ ] Razumem nivoe logovanja (DEBUG, INFO, WARNING, ERROR, CRITICAL)
-   [ ] Konfigurišem logging u konzolu + fajl
-   [ ] Izbegavam duplicate handlere sa `if not logger.handlers:`
-   [ ] Koristim RotatingFileHandler za production

### Argparse CLI

-   [ ] Kreiram CLI sa pozicionim i opcionim argumentima
-   [ ] Koristim boolean flagove (`action="store_true"`)
-   [ ] Koristim choices za ograničene opcije
-   [ ] Prihvatam više argumenata sa `nargs`
-   [ ] Implementiram subparsers (git-style komande)
-   [ ] Vraćam exit kodove (0 = uspeh, 1+ = greška)
-   [ ] Auto-generišem `--help`

### JSON/CSV

-   [ ] Čitam/pišem JSON sa `json.load/dump`
-   [ ] Koristim `ensure_ascii=False` za Unicode
-   [ ] Handlujem `JSONDecodeError`
-   [ ] Čitam/pišem CSV sa `DictReader/DictWriter`
-   [ ] Koristim `newline=""` sa csv modulom
-   [ ] Konvertujem CSV↔JSON
-   [ ] Validišem strukturu podataka

### Pytest

-   [ ] Pišem unit testove sa fixtures
-   [ ] Koristim `tmp_path` za test fajlove
-   [ ] Testiram CLI parsing
-   [ ] Testiram logging sa `caplog`
-   [ ] Koristim `pytest.raises` za error testove

### Pathlib (Bonus)

-   [ ] Razumem Path objekte umesto stringova
-   [ ] Koristim glob patterns za pretragu fajlova
-   [ ] Kreiram/brišem foldere sa `mkdir/rmdir`

### Integrisani Projekat

-   [ ] Kreirao `data_converter.py` CLI alat (CLI + Logging + JSON/CSV)
-   [ ] Refaktoriše `projects/01-web-scraper/scraper.py` sa svim konceptima
-   [ ] Kreirao reusable utility module

---

## 🎯 SLEDEĆI KORACI

-   [ ] Pređi na Dan 6-7: HTTP requests + BeautifulSoup4
-   [ ] Finaliziraj `projects/01-web-scraper/` sa svim featuresima
-   [ ] Kreiraj novi projekat (CSV processor, log analyzer, API wrapper)

---

**STATUS:** 🚧 U toku / ✅ Završeno
**Poslednji update:** _[datum]_
