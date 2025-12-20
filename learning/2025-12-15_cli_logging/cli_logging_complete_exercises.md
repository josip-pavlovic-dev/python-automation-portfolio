---
type: exercises
topic: CLI + Logging + JSON/CSV — Python REPL Praksa
date: 2025-12-15
linked_to: 2025-12-15_cli_logging
language: bilingual
status: active
difficulty: beginner-intermediate
environment: python_repl + files
estimated_time: 5-7 hours
---

# 🎯 CLI + Logging + JSON/CSV REPL Vežbe — Kompletna Praksa

**Cilj:** Savladaj argparse, logging sistem, JSON/CSV obradu kroz praktične primere
**Format:** Copy-paste ready kod za Python REPL i fajlove
**Trajanje:** 5-7 sati (radi u fazama)

---

## 🏁 SETUP — Priprema Test Okruženja (15 min)

### 1. Kreiraj Folder za Vežbe

```bash
cd ~/code/python-automation-lab/python-automation-portfolio/sandbox/basics
mkdir -p cli_logging_practice
cd cli_logging_practice

# Kreiraj strukturu
mkdir -p {logs,data,scripts}
pwd
```

---

### 2. Pripremi Test Data

```bash
# Kreiraj test CSV
cat > data/users.csv << 'EOF'
name,age,city
Ana,28,Beograd
Marko,35,Novi Sad
Jelena,42,Niš
Stefan,31,Subotica
EOF

# Kreiraj test JSON
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
cat data/users.csv
cat data/config.json
```

---

## 📂 FAZA 1: LOGGING OSNOVE (60-90 min)

### 1.1 BasicConfig — Najjednostavnije Logovanje

**Teorija:** `basicConfig()` je najbrži način da počneš sa loggovanjem. Postavlja root logger.

```python
# Otvori Python REPL
# python3

import logging

# 1. Osnovna konfiguracija
logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug poruka")
logging.info("Info poruka")
logging.warning("Warning poruka")
logging.error("Error poruka")
logging.critical("Critical poruka")

# Output (ide u stderr):
# DEBUG:root:Debug poruka
# INFO:root:Info poruka
# WARNING:root:Warning poruka
# ERROR:root:Error poruka
# CRITICAL:root:Critical poruka
```

**Objašnjenje nivoa:**

-   `DEBUG (10)`: Detaljne info za debugging (dev only)
-   `INFO (20)`: Potvrdni događaji (app started, file processed)
-   `WARNING (30)`: Upozorenja, ali app nastavlja rad
-   `ERROR (40)`: Ozbiljna greška, ali app još može nastaviti
-   `CRITICAL (50)`: Najgori scenario, app se može srušiti

---

### 1.2 Custom Format — Bolje Poruke

```python
import logging

# Resetuj prethodni config (VAŽNO u REPL-u!)
# Napomena: U REPL-u možeš resetovati sa reload(logging) ali bolje je restartovati REPL
# exit()  # Izađi iz REPL-a
# python3  # Ponovo uđi

import logging

# Custom format sa vremenom i imenom
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("my_app") # Kreiraj named logger
logger.debug("Startovanje aplikacije") # Koristi logger
logger.info("Korisnik se ulogovao")
logger.warning("Disk je pun 80%")
logger.error("Fajl nije pronađen")

# Output primer:
# 2025-12-15 14:23:45 | DEBUG    | my_app | Startovanje aplikacije
# 2025-12-15 14:23:45 | INFO     | my_app | Korisnik se ulogovao
# 2025-12-15 14:23:45 | WARNING  | my_app | Disk je pun 80%
# 2025-12-15 14:23:45 | ERROR    | my_app | Fajl nije pronađen
```

**Format Stringovi:**

-   `%(asctime)s`: Vreme događaja
-   `%(levelname)s`: Nivo (DEBUG, INFO, itd.)
-   `%(name)s`: Ime logger-a
-   `%(message)s`: Tvoja poruka
-   `%(filename)s`: Ime fajla
-   `%(lineno)d`: Broj linije

---

### 1.3 Logovanje u Fajl + Console

**Teorija:** Handler je objekat koji određuje KUDA idu log poruke (konzola, fajl, email, itd.)

Kreiraj fajl `scripts/log_to_file.py`:

```python
import logging
from pathlib import Path

# Kreiraj logs folder ako ne postoji
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# 1. Kreiraj logger
logger = logging.getLogger("file_app")
logger.setLevel(logging.DEBUG)

# 2. Kreiraj formatere
formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# 3. StreamHandler (konzola)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Samo INFO i iznad
console_handler.setFormatter(formatter)

# 4. FileHandler (fajl)
file_handler = logging.FileHandler(log_dir / "app.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)  # Sve poruke u fajlu sa DEBUG i iznad
file_handler.setFormatter(formatter)

# 5. Dodaj handlere (JEDNOM!)
if not logger.handlers:  # Izbegni duplikate!
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

# 6. Koristi logger
logger.debug("Ovo ide samo u fajl")
logger.info("Ovo ide u konzolu I fajl")
logger.warning("I ovo u oba")
logger.error("Greška - oba izlaza")

print("\n✅ Proveri logs/app.log fajl!")
```

