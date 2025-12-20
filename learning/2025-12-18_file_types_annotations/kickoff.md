---
type: kickoff
date: 2025-12-18
linked_to: python-automation-portfolio
phase: foundation
milestone: type_safety_mastery
status: init
---

# 🚀 Daily Kickoff — 2025-12-18

## ☀️ DAN: FILE TYPES + TYPE ANNOTATIONS (8 sati)

**Cilj Dana:** Savladaj Type Annotations potpuno — od osnova do integracije sa CSV/JSON/CLI

---

## 🗓️ Predložena Raspodela Vremena

```
09:00-10:30  | FAZA 1: Osnove (1.5h)
10:30-10:45  | ☕ PAUZA
10:45-12:30  | FAZA 2: CSV sa Tipima (1.5h)
12:30-13:30  | 🍽️ RUČAK
13:30-15:00  | FAZA 3: Argparse sa Tipima (1.5h)
15:00-15:15  | ☕ PAUZA
15:15-16:15  | FAZA 4-5: JSON + Kompleksne Tipizacije (1h)
16:15-17:45  | FAZA 6: Integracija sa Tvojim Projektima (1.5h)
17:45-18:30  | FAZA 7-8: Best Practices + Vežbe (45 min)
```

**Total:** 8 sati

---

## 🎯 Redosled Vežbi

**Pre Nego Što Počneš (30 min):**

-   [ ] Pročitaj: [cheatsheet_csv_annotations.md](../../scratch/docs/cheatsheet_csv_annotations.md)
-   [ ] Pročitaj: [cheatsheet_modern_mypy_pylance.md](../../scratch/docs/cheatsheet_modern_mypy_pylance.md)

**Glavne Vežbe (8h):**

-   [ ] Kreni sa [file_types_annotation_complete_exercises.md](./file_types_annotation_complete_exercises.md) — FAZA 1-8
-   [ ] Svaku fazu praktikovati sa REPL → fajl → mypy
-   [ ] Vežbaj refaktorisavanje tvojih postojećih skripti

---

## 💡 Ključne Stvari za Pamćenje

1. **Type Annotations su "napomene"** — Python ih ignoriše, ali Pylance proverava
2. **`TypedDict`** je najbolji za CSV/JSON redove
3. **`Protocol`** je best za dinamičke objekte (argparse.Namespace)
4. **`from __future__ import annotations`** omgući 3.10+ sintaksu svugde
5. **mypy/Pylance su tvoji prijatelji** — hvataće greške PRE nego što pokreneš kod

---

## ⚠️ Česta Greška

❌ Koristi `typing.List`, `typing.Dict`
✅ Koristi `list[T]`, `dict[K, V]`

---

## 📋 Checklist Za Završetak Dana

-   [ ] Sve vežbe iz FAZE 1-8 su completed (bar do FAZE 6)
-   [ ] mypy se pokreće bez greške na tvojim fajlovima
-   [ ] Razumeš šta je TypedDict vs Protocol
-   [ ] Refaktorisao si `basic_cli.py` i `subcommands_cli.py` sa tipima
-   [ ] Spreman si za integracijom sa Web Scraper projektom

---

## 🧭 Sledeće: DAN 2025-12-19

-   Pathlib + File I/O osnove
-   Testing + Pytest
-   Error Handling patterns
-   Spreman si za Web Scraper v1!

**Počni sa FAZA 1! 🔥**
