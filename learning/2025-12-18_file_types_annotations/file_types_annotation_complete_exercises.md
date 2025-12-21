---
type: exercises
topic: File Types + Type Annotations — Python Type System za Automaciju
date: 2025-12-18
linked_to: python-automation-portfolio
language: bilingual
status: active
difficulty: beginner-intermediate
environment: python_repl + files
estimated_time: 8 hours
phase: foundation
milestone: type_safety_mastery
---

# 🎯 File Types + Type Annotations — KOMPLETNE VEŽBE (8h)

## 🎬 INTRO — Zašto Type Annotations?

**Problem koji rešavamo:**

-   Imaš `args` u CLI i ne znaš koji tip je
-   Linter se žali "Type of parameter is unknown"
-   Pisaćeš kod koji će pisati drugi → trebaju mu tipovi
-   CSV `DictReader` vraća šta? Koja polja su u `dict`-u?
-   Web scraper vraća liste šta? Šta su elementi?

**Rešenje:** Type annotations + modern Python 3.10+

---

## 📚 PREDZNANJE (Čitaj Pre Nego Što Počneš)

### Files da Pročitaš

1. [scratch/docs/cheatsheet_csv_annotations.md](../../scratch/docs/cheatsheet_csv_annotations.md) — CSV + Type Hints (15 min)
2. [scratch/docs/cheatsheet_modern_mypy_pylance.md](../../scratch/docs/cheatsheet_modern_mypy_pylance.md) — Modern Imports (20 min)

### Šta Trebao da Znaš Pre

-   Python `if __name__ == "__main__":` (iz Dan 1)
-   Argparse + subparsers (iz Dan 2 - cli_logging)
-   CSV reader/writer (iz Dan 0 - csv_basics)
-   Logging setup (iz Dan 2 - logging)

---

# 🏁 FAZA 1: OSNOVE TYPE ANNOTATIONS (1.5 sata)

## 1.1 | Šta Je Type Annotation?

**Teorija (SRB, 2-3 rečenice):**
Type annotation je "napomena" za type checker (Pylance) — Python je ne koristi pri izvršavanju. Pisaš `x: int = 5` i time kažeš: "x je tipa int". Type checker ti hvata greške pre nego što pokreneš kod — ako kasnije napraviš `x = "string"` ili `x + y` gde `y` nije int, upozoriće te.

**REPL vežba:**

```python
# 1. Otvori Python REPL
python3

# 2. Bez anotacija — Python ignoriše, ali šta je x?
x = 5
print(type(x))  # <class 'int'>

# 3. Sa anotacijom — samo za type checker
x: int = 5
print(x)  # Output: 5
print(type(x))  # <class 'int'> — Python ga ignoriše!

# 4. Pogrešna vrednost — Python je svakako sprema
x: int = "string"  # ✅ Python ne pravi problem
print(x)  # Output: "string"
print(type(x))  # <class 'str'> — Python je tretira kao string!

# 5. ALI — Pylance će se žaliti!
# (Ako koristiš VSCode sa Pylance extension-om)
```

**Zaključak:** Type annotations su "napomene" — Python ih ignoriše, ali **Pylance** (type checker) proverava pre nego što pokreneš kod.

---

## 1.2 | Osnove Type Hints

Kreiraj fajl `sandbox/basics/cli_logging_practice/scripts/type_annotations_intro.py`:

