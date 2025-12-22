---
type: exercises
date: 2025-12-23
linked_to: 2025-12-23_testing_advanced
blocks: 4
status: planned
---

# 🏋️‍♂️ Testing Complete Exercises (8h)

## FAZA 1 (2h) — Pytest osnove

-   Napravi `tests/test_basics.py`:
    -   3 brza testa za pure functions (`add`, `to_int`, `slugify`), Arrange/Act/Assert stil.
    -   Jedan test za očekivani exception (`with pytest.raises(ValueError)`).
    -   Dodaj marker `@pytest.mark.unit` i filtriraj sa `-m unit`.
-   Pokreni `pytest -q -k basics`.

## FAZA 2 (2h) — Fixtures + Parametrizacija

-   Napravi `tests/test_io_helpers.py` (cilj: helperi iz Pathlib dana):
    -   Fixture `sample_csv(tmp_path)` koji kreira mali CSV.
    -   Parametrize za ekstenzije: `ensure_suffix` prima različite ulaze.
    -   Test `read_text_safe` da baca `FileNotFoundError`.
-   Dodaj `conftest.py` ako treba zajedničke fixturе.

## FAZA 3 (2h) — Monkeypatch / Mocking / Error Cases

-   Napravi `tests/test_scraper_errors.py`:
    -   Monkeypatch `requests.get` da vrati fake response (status 500) i proveri da scraper loguje error.
    -   Monkeypatch `time.sleep` ili `Path.exists` za brže testiranje.
    -   Iskoristi `caplog` da proveri log tekst.
-   Opcija: koristi `pytest.raises` za network error scenario.

## FAZA 4 (2h) — Integracija + Coverage

-   U `projects/01-web-scraper/tests/` dodaj ili proširi testove:
    -   `test_output_dir_created(tmp_path)` koristi helper iz Pathlib dana.
    -   `test_write_csv(tmp_path)` proverava da scraper upisuje CSV uz `encoding="utf-8"`.
-   Pokreni: `pytest --maxfail=1 -q --cov=projects/01-web-scraper --cov=sandbox/basics`
-   Snimi ključne rezultate u `summary.md`.

## Hints

-   Kratki nazivi testova: `test_<function>_<case>`
-   Uvek `tmp_path` za fajl sisteme; ne koristi realne putanje
-   Parametrizacija smanjuje duplikate, koristi tabele
-   Ako test postane složen, ekstraktuj helper funkciju u sam test fajl

## Validation

-   `pytest -q` čist
-   Coverage za target module >= 80% (ili zabeleži procenat)
-   Svi taskovi čekirani u `tasks.md`
