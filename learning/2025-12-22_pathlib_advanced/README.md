---
type: day_overview
linked_to: 2025-12-22_pathlib_advanced
date: 2025-12-22
status: planned
language: bilingual
---

# 📂 Dan 6 — Pathlib + File I/O (8h)

## 🎯 Cilj (Serbian)

Modernizuj rad sa fajlovima: koristi `pathlib.Path`, sigurno čitanje/pisanje, globbing, validaciju ekstenzija, robustan error handling.

**Zašto Pathlib?**

-   Bez string concat bugova (`/` operator je čistiji od `os.path.join`).
-   Portabilno (Win/Linux bez ručnog separatore).
-   Stat + resolve daju sigurnost gde tačno pišeš.

---

## 🧭 Šta radiš danas (English code)

-   Use `Path` for joins (`Path(__file__).parent / "data" / "users.csv"`) | Koristi `Path` za joinove (`Path(__file__).parent / "data" / "users.csv"`)
-   Read/write safely (`read_text`, `write_text`, `open`, `encoding="utf-8"`) | Čitaj/piši bezbedno (`read_text`, `write_text`, `open`, `encoding="utf-8"`)
-   Inspect files (`stat`, `exists`, `is_file`, `suffix`, `stem`) | Inspekcija fajlova (`stat`, `exists`, `is_file`, `suffix`, `stem`)
-   Traverse (`iterdir`, `glob`, `rglob`, `resolve`) | Pretraživanje (`iterdir`, `glob`, `rglob`, `resolve`)
-   Error handling + logging wrappers for file ops | Error handling + logging omotači za file operacije
-   Validate user input (`expanduser`, `resolve`, suffix checks) | Validiraj ulaze (`expanduser`, `resolve`, provera ekstenzije`)
-   Test file ops sa `tmp_path`, `caplog`, `monkeypatch` | Testiraj fajl operacije sa `tmp_path`, `caplog`, `monkeypatch`

---

## ✅ Rezultat dana

-   Utility modul `path_utils.py` u `sandbox/basics/` i/ili `projects/01-web-scraper`
-   4 kompletna bloka vežbi (8h) završena
-   Minimalno 4 pytest testa za file utilse (`tmp_path`, `caplog`)
-   Konfigurisan output/log dir u scraperu uz `Path`
-   Dokumentovan checklist i summary popunjen

---

## 🔗 Gde radiš

-   Primary: `learning/2025-12-22_pathlib_advanced/`
-   Playground: `sandbox/basics/` (kreiraj `pathlib_playground/` ako treba)
-   Project hook: `projects/01-web-scraper/` (log dir, output dir, config paths)

---

## 🧰 Prerequisites

-   Aktiviran venv (web-scraper): `source projects/01-web-scraper/venv/bin/activate`
-   Sve testove možeš pokrenuti: `python -m pytest`
-   Znaš osnove `Path`, pytest bazu (assert, fixtures)
-   Pročitao `scratch/docs/python_testing_guide.md` (10 min)
-   Postoji test podaci ili spreman si da ih generišeš u `tmp_path`

---

## 🗂️ Struktura fajlova danas

-   `kickoff.md` — dnevni raspored 4x2h + pauze
-   `pathlib_complete_exercises.md` — detaljne faze i zadaci (8h)
-   `cheatsheet.md` — brzi primeri `Path` (join, IO, glob, safety)
-   `tasks.md` — checklist za validaciju (po fazama)
-   `summary.md` — upiši šta si završio + test output
-   `chatlog.md` — Q&A zapis (po potrebi)
-   `path_utils.py` / `glob_filters.py` / `file_io_safe.py` — deliverables

---

## 🧠 Focus

-   Uvek koristi `Path` umesto stringova
-   Uvek postavi encoding (`encoding="utf-8"`)
-   Koristi `exists()` + error handling pre I/O
-   Piši testove uz `tmp_path` i `caplog` (log assertion)
-   Normalizuj korisničke ulaze `expanduser().resolve()`
-   Ne ostavljaj hardkodirane string putanje u scraperu

## 💻 Šta ćeš praktikovati

| Faza | Tema                        | Rezultat                                  |
| ---- | --------------------------- | ----------------------------------------- |
| 1    | Path osnove + normalize     | `path_basics.py` + `normalize()` helper   |
| 2    | IO helpers + logging        | `file_io_safe.py` + jasne error poruke    |
| 3    | Globbing + filters + mtime  | `glob_filters.py` + size/time filteri     |
| 4    | Integracija u scraper + TDD | `test_paths.py` + `get_output_dir()` radi |

## 🔄 Pre vs Posle

**Pre:**

```python
log_path = "logs/app.log"  # string, nema kreiranja dir-a
open(log_path, "w").write("hi")
```

**Posle:**

```python
from pathlib import Path
def get_log_file(root: Path) -> Path:
	log_dir = root / "logs"
	log_dir.mkdir(parents=True, exist_ok=True)
	log_file = log_dir / "app.log"
	log_file.write_text("hi", encoding="utf-8")
	return log_file
```

Benefiti: nema hardcoded stringova, dir se kreira, encoding definisan, testira se sa `tmp_path`.

---

## 🚀 Quick start

-   Pokreni `pytest -q -k pathlib` posle svake faze
-   Uporedi sa primerima u `path_utils.py` kada dodaš helper funkcije
-   Dodaj `print(path.resolve())` u repro ako ne vidiš gde pišeš
-   Prođi `cheatsheet.md` za brze reference
-   Radi FAZA 1-4 u `pathlib_complete_exercises.md` redom
-   Popuni `tasks.md` i `summary.md` na kraju dana
-   Koristi `chatlog.md` za beleške i Q&A tokom rada
-   Uživaj u radu sa fajlovima na moderan način!

---