```python
"""
Demo: Osnove Type Annotations
"""

# 1. PRIMITIVI
age: int = 25
name: str = "Jole"
height: float = 1.85
is_active: bool = True

# 2. KOMPLEKSNI TIPOVI
from typing import Optional  # Za stariji Python kod; 3.10+ koristi X | None

# Opciona vrednost — može biti string ili None
maybe_email: Optional[str] = None  # Ili: str | None (3.10+)
maybe_email = "jole@example.com"   # OK
maybe_email = None                 # OK

# 3. FUNKCIJE
def add(a: int, b: int) -> int:
    """Dodaj dva broja"""
    return a + b

result: int = add(3, 5)
print(result)  # 8

# 4. FUNKCIJE SA OPTIONAL PARAMETRIMA
def greet(name: str, greeting: str = "Zdravo") -> str:
    """Pozdrav sa default parametrom"""
    return f"{greeting}, {name}!"

msg: str = greet("Ana")  # Koristi default
print(msg)  # Zdravo, Ana!

# 5. LISTE
numbers: list[int] = [1, 2, 3, 4, 5]  # Nova sintaksa (3.9+)
# Alternativa (starija): from typing import List; numbers: List[int] = [1, 2, 3]

# 6. REČNICI
user: dict[str, str] = {"name": "Jole", "city": "Beograd"}
# ili: from typing import Dict; user: Dict[str, str] = ...

# 7. TUPLE (fiksna dužina, različiti tipovi)
coordinates: tuple[float, float] = (45.8150, 15.9819)  # Beograd

# 8. SET
unique_cities: set[str] = {"Beograd", "Novi Sad", "Niš"}
```

Pokreni:

```bash
python3 sandbox/basics/cli_logging_practice/scripts/type_annotations_intro.py
# Output: sve prosledi (8 bez greške)
```

Sada uključi type checking:

```bash
# Trebalo bi da imaš mypy instaliran; ako nemaš:
pip install mypy

# Proveri tipove
mypy sandbox/basics/cli_logging_practice/scripts/type_annotations_intro.py
# Output: Success: no issues found in 1 source file
```

---

## 1.3 | Greške koje Type Checker Hvata

Kreiraj `sandbox/basics/cli_logging_practice/scripts/type_errors_demo.py`:

```python
"""
Greške koje mypy/Pylance hvata
"""

def add(a: int, b: int) -> int:
    return a + b

# ❌ GREŠKA 1: Pogrešan tip argumenta
result1: int = add("3", 5)  # mypy: error: Argument 1 to "add" has incompatible type "str"; expected "int"

# ❌ GREŠKA 2: Pogrešan tip povratne vrednosti
def get_name() -> str:
    return 42  # mypy: error: Incompatible return value type (got "int", expected "str")

# ❌ GREŠKA 3: Pristup atributu koji ne postoji
name: str = "Jole"
print(name.upper())  # OK
print(name.invalid_method())  # mypy: error: "str" has no attribute "invalid_method"

# ❌ GREŠKA 4: Pristup list elementu pogrešnog tipa
numbers: list[int] = [1, 2, 3]
value: int = numbers[0]  # OK
value: str = numbers[0]  # mypy: error: Incompatible types in assignment

# ❌ GREŠKA 5: None pristup
maybe_name: str | None = None
print(maybe_name.upper())  # mypy: error: Item "None" has no attribute "upper"

# ✅ ISPRAVKA: Proveri prvo
if maybe_name is not None:
    print(maybe_name.upper())  # OK
```

Pokreni mypy:

```bash
mypy sandbox/basics/type_errors_demo.py

# Output (3 greške):
# error: Argument 1 to "add" has incompatible type "str"; expected "int"
# error: Incompatible return value type (got "int", expected "str")
# error: "str" has no attribute "invalid_method"
# ...
```

**Zaključak:** mypy/Pylance hvata greške pre nego što pokreneš kod! To ti štedi sate debugovanja.

---

# 🏗️ FAZA 2: CSV + TYPE ANNOTATIONS (1.5 sata)

## 2.1 | CSV Reader Tipizacija

Kreiraj test CSV:

```bash
mkdir -p sandbox/basics/type_exercises_data
cat > sandbox/basics/type_exercises_data/users.csv << 'EOF'
name,age,city
Jole,30,Beograd
Ana,28,Novi Sad
Marko,35,Nis
EOF
```

Kreiraj `sandbox/basics/csv_with_types.py`:

```python
"""
CSV sa Type Annotations — DictReader verzija
"""
from pathlib import Path
import csv
from typing import TypedDict

# 1. Definiši strukturu podataka sa TypedDict
class UserRecord(TypedDict):
    """Struktura jednog reda iz users.csv"""
    name: str
    age: str  # CSV je sve stringovi!
    city: str

# 2. Helper funkcija za čitanje
def load_users(filepath: Path) -> list[UserRecord]:
    """Učitaj korisnike iz CSV fajla sa type safety-jem"""
    users: list[UserRecord] = []

    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row is not None:  # DictReader može vratiti None za prazne redove
                user: UserRecord = {
                    'name': row['name'],
                    'age': row['age'],
                    'city': row['city']
                }
                users.append(user)

    return users

# 3. Main
def main() -> None:
    data_dir = Path(__file__).parent / "type_exercises_data"
    csv_file = data_dir / "users.csv"

    users = load_users(csv_file)

    for user in users:
        print(f"{user['name']} ({user['age']}) iz {user['city']}")

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
python3 sandbox/basics/csv_with_types.py

# Output:
# Jole (30) iz Beograd
# Ana (28) iz Novi Sad
# Marko (35) iz Nis
```

Proveri sa mypy:

```bash
mypy sandbox/basics/csv_with_types.py
# Success: no issues found in 1 source file
```

---

## 2.2 | CSV Writer sa Tipima

Kreiraj `sandbox/basics/csv_write_with_types.py`:

```python
"""
CSV pisanje sa Type Annotations
"""
from pathlib import Path
import csv
from typing import TypedDict

class PersonRecord(TypedDict):
    """Format osobe"""
    ime: str
    godine: str
    grad: str

def save_people(people: list[PersonRecord], output_path: Path) -> None:
    """Sačuva listu osoba u CSV"""
    fieldnames = ['ime', 'godine', 'grad']

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(people)

def main() -> None:
    # Pripremi podatke
    people: list[PersonRecord] = [
        {'ime': 'Jole', 'godine': '30', 'grad': 'Beograd'},
        {'ime': 'Ana', 'godine': '28', 'grad': 'Novi Sad'},
        {'ime': 'Stefan', 'godine': '35', 'grad': 'Niš'},
    ]

    # Sačuva
    output_dir = Path(__file__).parent / "type_exercises_data"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "output_people.csv"

    save_people(people, output_file)
    print(f"✅ Sačuvano u {output_file}")

    # Pročitaj nazad
    with open(output_file, newline='', encoding='utf-8') as f:
        print("\n📖 Sadržaj:")
        print(f.read())

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
python3 sandbox/basics/csv_write_with_types.py
# ✅ Sačuvano u sandbox/basics/type_exercises_data/output_people.csv
```

---

## 2.3 | CSV sa Konverzijom Tipova

Kreiraj `sandbox/basics/csv_with_conversion.py`:

```python
"""
CSV sa konverzijom stringova u prave tipove
"""
from pathlib import Path
import csv
from typing import TypedDict, NotRequired

# TypedDict sa NotRequired (3.11+) — polja koja nisu obavezna
class UserStrict(TypedDict):
    """Stroga tipizacija — svi stringovi"""
    name: str
    age: str
    city: str

class UserConverted(TypedDict):
    """Konvertovani tipovi — age je integer"""
    name: str
    age: int  # Ovo će biti integer
    city: str

def load_and_convert(csv_path: Path) -> list[UserConverted]:
    """Učitaj CSV i konvertuj age u integer"""
    users: list[UserConverted] = []

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row and 'name' in row and 'age' in row and 'city' in row:
                try:
                    user: UserConverted = {
                        'name': row['name'].strip(),
                        'age': int(row['age']),  # Konverzija!
                        'city': row['city'].strip()
                    }
                    users.append(user)
                except ValueError as e:
                    print(f"⚠️ Greška pri konverziji: {row['age']} nije integer — {e}")

    return users

def main() -> None:
    csv_file = Path(__file__).parent / "type_exercises_data" / "users.csv"
    users = load_and_convert(csv_file)

    for user in users:
        # Sada age je integer
        next_age: int = user['age'] + 1
        print(f"{user['name']}: Sada {user['age']}, sledeće godine {next_age}")

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
python3 sandbox/basics/csv_with_conversion.py
# Jole: Sada 30, sledeće godine 31
# Ana: Sada 28, sledeće godine 29
# Marko: Sada 35, sledeće godine 36
```

---

# 🎛️ FAZA 3: ARGPARSE + TYPE ANNOTATIONS (1.5 sata)

## 3.1 | Protocol Classes za CLI Args

