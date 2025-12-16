# Cheatsheet: CLI + Logging + Moderni Importi

## 1. argparse – CLI argumenti

```python
import argparse

parser = argparse.ArgumentParser(description="Demo app")
parser.add_argument("--input", type=Path, required=True, help="Input file")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

print(args.input, args.verbose)
```

## 2. logging – Logovanje umesto print()

```python
import logging

LOGGER = logging.getLogger(__name__)

# U main:
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# U kodu:
LOGGER.info("Starting process")
LOGGER.warning("Be careful!")
LOGGER.error("Something went wrong")
```

### Sa rotacijom (za log file)

```python
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app.log", maxBytes=5*1024*1024, backupCount=3)
logging.basicConfig(handlers=[handler], level=logging.INFO)
```

## 3. Path – Stabilne putanje (umesto stringova)

```python
from pathlib import Path

# Gde se nalazi skripta
SCRIPT_DIR = Path(__file__).parent
DATA_FILE = SCRIPT_DIR / "data" / "sample.csv"

with DATA_FILE.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # ...
```

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
```

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
