---
type: master_plan
date: 2025-12-18
linked_to: python-automation-portfolio
phase: foundation_complete
status: ready
---

# 📊 MASTER PLAN — Kompletan Pregled (Dan 1-30)

## 🎯 Gde Si Sada (18. Decembar 2025)

✅ **Dan 1-4:** Terminal + CSV + CLI + Logging (Foundation Complete)
🔴 **Dan 5:** File Types + Type Annotations (TODAY — 2025-12-18)
⏳ **Dan 6-7:** Pathlib + Testing (Planned)
🚀 **Dan 8+:** Web Scraper + Projects (Ready to Launch)

---

## 📚 KOMPLETNA STRUKTURA UČENJA

```
NEDELJA 1 (Dan 1-7):
├─ ✅ Dan 1-2: Terminal + Git
├─ ✅ Dan 3-4: CSV + Logging + CLI
├─ ✅ Dan 5: FILE TYPES + ANNOTATIONS
├─ 🔴 Dan 6: Pathlib + File I/O (SADA!)
└─ ⏳ Dan 7: Pytest + Error Handling

NEDELJA 2 (Dan 8-14):
├─ 📌 Dan 8: Web Scraper v1 Setup
├─ 📌 Dan 9-10: Web Scraper Implementation
├─ 📌 Dan 11: CSV Cleaner v2
├─ 📌 Dan 12: Integration
├─ 📌 Dan 13: Deployment + README
└─ 📌 Dan 14: Consolidation

NEDELJA 3-4 (Dan 15-30):
├─ 📌 Real Projects
├─ 📌 Client Work
└─ 📌 Portfolio Building
```

---

## 🗺️ VAŽNE ODREDNICE: Šta Si Naučio Po Danu

### ✅ Dan 0-4: FOUNDATION COMPLETE

**Terminal (Dan 1-2):**

-   `pwd`, `cd`, `ls`, `cat`, `grep`, `find`
-   Pipes i redirects (`|`, `>`)
-   Git basics (`init`, `add`, `commit`, `log`)

**Python Core (Dan 3-4):**

-   CSV: `reader`, `DictReader`, `writer`, `DictWriter`, `Dialect`, `Sniffer`
-   CLI: `argparse`, subcommands, validation
-   Logging: `basicConfig`, handlers, formatters, levels
-   JSON: `load`, `dump`, `loads`, `dumps`

---

### ✅ Dan 5: FILE TYPES + TYPE ANNOTATIONS

**Što Si Naučio:**

1. **Type Annotations Osnove**

    - Šta je type hinting?
    - Primitivni tipovi:
    - `int`, `str`, `list[T]`, `dict[K, V]`, `tuple`, `set`
    - Funkcije sa tipovima: `def func(x: int) -> str:`

2. **TypedDict za CSV/JSON**

    ```python
    class UserRecord(TypedDict):
        name: str
        age: int
        city: str
    ```

3. **Protocol za Argparse**

    ```python
    class ProcessArgs(Protocol):
        input_file: str
        verbose: bool
    ```

4. **Modern Python Types**

    - `from __future__ import annotations`
    - `collections.abc` za `Iterable`, `Sequence`, `Mapping`
    - `X | None` umesto `Optional[X]`

5. **Type Checking sa mypy**
    ```bash
    mypy script.py
    ```

**Rezultat:** Tvoj kod je type-safe + linter je tih!

---

### ⏳ Dan 6-7: PATHLIB + TESTING (This Week -> Today!)

**Što Će Se Pokrivati:**

```python
# PATHLIB
from pathlib import Path
csv_file = Path(__file__).parent / "data" / "users.csv"
data = csv_file.read_text()

# PYTEST
def test_load_csv():
    csv = Path("test.csv")
    result = load_csv(csv)
    assert len(result) > 0

pytest script.py -v
```

---

## 🎓 SVEUKUPNI PLAN — NEDELJA ZA NEDELJOM

### NEDELJA 1: FOUNDATION (Dan 1-7)