Kreiraj `sandbox/basics/cli_with_types.py`:

```python
"""
CLI sa Type Annotations - Protocol klase za args
"""
import argparse
from typing import Protocol
from pathlib import Path

# 1. Definiši šta očekuješ od args objekta
class ProcessArgs(Protocol):
    """Struktura argumenata za process komandu"""
    input_file: str
    output_file: str | None
    verbose: bool
    limit: int

# 2. Handler funkcije sa tipizacijom
def cmd_process(args: ProcessArgs) -> None:
    """Process komanda"""
    input_path = Path(args.input_file)

    if not input_path.exists():
        print(f"❌ Fajl ne postoji: {input_path}")
        return

    print(f"📖 Procesuiram: {args.input_file}")
    if args.verbose:
        print(f"   - Limit: {args.limit}")
        if args.output_file:
            print(f"   - Output: {args.output_file}")

# 3. Main sa argparse
def main() -> None:
    parser = argparse.ArgumentParser(
        prog="file_processor",
        description="Procesuira fajlove sa tipskom sigurnošću"
    )

    parser.add_argument("input_file", help="Ulazni fajl")
    parser.add_argument("-o", "--output", dest="output_file", help="Izlazni fajl")
    parser.add_argument("-v", "--verbose", action="store_true", help="Detaljni ispis")
    parser.add_argument("-l", "--limit", type=int, default=100, help="Limit redova")

    args = parser.parse_args()

    # Type cast ako trebá (Python to radi automatski pri argparse)
    typed_args: ProcessArgs = args  # type: ignore  # Ili koristi cast()

    cmd_process(typed_args)

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
python3 sandbox/basics/cli_with_types.py --help

python3 sandbox/basics/cli_with_types.py sandbox/basics/type_exercises_data/users.csv -v -l 50

# Output:
# 📖 Procesuiram: sandbox/basics/type_exercises_data/users.csv
#    - Limit: 50
```

---

## 3.2 | Protocol + cast() za Type Safety

Kreiraj `sandbox/basics/cli_with_cast.py`:

```python
"""
Bolje: Koristi cast() umesto type: ignore
"""
import argparse
from typing import Protocol, cast
from pathlib import Path

class ProcessArgs(Protocol):
    input_file: str
    output_file: str | None
    verbose: bool
    limit: int

def cmd_process(args: ProcessArgs) -> None:
    input_path = Path(args.input_file)
    print(f"📖 Procesuiram: {input_path}")
    if args.verbose:
        print(f"   - Limit: {args.limit}")
        if args.output_file:
            print(f"   - Output: {args.output_file}")

def main() -> None:
    parser = argparse.ArgumentParser(prog="file_processor")
    parser.add_argument("input_file")
    parser.add_argument("-o", "--output", dest="output_file")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-l", "--limit", type=int, default=100)

    args = parser.parse_args()

    # BOLJE: Koristi cast() - jasno je da konvertuješ
    typed_args: ProcessArgs = cast(ProcessArgs, args)

    cmd_process(typed_args)

if __name__ == "__main__":
    main()
```

---

# 📁 FAZA 4: JSON + TYPE ANNOTATIONS (1 sat)

## 4.1 | JSON Tipizacija sa TypedDict

Kreiraj test JSON:

```bash
cat > sandbox/basics/type_exercises_data/config.json << 'EOF'
{
  "app_name": "DataProcessor",
  "version": "1.0.0",
  "settings": {
    "debug": true,
    "timeout": 30
  }
}
EOF
```

Kreiraj `sandbox/basics/json_with_types.py`:

```python
"""
JSON sa Type Annotations
"""
import json
from pathlib import Path
from typing import TypedDict, NotRequired

# 1. Definiši struktu JSON-a
class Settings(TypedDict):
    """Nested TypedDict"""
    debug: bool
    timeout: int

class Config(TypedDict):
    """Struktura config.json"""
    app_name: str
    version: str
    settings: Settings

def load_config(json_path: Path) -> Config:
    """Učitaj config sa tipskom sigurnošću"""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Type checker sada zna šta je u `data`
    config: Config = {
        'app_name': data['app_name'],
        'version': data['version'],
        'settings': {
            'debug': data['settings']['debug'],
            'timeout': data['settings']['timeout']
        }
    }
    return config

def main() -> None:
    json_file = Path(__file__).parent / "type_exercises_data" / "config.json"
    config = load_config(json_file)

    print(f"🔧 Aplikacija: {config['app_name']} v{config['version']}")
    print(f"   Debug: {config['settings']['debug']}")
    print(f"   Timeout: {config['settings']['timeout']}s")

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
python3 sandbox/basics/json_with_types.py
# 🔧 Aplikacija: DataProcessor v1.0.0
#    Debug: True
#    Timeout: 30s
```

---

## 4.2 | Pisanje JSON sa Tipima

Kreiraj `sandbox/basics/json_write_with_types.py`:

```python
"""
Pisanje JSON sa Type Annotations
"""
import json
from pathlib import Path
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str | None

class Database(TypedDict):
    version: str
    people: list[Person]

def save_database(db: Database, output_path: Path) -> None:
    """Sačuva database u JSON"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def main() -> None:
    # Pripremi podatke
    db: Database = {
        'version': '1.0',
        'people': [
            {'name': 'Jole', 'age': 30, 'email': 'jole@example.com'},
            {'name': 'Ana', 'age': 28, 'email': None},
        ]
    }

    output_dir = Path(__file__).parent / "type_exercises_data"
    output_path = output_dir / "database.json"

    save_database(db, output_path)
    print(f"✅ Sačuvano u {output_path}")

if __name__ == "__main__":
    main()
```

Pokreni:

```bash
python3 sandbox/basics/json_write_with_types.py
cat sandbox/basics/type_exercises_data/database.json
```

---

# 🧮 FAZA 5: KOMPLEKSNE TIPIZACIJE (1 sat)

## 5.1 | Union Tipovi i Literal

Kreiraj `sandbox/basics/complex_types.py`:

```python
"""
Kompleksnije tipizacije
"""
from typing import Literal, Union
from pathlib import Path

# 1. UNION — više mogućih tipova
def process_data(data: str | int | list[str]) -> str:
    """Prihvata više tipova"""
    if isinstance(data, str):
        return f"String: {data}"
    elif isinstance(data, int):
        return f"Number: {data}"
    else:
        return f"List sa {len(data)} elementa"

# 2. LITERAL — ograničene vrednosti
def set_log_level(level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]) -> None:
    """Samo ove vrednosti su dozvoljene"""
    print(f"Log level: {level}")

# 3. Callable — funkcije kao tipovi
def apply_operation(a: int, b: int, op: Callable[[int, int], int]) -> int:
    """Prihvata funkciju kao argument"""
    return op(a, b)

from typing import Callable

def test() -> None:
    # OK
    print(process_data("hello"))
    print(process_data(42))
    print(process_data(["a", "b", "c"]))

    # OK
    set_log_level("DEBUG")

    # ❌ Greška — Pylance javlja
    # set_log_level("TRACE")  # Not a Literal value

    # Callable test
    result = apply_operation(5, 3, lambda x, y: x + y)
    print(f"5 + 3 = {result}")

if __name__ == "__main__":
    test()
```

---

## 5.2 | Generic Tipovi — Svoju Klasu sa Tipima

Kreiraj `sandbox/basics/generic_types.py`:

```python
"""
Generički tipovi za sopstvene klase
"""
from typing import TypeVar, Generic, Optional

# TypeVar — varijabla tipa (kao template)
T = TypeVar('T')

class Container(Generic[T]):
    """Generička klasa koja čuva bilo šta"""

    def __init__(self, value: T) -> None:
        self.value: T = value

    def get(self) -> T:
        return self.value

    def set(self, value: T) -> None:
        self.value = value

def test() -> None:
    # Container sa stringom
    str_container: Container[str] = Container("hello")
    text: str = str_container.get()
    print(f"Text: {text}")

    # Container sa brojem
    int_container: Container[int] = Container(42)
    number: int = int_container.get()
    print(f"Number: {number}")

    # Container sa listom
    list_container: Container[list[str]] = Container(["a", "b", "c"])
    items: list[str] = list_container.get()
    print(f"Items: {items}")

if __name__ == "__main__":
    test()
```

