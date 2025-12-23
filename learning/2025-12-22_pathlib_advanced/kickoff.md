---
type: kickoff
date: 2025-12-22
linked_to: 2025-12-22_pathlib_advanced
phase: foundation
milestone: type_safety_mastery
status: init
---

# 🚀 Kickoff — Dan 6: Pathlib + File I/O (8h)

## 🕒 Raspored (4x2h)

1. 09:00-11:00 — FAZA 1: Path osnove + joins + normalize
2. 11:15-13:15 — FAZA 2: Čitanje/pisanje + encoding + error handling
3. 14:00-16:00 — FAZA 3: Globbing, traversal, filtering, metadata
4. 16:15-18:15 — FAZA 4: Primena u Web Scraper + tests (`tmp_path`, `caplog`)

**Pauze:** 10-15 min između blokova; reset fokusa i kratko prođi `cheatsheet.md`.

---

## 🎯 Deliverables po bloku

-   FAZA 1: `path_basics.py` sa 12+ Path primera (cwd/home/resolve/parents/relative_to/expanduser)
-   FAZA 2: `file_io_safe.py` sa helperima + logovanjem + exception msg
-   FAZA 3: `glob_filters.py` za filtiranje po ekstenziji/veličini + mtime
-   FAZA 4: Integrisani utilsi u `projects/01-web-scraper/` + 4 pytest testa (`tmp_path`, `caplog`)

---

## 🧭 Koraci za početak

-   Aktiviraj venv: `source projects/01-web-scraper/venv/bin/activate`
-   Otvori `cheatsheet.md` (10 min)
-   Prođi `pathlib_complete_exercises.md` FAZA 1-4 redom
-   Pogledaj `scratch/docs/python_testing_guide.md` (15 min) za `tmp_path` pattern

---

## 🔄 Loop kad zaglaviš (15+ min)

1. Pogledaj primer iz `cheatsheet.md`
2. Čitaj sekciju "Hints" u `pathlib_complete_exercises.md`
3. Napravi minimalni repro u `sandbox/basics/pathlib_playground/`
4. Pokreni `pytest -q` uz `-k pathlib`
5. Dodaj `print(path.resolve())` u repro da vidiš realnu putanju

---

## ✅ Checkpointi

-   Posle FAZA 1: Znaš `Path.cwd()`, `.parent`, `.resolve()`, `.expanduser()`, `/` operator
-   Posle FAZA 2: Imaš helper `read_text_safe(path: Path) -> str` i podižeš jasan `FileNotFoundError`
-   Posle FAZA 3: Filtriraš fajlove `*.csv` novije od X sekundi i umeš da meriš `st_size`
-   Posle FAZA 4: Scraper koristi `Path` i prolazi testove (`tmp_path`, `caplog`)

---

## 📝 Napomene

-   Uvek postavi `encoding="utf-8"`
-   Loguj greške (`logger.exception`)
-   Ne koristi `os.path` osim poređenja (legacy only)
-   Validiraj korisničke putanje (suffix, exists) pre rada
-   U testovima uvek koristi `tmp_path`/`caplog`; ne piši u repo

---
