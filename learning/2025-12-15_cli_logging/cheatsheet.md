---
type: cheatsheet
topic: CLI + Logging + JSON/CSV — Quick Reference
date: 2025-12-15
linked_to: 2025-12-15_cli_logging
language: bilingual
status: active
---

# 🚀 CLI + Logging + JSON/CSV Cheatsheet

**Brzi referentni vodič za najčešće operacije**

---

## 📚 LOGGING

### BasicConfig — Najbrže

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("app")
logger.debug("Debug poruka")
logger.info("Info poruka")
logger.warning("Warning poruka")
logger.error("Error poruka")
logger.critical("Critical poruka")
```

---

### Console + File Logging

```python
import logging
from pathlib import Path

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Console handler (INFO i iznad)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

# File handler (DEBUG i iznad)
file_handler = logging.FileHandler("app.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Dodaj handlere (JEDNOM!)
if not logger.handlers:
    logger.addHandler(console)
    logger.addHandler(file_handler)

logger.info("Ovo ide u konzolu I fajl")
logger.debug("Ovo ide samo u fajl")
```

---

### RotatingFileHandler

```python
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    "app.log",
    maxBytes=5_000_000,  # 5MB
    backupCount=3,        # app.log.1, app.log.2, app.log.3
    encoding="utf-8"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
```

---

### Logging Nivoi

| Nivo     | Numerička Vrednost | Kada Koristiti                           |
| -------- | ------------------ | ---------------------------------------- |
| DEBUG    | 10                 | Detaljne info za debugging (dev only)    |
| INFO     | 20                 | Potvrdni događaji (app started, file OK) |
| WARNING  | 30                 | Upozorenja, ali app nastavlja            |
| ERROR    | 40                 | Ozbiljna greška, ali app još radi        |
| CRITICAL | 50                 | Najgori scenario, app se može srušiti    |

---

### Format Stringovi

| Kod             | Značenje                    |
| --------------- | --------------------------- |
| `%(asctime)s`   | Vreme (2025-12-15 14:23:45) |
| `%(levelname)s` | Nivo (DEBUG, INFO, itd.)    |
| `%(name)s`      | Ime logger-a                |
| `%(message)s`   | Log poruka                  |
| `%(filename)s`  | Ime fajla                   |
| `%(lineno)d`    | Broj linije                 |
| `%(funcName)s`  | Ime funkcije                |
| `%(pathname)s`  | Puna putanja fajla          |

---

## 🖥️ ARGPARSE — CLI

### Osnovni Parser

```python
import argparse

parser = argparse.ArgumentParser(
    prog="my-tool",
    description="Opis alata",
    epilog="Hvala što koristiš alat!"
)

# Pozicioni argument (obavezan)
parser.add_argument("input", help="Input fajl")

# Opcioni argument sa default-om
parser.add_argument(
    "--output", "-o",
    default="output.txt",
    help="Output fajl (default: output.txt)"
)

# Boolean flag
parser.add_argument(
    "--verbose", "-v",
    action="store_true",
    help="Detaljniji izlaz"
)

# Ograničene opcije
parser.add_argument(
    "--format",
    choices=["json", "csv", "xml"],
    default="json",
    help="Output format"
)

# Više argumenata
parser.add_argument(
    "files",
    nargs="+",  # Jedan ili više
    help="Fajlovi za obradu"
)

args = parser.parse_args()
print(args.input, args.output, args.verbose)
```

---

### Tipovi Argumenata

| `add_argument()` Opcija | Značenje                                |
| ----------------------- | --------------------------------------- |
| `"arg"`                 | Pozicioni (obavezan)                    |
| `"--arg"` ili `"-a"`    | Opcioni                                 |
| `type=int`              | Konvertuj u int (ili float, Path, itd.) |
| `default="val"`         | Default vrednost                        |
| `action="store_true"`   | Boolean flag (False ako nema)           |
| `choices=["a","b"]`     | Ograniči opcije                         |
| `nargs="+"`             | Jedan ili više argumenata               |
| `nargs="*"`             | Nula ili više argumenata                |
| `nargs=2`               | Tačno 2 argumenta                       |

---

### Subparsers (git-style)

```python
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True)

# Komanda: add
p_add = subparsers.add_parser("add", help="Dodaj fajl")
p_add.add_argument("file", help="Fajl za dodavanje")
p_add.set_defaults(func=cmd_add)

# Komanda: list
p_list = subparsers.add_parser("list", help="Lista fajlova")
p_list.add_argument("-r", "--recursive", action="store_true")
p_list.set_defaults(func=cmd_list)