---

# 🔗 FAZA 6: INTEGRACIJA SA TVOJIM PROJEKTIMA (1.5 sata)

## 6.1 | Refaktoriši basic_cli.py sa Tipima

Kreiraj `sandbox/basics/cli_logging_practice/scripts/basic_cli_typed.py`:

```python
"""
Refaktorisani basic_cli.py sa type annotations
"""
from __future__ import annotations

import argparse
import logging
from typing import Optional

# Logger setup
logger = logging.getLogger("basic_cli")

def positive_int(value: str) -> int:
    """Validator — vrednost mora biti pozitivan broj"""
    ivalue = int(value)
    if ivalue < 0:
        raise argparse.ArgumentTypeError("Age must be non-negative")
    return ivalue

def configure_logging(verbose: int) -> None:
    """Konfiguracija logovanja prema verbosity levelu"""
    level = logging.WARNING
    if verbose == 1:
        level = logging.INFO
    elif verbose >= 2:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger.debug("Logger configured")

def main(argv: Optional[list[str]] = None) -> int:
    """Glavna funkcija sa tipskom sigurnošću"""
    parser = argparse.ArgumentParser(
        prog="basic_cli",
        description="CLI alat sa tipskim anotacijama"
    )

    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="Verbosity (-v, -vv)")
    parser.add_argument("name", help="Your name")
    parser.add_argument("age", type=positive_int, help="Your age (>= 0)")

    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    logger.info("Starting application")
    print(f"Zdravo, {args.name}! Imaš {args.age} godina.")
    logger.debug(f"Processed: name={args.name}, age={args.age}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

Pokreni:

```bash
python3 sandbox/basics/cli_logging_practice/scripts/basic_cli_typed.py Jole 30
python3 sandbox/basics/cli_logging_practice/scripts/basic_cli_typed.py Jole 30 -v
python3 sandbox/basics/cli_logging_practice/scripts/basic_cli_typed.py Jole 30 -vv
```

Proveri sa mypy:

```bash
mypy sandbox/basics/cli_logging_practice/scripts/basic_cli_typed.py
# Success: no issues found
```

---

## 6.2 | Tipizacija subcommands_cli.py

Kreiraj `sandbox/basics/cli_logging_practice/scripts/subcommands_cli_typed.py`:

```python
"""
Refaktorisani subcommands_cli.py sa type annotations
"""
from __future__ import annotations

import argparse
import logging
from typing import Protocol, Callable

logger = logging.getLogger("datatools")

# 1. Definiši strukture za svaku komandu
class ListArgs(Protocol):
    path: str
    recursive: bool
    verbose: bool

class SearchArgs(Protocol):
    pattern: str
    file: str
    verbose: bool

class ExportArgs(Protocol):
    format: str
    output: str | None
    verbose: bool

# 2. Handler funkcije sa tipama
def cmd_list(args: ListArgs) -> None:
    """List command"""
    logger.info(f"Listing: {args.path}")
    print(f"📝 Listanje fajlova u: {args.path}")
    if args.recursive:
        logger.debug("Recursive mode enabled")
        print("🔄 Rekurzivno listanje uključeno.")

def cmd_search(args: SearchArgs) -> None:
    """Search command"""
    logger.info(f"Searching for: {args.pattern} in {args.file}")
    print(f"🔍 Pretraga fajlova za: {args.pattern}")
    print(f" 💾 U fajlu: {args.file}")

def cmd_export(args: ExportArgs) -> None:
    """Export command"""
    logger.info(f"Exporting as: {args.format}")
    print(f"📤 Izvoz fajlova u format: {args.format}")
    if args.output:
        logger.info(f"Output file: {args.output}")
        print(f" 💾 Izlazni fajl: {args.output}")

