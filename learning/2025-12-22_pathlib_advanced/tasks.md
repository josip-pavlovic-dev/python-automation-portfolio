---
type: tasks
linked_to: 2025-12-22_pathlib_advanced
date: 2025-12-22
status: active
---

# ✅ Tasks — Pathlib Day

-   [x] Aktiviran venv (`projects/01-web-scraper/venv`)
-   [x] Cheatsheet pročitan (10 min)

## FAZA 1 — Osnove Path

-   [x] `path_basics.py` napravljen (12+ primera cwd/home/resolve/parents/relative_to/expanduser)
-   [ ] `ensure_dir(path: Path)` radi i testiran sa `tmp_path`
-   [ ] Demo join za `data/users.csv`, `logs/app.log` bez `os.path`

---

## FAZA 2 — IO + Error handling

-   [ ] `file_io_safe.py` kreiran sa `read_text_safe`, `write_text_safe`, `append_lines`
-   [ ] Svaki helper loguje success/error (`logger.info/exception`)
-   [ ] `FileNotFoundError` poruka jasna (uključuje path)
-   [ ] Mini zadatak: kopiran `csv_with_types.py` u temp fajl koristeći helper

---

## FAZA 3 — Globbing + Filters

-   [ ] `glob_filters.py` sa `list_csv_sorted`, `recent_logs`, `ensure_suffix`
-   [ ] Filter za `.json` preko `rglob`; size limit 1 MB dodat
-   [ ] Test primer u `tmp_path` (kreiraj 3 fajla, proveri filtriranje)

---

## FAZA 4 — Integracija + Tests

-   [ ] `projects/01-web-scraper/config.py` koristi `Path`
-   [ ] Helper `get_output_dir()` kreira dir i loguje putanju
-   [ ] `test_paths.py` dodat sa `tmp_path`, `caplog`
-   [ ] `pytest -q -k pathlib` prolazi (min 4 testa)

---

## Završetak

-   [ ] `summary.md` popunjen (šta naučeno, test output)
-   [ ] Komanda zabeležena: `python -m pytest -q -k pathlib`

---

## 🔗 Gde radiš

-   Primary: `learning/2025-12-22_pathlib_advanced/`
-   Playground: `sandbox/basics/pathlib_playground/`
-   Project hook: `projects/01-web-scraper/`
-   Testovi: `learning/2025-12-22_pathlib_advanced/test_paths.py`
-   Deliverables: `path_basics.py`, `file_io_safe.py`, `glob_filters.py`
-   Cheatsheet: `cheatsheet.md`
-   Exercises: `pathlib_complete_exercises.md`
-   Tasks: `tasks.md`
-   Summary: `summary.md`
-   Chatlog: `chatlog.md`
-   Kickoff: `kickoff.md`
-   Prerequisites: `README.md`
-   Project tests: `projects/01-web-scraper/tests/`
-   Project config: `projects/01-web-scraper/config.py`
-   Project scraper: `projects/01-web-scraper/scraper.py`
-   Project venv: `projects/01-web-scraper/venv/`
-   Project log dir: `projects/01-web-scraper/logs/`
-   Project output dir: `projects/01-web-scraper/output/`
-   Project data dir: `projects/01-web-scraper/data/`
-   Project helpers: `projects/01-web-scraper/utils/`

---
