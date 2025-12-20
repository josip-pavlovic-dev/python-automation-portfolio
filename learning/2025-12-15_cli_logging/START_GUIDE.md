---
type: guide
topic: CLI + Logging + JSON/CSV — 48h Learning Plan
date: 2025-12-15
linked_to: 2025-12-15_cli_logging
language: bilingual
status: active
difficulty: beginner
estimated_time: 48 hours (6 days × 8h)
---

# 🚀 START GUIDE – 2025-12-15 CLI + Logging + JSON/CSV

## 📋 Pregled

**Cilj:** Savladaj argparse (CLI), logging sistem, JSON/CSV obradu
**Trajanje:** 48 sati (6 dana po 8h)
**Prerekviziti:** Terminal osnove (Dan 1-2), Python osnove, git osnove

---

## 🗓️ 48-Satni Plan

### **DAN 1 (8h) — Logging Fundamentals**

#### Jutro (4h)

-   [ ] 08:00-10:00: Pročitaj [L08_logging_osnove](../../scratch/theory/published/L08_logging_osnove_logger_handler_formatter,_nivoi,_izbegavanje_duplih_handlera.md)
-   [ ] 10:00-12:00: [FAZA 1.1-1.3](cli_logging_complete_exercises.md#faza-1-logging-osnove-60-90-min) (BasicConfig, Custom Format, FileHandler)

---

#### Popodne (4h)

-   [ ] 13:00-15:00: [FAZA 1.4-1.6](cli_logging_complete_exercises.md#14-izbegavanje-duplikata-handlera) (Duplicate handlers, Propagation, RotatingFileHandler)
-   [ ] 15:00-17:00: Kreiraj `sandbox/basics/my_logger.py` sa reusable `setup_logger()` funkcijom

---

**Dan 1 Output:**

-   Razumeš nivoe logovanja (DEBUG, INFO, WARNING, ERROR, CRITICAL)
-   Konfigurišeš logging u konzolu + fajl istovremeno
-   Izbegavaš duplicate handlere
-   Koristiš RotatingFileHandler

---

### **DAN 2 (8h) — Argparse CLI**

#### Jutro (4h)

-   [ ] 08:00-09:00: Pročitaj [L11_cli_sa_argparse](../../scratch/theory/published/L11_cli_sa_argparse_argumenti,_flagovi,_validacija,_exit_kodovi.md)
-   [ ] 09:00-12:00: [FAZA 2.1-2.4](cli_logging_complete_exercises.md#faza-2-argparse--cli-argumenti-60-90-min) (Basic parser, Optional args, Boolean flags, Choices)

---

#### Popodne (4h)

-   [ ] 13:00-15:00: [FAZA 2.5-2.7](cli_logging_complete_exercises.md#25-nargs--više-argumenata) (nargs, Subparsers, Exit codes)
-   [ ] 15:00-17:00: Kreiraj `sandbox/basics/file_reporter.py` CLI alat koji lista fajlove sa filterima

---

**Dan 2 Output:**

-   Kreiraš CLI sa pozicionim i opcionim argumentima
-   Koristiš boolean flagove i choices
-   Razumeš subparsers (git-style komande)
-   Vraćaš exit kodove (0/1)

---

### **DAN 3 (8h) — JSON i CSV**

#### Jutro (4h)

-   [ ] 08:00-09:00: Pročitaj [L13_json_i_csv](../../scratch/theory/published/L13_json_i_csv_čitanje_pisanje,_validacija,_rad_sa_većim_fajlovima.md)
-   [ ] 09:00-12:00: [FAZA 3.1-3.3](cli_logging_complete_exercises.md#faza-3-json-i-csv-60-90-min) (JSON osnove, File operations, Error handling)

---

#### Popodne (4h)

-   [ ] 13:00-15:00: [FAZA 3.4-3.5](cli_logging_complete_exercises.md#34-csv--osnove-csvreaderwriter) (CSV osnove, DictReader/DictWriter)
-   [ ] 15:00-17:00: [FAZA 3.6-3.7](cli_logging_complete_exercises.md#36-csv--json-konverzija) (CSV↔JSON konverzije)

---

**Dan 3 Output:**

-   Čitaš/pišeš JSON sa `json.load/dump`
-   Koristiš `ensure_ascii=False` za Unicode
-   Čitaš/pišeš CSV sa `DictReader/DictWriter`
-   Konvertuješ CSV↔JSON

---

### **DAN 4 (8h) — Integrisani Projekat**

#### Jutro (4h)

-   [ ] 08:00-12:00: [FAZA 4.1](cli_logging_complete_exercises.md#faza-4-integrisani-projekat-90-120-min) — Implementiraj `data_converter.py` (CLI + Logging + JSON/CSV)

#### Popodne (4h)

-   [ ] 13:00-15:00: [FAZA 4.2](cli_logging_complete_exercises.md#42-dodaj-validaciju-i-filtriranje) — Dodaj filtriranje po uslovima
-   [ ] 15:00-17:00: Refaktoriši `projects/01-web-scraper/scraper.py`:
    -   Dodaj argparse (`--url`, `--output`, `--log-level`)
    -   Integriši logging (console + file)
    -   Dodaj JSON/CSV output format

**Dan 4 Output:**

-   Funkcionalan CLI alat sa svim konceptima
-   Web scraper sa CLI + logging

---

### **DAN 5 (8h) — Pytest Testiranje**

#### Jutro (4h)

-   [ ] 08:00-10:00: Instalacija pytest, pročitaj [L14_pytest_osnove](../../scratch/theory/published/L14_pytest_osnove_struktura_testova,_fixture,_parametrize,_caplog.md)
-   [ ] 10:00-12:00: [FAZA 5.1-5.2](cli_logging_complete_exercises.md#faza-5-pytest--testiranje-60-min) (JSON testovi)

#### Popodne (4h)

-   [ ] 13:00-15:00: [FAZA 5.3-5.4](cli_logging_complete_exercises.md#53-testiranje-cli-argumenta) (CLI parsing testovi, Logging testovi sa caplog)
-   [ ] 15:00-17:00: Napiši testove za `projects/01-web-scraper/tests/`

**Dan 5 Output:**

-   Pišeš pytest testove sa fixtures
-   Testiš CLI parsing
-   Testiš logging sa `caplog`

---

### **DAN 6 (8h) — Bonus + Praksa**

#### Jutro (4h)

-   [ ] 08:00-10:00: [BONUS FAZA](cli_logging_complete_exercises.md#-bonus-faza-pathlib-30-45-min) — Pathlib (Path objekti, glob patterns)
-   [ ] 10:00-12:00: Kreiraj `utils/file_utils.py` sa pathlib helper funkcijama

---

#### Popodne (4h)

-   [ ] 13:00-17:00: **REPL Slobodna Praksa** — Vrati se na vežbe koje su ti bile nejasne i ponovi ih dok ne budu jasne
-   [ ] 17:00-18:00: Napiši kratki rezime naučenog u `summary.md`

---

**Dan 6 Output:**

-   Razumeš Path objekte
-   Koristiš glob za pretragu fajlova
-   Consolidiraš svo naučeno kroz praksu

---

## 📂 Potrebni Fajlovi

```
learning/2025-12-15_cli_logging/
├── README.md                          # Pregled
├── START_GUIDE.md                     # Ovaj fajl
├── kickoff.md                         # Detaljni dnevni plan
├── cheatsheet.md                      # Brzi referentni vodič
├── cli_logging_complete_exercises.md  # 2000+ linija vežbi
├── tasks.md                           # Checklist
├── chatlog.md                         # Q&A
└── summary.md                         # Beleške nakon završetka

scratch/theory/published/
├── L08_logging_osnove_logger_handler_formatter,_nivoi,_izbegavanje_duplih_handlera.md
├── L11_cli_sa_argparse_argumenti,_flagovi,_validacija,_exit_kodovi.md
└── L13_json_i_csv_čitanje_pisanje,_validacija,_rad_sa_većim_fajlovima.md
```

---

## 🎯 Kako Koristiti Materijale

### 1. **Teorija PRE Vežbi**

Prvo pročitaj teorijske fajlove (L08, L11, L13) da razumeš koncepte, ONDA radi REPL vežbe.

---

### 2. **REPL Vežbe — Copy-Paste Ready**

Sve vežbe u `cli_logging_complete_exercises.md` su kopija-pasta spremne. Otvori Python REPL ili kreiraj fajlove i testuj.

---

### 3. **Incremental Learning**

Radi po fazama (1.1 → 1.2 → 1.3...). Ne preskači korake!

---

### 4. **Beleži Pitanja**

U `chatlog.md` zapisuj pitanja koja imaš tokom učenja.

---

### 5. **Dnevni Commit**

Na kraju svakog dana commituj napredak:

```bash
cd ~/code/python-automation-lab/python-automation-portfolio
git add learning/2025-12-15_cli_logging
git commit -m "Dan X: Završio logging/argparse/JSON vežbe"
```

---

## ✅ Pre Početka

```bash
# 1. Kreiraj folder za vežbe
cd ~/code/python-automation-lab/python-automation-portfolio/sandbox/basics
mkdir -p cli_logging_practice/{scripts,data,logs,tests}

# 2. Pripremi test podatke
cd cli_logging_practice
cat > data/users.csv << 'EOF'
name,age,city
Ana,28,Beograd
Marko,35,Novi Sad
Jelena,42,Niš
Stefan,31,Subotica
EOF

cat > data/config.json << 'EOF'
{
  "app_name": "DataProcessor",
  "version": "1.0.0",
  "settings": {
    "debug": false,
    "max_items": 100
  }
}
EOF

# 3. Proveri
ls -lh data/
```

---

## 🚦 Check Points

### Nakon Dana 1

```bash
python3 scripts/log_to_file.py
cat logs/app.log  # Trebalo bi da vidiš logove
```

---

### Nakon Dana 2

```bash
python3 scripts/basic_cli.py --help  # Prikazuje help
python3 scripts/subcommands_cli.py list /tmp -r  # Radi subcommand
```

---

### Nakon Dana 3

```bash
python3 scripts/csv_to_json.py
cat data/users_from_csv.json  # Konvertovani podaci
```

---

### Nakon Dana 4

```bash
python3 scripts/data_converter.py csv2json data/users.csv data/test.json
cat logs/converter.log  # Kompletan log
```

---

### Nakon Dana 5

```bash
cd ~/code/python-automation-lab/python-automation-portfolio/sandbox/basics/cli_logging_practice
pytest tests/ -v  # Svi testovi prolaze
```

---

## 🆘 Ako Zapneš

1. **Pročitaj Error Poruku Pažljivo** — Često ti kaže tačno šta je problem
2. **Proveri Teoriju** — Vrati se na L08/L11/L13 fajlove
3. **Zapiši u chatlog.md** — Dokumentuj problem
4. **Pitaj Me** — "Imam problem sa X kodom, dobijam Y grešku"

---

## 📖 Sledeći Koraci (Nakon 6 Dana)

1. Refaktoriši `projects/01-web-scraper/scraper.py` sa svim naučenim
2. Počni Dan 6-7: HTTP requests + beautifulsoup4
3. Integriši sve u finalnu verziju web scraper-a

---

**SREĆNO!** 🚀
Pogledaj `kickoff.md` za detaljniji hourly schedule.