Pokreni:

```bash
cd ~/code/python-automation-lab/python-automation-portfolio/sandbox/basics/cli_logging_practice
python3 scripts/log_to_file.py

# Proveri fajl
cat logs/app.log
```

**Ključni koncepti:**

-   **Logger**: Glavni objekat koji koristi (`getLogger()`)
-   **Handler**: Definiše destinaciju (StreamHandler → stdout, FileHandler → fajl)
-   **Formatter**: Definiše format poruke
-   **Level**: Možeš postaviti različite nivoe za logger i svaki handler

---

### 1.4 Izbegavanje Duplikata Handlera

**Problem:** Ako pozoveš `logger.addHandler()` više puta, dobijaš duplih poruka!

Kreiraj `scripts/duplicate_problem.py`:

```python
import logging

def get_logger():
    logger = logging.getLogger("dup_test")
    logger.setLevel(logging.DEBUG)

    # LOŠE — svaki put dodaješ novi handler!
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    return logger

# Pozovi 3 puta
for i in range(3):
    log = get_logger()
    log.info(f"Poruka {i+1}")

# Output:
# Poruka 1
# Poruka 2
# Poruka 2
# Poruka 3
# Poruka 3
# Poruka 3
#
# Svaki poziv dodaje još jedan handler!
```

**Rešenje — Proveri postojeće handlere:**

```python
import logging

def get_logger():
    logger = logging.getLogger("dup_test_fixed")
    logger.setLevel(logging.DEBUG)

    # ✅ DOBRO — dodaj samo ako ne postoje
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

# Sada je OK
for i in range(3):
    log = get_logger()
    log.info(f"Poruka {i+1}")

# Output:
# INFO: Poruka 1
# INFO: Poruka 2
# INFO: Poruka 3
```

---

### 1.5 Logger Hijerarhija i Propagation

**Teorija:** Logger-i imaju hijerarhiju baziranu na imenima (odvojenim tačkom).

```python
import logging

# Konfiguraj root logger
logging.basicConfig(level=logging.DEBUG, format="[%(name)s] %(message)s")

# Parent logger
parent = logging.getLogger("app")
parent.info("Parent poruka")

# Child logger-i
child1 = logging.getLogger("app.module1")
child1.info("Child1 poruka")

child2 = logging.getLogger("app.module2")
child2.info("Child2 poruka")

grandchild = logging.getLogger("app.module1.submodule")
grandchild.info("Grandchild poruka")

# Output:
# [app] Parent poruka
# [app.module1] Child1 poruka
# [app.module2] Child2 poruka
# [app.module1.submodule] Grandchild poruka

# Zaključak: Svi logger-i nasleđuju postavke od root logger-a, i propagate poruke gore u hijerarhiji.
```

**Propagation OFF:**

```python
import logging

logging.basicConfig(level=logging.DEBUG, format="[%(name)s] %(message)s")

child = logging.getLogger("app.secret")
child.propagate = False  # Ne prosljeđuj poruke parent logger-u

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("SECRET: %(message)s"))
child.addHandler(handler)
child.setLevel(logging.DEBUG)

child.info("Ovo ne ide parent logger-u")
# Output:
# SECRET: Ovo ne ide parent logger-u
# Nema output iz parent logger-a

# Zaključak: Isključi propagation ako želiš da child logger ima sopstveni tok logova. Ova praksa se često koristi za specijalizovane loggere sa sopstvenim handler-ima.
```

---

### 1.6 RotatingFileHandler — Za Production

**Teorija:** Sprečava da log fajl postane prevelik. Rotira kada dosegne max veličinu.

Kreiraj `scripts/rotating_log.py`:

```python
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

logger = logging.getLogger("rotating_app")
logger.setLevel(logging.DEBUG)

# Rotating handler
# maxBytes: Maksimalna veličina fajla (1MB = 1_000_000)
# backupCount: Broj backup fajlova (app.log.1, app.log.2, itd.)
handler = RotatingFileHandler(
    log_dir / "rotating.log",
    maxBytes=1_000,  # 1KB za demo svrhe
    backupCount=3, # Čuva poslednja 3 fajla
    encoding="utf-8"
)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(handler)

# Generiši mnogo logova
for i in range(100):
    logger.info(f"Log poruka broj {i} sa dodatnim tekstom da bi povećali veličinu fajla")

print("✅ Proveri logs/ folder — trebalo bi da ima rotating.log, rotating.log.1, rotating.log.2, rotating.log.3")

# Zaključak: RotatingFileHandler je odličan za produkciju gde log fajlovi mogu brzo rasti. Podesi maxBytes i backupCount prema potrebama tvoje aplikacije.
```

Pokreni:

```bash
python3 scripts/rotating_log.py
ls -lh logs/
```

---

## 📂 FAZA 2: ARGPARSE — CLI Argumenti (60-90 min)

### 2.1 Osnovni Parser

**Teorija:** `argparse` parsira komandnu liniju i pravi čitljiv `--help`.

Kreiraj `scripts/basic_cli.py`:

```python
#!/usr/bin/env python3
"""
Basic CLI primer
"""
import argparse

def main():
    # 1. Kreiraj parser
    parser = argparse.ArgumentParser(
        prog="basic-cli",
        description="Jednostavan CLI alat",
        epilog="Hvala što koristiš ovaj alat!"
    )

    # 2. Dodaj argumente
    parser.add_argument("name", help="Vaše ime")
    parser.add_argument("age", type=int, help="Vaše godine")

    # 3. Parsuj
    args = parser.parse_args()

    # 4. Koristi
    print(f"Zdravo {args.name}, imaš {args.age} godina!")

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
chmod +x scripts/basic_cli.py

# Vidi help
python3 scripts/basic_cli.py --help

# Pozovi
python3 scripts/basic_cli.py Ana 28

# Greška ako nije int
python3 scripts/basic_cli.py Ana dvadeset-osam
# Output: error: argument age: invalid int value: 'dvadeset-osam'
```

---

### 2.2 Opcioni Argumenti i Default Values

Kreiraj `scripts/optional_cli.py`:

```python
#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI sa opcionim argumentima")

    # Pozicioni (obavezan)
    parser.add_argument("input_file", help="Input fajl")

    # Opcioni (počinje sa -- ili -)
    parser.add_argument(
        "--output",
        "-o",
        default="output.txt",
        help="Output fajl (default: output.txt)"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maksimalan broj rezultata (default: 10)"
    )

    args = parser.parse_args()

    print(f"Input: {args.input_file}")
    print(f"Output: {args.output}")
    print(f"Limit: {args.limit}")

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
# Samo obavezni
python3 scripts/optional_cli.py data/users.csv

# Sa opcionim
python3 scripts/optional_cli.py data/users.csv --output results.txt --limit 5

# Kratka forma
python3 scripts/optional_cli.py data/users.csv -o results.txt
```

---

### 2.3 Boolean Flagovi (action="store_true")

Kreiraj `scripts/flags_cli.py`:

```python
#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI sa boolean flagovima")

    parser.add_argument("path", help="Putanja za obradu")

    # Boolean flag (default False)
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Prikaži detaljne poruke"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simuliraj izvršavanje bez izmena"
    )

    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Ne prikazuj ništa osim grešaka"
    )

    args = parser.parse_args()

    print(f"Path: {args.path}")
    print(f"Verbose: {args.verbose}")
    print(f"Dry-run: {args.dry_run}")
    print(f"Quiet: {args.quiet}")

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
# Bez flagova
python3 scripts/flags_cli.py /tmp

# Sa flagovima
python3 scripts/flags_cli.py /tmp --verbose --dry-run

# Kratke forme
python3 scripts/flags_cli.py /tmp -v -q
```

---

### 2.4 Choices — Ograničene Opcije

Kreiraj `scripts/choices_cli.py`:

```python
#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI sa ograničenim izborom")

    parser.add_argument(
        "format",
        choices=["json", "csv", "xml"],
        help="Format output-a"
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Nivo logovanja (default: INFO)"
    )

    args = parser.parse_args()

    print(f"Format: {args.format}")
    print(f"Log level: {args.log_level}")

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
# OK
python3 scripts/choices_cli.py json

# Greška
python3 scripts/choices_cli.py yaml
# Output: error: argument format: invalid choice: 'yaml' (choose from 'json', 'csv', 'xml')

# Sa log-level
python3 scripts/choices_cli.py csv --log-level DEBUG
```

---

### 2.5 nargs — Više Argumenata

Kreiraj `scripts/nargs_cli.py`:

```python
#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI sa višestrukim argumentima")

    # nargs="+" : Jedan ili više
    parser.add_argument(
        "files",
        nargs="+",
        help="Fajlovi za obradu (jedan ili više)"
    )

    # nargs="*" : Nula ili više
    parser.add_argument(
        "--ignore",
        nargs="*",
        default=[],
        help="Ignorisani patern-i"
    )

    # nargs=2 : Tačno 2
    parser.add_argument(
        "--range",
        nargs=2,
        type=int,
        help="Početak i kraj (npr: --range 1 10)"
    )

    args = parser.parse_args()

    print(f"Files: {args.files}")
    print(f"Ignore: {args.ignore}")
    print(f"Range: {args.range}")

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
# Jedan fajl
python3 scripts/nargs_cli.py data/users.csv

# Više fajlova
python3 scripts/nargs_cli.py data/users.csv data/config.json logs/app.log

# Sa ignore i range
python3 scripts/nargs_cli.py data/* --ignore "*.log" "*.tmp" --range 1 100
```

---

### 2.6 Subparsers — Git-Style Commands

**Teorija:** Kreiraj CLI sa pod-komandama (npr: `git add`, `git commit`).

Kreiraj `scripts/subcommands_cli.py`:

```python
#!/usr/bin/env python3
import argparse

def cmd_list(args):
    print(f"📋 Listanje fajlova u: {args.path}")
    if args.recursive:
        print("  (rekurzivno)")

def cmd_search(args):
    print(f"🔍 Pretraga za: {args.pattern}")
    print(f"   U fajlu: {args.file}")

def cmd_export(args):
    print(f"💾 Export u format: {args.format}")
    print(f"   Output: {args.output}")

def main():
    parser = argparse.ArgumentParser(
        prog="datatool",
        description="Alat za obradu podataka"
    )

    # Global argumenti
    parser.add_argument("--verbose", "-v", action="store_true")

    # Kreiraj subparsers
    subparsers = parser.add_subparsers(
        title="Komande",
        description="Dostupne komande",
        dest="command",
        required=True
    )

    # 1. list komanda
    parser_list = subparsers.add_parser("list", help="Lista fajlova")
    parser_list.add_argument("path", help="Putanja")
    parser_list.add_argument("-r", "--recursive", action="store_true", help="Rekurzivno")
    parser_list.set_defaults(func=cmd_list)

    # 2. search komanda
    parser_search = subparsers.add_parser("search", help="Pretraži fajlove")
    parser_search.add_argument("pattern", help="Šta traži")
    parser_search.add_argument("file", help="Gde traži")
    parser_search.set_defaults(func=cmd_search)

    # 3. export komanda
    parser_export = subparsers.add_parser("export", help="Exportuj podatke")
    parser_export.add_argument("--format", choices=["json", "csv"], default="json")
    parser_export.add_argument("--output", "-o", required=True, help="Output fajl")
    parser_export.set_defaults(func=cmd_export)

    # Parsuj i pozovi funkciju
    args = parser.parse_args()

    if args.verbose:
        print(f"🔊 Verbose mode ON")

    args.func(args)

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
# Vidi help
python3 scripts/subcommands_cli.py --help

# Svaka komanda ima svoj help
python3 scripts/subcommands_cli.py list --help

# list komanda
python3 scripts/subcommands_cli.py list /tmp
python3 scripts/subcommands_cli.py list /tmp -r --verbose

# search komanda
python3 scripts/subcommands_cli.py search "TODO" src/main.py

# export komanda
python3 scripts/subcommands_cli.py export --format csv -o results.csv
```

---

### 2.7 Exit Kodovi — sys.exit()

**Teorija:** Exit kodovi omogućavaju shell skriptama da znaju da li je program uspeo.

Kreiraj `scripts/exit_codes.py`:

```python
#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Provera fajla")
    parser.add_argument("file", help="Fajl za proveru")
    args = parser.parse_args()

    path = Path(args.file)

    if not path.exists():
        print(f"❌ ERROR: Fajl '{args.file}' ne postoji!", file=sys.stderr)
        sys.exit(1)  # Exit kod 1 = greška

    if not path.is_file():
        print(f"❌ ERROR: '{args.file}' nije fajl!", file=sys.stderr)
        sys.exit(2)  # Exit kod 2 = različit tip greške

    print(f"✅ SUCCESS: Fajl '{args.file}' je validan!")
    sys.exit(0)  # Exit kod 0 = uspeh

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
# Uspeh
python3 scripts/exit_codes.py data/users.csv
echo "Exit kod: $?"  # Prikazuje exit kod prethodne komande

# Greška — fajl ne postoji
python3 scripts/exit_codes.py nonexistent.txt
echo "Exit kod: $?"

# U shell skripti:
if python3 scripts/exit_codes.py data/users.csv; then
    echo "Validacija uspela!"
else
    echo "Validacija nije uspela!"
fi
```

**Konvencije Exit Kodova:**

-   `0`: Uspeh
-   `1`: Opšta greška
-   `2`: Pogrešan argument/sintaksa
-   `3-125`: Specifične greške (definiše developer)
-   `126`: Komanda ne može da se izvrši
-   `127`: Komanda nije pronađena
-   `128+N`: Program prekinut sa signalom N

---

## 📂 FAZA 3: JSON I CSV (60-90 min)

### 3.1 JSON — Osnove

**Teorija:** JSON je text format za strukturirane podatke (slično Python dict/list).

```python
import json

# Python → JSON
data = {
    "name": "Ana Petrović",
    "age": 28,
    "skills": ["Python", "JavaScript", "SQL"],
    "active": True
}

json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

# JSON → Python
parsed = json.loads(json_str)
print(type(parsed))  # <class 'dict'>
print(parsed["name"])
```

---

### 3.2 JSON sa Fajlovima

Kreiraj `scripts/json_file_ops.py`:

```python
import json
from pathlib import Path

data_dir = Path(__file__).parent.parent / "data"

# 1. PISANJE JSON-a
users = [
    {"id": 1, "name": "Ana", "email": "ana@example.com"},
    {"id": 2, "name": "Marko", "email": "marko@example.com"},
    {"id": 3, "name": "Jelena", "email": "jelena@example.com"}
]

output_path = data_dir / "users_output.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print(f"✅ Zapisano u: {output_path}")

# 2. ČITANJE JSON-a
with open(output_path, "r", encoding="utf-8") as f:
    loaded_users = json.load(f)

print(f"\n📖 Učitano {len(loaded_users)} korisnika:")
for user in loaded_users:
    print(f"  - {user['name']} ({user['email']})")

# 3. VALIDACIJA STRUKTURE
for user in loaded_users:
    if "id" not in user or "name" not in user:
        print(f"⚠️  INVALID: {user}")
    else:
        print(f"✅ VALID: {user['name']}")
```

