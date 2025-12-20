---
type: tasks
date: 2025-12-18
linked_to: file_types_annotations
status: ready
---

# ✅ TASKS — Šta Trebalo da Uradiš (Dan 5)

## 🎯 Daily Objectives (8 hours)

-   [ ] **FAZA 1 (1.5h):** Osnove Type Annotations

    -   [ ] Razumi šta je type hint
    -   [ ] REPL praksa sa primitvima
    -   [ ] Kreiraj `type_annotations_intro.py`
    -   [ ] Pokreni `mypy` bez greške

-   [ ] **FAZA 2 (1.5h):** CSV sa Type Annotations

    -   [ ] Pročitaj TypedDict concept
    -   [ ] Kreiraj `csv_with_types.py` (čitanje)
    -   [ ] Kreiraj `csv_write_with_types.py` (pisanje)
    -   [ ] Kreiraj `csv_with_conversion.py` (int konverzija)

-   [ ] **FAZA 3 (1.5h):** Argparse + CLI

    -   [ ] Razumi Protocol klase
    -   [ ] Refaktorisaj `basic_cli.py` sa tipima
    -   [ ] Kreiraj `basic_cli_typed.py` (model)
    -   [ ] Testira sa `mypy`

-   [ ] **FAZA 4-5 (1.5h):** JSON + Kompleksne Tipizacije

    -   [ ] Kreiraj `json_with_types.py`
    -   [ ] Kreiraj `complex_types.py`
    -   [ ] Kreiraj `generic_types.py`
    -   [ ] Razumi Union i Literal

-   [ ] **FAZA 6 (1.5h):** Integracija

    -   [ ] Refaktorisaj `cli_logging_practice/scripts/basic_cli.py`
    -   [ ] Refaktorisaj `cli_logging_practice/scripts/subcommands_cli.py`
    -   [ ] Kreiraj tipizovane verzije
    -   [ ] Commit: "refactor: Add type annotations"

-   [ ] **FAZA 7-8 (1h):** Best Practices + Vežbe
    -   [ ] Čitaj checklist
    -   [ ] Uradi zadatke (4 mini projekta)
    -   [ ] `mypy --strict` na svim fajlovima
    -   [ ] Finalize + Commit

---

## 📋 Folder Structure — Gde Čuvaš Fajlove?

```
sandbox/basics/
├── type_annotations_intro.py                  # FAZA 1
├── type_errors_demo.py                        # FAZA 1
├── csv_with_types.py                          # FAZA 2
├── csv_write_with_types.py                    # FAZA 2
├── csv_with_conversion.py                     # FAZA 2
├── cli_with_types.py                          # FAZA 3
├── cli_with_cast.py                           # FAZA 3
├── json_with_types.py                         # FAZA 4
├── json_write_with_types.py                   # FAZA 4
├── complex_types.py                           # FAZA 5
├── generic_types.py                           # FAZA 5
├── modern_types.py                            # FAZA 7
├── type_check_checklist.md                    # FAZA 7
├── file_processor_typed.py                    # FAZA 8
│
├── type_exercises_data/                       # Test podaci
│   ├── users.csv
│   ├── config.json
│   ├── output_people.csv
│   ├── database.json
│   └── ...
│
└── cli_logging_practice/scripts/
    ├── basic_cli.py                           # ORIGINAL
    ├── basic_cli_typed.py                     # REFACTORED (FAZA 3)
    ├── subcommands_cli.py                     # ORIGINAL
    ├── subcommands_cli_typed.py               # REFACTORED (FAZA 3)
    └── ...
```

---

## 🏁 Checklist — Šta Mora Biti Završeno

### Pre Nego Što Počneš (30 min)

-   [ ] Pročitaj: `cheatsheet_csv_annotations.md` (15 min)
-   [ ] Pročitaj: `cheatsheet_modern_mypy_pylance.md` (15 min)

### FAZA 1 (90 min)

-   [ ] Kreiraj `type_annotations_intro.py`
-   [ ] Kreiraj `type_errors_demo.py`
-   [ ] REPL praksa sa 5+ primere
-   [ ] `mypy` provera — bez greške
-   [ ] Razume osnove type hints

### FAZA 2 (90 min)