args = parser.parse_args()
args.func(args)  # Pozovi funkciju
```

---

### Exit Kodovi

```python
import sys

# Uspeh
sys.exit(0)

# Greška
print("ERROR: Fajl ne postoji!", file=sys.stderr)
sys.exit(1)
```

---

## 📄 JSON

### Čitanje/Pisanje

```python
import json
from pathlib import Path

# Python dict → JSON string
data = {"name": "Ana", "age": 28}
json_str = json.dumps(data, ensure_ascii=False, indent=2)

# JSON string → Python dict
parsed = json.loads(json_str)

# Zapiši u fajl
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Učitaj iz fajla
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
```

---

### Error Handling

```python
try:
    data = json.loads(bad_json)
except json.JSONDecodeError as e:
    print(f"JSON Greška: {e.msg}")
    print(f"Linija {e.lineno}, kolona {e.colno}")
    sys.exit(1)
```

---

### Validacija

```python
data = json.load(f)

# Proveri tip
if not isinstance(data, list):
    raise ValueError(f"Očekujem listu, dobio {type(data)}")

# Proveri ključeve
for obj in data:
    if "id" not in obj or "name" not in obj:
        raise ValueError(f"Neispravan objekat: {obj}")
```

---

## 📊 CSV

### csv.reader/writer (Lista Redova)

```python
import csv

# Čitanje
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # Prva linija

    for row in reader:
        print(row)  # ['Ana', '28', 'Beograd']

# Pisanje
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Ana", 28, "Beograd"])
```

---

### DictReader/DictWriter (BOLJE!)

```python
import csv

# Čitanje
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)  # {'name': 'Ana', 'age': '28', 'city': 'Beograd'}

# Pisanje
users = [
    {"name": "Ana", "age": 28, "city": "Beograd"},
    {"name": "Marko", "age": 35, "city": "Novi Sad"}
]

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()  # Zapiši header red
    writer.writerows(users)
```

---

### CSV → JSON

```python
import csv
import json

# Čitaj CSV
users = []
with open("users.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["age"] = int(row["age"])  # Konvertuj tipove
        users.append(row)

# Zapiši JSON
with open("users.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)
```

---

### JSON → CSV

```python
import csv
import json

# Čitaj JSON
with open("users.json", "r", encoding="utf-8") as f:
    users = json.load(f)

# Zapiši CSV
with open("users.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = list(users[0].keys())
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users)
```

---

## 🧪 PYTEST

### Osnovna Struktura

```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

Pokreni:

```bash
pytest test_math.py -v
```

---

### tmp_path Fixture

```python
def test_file_ops(tmp_path):
    # tmp_path je Path objekat u temp folderu
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello")

    content = test_file.read_text()
    assert content == "Hello"
```

---

### caplog Fixture (Testiranje Logging-a)

```python
import logging

def process(items, logger):
    logger.info(f"Obrada {len(items)} stavki")
    return len(items)

def test_logging(caplog):
    logger = logging.getLogger("test")

    with caplog.at_level(logging.INFO):
        result = process([1, 2, 3], logger)

    assert result == 3
    assert "Obrada 3 stavki" in caplog.text
```

---

### pytest.raises

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Deljenje sa nulom!")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Deljenje sa nulom"):
        divide(10, 0)
```

---

## 📂 PATHLIB

### Osnove

```python
from pathlib import Path

# Trenutni direktorijum
cwd = Path.cwd()

# Home direktorijum
home = Path.home()

# Kreiranje putanja
path = Path("data") / "users" / "profile.json"

# Provere
path.exists()
path.is_file()
path.is_dir()

# Delovi putanje
path.name        # profile.json
path.stem        # profile
path.suffix      # .json
path.parent      # data/users
path.absolute()  # /home/user/code/data/users/profile.json
```

---

### Glob Patterns

```python
from pathlib import Path

# Svi CSV fajlovi u folderu
for p in Path("data").glob("*.csv"):
    print(p)

# Rekurzivno pretraži sve JSON fajlove
for p in Path("data").rglob("*.json"):
    print(p)

# Lista svih fajlova (ne foldera)
files = [p for p in Path("data").iterdir() if p.is_file()]
```

---

### Čitanje/Pisanje

```python
path = Path("test.txt")

# Zapiši text
path.write_text("Hello World", encoding="utf-8")

# Čitaj text
content = path.read_text(encoding="utf-8")

# Zapiši bytes
path.write_bytes(b"\x00\x01\x02")

# Čitaj bytes
data = path.read_bytes()
```

---

### Kreiranje/Brisanje

```python
# Kreiraj folder
Path("output/reports").mkdir(parents=True, exist_ok=True)

# Obriši fajl
Path("test.txt").unlink(missing_ok=True)

# Obriši prazan folder
Path("temp").rmdir()
```

---

## 🔧 INTEGRISANI PRIMER

```python
#!/usr/bin/env python3
import argparse
import csv
import json
import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

def setup_logging(level: str) -> logging.Logger:
    logger = logging.getLogger("app")
    logger.setLevel(getattr(logging, level))

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        "app.log", maxBytes=5_000_000, backupCount=3
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console)
        logger.addHandler(file_handler)

    return logger