Pokreni:

```bash
python3 scripts/json_file_ops.py
cat data/users_output.json
```

---

### 3.3 JSON Error Handling

Kreiraj `scripts/json_errors.py`:

```python
import json
import sys

# LOŠE FORMATIRAN JSON
bad_json = '''
{
  "name": "Ana",
  "age": 28,
  "skills": ["Python", "SQL"]  // GREŠKA: JavaScript komentar nije dozvoljen!
}
'''

try:
    data = json.loads(bad_json)
except json.JSONDecodeError as e:
    print(f"❌ JSON Greška:")
    print(f"   Poruka: {e.msg}")
    print(f"   Linija: {e.lineno}, Kolona: {e.colno}")
    print(f"   Pozicija: {e.pos}")
    sys.exit(1)

# DOBRO FORMATIRAN
good_json = '''
{
  "name": "Ana",
  "age": 28,
  "skills": ["Python", "SQL"]
}
'''

try:
    data = json.loads(good_json)
    print(f"✅ JSON je validan!")
    print(f"   Ime: {data['name']}")
except json.JSONDecodeError as e:
    print(f"❌ Greška: {e}")
```

Pokreni:

```bash
python3 scripts/json_errors.py
```

---

### 3.4 CSV — Osnove (csv.reader/writer)

Kreiraj `scripts/csv_basic.py`:

```python
import csv
from pathlib import Path

data_dir = Path(__file__).parent.parent / "data"
input_csv = data_dir / "users.csv"
output_csv = data_dir / "users_output.csv"

# 1. ČITANJE SA csv.reader
print("📖 Čitanje sa csv.reader (lista redova):")
with open(input_csv, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # Prva linija = header
    print(f"   Header: {header}")

    for row in reader:
        print(f"   {row}")

print()

# 2. PISANJE SA csv.writer
print("💾 Pisanje sa csv.writer:")
with open(output_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Stefan", 31, "Subotica"])
    writer.writerow(["Milica", 29, "Kragujevac"])

print(f"✅ Zapisano u: {output_csv}")
```

Pokreni:

```bash
python3 scripts/csv_basic.py
cat data/users_output.csv
```

---

### 3.5 CSV DictReader/DictWriter — BOLJA OPCIJA

**Teorija:** `DictReader` vraća svaki red kao `dict` umesto liste. Čitljivije!

Kreiraj `scripts/csv_dict.py`:

```python
import csv
from pathlib import Path

data_dir = Path(__file__).parent.parent / "data"
input_csv = data_dir / "users.csv"
output_csv = data_dir / "users_dict_output.csv"

# 1. ČITANJE SA DictReader
print("📖 Čitanje sa DictReader:")
with open(input_csv, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        # row je dict!
        print(f"   {row['name']} (age: {row['age']}, city: {row['city']})")

print()

# 2. PISANJE SA DictWriter
users = [
    {"name": "Nikola", "age": 33, "city": "Leskovac"},
    {"name": "Jovana", "age": 26, "city": "Valjevo"}
]

print("💾 Pisanje sa DictWriter:")
with open(output_csv, "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()  # VAŽNO: Zapiši header red
    for user in users:
        writer.writerow(user)

print(f"✅ Zapisano u: {output_csv}")

# 3. PROVERI
with open(output_csv, "r", encoding="utf-8") as f:
    content = f.read()
    print(f"\n📄 Sadržaj fajla:\n{content}")
```

Pokreni:

```bash
python3 scripts/csv_dict.py
```

---

### 3.6 CSV → JSON Konverzija

Kreiraj `scripts/csv_to_json.py`:

```python
import csv
import json
from pathlib import Path

data_dir = Path(__file__).parent.parent / "data"
input_csv = data_dir / "users.csv"
output_json = data_dir / "users_from_csv.json"

# Čitaj CSV
users = []
with open(input_csv, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Konvertuj age u int
        row["age"] = int(row["age"])
        users.append(row)

# Zapiši JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print(f"✅ Konvertovano {len(users)} redova iz CSV u JSON")
print(f"   Input:  {input_csv}")
print(f"   Output: {output_json}")

# Proveri
with open(output_json, "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(f"\n📄 JSON sadržaj:")
    print(json.dumps(loaded, ensure_ascii=False, indent=2))
```

Pokreni:

```bash
python3 scripts/csv_to_json.py
cat data/users_from_csv.json
```

---

### 3.7 JSON → CSV Konverzija

Kreiraj `scripts/json_to_csv.py`:

```python
import csv
import json
from pathlib import Path

data_dir = Path(__file__).parent.parent / "data"
input_json = data_dir / "users_from_csv.json"
output_csv = data_dir / "users_from_json.csv"

# Čitaj JSON
with open(input_json, "r", encoding="utf-8") as f:
    users = json.load(f)

# Zapiši CSV
with open(output_csv, "w", newline="", encoding="utf-8") as f:
    # Uzmi fieldnames iz prvog objekta
    fieldnames = list(users[0].keys())

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users)  # writerows = više redova odjednom

print(f"✅ Konvertovano {len(users)} objekata iz JSON u CSV")
print(f"   Input:  {input_json}")
print(f"   Output: {output_csv}")

# Proveri
with open(output_csv, "r", encoding="utf-8") as f:
    print(f"\n📄 CSV sadržaj:\n{f.read()}")
```