-   [ ] Kreiraj test CSV: `type_exercises_data/users.csv`
-   [ ] Kreiraj `csv_with_types.py` — čitanje sa TypedDict
-   [ ] Kreiraj `csv_write_with_types.py` — pisanje sa TypedDict
-   [ ] Kreiraj `csv_with_conversion.py` — konverzija tipova
-   [ ] `mypy` provera — bez greške

### FAZA 3 (90 min)

-   [ ] Razume Protocol klase
-   [ ] Kreiraj `cli_with_types.py`
-   [ ] Kreiraj `cli_with_cast.py`
-   [ ] Refaktorisaj `basic_cli.py` → dodaj tipove
-   [ ] `mypy` provera — bez greške

### FAZA 4-5 (90 min)

-   [ ] Kreiraj test JSON: `type_exercises_data/config.json`
-   [ ] Kreiraj `json_with_types.py`
-   [ ] Kreiraj `json_write_with_types.py`
-   [ ] Kreiraj `complex_types.py`
-   [ ] Kreiraj `generic_types.py`
-   [ ] `mypy` provera — bez greške

### FAZA 6 (90 min)

-   [ ] Refaktorisaj `cli_logging_practice/scripts/basic_cli.py` sa tipima
-   [ ] Refaktorisaj `cli_logging_practice/scripts/subcommands_cli.py` sa tipima
-   [ ] Kreiraj `cli_logging_practice/scripts/basic_cli_typed.py` (model)
-   [ ] Kreiraj `cli_logging_practice/scripts/subcommands_cli_typed.py` (model)
-   [ ] `mypy` provera — bez greške

### FAZA 7-8 (60 min)

-   [ ] Kreiraj `modern_types.py`
-   [ ] Kreiraj `type_check_checklist.md`
-   [ ] Uradi 4 zadatka iz FAZA 8.1:
    -   [ ] Zadatak 1: Tipizuj CSV helpers
    -   [ ] Zadatak 2: Refaktoriši csv_cleaner.py
    -   [ ] Zadatak 3: Tipizuj web scraper config
    -   [ ] Zadatak 4: Mini projekat (File Processor)
-   [ ] `mypy --strict` na svim fajlovima — bez greške

---

## 🎓 Knowledge Validation

**Nakon što završiš Dan 5, trebao bi da možeš:**

✅ Objasni šta su type annotations i zašto važne
✅ Kreira TypedDict za CSV redove
✅ Kreira Protocol za argparse args
✅ Koristi `mypy` za type checking
✅ Razume `from __future__ import annotations`
✅ Koristi modern Python tipove (`list[T]`, `X | None`)
✅ Refaktorisaš `basic_cli.py` i `subcommands_cli.py`
✅ Razume razliku između `collections.abc` i `typing`
✅ Napravim mini projekat sa tipskom sigurnošću

---

## 📞 Support — Ako Zaglavim

**Za TYPE ANNOTATION greške:**

```bash
mypy --show-error-codes script.py
# Pogledam error, otvorim cheatsheet, eksperimentujem
```

**Za TypedDict:**

-   Pogledaj `csv_with_types.py` kao model
-   Čitaj sec. 2.1 u `file_types_annotation_complete_exercises.md`

**Za Protocol:**

-   Pogledaj `cli_with_types.py` kao model
-   Čitaj sec. 3.1 u vežbama

**Za mypy greške:**

-   `mypy --no-error-summary` za detaljne poruke
-   Google error message
-   Pitaj AI sa full error output-om

---

## 🎯 FINAL VALIDATION

**Završen Dan 5 Kada:**

```bash
# Sve fajlove su tipizovani
mypy --strict sandbox/basics/

# Svi fajlovi iz cli_logging_practice su refaktorisani
mypy sandbox/basics/cli_logging_practice/scripts/*.py

# Minimalno 4 zadatka iz FAZA 8 su completed
# Refaktorisanje basic_cli.py i subcommands_cli.py je done
# Razumeš TypedDict, Protocol, modern types, collections.abc
```

---

## 🚀 Commit-uj Posle Dana

```bash
git add -A
git commit -m "feat: Type annotations mastery + refactoring

- Add type hints to all functions
- Refactor basic_cli.py and subcommands_cli.py
- Implement TypedDict for CSV/JSON records
- Implement Protocol for CLI args
- Add mypy type checking
- Complete 8h type annotations exercises"
```

---

**Spreman za Dan 5? 🔥 KRENI!**
