---
type: practice_plan
days: Dan 6-7
topics: Pathlib + Testing + Error Handling
duration: 2 dana (8h + 8h)
status: active
---

# 🎯 Plan vežbe — Dan 6-7: Pathlib + Testing + Error Handling

## 📊 Trenutno stanje

✅ **Završio si:**

-   Dan 1: Terminal + Git osnove
-   Dan 2: CSV basics (CSV module, DictReader/writer)
-   Dan 3: CLI + argparse (Protocol tipizacija, parent parsers)
-   Dan 4: Logging (levels, caplog)
-   Dan 5: Type annotations (TypedDict, Protocol, NotRequired)

📂 **Imaš ove funkcionalne skripte u sandbox/basics/**:

-   `csv_cleaner_final.py` (60 lines) — Dialect detection, row cleaning, stats
-   `csv_with_conversion.py` (75 lines) — TypedDict sa NotRequired, konverzija age u int
-   `path_basics.py` (184 lines) — 12+ Path metoda (cwd, home, resolve, relative_to, parents, iterdir)
-   `cli_with_types.py` (50 lines) — Protocol klasa za argparse args
-   `cli_logging_practice/scripts/subcommands_cli_typed.py` (120+ lines) — Parent parser za verbose flag
-   `json_with_types.py` — JSON read/write sa type annotations

🎯 **Cilj za naredna 2 dana:**

-   Dodaj **testove** svim postojećim skriptama
-   Integriši **error handling** patterns
-   Nauči **tmp_path** fixture za file operations
-   Nauči **caplog** za testing logging
-   **Refaktoriši** postojeće skripte da budu robustnije

---

## 📅 DAN 6: Pathlib + Testing Osnove (8h)

### ⏰ FAZA 1 (2h) — Refaktorisanje path_basics.py

**Zadatak:** Pretvori sve print() funkcije u path_basics.py u funkcije koje vraćaju vrednosti i piši testove za njih.

**Koraci:**

1. **Čitaj** [cheatsheet_pathlib_file_io.md](../scratch/docs/cheatsheet_pathlib_file_io.md) (30min)

    - Fokus: Path kreiranje, resolve(), relative_to(), iterdir()
    - Vežbaj u REPL-u `python -m pathlib_playground`

2. **Refaktoriši** `path_basics.py` (60min):

    ```python
    # BILO (primer):
    def demo_cwd():
        print(Path.cwd())

    # TREBA (refaktorisano):
    def get_current_dir() -> Path:
        """Vrati trenutni working directory."""
        return Path.cwd()

    def get_home_dir() -> Path:
        """Vrati home directory."""
        return Path.home()

    def resolve_path(path: Path) -> Path:
        """Vrati apsolutnu putanju."""
        return path.resolve()
    ```

3. **Kreiraj** `sandbox/basics/tests/test_path_basics.py` (30min):

    ```python
    import pytest
    from pathlib import Path
    from sandbox.basics.path_basics import (
        get_current_dir,
        get_home_dir,
        resolve_path,
    )

    def test_get_current_dir():
        """Test da get_current_dir vraća Path objekat."""
        result = get_current_dir()
        assert isinstance(result, Path)
        assert result.is_absolute()

    def test_get_home_dir():
        """Test da get_home_dir vraća home direktorijum."""
        result = get_home_dir()
        assert isinstance(result, Path)
        assert result.exists()
        assert result.is_dir()

    def test_resolve_path(tmp_path: Path):
        """Test da resolve_path vraća apsolutnu putanju."""
        relative = Path("some/relative/path")
        resolved = resolve_path(relative)
        assert resolved.is_absolute()
    ```

**Deliverable:** `path_basics.py` sa 8+ funkcija koje vraćaju vrednosti + `test_path_basics.py` sa 8+ testova.

**Checkpoint:** Pokreni testove: `pytest sandbox/basics/tests/test_path_basics.py -v`

---

### ⏰ FAZA 2 (2h) — File I/O sa tmp_path

**Zadatak:** Nauči `tmp_path` fixture i dodaj testove za file read/write operacije.

**Koraci:**

1. **Kreiraj** `sandbox/basics/file_operations.py` (45min):

    ```python
    from pathlib import Path

    def safe_read_text(path: Path) -> str | None:
        """Sigurno čitaj tekst iz fajla."""
        if not path.exists():
            return None
        try:
            return path.read_text(encoding="utf-8")
        except PermissionError:
            return None

    def safe_write_text(path: Path, content: str) -> bool:
        """Sigurno piši tekst u fajl, kreiraj parent direktorijum."""
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            return True
        except (PermissionError, OSError):
            return False

    def backup_file(source: Path, backup_dir: Path) -> Path | None:
        """Backup fajl u backup_dir sa timestamp."""
        if not source.exists():
            return None

        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{source.stem}_{timestamp}{source.suffix}"
        backup_path = backup_dir / backup_name

        try:
            backup_dir.mkdir(parents=True, exist_ok=True)
            backup_path.write_bytes(source.read_bytes())
            return backup_path
        except (PermissionError, OSError):
            return None
    ```

2. **Piši testove** `tests/test_file_operations.py` (45min):

    ```python
    import pytest
    from pathlib import Path
    from sandbox.basics.file_operations import (
        safe_read_text,
        safe_write_text,
        backup_file,
    )

    def test_safe_read_text_existing(tmp_path: Path):
        """Test čitanja postojećeg fajla."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello, world!", encoding="utf-8")

        result = safe_read_text(test_file)
        assert result == "Hello, world!"

    def test_safe_read_text_missing(tmp_path: Path):
        """Test čitanja nepostojećeg fajla."""
        missing = tmp_path / "missing.txt"
        result = safe_read_text(missing)
        assert result is None

    def test_safe_write_text_creates_parent(tmp_path: Path):
        """Test da safe_write_text kreira parent direktorijum."""
        nested = tmp_path / "sub" / "nested" / "file.txt"
        success = safe_write_text(nested, "content")

        assert success is True
        assert nested.exists()
        assert nested.read_text(encoding="utf-8") == "content"

    def test_backup_file_creates_copy(tmp_path: Path):
        """Test da backup_file kreira backup sa timestamp."""
        source = tmp_path / "original.txt"
        source.write_text("original content", encoding="utf-8")

        backup_dir = tmp_path / "backups"
        backup_path = backup_file(source, backup_dir)

        assert backup_path is not None
        assert backup_path.exists()
        assert backup_path.read_text(encoding="utf-8") == "original content"
        assert backup_path.name.startswith("original_")
    ```

3. **Čitaj** [cheatsheet_pytest_testing.md](../scratch/docs/cheatsheet_pytest_testing.md) (30min)
    - Fokus: tmp_path fixture, pytest.raises, assertions

**Deliverable:** `file_operations.py` sa 3+ funkcije + `test_file_operations.py` sa 8+ testova.

**Checkpoint:** Pokreni testove: `pytest sandbox/basics/tests/test_file_operations.py -v`

---

### ⏰ FAZA 3 (2h) — Testing CSV Cleanera

**Zadatak:** Dodaj testove za `csv_cleaner_final.py` koristeći `tmp_path` i fixtures.

**Koraci:**

1. **Refaktoriši** `csv_cleaner_final.py` (30min):

    - Trenutno je funcijski kompletusan, ali nema testove
    - Dodaj type hints za return tipove gde nedostaju

2. **Kreiraj** `sandbox/basics/tests/conftest.py` (30min):

    ```python
    """Shared fixtures for CSV tests."""
    import pytest
    from pathlib import Path

    @pytest.fixture
    def sample_csv(tmp_path: Path) -> Path:
        """Create sample CSV file."""
        csv_path = tmp_path / "sample.csv"
        csv_path.write_text(
            "name,age,city\n"
            "Alice,30,New York\n"
            "Bob,25,Los Angeles\n"
            "  Charlie  ,35,  Chicago  \n",
            encoding="utf-8"
        )
        return csv_path

    @pytest.fixture
    def invalid_csv(tmp_path: Path) -> Path:
        """Create invalid CSV file."""
        csv_path = tmp_path / "invalid.csv"
        csv_path.write_text(
            "name,age\n"
            "Alice,abc\n",  # Invalid age
            encoding="utf-8"
        )
        return csv_path
    ```

3. **Piši testove** `tests/test_csv_cleaner.py` (60min):

    ```python
    import pytest
    from pathlib import Path
    from sandbox.basics.csv_cleaner_final import (
        detect_dialect,
        read_rows,
        clean_rows,
        write_rows,
    )

    def test_detect_dialect(sample_csv: Path):
        """Test dialect detection."""
        dialect = detect_dialect(sample_csv)
        assert dialect is not None
        assert dialect.delimiter == ","

    def test_read_rows(sample_csv: Path):
        """Test reading CSV rows."""
        dialect = detect_dialect(sample_csv)
        rows = read_rows(sample_csv, dialect)
        assert len(rows) == 3
        assert rows[0]["name"] == "Alice"

    def test_clean_rows_strips_whitespace(sample_csv: Path):
        """Test da clean_rows uklanja whitespace."""
        dialect = detect_dialect(sample_csv)
        rows = read_rows(sample_csv, dialect)
        cleaned, stats = clean_rows(rows)

        # Check last row (has whitespace)
        assert cleaned[-1]["name"] == "Charlie"
        assert cleaned[-1]["city"] == "Chicago"
        assert stats["cleaned_rows"] == 3

    def test_write_rows_creates_file(tmp_path: Path, sample_csv: Path):
        """Test writing CSV rows."""
        dialect = detect_dialect(sample_csv)
        rows = read_rows(sample_csv, dialect)
        cleaned, _ = clean_rows(rows)

        output = tmp_path / "output.csv"
        write_rows(output, cleaned, dialect)

        assert output.exists()
        content = output.read_text(encoding="utf-8")
        assert "Alice" in content
        assert "Charlie" in content
    ```

**Deliverable:** `conftest.py` sa shared fixtures + `test_csv_cleaner.py` sa 6+ testova.

**Checkpoint:** Pokreni testove: `pytest sandbox/basics/tests/ -v`

---

### ⏰ FAZA 4 (2h) — Integracija sa logovanjem

**Zadatak:** Dodaj logging u file_operations.py i testuj sa caplog.

**Koraci:**

1. **Dodaj logging** u `file_operations.py` (30min):

    ```python
    import logging
    from pathlib import Path

    logger = logging.getLogger(__name__)

    def safe_read_text(path: Path) -> str | None:
        """Sigurno čitaj tekst iz fajla sa logovanjem."""
        if not path.exists():
            logger.error(f"File not found: {path}")
            return None

        try:
            logger.info(f"Reading {path}")
            return path.read_text(encoding="utf-8")
        except PermissionError:
            logger.error(f"Permission denied: {path}")
            return None
    ```

2. **Piši testove sa caplog** (60min):

    ```python
    import pytest
    import logging
    from pathlib import Path
    from sandbox.basics.file_operations import safe_read_text

    def test_safe_read_text_logs_missing_file(tmp_path: Path, caplog):
        """Test da safe_read_text loguje kada fajl ne postoji."""
        missing = tmp_path / "missing.txt"

        with caplog.at_level(logging.ERROR):
            result = safe_read_text(missing)

        assert result is None
        assert "File not found" in caplog.text
        assert str(missing) in caplog.text

    def test_safe_read_text_logs_success(tmp_path: Path, caplog):
        """Test da safe_read_text loguje uspešno čitanje."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("content", encoding="utf-8")

        with caplog.at_level(logging.INFO):
            result = safe_read_text(test_file)

        assert result == "content"
        assert "Reading" in caplog.text
    ```

3. **Čitaj** [cheatsheet_pytest_testing.md](../scratch/docs/cheatsheet_pytest_testing.md) (30min)
    - Fokus: caplog fixture, log level assertions

**Deliverable:** `file_operations.py` sa logging + testovi sa caplog assertions.

**Checkpoint:** Pokreni testove: `pytest sandbox/basics/tests/test_file_operations.py::test_safe_read_text_logs_missing_file -v`

**Kraj Dana 6:** Napisi SUMMARY_DAN_06.md sa coverage izveštajem:

```bash
pytest --cov=sandbox.basics --cov-report=term-missing
```

---

## 📅 DAN 7: Error Handling + Advanced Testing (8h)

### ⏰ FAZA 1 (2h) — Error Handling u CSV cleaneru

**Zadatak:** Dodaj robust error handling u `csv_cleaner_final.py`.

**Koraci:**

1. **Čitaj** [cheatsheet_error_handling.md](../scratch/docs/cheatsheet_error_handling.md) (30min)

    - Fokus: Custom exceptions, validation patterns, logging sa exceptions

2. **Dodaj custom exceptions** u `csv_cleaner_final.py` (45min):

    ```python
    class CSVError(Exception):
        """Base exception za CSV operacije."""
        pass

    class CSVValidationError(CSVError):
        """Greška u validaciji CSV redova."""
        pass

    class CSVDialectError(CSVError):
        """Greška u detekciji CSV dialect-a."""
        pass

    def detect_dialect(path: Path) -> csv.Dialect:
        """Detect CSV dialect ili baci CSVDialectError."""
        if not path.exists():
            raise FileNotFoundError(f"CSV file not found: {path}")

        try:
            with path.open(encoding="utf-8") as f:
                sample = f.read(1024)
                sniffer = csv.Sniffer()
                return sniffer.sniff(sample)
        except csv.Error as e:
            raise CSVDialectError(f"Cannot detect dialect: {e}") from e
    ```

3. **Piši testove za exception cases** (45min):

    ```python
    import pytest
    from sandbox.basics.csv_cleaner_final import (
        detect_dialect,
        CSVDialectError,
    )

    def test_detect_dialect_missing_file(tmp_path: Path):
        """Test da detect_dialect baca FileNotFoundError."""
        missing = tmp_path / "missing.csv"

        with pytest.raises(FileNotFoundError, match="not found"):
            detect_dialect(missing)

    def test_detect_dialect_invalid_csv(tmp_path: Path):
        """Test da detect_dialect baca CSVDialectError za invalid CSV."""
        invalid = tmp_path / "invalid.csv"
        invalid.write_text("not a csv", encoding="utf-8")

        with pytest.raises(CSVDialectError, match="Cannot detect"):
            detect_dialect(invalid)
    ```

**Deliverable:** `csv_cleaner_final.py` sa custom exceptions + testovi za exception paths.

**Checkpoint:** Pokreni testove: `pytest sandbox/basics/tests/test_csv_cleaner.py -v`

---

### ⏰ FAZA 2 (2h) — Validation patterns

**Zadatak:** Dodaj validation funkcije sa error reporting.

**Koraci:**

1. **Kreiraj** `sandbox/basics/validators.py` (60min):

    ```python
    """Validation helpers sa error reporting."""
    from typing import Optional

    def validate_csv_row(row: dict, required_keys: list[str]) -> Optional[str]:
        """Validate CSV row, vrati error poruku ili None."""
        # Check required keys
        missing = [k for k in required_keys if k not in row]
        if missing:
            return f"Missing keys: {missing}"

        # Check empty values
        empty = [k for k in required_keys if not row[k].strip()]
        if empty:
            return f"Empty values: {empty}"

        # Check age is numeric
        if "age" in row:
            try:
                int(row["age"])
            except ValueError:
                return f"Invalid age: {row['age']}"

        return None  # No errors

    def validate_age(age_str: str) -> tuple[bool, Optional[str]]:
        """Validate age string, vrati (is_valid, error_message)."""
        try:
            age = int(age_str)
            if age < 0 or age > 150:
                return False, f"Age out of range: {age}"
            return True, None
        except ValueError:
            return False, f"Invalid age format: {age_str}"
    ```

2. **Piši testove** `tests/test_validators.py` (60min):

    ```python
    import pytest
    from sandbox.basics.validators import (
        validate_csv_row,
        validate_age,
    )

    def test_validate_csv_row_valid():
        """Test validacije validnog reda."""
        row = {"name": "Alice", "age": "30"}
        error = validate_csv_row(row, ["name", "age"])
        assert error is None

    def test_validate_csv_row_missing_key():
        """Test validacije reda sa missing key."""
        row = {"name": "Alice"}
        error = validate_csv_row(row, ["name", "age"])
        assert error is not None
        assert "Missing keys" in error
        assert "age" in error

    def test_validate_csv_row_empty_value():
        """Test validacije reda sa praznom vrednoscu."""
        row = {"name": "", "age": "30"}
        error = validate_csv_row(row, ["name", "age"])
        assert error is not None
        assert "Empty values" in error

    @pytest.mark.parametrize("age_str,expected", [
        ("30", (True, None)),
        ("0", (True, None)),
        ("150", (True, None)),
        ("-1", (False, "Age out of range")),
        ("151", (False, "Age out of range")),
        ("abc", (False, "Invalid age format")),
    ])
    def test_validate_age(age_str: str, expected: tuple[bool, Optional[str]]):
        """Test validacije age stringa."""
        is_valid, error = validate_age(age_str)
        assert is_valid == expected[0]
        if error:
            assert expected[1] in error
    ```

**Deliverable:** `validators.py` sa 2+ validation funkcije + `test_validators.py` sa parametrized testovima.

**Checkpoint:** Pokreni testove: `pytest sandbox/basics/tests/test_validators.py -v`

---

### ⏰ FAZA 3 (2h) — Retry pattern i batch processing

**Zadatak:** Implementuj retry pattern i batch file processor.

**Koraci:**

1. **Kreiraj** `sandbox/basics/batch_processor.py` (90min):

    ```python
    """Batch file processor sa error recovery."""
    import logging
    from pathlib import Path
    from typing import Callable, TypedDict

    logger = logging.getLogger(__name__)

    class ProcessStats(TypedDict):
        """Statistika batch processinga."""
        total: int
        success: int
        failed: int
        errors: list[tuple[Path, str]]

    def batch_process_files(
        input_dir: Path,
        process_func: Callable[[Path], None],
        pattern: str = "*.csv",
    ) -> ProcessStats:
        """Process sve fajlove sa error recovery."""
        stats: ProcessStats = {
            "total": 0,
            "success": 0,
            "failed": 0,
            "errors": [],
        }

        if not input_dir.exists():
            logger.error(f"Input directory not found: {input_dir}")
            return stats

        files = list(input_dir.glob(pattern))
        stats["total"] = len(files)

        for file_path in files:
            try:
                logger.info(f"Processing {file_path.name}")
                process_func(file_path)
                stats["success"] += 1

            except Exception as e:
                logger.exception(f"Failed to process {file_path.name}")
                stats["failed"] += 1
                stats["errors"].append((file_path, str(e)))

        logger.info(f"Batch complete: {stats['success']}/{stats['total']} succeeded")
        return stats
    ```

2. **Piši testove** (30min):

    ```python
    import pytest
    from pathlib import Path
    from sandbox.basics.batch_processor import batch_process_files

    def test_batch_process_all_success(tmp_path: Path):
        """Test batch processinga svih uspešnih fajlova."""
        # Create test files
        for i in range(3):
            (tmp_path / f"file_{i}.csv").write_text("content", encoding="utf-8")

        processed = []
        def process_func(path: Path):
            processed.append(path.name)

        stats = batch_process_files(tmp_path, process_func, "*.csv")

        assert stats["total"] == 3
        assert stats["success"] == 3
        assert stats["failed"] == 0
        assert len(processed) == 3

    def test_batch_process_with_failures(tmp_path: Path):
        """Test batch processinga sa nekim greškama."""
        # Create test files
        (tmp_path / "good.csv").write_text("content", encoding="utf-8")
        (tmp_path / "bad.csv").write_text("content", encoding="utf-8")

        def process_func(path: Path):
            if "bad" in path.name:
                raise ValueError("Bad file")

        stats = batch_process_files(tmp_path, process_func, "*.csv")

        assert stats["total"] == 2
        assert stats["success"] == 1
        assert stats["failed"] == 1
        assert len(stats["errors"]) == 1
    ```

**Deliverable:** `batch_processor.py` sa TypedDict stats + testovi sa mock processingom.

**Checkpoint:** Pokreni testove: `pytest sandbox/basics/tests/test_batch_processor.py -v`

---

### ⏰ FAZA 4 (2h) — Integration test: CLI + CSV + Logging

**Zadatak:** Kreiraj integration test koji testira ceo flow: CLI argparse → CSV processing → logging → output.

**Koraci:**

1. **Refaktoriši** `cli_with_types.py` da ima testable handler (45min):

    ```python
    import logging
    from pathlib import Path
    from typing import Protocol
    from sandbox.basics.csv_cleaner_final import (
        detect_dialect,
        read_rows,
        clean_rows,
        write_rows,
    )

    logger = logging.getLogger(__name__)

    class ProcessArgs(Protocol):
        input_file: str
        output_file: str | None
        verbose: bool
        limit: int

    def cmd_process(args: ProcessArgs) -> bool:
        """Process komanda sa CSV cleaningom."""
        input_path = Path(args.input_file)

        if not input_path.exists():
            logger.error(f"File not found: {input_path}")
            return False

        if args.verbose:
            logger.info(f"Processing {args.input_file} (limit={args.limit})")

        try:
            dialect = detect_dialect(input_path)
            rows = read_rows(input_path, dialect)
            cleaned, stats = clean_rows(rows[:args.limit])

            if args.output_file:
                output_path = Path(args.output_file)
                write_rows(output_path, cleaned, dialect)
                logger.info(f"Wrote {stats['cleaned_rows']} rows to {output_path}")

            return True
        except Exception as e:
            logger.exception(f"Processing failed: {e}")
            return False
    ```

2. **Piši integration test** `tests/test_cli_integration.py` (75min):

    ```python
    import pytest
    import logging
    from pathlib import Path
    from argparse import Namespace
    from sandbox.basics.cli_with_types import cmd_process

    def test_cli_process_success(tmp_path: Path, sample_csv: Path, caplog):
        """Test celog CLI flow sa uspešnim processingom."""
        output = tmp_path / "output.csv"

        args = Namespace(
            input_file=str(sample_csv),
            output_file=str(output),
            verbose=True,
            limit=10,
        )

        with caplog.at_level(logging.INFO):
            success = cmd_process(args)

        assert success is True
        assert output.exists()
        assert "Processing" in caplog.text
        assert "Wrote" in caplog.text

    def test_cli_process_missing_file(tmp_path: Path, caplog):
        """Test CLI handleanja nepostojećeg fajla."""
        missing = tmp_path / "missing.csv"

        args = Namespace(
            input_file=str(missing),
            output_file=None,
            verbose=False,
            limit=10,
        )

        with caplog.at_level(logging.ERROR):
            success = cmd_process(args)

        assert success is False
        assert "File not found" in caplog.text
    ```

**Deliverable:** Integration test koji testira CLI → CSV → Logging flow.

**Checkpoint:** Pokreni testove: `pytest sandbox/basics/tests/test_cli_integration.py -v`

**Kraj Dana 7:** Napisi SUMMARY_DAN_07.md sa coverage izveštajem:

```bash
pytest --cov=sandbox.basics --cov-report=html
xdg-open htmlcov/index.html  # Pogledaj coverage u browser
```

---

## ✅ Finalni Checklist

**Dan 6:**

-   [ ] Refaktorisao path_basics.py u testable funkcije
-   [ ] Napisao 8+ testova za Path operacije
-   [ ] Kreirao file_operations.py sa safe read/write/backup
-   [ ] Napisao 8+ testova sa tmp_path fixture
-   [ ] Dodao testove za csv_cleaner_final.py
-   [ ] Kreirao conftest.py sa shared fixtures
-   [ ] Integrirao logging u file_operations.py
-   [ ] Napisao testove sa caplog assertions
-   [ ] Generisao coverage izveštaj (cilj: >80%)

**Dan 7:**

-   [ ] Dodao custom exceptions u csv_cleaner_final.py
-   [ ] Napisao testove za exception paths
-   [ ] Kreirao validators.py sa validation patterns
-   [ ] Napisao parametrized testove za validators
-   [ ] Implementirao batch_processor.py sa error recovery
-   [ ] Napisao testove za batch processing
-   [ ] Refaktorisao cli_with_types.py u testable handler
-   [ ] Napisao integration test CLI → CSV → Logging
-   [ ] Generisao finalni coverage HTML report (cilj: >85%)

---

## 📚 Reference Materijali

**Cheatsheets (scratch/docs/):**

-   [cheatsheet_pathlib_file_io.md](../scratch/docs/cheatsheet_pathlib_file_io.md) — 600+ linija
-   [cheatsheet_pytest_testing.md](../scratch/docs/cheatsheet_pytest_testing.md) — 550+ linija
-   [cheatsheet_error_handling.md](../scratch/docs/cheatsheet_error_handling.md) — 500+ linija

**Learning materials (learning/):**

-   [2025-12-22_pathlib_advanced/README.md](./2025-12-22_pathlib_advanced/README.md)
-   [2025-12-22_pathlib_advanced/kickoff.md](./2025-12-22_pathlib_advanced/kickoff.md)
-   [2025-12-22_pathlib_advanced/cheatsheet.md](./2025-12-22_pathlib_advanced/cheatsheet.md)
-   [2025-12-23_testing_advanced/README.md](./2025-12-23_testing_advanced/README.md)

**Postojeće skripte (sandbox/basics/):**

-   `csv_cleaner_final.py` — CSV cleaning sa dialect detection
-   `csv_with_conversion.py` — TypedDict sa konverzijom tipova
-   `path_basics.py` — 12+ Path metoda
-   `cli_with_types.py` — Protocol za argparse args
-   `cli_logging_practice/scripts/subcommands_cli_typed.py` — Parent parser pattern

---

## 💡 Tips

1. **Pokreni testove posle svake funkcije:** `pytest -v` da odmah vidiš greške.
2. **Koristi `pytest -k test_name`** za pokretanje samo jednog testa.
3. **Watch mode:** `pytest-watch` za automatsko pokretanje testova na save.
4. **Coverage:** `pytest --cov=sandbox.basics --cov-report=term-missing` da vidiš šta nije pokriveno.
5. **Debug:** `pytest -v -s` da vidiš print() output u testovima.
6. **Fixture debug:** `pytest --fixtures` da vidiš sve dostupne fixtures.
7. **Caplog:** `print(caplog.text)` u testu da vidiš log output.
8. **Pause:** Pravi pauzu na svakih 50min, ustani, prošetaj.

---

**🎯 Cilj:** Na kraju Dana 7, trebaš imati:

-   30+ testova koji pokrivaju sve tvoje sandbox skripte
-   Coverage >85%
-   Robustne skripte sa error handling patterns
-   Solidno razumevanje tmp_path, caplog, pytest.raises
-   Spremnost za Dan 8: Web Scraper projekat

**Srećno! 🚀**
