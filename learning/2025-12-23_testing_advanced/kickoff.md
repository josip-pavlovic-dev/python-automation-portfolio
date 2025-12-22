---
type: kickoff
date: 2025-12-23
linked_to: 2025-12-23_testing_advanced
status: planned
blocks: 4
---

# 🚀 Kickoff — Dan 7: Testing + Pytest (8h)

## 🕒 Raspored (4x2h)

1. 09:00-11:00 — FAZA 1: Pytest osnove + discovery
2. 11:15-13:15 — FAZA 2: Fixtures (`tmp_path`, custom), parametrizacija
3. 14:00-16:00 — FAZA 3: Monkeypatch/mocking + error cases
4. 16:15-18:15 — FAZA 4: Integracija na Web Scraper + coverage

## 🎯 Deliverables

-   FAZA 1: `tests/test_basics.py` sa 5+ assert primera
-   FAZA 2: `tests/test_io_helpers.py` sa `tmp_path` i parametrizacijom
-   FAZA 3: `tests/test_scraper_errors.py` sa monkeypatch i fake responses
-   FAZA 4: `pytest -q` prolazi + `coverage` kratki izveštaj

## 🧭 Koraci za početak

-   Aktiviraj venv: `source projects/01-web-scraper/venv/bin/activate`
-   `pip install -r projects/01-web-scraper/requirements.txt` ako treba
-   Otvori `cheatsheet.md`, zatim `testing_complete_exercises.md`

## 🔄 Loop kad zaglaviš (15+ min)

1. Smanji scope: napiši najkraći test koji pukne
2. Uključi `-vv -k <pattern>` da izoluješ
3. Proveri fixtures u `conftest.py` (kreiraj ako nedostaje)
4. Pogledaj pytest docs snippet u `cheatsheet.md`

## ✅ Checkpointi

-   Posle FAZA 1: znaš osnovni naming i asserts
-   Posle FAZA 2: koristiš `@pytest.mark.parametrize` i `tmp_path`
-   Posle FAZA 3: monkeypatch request/session i proveravaš log/error
-   Posle FAZA 4: 80%+ pokrivenost utility modula

## 📝 Napomene

-   Testovi nemaju `print`; koriste `assert` i eventualno `caplog`/`capsys`
-   Fajl sistem testovi uvek idu kroz `tmp_path`
-   Markiraj spore testove `@pytest.mark.slow`