Pokreni:

```bash
python3 scripts/json_to_csv.py
```

---

## 📂 FAZA 4: INTEGRISANI PROJEKAT (90-120 min)

### 4.1 CLI Alat sa Logging i JSON/CSV

**Cilj:** Napravi CLI alat koji konvertuje CSV↔JSON sa logging-om i error handling-om.

Kreiraj `scripts/data_converter.py`:

```python
#!/usr/bin/env python3
"""
Data Converter — CLI alat za konverziju CSV ↔ JSON
"""
import argparse
import csv
import json
import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

# ============================================
# LOGGING SETUP
# ============================================

def setup_logging(log_level: str, log_dir: Path) -> logging.Logger:
    """Konfiguracija logging sistema"""

    log_dir.mkdir(exist_ok=True)
    logger = logging.getLogger("data_converter")
    logger.setLevel(getattr(logging, log_level.upper()))

    # Format
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # File handler (rotating)
    file_handler = RotatingFileHandler(
        log_dir / "converter.log",
        maxBytes=5_000_000,  # 5MB
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Dodaj handlere
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

# ============================================
# KONVERZIJA FUNKCIJE
# ============================================

def csv_to_json(input_path: Path, output_path: Path, logger: logging.Logger) -> None:
    """Konvertuj CSV → JSON"""

    logger.info(f"Započinjem CSV→JSON konverziju")
    logger.debug(f"Input: {input_path}")
    logger.debug(f"Output: {output_path}")

    # Validacija
    if not input_path.exists():
        logger.error(f"Input fajl ne postoji: {input_path}")
        sys.exit(1)

    try:
        # Čitaj CSV
        with open(input_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        logger.info(f"Učitano {len(data)} redova iz CSV")

        # Zapiši JSON
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        logger.info(f"Uspešno zapisano u JSON: {output_path}")

    except Exception as e:
        logger.exception(f"Greška tokom konverzije: {e}")
        sys.exit(1)

def json_to_csv(input_path: Path, output_path: Path, logger: logging.Logger) -> None:
    """Konvertuj JSON → CSV"""

    logger.info(f"Započinjem JSON→CSV konverziju")
    logger.debug(f"Input: {input_path}")
    logger.debug(f"Output: {output_path}")

    # Validacija
    if not input_path.exists():
        logger.error(f"Input fajl ne postoji: {input_path}")
        sys.exit(1)

    try:
        # Čitaj JSON
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            logger.error(f"JSON mora biti lista objekata, dobio: {type(data)}")
            sys.exit(1)

        if len(data) == 0:
            logger.warning("JSON lista je prazna!")
            data = [{}]

        logger.info(f"Učitano {len(data)} objekata iz JSON")

        # Zapiši CSV
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        logger.info(f"Uspešno zapisano u CSV: {output_path}")

    except json.JSONDecodeError as e:
        logger.error(f"Neispravan JSON format: {e}")
        sys.exit(1)

    except Exception as e:
        logger.exception(f"Greška tokom konverzije: {e}")
        sys.exit(1)

# ============================================
# CLI
# ============================================

def main():
    parser = argparse.ArgumentParser(
        prog="data-converter",
        description="Konvertuj CSV ↔ JSON sa logging-om",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Primeri:
  %(prog)s csv2json input.csv output.json
  %(prog)s json2csv data.json result.csv --log-level DEBUG
        """
    )

    # Subcommands
    subparsers = parser.add_subparsers(dest="command", required=True)

    # csv2json
    p_csv2json = subparsers.add_parser("csv2json", help="CSV → JSON")
    p_csv2json.add_argument("input", type=Path, help="Input CSV fajl")
    p_csv2json.add_argument("output", type=Path, help="Output JSON fajl")

    # json2csv
    p_json2csv = subparsers.add_parser("json2csv", help="JSON → CSV")
    p_json2csv.add_argument("input", type=Path, help="Input JSON fajl")
    p_json2csv.add_argument("output", type=Path, help="Output CSV fajl")

    # Global options
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Nivo logovanja (default: INFO)"
    )

    parser.add_argument(
        "--log-dir",
        type=Path,
        default=Path(__file__).parent.parent / "logs",
        help="Folder za log fajlove"
    )

    args = parser.parse_args()

    # Setup logging
    logger = setup_logging(args.log_level, args.log_dir)

    logger.info(f"═══════════════════════════════════════")
    logger.info(f"Data Converter Started")
    logger.info(f"Command: {args.command}")

    # Execute command
    if args.command == "csv2json":
        csv_to_json(args.input, args.output, logger)
    elif args.command == "json2csv":
        json_to_csv(args.input, args.output, logger)

    logger.info(f"Gotovo! ✅")
    logger.info(f"═══════════════════════════════════════")

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
chmod +x scripts/data_converter.py

# Help
python3 scripts/data_converter.py --help
python3 scripts/data_converter.py csv2json --help

# CSV → JSON
python3 scripts/data_converter.py csv2json data/users.csv data/converted.json

# JSON → CSV
python3 scripts/data_converter.py json2csv data/converted.json data/converted_back.csv

# Sa DEBUG logging-om
python3 scripts/data_converter.py csv2json data/users.csv data/test.json --log-level DEBUG

# Proveri log
cat logs/converter.log
```

