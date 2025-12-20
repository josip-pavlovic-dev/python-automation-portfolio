---
type: cheatsheet
topic: File Types + Type Annotations — Quick Reference
date: 2025-12-18
language: bilingual
difficulty: beginner-intermediate
---

# 📘 Cheatsheet: Type Annotations — Quick Reference

## ✅ Osnove (Za Brzu Pretragu)

### Type Hints — Bazični Tipovi

```python
from typing import Optional
from collections.abc import Sequence, Iterable, Mapping

# Primitivi
age: int = 25
name: str = "Jole"
height: float = 1.85
active: bool = True

# Kolekcije (Python 3.9+)
numbers: list[int] = [1, 2, 3]
user: dict[str, str] = {"name": "Jole"}
coords: tuple[float, float] = (45.8, 15.9)
tags: set[str] = {"python", "automation"}

# Optional (može biti None)
email: str | None = None  # Modern (3.10+)
email: Optional[str] = None  # Stari način

# Funkcije
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

def process(items: list[str]) -> None:
    for item in items:
        print(item)
```

---

## 📦 TypedDict — Za CSV/JSON Redove

### Osnovna TypedDict

```python
from typing import TypedDict

class User(TypedDict):
    """Struktura korisnika"""
    name: str
    age: int
    email: str | None

# Upotreba
user: User = {
    "name": "Jole",
    "age": 30,
    "email": "jole@example.com"
}

# Sa CSV DictReader
import csv
from pathlib import Path

users: list[User] = []
with open("users.csv", newline='') as f:
    for row in csv.DictReader(f):
        user: User = {
            "name": row["name"],
            "age": int(row["age"]),
            "email": row.get("email")
        }
        users.append(user)
```

### TypedDict sa NotRequired (3.11+)

```python
from typing import NotRequired

class PersonRecord(TypedDict):
    name: str
    age: int
    email: NotRequired[str]  # Opciono polje
```

---

## 🎯 Protocol — Za Argparse Args

### Osnovna Protocol

```python
from typing import Protocol

class ProcessArgs(Protocol):
    input_file: str
    output_file: str | None
    verbose: bool
    limit: int

def process(args: ProcessArgs) -> None:
    """Handler funkcija sa tipskom sigurnošću"""
    print(f"Processing: {args.input_file}")
    if args.verbose:
        print(f"Limit: {args.limit}")
```

### Sa argparse

```python
import argparse
from typing import Protocol, cast

class ProcessArgs(Protocol):
    input: str
    output: str | None
    verbose: bool

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("-o", "--output", dest="output")
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()
    typed_args: ProcessArgs = cast(ProcessArgs, args)

    process(typed_args)
```

---

## 🆕 Modern Python Types (3.10+)

### Union sa |

```python
# Staro
from typing import Union
result: Union[str, int, None] = None

# Novo (bolje!)
result: str | int | None = None
```

### Literal — Ograničene Vrednosti

```python
from typing import Literal

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]

def set_log_level(level: LogLevel) -> None:
    print(f"Log level: {level}")

set_log_level("DEBUG")       # ✅ OK
set_log_level("TRACE")       # ❌ Pylance: Invalid Literal value
```

### from **future** import annotations

```python
from __future__ import annotations

# Omogući forward references bez stringova
def process(items: list[Item]) -> Item:
    return items[0]

class Item:
    """Klasa se može referensirati pre nego što je definisana"""
    pass
```

---

## 📚 Collections.abc — Apstraktne Kolekcije

```python
from collections.abc import Iterable, Sequence, Mapping, Callable

# Iterable — bilo šta što se može iterirati
def process_items(items: Iterable[str]) -> None:
    for item in items:
        print(item)

# Sequence — list-like (sa indexom)
def first_element(seq: Sequence[str]) -> str:
    return seq[0]

# Mapping — dict-like
def get_value(m: Mapping[str, str], key: str) -> str:
    return m[key]

# Callable — funkcije
def apply(op: Callable[[int, int], int], a: int, b: int) -> int:
    return op(a, b)
```