def csv_to_json(input_path: Path, output_path: Path, logger: logging.Logger):
    logger.info(f"CSV→JSON: {input_path} → {output_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    logger.info(f"✅ Konvertovano {len(data)} redova")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--log-level", default="INFO",
                        choices=["DEBUG", "INFO", "WARNING"])

    args = parser.parse_args()
    logger = setup_logging(args.log_level)

    try:
        csv_to_json(args.input, args.output, logger)
    except Exception as e:
        logger.exception(f"Greška: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

## 📌 Najčešće Greške

### Logging

-   ❌ Dupliranje handlera → ✅ Proveri `if not logger.handlers:`
-   ❌ Previsok nivo (WARNING) → ✅ Postavi DEBUG/INFO za dev
-   ❌ Koristiti `print()` → ✅ Koristiti `logger.info()`

### Argparse

-   ❌ Ne testiraš `--help` → ✅ Uvek testiraj help output
-   ❌ Loši opisi argumenta → ✅ Piši jasne `help=` stringove
-   ❌ Ne vraćaš exit kod → ✅ Uvek vraćaj `sys.exit(0/1)`

### JSON

-   ❌ Zaboraviti `ensure_ascii=False` → ✅ Uvek za srpske znakove
-   ❌ Ne handlovati `JSONDecodeError` → ✅ Uvek `try/except`

### CSV

-   ❌ Zaboraviti `newline=""` → ✅ Uvek dodaj na Windows-u
-   ❌ Koristiti `reader` umesto `DictReader` → ✅ `DictReader` je čitljiviji
-   ❌ Ne zapisati header → ✅ `writeheader()` PRE `writerows()`

---

**KRAJ CHEATSHEET-a** 📖
Za detaljnije vežbe vidi [cli_logging_complete_exercises.md](cli_logging_complete_exercises.md)
DATA_FILE = SCRIPT_DIR / "data" / "sample.csv"

with DATA_FILE.open(newline="", encoding="utf-8") as f:
reader = csv.DictReader(f) # ...

````

## 4. Moderni import skeleton

```python
from __future__ import annotations

import argparse
import csv
import logging
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import TypedDict

LOGGER = logging.getLogger(__name__)

class Row(TypedDict):
    name: str
    age: int

def load_data(path: Path) -> list[Row]:
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(Row(name=row["name"], age=int(row["age"])))
    return rows

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()

    LOGGER.info("Loading from %s", args.input)
    data = load_data(args.input)
    LOGGER.info("Loaded %d rows", len(data))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
````

## 5. Tipske anotacije (Python 3.9+)

-   ✅ Koristi ugrađene: `list[str]`, `dict[str, int]`, `tuple[int, str]`
-   ✅ `collections.abc` za apstrakcije: `Iterable`, `Sequence`, `Mapping`
-   ✅ `typing` za special: `TypedDict`, `Any`, `Literal`, `Protocol`
-   ❌ Izbegavaj `typing.List`, `typing.Dict` (zastarelo)
-   ❌ Izbegavaj string putanja – koristi `Path`

## 6. CSV + DictReader (sa tipima)

```python
from csv import DictReader
from pathlib import Path
from typing import TypedDict

class Product(TypedDict):
    id: str
    name: str
    price: float

def read_products(path: Path) -> list[Product]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = DictReader(f)
        return [
            Product(id=row["id"], name=row["name"], price=float(row["price"]))
            for row in reader
        ]
```

## 7. Brzi checklist

-   [ ] Importi sortirani (stdlib, third-party, local)
-   [ ] Nema `typing.List/Dict` – samo `list[...]`, `dict[...]`
-   [ ] `Path` za sve datoteke (ne string)
-   [ ] Logger umesto `print`
-   [ ] `__future__.annotations` na vrhu (za kompatibilnost)
-   [ ] Sve funkcije imaju type hints

---

**Više detalja:** [../../../scratch/docs/cheatsheet_modern_mypy_pylance.md](../../../scratch/docs/cheatsheet_modern_mypy_pylance.md)