| Dan   | Tema                 | Zadaci                                  | Rezultat                 |
| ----- | -------------------- | --------------------------------------- | ------------------------ |
| 1-2   | Terminal + Git       | Navigation, file ops, git workflow      | Komforan sa terminalnim  |
| 3     | CSV Osnove           | `reader`, `writer`, `DictReader`        | Mogu čitati/pisati CSV   |
| 4     | CLI + Logging        | `argparse`, `logging`, JSON             | CLI alat sa logovanjem   |
| **5** | **Type Annotations** | **TypedDict, Protocol, mypy**           | **Type-safe kod**        |
| 6     | Pathlib + File I/O   | `Path`, `mkdir`, `glob`, error handling | Moderni rad sa fajlovima |
| 7     | Testing + Pytest     | `test_`, assertions, fixtures           | Testovi za kod           |

**EOW Rezultat:** Spreman sa svim alatima za Web Scraper! 🎉

---

### NEDELJA 2: WEB SCRAPER v1 (Dan 8-14)

| Dan  | Tema                     | Što Radiš                           | Rezultat                        |
| ---- | ------------------------ | ----------------------------------- | ------------------------------- |
| 8    | Setup                    | Inicijalizacija projekta, structure | `projects/01-web-scraper` ready |
| 9-10 | Implementation           | Requests + BeautifulSoup            | Skrapuj web stranice            |
| 11   | CSV Output               | Sačuvi rezultate u CSV              | CSV sa scrapovanih podataka     |
| 12   | Logging + Error Handling | Loguj sve korake                    | Production-ready scraper        |
| 13   | README + Tests           | Test coverage 80%+                  | Dokumentovan i testiran         |
| 14   | Consolidation            | Review + Refactor                   | Spreman za klijente!            |

**EOW Rezultat:** Prvi "proizvod"! 🚀

---

### NEDELJA 3-4: PROJECTS + CLIENTS (Dan 15-30)

```
📌 Projekat 2: CSV Cleaner (Dan 15-18)
   ├─ Clean data
   ├─ Handle duplicates
   └─ Export clean CSV

📌 Projekat 3: Data Pipeline (Dan 19-22)
   ├─ Read CSV
   ├─ Transform data
   └─ Export JSON/CSV

📌 Projekat 4: Automation Tool (Dan 23-26)
   ├─ Combine prethodna
   ├─ Add scheduling
   └─ Deploy

📌 Portfolio + Marketing (Dan 27-30)
   ├─ Build portfolio website
   ├─ Write case studies
   └─ Spreman za first clients!
```

---

## 🎯 MASTER STRUCTURE — Fajlovi Koje Koristiš

### learning/ Materijali (Follow religiously!)

```
learning/
├── 2025-12-14_csv_basics/              ✅ Done
│   └── cli_logging_complete_exercises.md (reference)
├── 2025-12-15_cli_logging/             ✅ Done
│   └── cli_logging_complete_exercises.md (reference)
├── 2025-12-16_python_automation/       ✅ Done
│   └── BAZA_POTREBNA.md (key reference!)
├── 2025-12-17_terminal_git_basics/     ✅ Done
│   └── terminal_repl_exercises.md
├── 2025-12-18_file_types_annotations/  🔴 TODAY!
│   ├── kickoff.md ← Read first (5 min)
│   ├── README.md ← Evo šta radiš (5 min)
│   └── file_types_annotation_complete_exercises.md ← MAIN (8h)
└── 2025-12-19_pathlib_testing/         ⏳ Planned
    └── PLANNED_KICKOFF.md
```

---

### sandbox/ za Praksu (Your Playground)

```
sandbox/basics/
├── cli_logging_practice/
│   └── scripts/
│       ├── basic_cli.py ← Refaktorisi sa tipovima!
│       ├── subcommands_cli.py ← Refaktorisi sa tipovima!
│       └── basic_cli_typed.py ← Model rešenja
├── type_annotations_intro.py
├── csv_with_types.py
├── csv_with_conversion.py
├── json_with_types.py
└── cli_with_types.py
```

---

### scratch/ Referenca

