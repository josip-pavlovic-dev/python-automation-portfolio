---
type: day_overview
linked_to: 2025-12-23_testing_advanced
date: 2025-12-23
status: planned
language: bilingual
---

# 🧪 Dan 7 — Testing + Pytest (8h)

## 🎯 Cilj (Serbian)

Nauči da pišeš pouzdane testove za automation skripte: pytest osnove, fixtures, parametrizacija, tmp_path, mocking, coverage signal.

---

## 🧭 Šta radiš danas

-   Pytest discovery, asserts, markers
-   Fixtures: `tmp_path`, custom fixtures za config/data
-   Parametrize inputs, table-driven tests
-   Monkeypatch/mocking za IO i vreme
-   Coverage i kratki CI-ready komandi

---

## ✅ Rezultat dana

-   `tests/` folder sa 3+ fajla u `sandbox/basics/` ili `projects/01-web-scraper`
-   4x2h blokovi odrađeni sa zadacima u `testing_complete_exercises.md`
-   10+ testova koji prolaze; osnovni markers (`slow`, `unit`)

---

## 🔗 Gde radiš

-   Primary: `learning/2025-12-23_testing_advanced/`
-   Playground: `sandbox/basics/` (dodaj `tests/`)
-   Project hook: `projects/01-web-scraper/tests/`

---

## 🧰 Prerequisites

-   Aktiviran venv: `source projects/01-web-scraper/venv/bin/activate`
-   Imaš funkcije iz Pathlib dana (helpers) kao target za test
-   Znaš osnovne assertions

---

## 🗂️ Struktura fajlova danas

-   `kickoff.md` — raspored 4x2h
-   `testing_complete_exercises.md` — glavne vežbe
-   `cheatsheet.md` — pytest primeri
-   `tasks.md` — checklist
-   `summary.md` — popuni na kraju
-   `chatlog.md` — beleške Q&A

---

## 🧠 Focus

-   Pisanje testova pre refaktora (TDD light)
-   Korišćenje `tmp_path` za sve fajl IO testove
-   Čisti asserts, bez print/log u testovima
-   Parametrizacija umesto dupliranih testova

---

## 🚀 Quick start

1. Otvori `kickoff.md` (5 min)
2. Prođi `cheatsheet.md` (10 min)
3. Radi FAZA 1-4 u `testing_complete_exercises.md`
4. `pytest -q` posle svake faze

---