# 3. Main sa potpunom tipizacijom
def main() -> int:
    """Main function"""
    parser = argparse.ArgumentParser(
        prog="datatools",
        description="Alat za rad sa podacima - listanje, pretraga i izvoz fajlova."
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Omogući detaljno ispisivanje informacija."
    )

    subparsers = parser.add_subparsers(
        title="Komande",
        description="Dostupne komande za rad sa podacima.",
        dest="command",
        required=True
    )

    # List subcommand
    parser_list = subparsers.add_parser("list", help="Listanje fajlova u direktorijumu.")
    parser_list.add_argument("path", help="Putanja do direktorijuma za listanje.")
    parser_list.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Rekurzivno listanje poddirektorijuma."
    )
    parser_list.set_defaults(func=cmd_list)

    # Search subcommand
    parser_search = subparsers.add_parser("search", help="Pretraga fajlova.")
    parser_search.add_argument("pattern", help="Šta tražiš?")
    parser_search.add_argument("file", help="Gde tražiš?")
    parser_search.set_defaults(func=cmd_search)

    # Export subcommand
    parser_export = subparsers.add_parser("export", help="Izvoz fajlova.")
    parser_export.add_argument(
        "--format",
        choices=["csv", "json"],
        default="csv",
        help="Format za export"
    )
    parser_export.add_argument(
        "--output", "-o",
        help="Putanja do izlaznog fajla."
    )
    parser_export.set_defaults(func=cmd_export)

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s"
    )

    if args.verbose:
        print("🔊 Verbose mode enabled.")

    # Pozovi handler
    args.func(args)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

Pokreni i proveri:

```bash
python3 sandbox/basics/cli_logging_practice/scripts/subcommands_cli_typed.py list /tmp -v
python3 sandbox/basics/cli_logging_practice/scripts/subcommands_cli_typed.py search "test" file.txt
mypy sandbox/basics/cli_logging_practice/scripts/subcommands_cli_typed.py
```

---

# 🎯 FAZA 7: BEST PRACTICES + REFAKTORISANJE (1 sat)

## 7.1 | Modern Imports — Sa `from __future__ import annotations`

Kreiraj `sandbox/basics/modern_types.py`:

```python
"""
Moderni Python types (3.10+)
"""
from __future__ import annotations  # Omogući lenjo evaluiranje anotacija!

from collections.abc import Iterable, Sequence, Mapping
from pathlib import Path
from typing import TypedDict, Optional, Literal

# 1. Union sa |
def process(data: str | int | list[str]) -> str:
    """Union sa | umesto Union[str, int, list[str]]"""
    return str(data)

# 2. Optional sa |
def get_config() -> dict[str, str] | None:
    """Vraća dict ili None — lakše od Optional[Dict[str, str]]"""
    return None

# 3. Specifične kolekcije sa collections.abc
def process_items(items: Iterable[str]) -> Sequence[str]:
    """Iterable input, Sequence output — fleksibilnije od list[str]"""
    return list(items)

# 4. TypedDict za recordove
class UserRecord(TypedDict):
    name: str
    age: int
    email: str | None

# 5. Literal za enum-like vrednosti
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def set_log_level(level: LogLevel) -> None:
    """Type checker će promeniti samo validne nivoe"""
    print(f"Log level: {level}")

def main() -> None:
    """Sve je type-safe"""
    user: UserRecord = {"name": "Jole", "age": 30, "email": "j@ex.com"}
    set_log_level("DEBUG")

if __name__ == "__main__":
    main()
```

---

## 7.2 | Checklista — Pre nego što Commitaš

Kreiraj `sandbox/basics/type_check_checklist.md`:

```markdown
# ✅ Type Annotations Checklist

Pre nego što commitaš kod, proveri:

## Imports

-   [ ] `from __future__ import annotations` na početku (3.10+ kompatibilnost)
-   [ ] Sortirani importi (stdlib, third-party, local)
-   [ ] Nema `typing.List`, `typing.Dict` — koristi `list[T]`, `dict[K, V]`
-   [ ] `collections.abc` za `Iterable`, `Sequence`, `Mapping`

## Funkcije

-   [ ] Sve funkcije imaju `-> NoneType` ili `-> <tip>`
-   [ ] Svi parametri imaju tipske anotacije
-   [ ] Optional vrednosti: `X | None` umesto `Optional[X]`

## Klase i TypedDict

-   [ ] Sve klase imaju `__init__` sa tipama
-   [ ] TypedDict umesto plain dict-a za recordove
-   [ ] Protokoli za dinamičke objekte (npr. argparse.Namespace)

## CSV/JSON

-   [ ] TypedDict za JSON strukture
-   [ ] list[TypedDict] za CSV redove
-   [ ] Konverzija stringova (CSV) u prave tipove

## Type Checking

-   [ ] `mypy --strict sandbox/basics/` — bez greške
-   [ ] Pylance u VSCode je tiho
-   [ ] Nema `type: ignore` comentara (ili su opravdani)

## Documentation

-   [ ] Docstring za sve javne funkcije
-   [ ] Primer tipske upotrebe u docstring-u
```