```
scratch/docs/
├── cheatsheet_csv_annotations.md
├── cheatsheet_modern_mypy_pylance.md
└── python_testing_guide.md ← Za Dan 6-7
```

---

## 🧠 KLJUČNI KONCEPTI — SVE 4 NEDELJE

### TIER 1: MUST-KNOW (Svaki Dan)

-   **Path** — Uvek koristi `Path` umesto stringova
-   **Type Hints** — Sve funkcije trebale imaju `->` return type
-   **Exception Handling** — `try/except` za sve fajl operacije
-   **Logging** — `logger` umesto `print` u produkciji
-   **Git** — Commit nakon svakog feature-a

---

### TIER 2: VERY USEFUL (Svake Nedelje)

-   **TypedDict** — Za redove iz CSV/JSON
-   **Protocol** — Za args i config objekta
-   **Pytest** — Za sve testove
-   **f-strings** — Umesto `.format()` ili `%`
-   **Context managers** — `with` za sve fajl operacije

---

### TIER 3: BONUS (Kasnije Kada Si Spreman))

-   **Generic tipovi** — `TypeVar`, `Generic`
-   **Async** — Nakon što znaš sync
-   **Decorators** — Nakon što znaš funkcije
-   **Metaclasses** — Malo kasnije
-   **Pandas** — Nakon što znaš csv modul

---

## 🎓 VALIDACIJA — Kako Znaš da Si Spreman?

### Dan 5 Checkout (File Types + Annotations)

```
Zaokruži DA/NE:

1. Mogu da koristim mypy bez greške
2. Znam razliku između TypedDict i Protocol
3. Mogu da tipizujem CSV redove
4. Mogu da tipizujem argparse args
5. Razumem `from __future__ import annotations`
6. Mogu da refaktorišem `basic_cli.py` sa tipovima
7. Razumem moderni Python tipove (`list[T]`, `X | None`)
```

**Min. 5/6 DA → Spreman za Dan 6!**

---

## 📞 SUPPORT STRUKTURA

### Ako Se Zaglaviš (15+ min)

1. **Čitaj Relevant Cheatsheet**

    - Type annotations? → `cheatsheet_modern_mypy_pylance.md`
    - CSV? → `cheatsheet_csv_annotations.md`

2. **Pogledaj Model Rešenja**

    - Vidiš `basic_cli_typed.py` kao primenu

3. **Pokrenuti mypy**

    ```bash
    mypy --strict sandbox/basics/
    ```

4. **Pitaj AI sa konkretnom greškom**
    - Skopaj error message
    - Skopaj problem kod
    - Javi šta si pokušao

---

## 🚀 FINALNI CILJ

**Posle Dana 7:** Spreman za Web Scraper projekat

```python
# To će biti tvoj kod:
from pathlib import Path
from typing import TypedDict
import csv
import requests
from bs4 import BeautifulSoup
import logging
import pytest

class ScrapedItem(TypedDict):
    title: str
    url: str
    price: float

def scrape_website(url: str) -> list[ScrapedItem]:
    """Scrape website sa type safety-jem"""
    ...

def test_scrape_website():
    """Test scraper sa pytest"""
    ...

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    items = scrape_website("https://example.com")
    Path("output.csv").write_text(...)
```

---

## ✅ CHECKLIST — Šta Si Naucio

### ✅ NEDELJA 1 COMPLETE

-   [x] Terminal osnove
-   [x] Git workflow
-   [x] CSV read/write
-   [x] CLI sa argparse
-   [x] Logging system
-   [x] Type Annotations
-   [ ] Pathlib (Dan 6) <!-- To radiš sada! -->
-   [ ] Pytest (Dan 7)

---

### ⏳ NEDELJA 2 READY

-   [ ] Web Scraper v1
-   [ ] Beautiful Soup
-   [ ] Requests library
-   [ ] Error handling
-   [ ] Documentation

---

### 🎯 NEDELJA 3+ POTENTIAL

-   [ ] CSV Cleaner
-   [ ] Data Pipeline
-   [ ] Portfolio
-   [ ] First Client

---

**Sada si spreman za Production-grade Python! 🎉**