---

### 4.2 Dodaj Validaciju i Filtriranje

**Proširenje:** Dodaj opciju da filtreš CSV redove pre konverzije.

Dodaj nakon `json_to_csv` funkcije:

```python
def filter_csv(input_path: Path, output_path: Path, min_age: int, logger: logging.Logger) -> None:
    """Filtriraj CSV po godinama"""

    logger.info(f"Filtriranje CSV redova (min_age={min_age})")

    if not input_path.exists():
        logger.error(f"Input fajl ne postoji: {input_path}")
        sys.exit(1)

    try:
        filtered_rows = []

        with open(input_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                age = int(row.get("age", 0))

                if age >= min_age:
                    filtered_rows.append(row)
                    logger.debug(f"Prihvaćen: {row['name']} (age={age})")
                else:
                    logger.debug(f"Odbačen: {row['name']} (age={age})")

        logger.info(f"Filtrirano: {len(filtered_rows)} od {len(list(csv.DictReader(open(input_path))))} redova")

        # Zapiši
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            if filtered_rows:
                fieldnames = list(filtered_rows[0].keys())
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(filtered_rows)

        logger.info(f"Zapisano u: {output_path}")

    except Exception as e:
        logger.exception(f"Greška: {e}")
        sys.exit(1)
```

Dodaj u `main()` nakon subparsers definicije:

```python
# filter
p_filter = subparsers.add_parser("filter", help="Filtriraj CSV po uslovu")
p_filter.add_argument("input", type=Path, help="Input CSV fajl")
p_filter.add_argument("output", type=Path, help="Output CSV fajl")
p_filter.add_argument("--min-age", type=int, required=True, help="Minimalne godine")
```

I u `if args.command` deo:

```python
elif args.command == "filter":
    filter_csv(args.input, args.output, args.min_age, logger)
```

Testiraj:

```bash
python3 scripts/data_converter.py filter data/users.csv data/filtered.csv --min-age 30 --log-level DEBUG
cat data/filtered.csv
```

---

## 📂 FAZA 5: PYTEST — Testiranje (60 min)

### 5.1 Instalacija pytest

```bash
cd ~/code/python-automation-lab/python-automation-portfolio/sandbox/basics/cli_logging_practice

# Ako nemaš venv
python3 -m venv venv
source venv/bin/activate

pip install pytest
```

---

### 5.2 Testiranje JSON Funkcionalnosti

Kreiraj `tests/test_json_ops.py`:

```python
import json
import pytest
from pathlib import Path

# Test funkcija
def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(data: dict, path: Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ============================================
# TESTS
# ============================================

def test_load_json_valid(tmp_path):
    """Test čitanja validnog JSON fajla"""

    # Setup
    test_file = tmp_path / "test.json"
    test_data = {"name": "Ana", "age": 28}

    with open(test_file, "w") as f:
        json.dump(test_data, f)

    # Execute
    result = load_json(test_file)

    # Assert
    assert result == test_data
    assert result["name"] == "Ana"

def test_load_json_invalid(tmp_path):
    """Test čitanja nevalidnog JSON-a"""

    test_file = tmp_path / "bad.json"
    test_file.write_text("{ invalid json }")

    with pytest.raises(json.JSONDecodeError):
        load_json(test_file)

def test_save_json(tmp_path):
    """Test pisanja JSON-a"""

    test_file = tmp_path / "output.json"
    test_data = {"items": [1, 2, 3]}

    save_json(test_data, test_file)

    # Proveri da fajl postoji
    assert test_file.exists()

    # Učitaj i uporedi
    loaded = load_json(test_file)
    assert loaded == test_data
```

Pokreni:

```bash
pytest tests/test_json_ops.py -v
```

---

### 5.3 Testiranje CLI Argumenta

Kreiraj `tests/test_cli_parsing.py`:

```python
import argparse
import pytest

def create_parser():
    """Helper za kreiranje parser-a"""
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input fajl")
    parser.add_argument("--format", choices=["json", "csv"], default="json")
    parser.add_argument("--verbose", action="store_true")
    return parser

def test_parser_defaults():
    """Test default vrednosti"""
    parser = create_parser()
    args = parser.parse_args(["test.txt"])

    assert args.input == "test.txt"
    assert args.format == "json"
    assert args.verbose is False

def test_parser_custom_values():
    """Test custom vrednosti"""
    parser = create_parser()
    args = parser.parse_args(["data.csv", "--format", "csv", "--verbose"])

    assert args.input == "data.csv"
    assert args.format == "csv"
    assert args.verbose is True

def test_parser_invalid_choice():
    """Test nevalidnog choice-a"""
    parser = create_parser()

    with pytest.raises(SystemExit):
        parser.parse_args(["test.txt", "--format", "xml"])
```

Pokreni:

```bash
pytest tests/test_cli_parsing.py -v
```

---

### 5.4 Testiranje Logging-a (caplog fixture)

Kreiraj `tests/test_logging.py`:

```python
import logging
import pytest

def process_data(items: list, logger: logging.Logger) -> int:
    """Primer funkcije koja loguje"""
    logger.info(f"Započinjem obradu {len(items)} stavki")

    processed = 0
    for item in items:
        if item > 0:
            logger.debug(f"Obrađujem: {item}")
            processed += 1
        else:
            logger.warning(f"Preskačem negativnu vrednost: {item}")

    logger.info(f"Obrađeno: {processed}/{len(items)}")
    return processed

def test_logging_info(caplog):
    """Test INFO logova"""

    logger = logging.getLogger("test")

    with caplog.at_level(logging.INFO):
        result = process_data([1, 2, 3], logger)

    assert result == 3
    assert "Započinjem obradu 3 stavki" in caplog.text
    assert "Obrađeno: 3/3" in caplog.text

def test_logging_warnings(caplog):
    """Test WARNING logova"""

    logger = logging.getLogger("test")

    with caplog.at_level(logging.WARNING):
        result = process_data([1, -5, 3], logger)

    assert result == 2
    assert "Preskačem negativnu vrednost: -5" in caplog.text

def test_logging_debug(caplog):
    """Test DEBUG logova"""

    logger = logging.getLogger("test")

    with caplog.at_level(logging.DEBUG):
        result = process_data([10, 20], logger)

    assert "Obrađujem: 10" in caplog.text
    assert "Obrađujem: 20" in caplog.text
```

Pokreni:

```bash
pytest tests/test_logging.py -v
```

---

## 🎓 BONUS FAZA: Pathlib (30-45 min)

### Pathlib Osnove

```python
from pathlib import Path

# Trenutni direktorijum
cwd = Path.cwd()
print(cwd)

# Home direktorijum
home = Path.home()
print(home)

# Kreiranje putanja
path = Path("data") / "users" / "profile.json"
print(path)  # data/users/profile.json

# Provere
path = Path("data/users.csv")
print(path.exists())
print(path.is_file())
print(path.is_dir())

# Delovi putanje
print(path.name)       # users.csv
print(path.stem)       # users
print(path.suffix)     # .csv
print(path.parent)     # data
print(path.absolute())

# Glob patterns
for p in Path("data").glob("*.csv"):
    print(p)

for p in Path("data").rglob("*.json"):  # Rekurzivno
    print(p)

# Kreiranje foldera
Path("output/reports").mkdir(parents=True, exist_ok=True)

# Čitanje/pisanje fajla
path = Path("test.txt")
path.write_text("Hello World", encoding="utf-8")
content = path.read_text(encoding="utf-8")
print(content)
```

---

## ✅ CHECKLIST — Proveri Da Li Si Savladao

-   [ ] Razumeš nivoe logovanja (DEBUG, INFO, WARNING, ERROR, CRITICAL)
-   [ ] Znaš razliku između Logger, Handler, Formatter
-   [ ] Možeš da konfigurišeš logging u konzolu I fajl istovremeno
-   [ ] Izbegavaš duplicate handlere sa `if not logger.handlers:`
-   [ ] Razumeš RotatingFileHandler i kada ga koristiti
-   [ ] Kreiraš CLI sa argparse (pozicioni + opcioni argumenti)
-   [ ] Koristiš boolean flagove (`action="store_true"`)
-   [ ] Ograničavaš izbor sa `choices`
-   [ ] Prihvataš više argumenata sa `nargs`
-   [ ] Razumeš subparsers (git-style komande)
-   [ ] Vraćaš exit kodove sa `sys.exit(0/1)`
-   [ ] Čitaš/pišeš JSON sa `json.load/dump`
-   [ ] Koristiš `ensure_ascii=False` za srpske znakove
-   [ ] Čitaš/pišeš CSV sa `DictReader/DictWriter`
-   [ ] Koristiš `newline=""` sa csv modulom
-   [ ] Konvertuješ CSV↔JSON
-   [ ] Validiraš JSON strukturu
-   [ ] Pišeš pytest testove za JSON/CSV funkcije
-   [ ] Testiš CLI parsing sa pytest
-   [ ] Testiš logging sa `caplog` fixture
-   [ ] Koristiš `tmp_path` fixture za test fajlove
-   [ ] (Bonus) Razumeš Path objekte i glob patterns

---

## 🎯 SLEDEĆI KORACI

1. **Refaktoriši csv_cleaner.py** sa novim znanjem (argparse + logging)
2. **Dodaj testove** u `projects/01-web-scraper/tests/`
3. **Implementiraj CLI** u `scraper.py` (--url, --output, --log-level)
4. **Kreiraj utility modul** `utils.py` sa reusable funkcijama

---

## 📚 DODATNI RESURSI

-   [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
-   [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
-   [CSV Module Docs](https://docs.python.org/3/library/csv.html)
-   [JSON Module Docs](https://docs.python.org/3/library/json.html)
-   [Pytest Docs](https://docs.pytest.org/)

---

**KRAJ VEŽBI** 🎉