---

# 🧪 FAZA 8: VEŽBE + PRAKTIKA (1 sat)

## 8.1 | Zadaci za Vežbanje

### Zadatak 1: Tipizuj svoje CSV helper funkcije

U `sandbox/basics/python_refresh.py` (ili novi fajl `sandbox/basics/csv_helpers_typed.py`):

-   [ ] Kreiraj `load_csv()` sa return type `list[dict[str, str]]`
-   [ ] Kreiraj `write_csv()` sa parametrima i povratnom vrednoscu
-   [ ] Dodaj TypedDict za tvoj specifičan CSV format
-   [ ] Pokreni `mypy` — sve treba biti OK

### Zadatak 2: Refaktoriši csv_cleaner.py sa Tipima

U `sandbox/basics/csv_cleaner.py`:

-   [ ] Dodaj `from __future__ import annotations`
-   [ ] Tipizuj sve funkcije
-   [ ] Kreiraj TypedDict za unispan red
-   [ ] Dodaj `-> None` za main()
-   [ ] Proveri sa mypy

### Zadatak 3: Tipizuj web scraper config

U `projects/01-web-scraper/config.py`:

-   [ ] Kreiraj `ScraperConfig` TypedDict
-   [ ] Tipizuj sve setter/getter funkcije
-   [ ] Dodaj `Optional` gde treba
-   [ ] Proveri sa mypy

### Zadatak 4: Mini Projekat — File Processor sa Tipima

Kreiraj `sandbox/basics/file_processor_typed.py`:

```python
"""
Mini projekat: File processor sa tipskom sigurnošću
- Učitaj CSV
- Filtrira redove prema uslov
- Eksportuj kao JSON sa tipima
- Sve potpuno typizovano
"""
```

Pravi tako da `mypy --strict` prođe bez greške!

---

# 📊 PROGRES TRACKER

Označi kada završiš:

-   [ ] 1.1-1.3: Osnove Type Annotations (30 min)
-   [ ] 1.2-1.3: Type Errors Demo (15 min)
-   [ ] 2.1-2.3: CSV sa Tipima (45 min)
-   [ ] 3.1-3.2: Argparse sa Tipima (45 min)
-   [ ] 4.1-4.2: JSON sa Tipima (60 min)
-   [ ] 5.1-5.2: Kompleksne Tipizacije (60 min)
-   [ ] 6.1-6.2: Integracija sa Tvojim Projektima (90 min)
-   [ ] 7.1-7.2: Best Practices (60 min)
-   [ ] 8.1: Zadaci za Vežbanje (60 min)

**TOTAL: 8 sati**

---

# 🎯 POSLE 8 SATI

Šta Će Se Desiti:

✅ Razumeš Type Annotations potpuno
✅ Mypy/Pylance nije strastan — to je tvoj prijatelj
✅ CSV/JSON sa tipima je prirodno
✅ CLI sa Protokol klasama je clean
✅ Spreman si za Web Scraper sa tipskom sigurnošću

**Motiv:** Type annotations te sprečavaju da napraviš greške PRE nego što pokreneš kod. To je kao sa GitHub — verzijuješ kod. Sa tipima — verzijuješ i tipske garance!

---

# 🧭 Sledeće: DAN 2025-12-19

Nakon što završiš Type Annotations, krećeš sa:

-   Pathlib + File I/O (Path je novi `os.path`)
-   Testing + Pytest osnove
-   Error Handling patterns

**Već ćeš biti spreman za Web Scraper projekat!**
