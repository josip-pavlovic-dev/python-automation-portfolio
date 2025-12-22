---
type: exercises
topic: Pathlib Complete Exercises
date: 2025-12-22
linked_to: 2025-12-22_pathlib_advanced
language: bilingual
status: active
difficulty: beginner-intermediate
environment: python_repl + files
estimated_time: 8 hours
phase: foundation
milestone: pathlib_mastery
---

# 🏋️‍♂️ Pathlib Complete Exercises (8h)

## FAZA 1 (2h) — Osnove Path

-   Napravi `path_basics.py` sa 12+ primera: `cwd`, `home`, `__file__`, `parent`, `parents`, `resolve`, `relative_to`, `expanduser`, `/` operator.
-   Zadaci:
    -   Spoji putanje za `data/users.csv` i `logs/app.log` bez `os.path`.
    -   Prikaži `stem`, `suffix`, `suffixes`, `name` za primer fajl.
    -   Napravi funkciju `def ensure_dir(path: Path) -> Path` koja kreira dir ako ne postoji i vrati ga.
    -   Napravi helper `def normalize(raw: str) -> Path` koji radi `expanduser().resolve()` i baca `ValueError` ako nema suffix.
-   Test hint: koristi `tmp_path / "a" / "b"` za kreiranje strukture.
-   Output hint: `print(path.resolve())` da vidiš realnu putanju.

---

## FAZA 2 (2h) — Čitanje/Pisanje + Encoding + Error Handling

-   Kreiraj `file_io_safe.py` sa funkcijama:
    -   `read_text_safe(path: Path) -> str`
    -   `write_text_safe(path: Path, content: str) -> None`
    -   `append_lines(path: Path, lines: Iterable[str]) -> None`
    -   `safe_copy(src: Path, dst: Path) -> None` (binarni copy sa logom)
-   Zahtevi:
    -   Uvek `encoding="utf-8"` i `newline=""` gde ima smisla.
    -   Ako fajl ne postoji u `read_text_safe`, podigni `FileNotFoundError` sa jasnim msg.
    -   Loguj `logger.info` za uspeh, `logger.exception` za grešku.
    -   `safe_copy` mora kreirati roditeljski folder za `dst` ako ne postoji.
-   Mini zadatak: kopiraj `sandbox/basics/csv_with_types.py` u privremeni fajl koristeći helper funkcije; proveri sadržaj.
-   Test hint: `caplog` za proveru da log poruke postoje; `tmp_path` za sve fajl operacije.

---

## FAZA 3 (2h) — Globbing, Traversal, Metadata

-   Kreiraj `glob_filters.py` sa:
    -   `list_csv_sorted(root: Path) -> list[Path]` (sort by name)
    -   `recent_logs(root: Path, seconds: int) -> list[Path]` (mtime newer than now-seconds)
    -   `ensure_suffix(path: Path, suffix: str) -> Path` (dodaj suffix ako fali)
    -   `filter_by_size(paths: Iterable[Path], max_bytes: int) -> list[Path]`
-   Zadaci:
    -   Filtriraj sve `.json` fajlove dublje (koristi `rglob`).
    -   Izbaci fajlove veće od 1 MB (`st_size`).
    -   Napravi symlink i testiraj `resolve()` na njemu.
-   Test hint: generiši dummy fajlove u `tmp_path` i koristi `time.sleep(1)` da simulira mtime; za symlink koristi `tmp_path / "logs" / "today.log"`.

---

## FAZA 4 (2h) — Integracija sa Web Scraper + Tests

-   U `projects/01-web-scraper/`:
    -   Uvedi `Path` u `config.py` i `scraper.py` gde je još string.
    -   Dodaj helper `get_output_dir() -> Path` koji kreira `output/` ako ne postoji.
    -   Loguj pune putanje pri upisu fajlova.
    -   Dodaj helper `get_log_file() -> Path` koji vraća putanju log fajla u `logs/` i kreira dir.
-   Testovi (kreiraj u `projects/01-web-scraper/tests/test_paths.py`):
    -   `test_output_dir_created(tmp_path)` — koristi `monkeypatch` za `config.BASE_DIR = tmp_path` ako treba.
    -   `test_write_log_path(tmp_path, caplog)` — proveri da log fajl postoji posle helpera i da loguje putanju.
    -   `test_ensure_suffix_cli_flag(tmp_path)` — validiraj da CLI flag `--output-dir` normalizuje `Path` i dodaje suffix ako tražiš fajl.
-   Opcioni stretch: dodaj CLI flag `--output-dir` i validiraj `Path`; dodaj `--log-file` sa suffix proverom.

---

## Hints

-   Uvek normalizuj `path = path.expanduser()` ako primaš input od korisnika, zatim `resolve()`.
-   `Path.write_bytes` i `Path.read_bytes` za binarne fajlove.
-   Za robustan copy: `dst.write_bytes(src.read_bytes())` u `try/except` sa loggerom.
-   Za mtime konverziju koristi `datetime.fromtimestamp(path.stat().st_mtime)`.
-   Koristi `missing_ok=True` u `unlink` ako brišeš opcionalne fajlove.
-   `caplog.text` hvata logove u testovima; assert substring.

---

## Validation

-   `python -m pytest -q -k pathlib`
-   `tasks.md` sve čekirano
-   Manualno test: pokreni skriptu koja čita i piše fajl u `sandbox/basics/pathlib_playground/`
-   Logovi pregledani (da sadrže putanje)
