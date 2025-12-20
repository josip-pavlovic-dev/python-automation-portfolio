---
type: overview
topic: CLI + Logging + JSON/CSV — Python Automation Module
date: 2025-12-15
linked_to: 2025-12-15_cli_logging
language: bilingual
status: active
difficulty: beginner-intermediate
estimated_time: 48 hours
---

# 2025-12-15 – CLI + Logging + JSON/CSV

**Dobrodošao u Dan 4-5 Python Automation Foundation!**

## 📋 Šta Ćeš Naučiti

Ovaj modul pokriva **ključne build blocks** za svaki automation projekat:

### 1. **Logging** (nivo produkcije)

-   Hijerarhija: Logger → Handler → Formatter
-   Nivoi logovanja: DEBUG, INFO, WARNING, ERROR, CRITICAL
-   Multi-destination logging (console + file istovremeno)
-   RotatingFileHandler za production (spreči prevelike log fajlove)
-   Izbegavanje duplikata handlera
-   Logger propagation i kontrola toka poruka

---

### 2. **CLI sa argparse** (profesionalni command-line interfejsi)

-   Pozicioni i opcioni argumenti
-   Boolean flagovi (`--verbose`, `--dry-run`)
-   Ograničene opcije sa `choices`
-   Višestruki argumenti sa `nargs`
-   Subparsers (git-style komande: `tool add`, `tool list`)
-   Exit kodovi (0 = uspeh, 1+ = greška)
-   Auto-generisan `--help`

---

### 3. **JSON & CSV** (sinhronizacija podataka)

-   `json.load/dump` sa Unicode podrškom (`ensure_ascii=False`)
-   Error handling za JSON (`JSONDecodeError`)
-   CSV čitanje/pisanje sa `DictReader/DictWriter`
-   CSV → JSON i JSON → CSV konverzija
-   Validacija strukture podataka
-   Streaming za velike fajlove

---

### 4. **Pytest** (unit testovi)

-   Osnovna struktura testova
-   `tmp_path` fixture za test fajlove
-   `caplog` fixture za testiranje logovanja
-   Testiranje CLI parsing-a
-   Parametrizovani testovi

---

### 5. **Pathlib** (Bonus — moderni rad sa putanjama)

-   Path objekti umesto stringova
-   Glob patterns za pretragu fajlova
-   Kreiranje/brisanje foldera
-   Čitanje/pisanje fajlova direktno sa Path-om

---

## 🎯 Cilj Modula

Po završetku ovog modula, biće u stanju da:

1. **Kreiraš production-ready CLI alate** sa jasnim argumentima i logging-om
2. **Obrađuješ JSON i CSV podatke** sa validacijom i konverzijom
3. **Integrišeš sve komponente** u jedan koherentan projekat
4. **Pišeš unit testove** za svoje funkcije
5. **Refaktorišeš `projects/01-web-scraper/`** sa novim znanjem

---

## 📂 Struktura Materijala

```
learning/2025-12-15_cli_logging/
├── README.md                          # 👈 Ovaj fajl (pregled)
├── START_GUIDE.md                     # 48h learning plan (6 dana × 8h)
├── kickoff.md                         # Hourly schedule sa pauzama
├── cheatsheet.md                      # Brzi referentni vodič
├── cli_logging_complete_exercises.md  # 2000+ linija REPL vežbi
├── tasks.md                           # Checklist zadataka
├── chatlog.md                         # Q&A tokom učenja
└── summary.md                         # Tvoje beleške nakon završetka
```

---

## 🗓️ Learning Path

### **Dan 1 (8h) — Logging**

-   Logging nivoi, handleri, formateri
-   Console + File logging
-   RotatingFileHandler
-   Duplicate handlers problem
-   Logger propagation

---

### **Dan 2 (8h) — Argparse CLI**

-   Basic parser
-   Pozicioni i opcioni argumenti
-   Boolean flagovi
-   Choices, nargs
-   Subparsers (git-style)
-   Exit kodovi

---

### **Dan 3 (8h) — JSON i CSV**

-   JSON čitanje/pisanje
-   Error handling
-   CSV DictReader/DictWriter
-   CSV ↔ JSON konverzija
-   Validacija

---

### **Dan 4 (8h) — Integrisani Projekat**

-   `data_converter.py` CLI alat (CLI + Logging + JSON/CSV)
-   Refaktorisanje `projects/01-web-scraper/scraper.py`

---

### **Dan 5 (8h) — Pytest**

-   Instalacija pytest
-   Unit testovi za JSON/CSV funkcije
-   Testiranje CLI parsing-a
-   Testiranje logging-a sa `caplog`