---

## 🔧 Type Checking sa mypy

### Instalacija

```bash
pip install mypy
```

### Pokretanje

```bash
# Proveri jedan fajl
mypy script.py

# Proveri ceo folder sa strict mode
mypy --strict sandbox/basics/

# Detaljnije poruke
mypy --show-error-codes script.py
mypy --show-traceback script.py

# Ignore greške u specifičnom liniji (ako je zaista potrebno)
value = some_function()  # type: ignore
```

### Ignoring problematic code

```python
# Ako MORA biti loose (izbegavaj!)
from typing import Any

def process(data: Any) -> None:
    print(data['field'])  # mypy ignores this

# Bolje — cast to specific type
from typing import cast

def process(data: dict[str, str]) -> None:
    typed = cast(dict[str, str], data)
    print(typed['field'])
```

---

## ✨ Best Practices (TL;DR)

### ❌ NE RADITI

```python
# Stari tipovi
from typing import List, Dict, Set, Tuple
data: List[str] = []  # ❌ Ne!

# os.path umesto Path
import os
path: str = "data/file.csv"  # ❌ Ne!

# Type ignore svugde
value = something()  # type: ignore  # ❌ Ne!

# Magic strings za imports
from typing import *  # ❌ Ne!
```

### ✅ RADITI

```python
# Novi tipovi
data: list[str] = []  # ✅ Da!

# Path umesto stringa
from pathlib import Path
path: Path = Path("data/file.csv")  # ✅ Da!

# Koristi cast gde je zaista potrebno
from typing import cast
typed_args: ProcessArgs = cast(ProcessArgs, args)

# Eksplicitan import
from collections.abc import Iterable, Callable
from typing import TypedDict, Protocol, Literal
```

---

## 🧪 CSV + Types — Brzi Primer

```python
from pathlib import Path
import csv
from typing import TypedDict

class PersonRecord(TypedDict):
    name: str
    age: int
    city: str

def load_csv(filepath: Path) -> list[PersonRecord]:
    """Učitaj CSV sa tipskom sigurnošću"""
    records: list[PersonRecord] = []
    with open(filepath, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            person: PersonRecord = {
                'name': row['name'],
                'age': int(row['age']),
                'city': row['city']
            }
            records.append(person)
    return records

def main() -> None:
    people = load_csv(Path("data/people.csv"))
    for person in people:
        print(f"{person['name']}: {person['age']}")

if __name__ == "__main__":
    main()
```

---

## 🎯 JSON + Types — Brzi Primer

```python
import json
from pathlib import Path
from typing import TypedDict

class Config(TypedDict):
    app_name: str
    version: str
    debug: bool

def load_config(path: Path) -> Config:
    """Učitaj JSON config sa tipima"""
    with open(path) as f:
        data = json.load(f)
    return Config(
        app_name=data["app_name"],
        version=data["version"],
        debug=data["debug"]
    )

def main() -> None:
    config = load_config(Path("config.json"))
    print(f"{config['app_name']} v{config['version']}")

if __name__ == "__main__":
    main()
```

---

## 📖 Validacija — Znošs li?

-   [ ] Mogu da napišem `def func(x: int) -> str:`
-   [ ] Znam šta je TypedDict
-   [ ] Znam šta je Protocol
-   [ ] Mogu da koristim `mypy`
-   [ ] Razumem `from __future__ import annotations`
-   [ ] Znam razliku `collections.abc` vs `typing`
-   [ ] Mogu da refaktorisem postojeći kod sa tipima
-   [ ] Mogu da napravim TypedDict za CSV redove

**Min. 6/8 YES → Spreman za praktične vežbe!**

---

**Koristi ovaj cheatsheet kao reference tokom Dana 5! 🔥**