---

### **Dan 6 (8h) — Bonus + Praksa**

-   Pathlib (Path objekti, glob)
-   Slobodna REPL praksa
-   Ponavljanje nejasnih delova

---

## 🏁 Kako Početi

### 1. Pročitaj Teoriju

Obavezno prvo pročitaj teorijske fajlove:

```bash
# Teorija logging-a
cat scratch/theory/published/L08_logging_osnove_logger_handler_formatter,_nivoi,_izbegavanje_duplih_handlera.md

# Teorija argparse-a
cat scratch/theory/published/L11_cli_sa_argparse_argumenti,_flagovi,_validacija,_exit_kodovi.md

# Teorija JSON/CSV
cat scratch/theory/published/L13_json_i_csv_čitanje_pisanje,_validacija,_rad_sa_većim_fajlovima.md
```

---

### 2. Setup Practice Environment

```bash
cd ~/code/python-automation-lab/python-automation-portfolio/sandbox/basics
mkdir -p cli_logging_practice/{scripts,data,logs,tests}
cd cli_logging_practice

# Kreiraj test podatke
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

# Proveri
ls -lh data/
```

### 3. Kreni sa Vežbama

Otvori `cli_logging_complete_exercises.md` i kreni od **FAZA 1.1** (BasicConfig).

---

## 📖 Dodatni Resursi

### Teorijski Fajlovi (Čitaj PRE vežbi!)

-   [L08_logging_osnove](../../scratch/theory/published/L08_logging_osnove_logger_handler_formatter,_nivoi,_izbegavanje_duplih_handlera.md)
-   [L11_cli_sa_argparse](../../scratch/theory/published/L11_cli_sa_argparse_argumenti,_flagovi,_validacija,_exit_kodovi.md)
-   [L13_json_i_csv](../../scratch/theory/published/L13_json_i_csv_čitanje_pisanje,_validacija,_rad_sa_većim_fajlovima.md)
-   [L14_pytest_osnove](../../scratch/theory/published/L14_pytest_osnove_struktura_testova,_fixture,_parametrize,_caplog.md)

---

### Praktične Vežbe

-   [cli_logging_complete_exercises.md](cli_logging_complete_exercises.md) — 2000+ linija copy-paste ready koda

---

### Brze Reference

-   [cheatsheet.md](cheatsheet.md) — Kada brzo trebaš sintaksu

---

### Detaljan Plan

-   [START_GUIDE.md](START_GUIDE.md) — 48h learning plan
-   [kickoff.md](kickoff.md) — Hourly schedule

---

## ✅ Success Criteria

Modul je završen kada možeš:

-   [ ] Konfigurisati logging sa više handlera bez duplikata
-   [ ] Kreirati CLI alat sa argparse (pozicioni, opcioni, flagovi, subparsers)
-   [ ] Vratiti pravilne exit kodove
-   [ ] Čitati/pisati JSON i CSV sa validacijom
-   [ ] Konvertovati CSV ↔ JSON
-   [ ] Napisati pytest testove za svoje funkcije
-   [ ] Testirati logging sa `caplog`
-   [ ] Integrisati sve u funkcionalan CLI alat (npr. `data_converter.py`)

---

## 🚀 Next Steps (Nakon Završetka)

1. **Refaktoriši `projects/01-web-scraper/scraper.py`:**

    - Dodaj argparse CLI (`--url`, `--output`, `--log-level`)
    - Integriši logging (console + rotating file)
    - Dodaj JSON/CSV output format opcije
    - Napiši pytest testove

2. **Pređi na Dan 6-7:** HTTP requests + BeautifulSoup4 (web scraping)

3. **Kreiraj utility module:**
    - `utils/logging_utils.py` — Reusable logging setup
    - `utils/file_utils.py` — JSON/CSV helperi sa pathlib

---

## 🆘 Help & Support

Ako zapneš:

1. **Pročitaj error poruku** — Često ti kaže tačno šta je problem
2. **Proveri teoriju** — Vrati se na L08/L11/L13 fajlove
3. **Zapiši pitanje u `chatlog.md`** — Dokumentuj problem
4. **Pitaj me** — "Imam problem sa X kodom, dobijam Y grešku"

---

## 📊 Progress Tracking

Koristi `tasks.md` za praćenje napretka. Update-uj nakon svake faze.

```bash
# Primer commit-a nakon Dana 1
git add learning/2025-12-15_cli_logging
git commit -m "Dan 1: Završio logging osnove (nivoi, handleri, formateri)"
```

---

**SREĆNO!** 🎯
Kreni sa `START_GUIDE.md` za detaljniji plan!
