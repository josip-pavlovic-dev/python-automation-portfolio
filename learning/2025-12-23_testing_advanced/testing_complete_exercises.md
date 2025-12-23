---
type: exercises
date: 2025-12-23
linked_to: 2025-12-23_testing_advanced
blocks: 4
status: active
updated: 2025-12-23
focus: testing existing sandbox scripts
---

# 🏋️‍♂️ Testing Complete Exercises (8h)

> **Cilj:** Dodaj robustne testove svim postojećim sandbox skriptama (csv_cleaner_final.py, path_basics.py, cli_with_types.py, validators.py, file_operations.py).

---

## FAZA 1 (2h) — Test Path Basics

### Zadatak 1.1: Refaktoriši path_basics.py (60min)

Trenutno `path_basics.py` ima samo demo funkcije sa `print()` outputom. Refaktoriši ih u pure funkcije koje vraćaju vrednosti.

**Bilo:**

```python
def demo_cwd():
    print(Path.cwd())
```

**Treba:**

```python
def get_current_dir() -> Path:
    """Vrati trenutni working directory."""
    return Path.cwd()

def get_home_dir() -> Path:
    """Vrati home directory."""
    return Path.home()

def resolve_path(path: Path) -> Path:
    """Vrati apsolutnu putanju."""
    return path.resolve()

def get_parent(path: Path) -> Path:
    """Vrati parent direktorijum."""
    return path.parent

def list_files(directory: Path, pattern: str = "*") -> list[Path]:
    """Vrati listu fajlova u direktorijumu."""
    return list(directory.glob(pattern))
```

### Zadatak 1.2: Kreiraj test_path_basics.py (60min)

**Lokacija:** `sandbox/basics/tests/test_path_basics.py`

```python
"""Test path_basics.py funkcije."""
import pytest
from pathlib import Path
from sandbox.basics.path_basics import (
    get_current_dir,
    get_home_dir,
    resolve_path,
    get_parent,
    list_files,
)


def test_get_current_dir():
    """Test da get_current_dir vraća Path objekat."""
    result = get_current_dir()

    assert isinstance(result, Path)
    assert result.is_absolute()
    assert result.exists()


def test_get_home_dir():
    """Test da get_home_dir vraća home direktorijum."""
    result = get_home_dir()

    assert isinstance(result, Path)
    assert result.is_absolute()
    assert result.exists()
    assert result.is_dir()


def test_resolve_path_relative():
    """Test da resolve_path pretvara relativnu putanju u apsolutnu."""
    relative = Path("some/relative/path")
    resolved = resolve_path(relative)

    assert resolved.is_absolute()


def test_resolve_path_already_absolute():
    """Test da resolve_path ne menja već apsolutnu putanju."""
    absolute = Path("/tmp")
    resolved = resolve_path(absolute)

    assert resolved.is_absolute()


def test_get_parent(tmp_path: Path):
    """Test da get_parent vraća parent direktorijum."""
    child = tmp_path / "child"
    parent = get_parent(child)

    assert parent == tmp_path


def test_list_files_empty(tmp_path: Path):
    """Test da list_files vraća praznu listu za prazan direktorijum."""
    files = list_files(tmp_path)
    assert files == []


def test_list_files_with_pattern(tmp_path: Path):
    """Test da list_files filtrira po patternu."""
    # Create test files
    (tmp_path / "file1.txt").touch()
    (tmp_path / "file2.csv").touch()
    (tmp_path / "file3.txt").touch()

    txt_files = list_files(tmp_path, "*.txt")

    assert len(txt_files) == 2
    assert all(f.suffix == ".txt" for f in txt_files)


@pytest.mark.parametrize("filename,expected_suffix", [
    ("test.txt", ".txt"),
    ("data.csv", ".csv"),
    ("archive.tar.gz", ".gz"),
])
def test_file_suffixes(tmp_path: Path, filename: str, expected_suffix: str):
    """Test da Path correctly detektuje file extensions."""
    file_path = tmp_path / filename
    file_path.touch()

    assert file_path.suffix == expected_suffix
```

**Checkpoint:** Pokreni testove:

```bash
pytest sandbox/basics/tests/test_path_basics.py -v
```

---

## FAZA 2 (2h) — Test File Operations

### Zadatak 2.1: Kreiraj file_operations.py (60min)

**Lokacija:** `sandbox/basics/file_operations.py`

```python
"""Safe file operation helpers."""
import logging
from pathlib import Path
from datetime import datetime

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


def safe_write_text(path: Path, content: str) -> bool:
    """Sigurno piši tekst u fajl, kreiraj parent direktorijum."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        logger.info(f"Wrote {len(content)} chars to {path}")
        return True
    except (PermissionError, OSError) as e:
        logger.error(f"Failed to write {path}: {e}")
        return False


def backup_file(source: Path, backup_dir: Path) -> Path | None:
    """Backup fajl u backup_dir sa timestamp."""
    if not source.exists():
        logger.error(f"Source file not found: {source}")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{source.stem}_{timestamp}{source.suffix}"
    backup_path = backup_dir / backup_name

    try:
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_path.write_bytes(source.read_bytes())
        logger.info(f"Backed up {source} to {backup_path}")
        return backup_path
    except (PermissionError, OSError) as e:
        logger.error(f"Backup failed: {e}")
        return None


def cleanup_old_files(directory: Path, days: int, pattern: str = "*.log") -> int:
    """Obriši fajlove starije od `days` dana."""
    if not directory.exists():
        logger.warning(f"Directory not found: {directory}")
        return 0

    import time
    cutoff = time.time() - (days * 86400)
    deleted = 0

    for file_path in directory.glob(pattern):
        if file_path.is_file() and file_path.stat().st_mtime < cutoff:
            try:
                file_path.unlink()
                logger.info(f"Deleted old file: {file_path}")
                deleted += 1
            except OSError as e:
                logger.error(f"Failed to delete {file_path}: {e}")

    return deleted
```

### Zadatak 2.2: Kreiraj test_file_operations.py (60min)

**Lokacija:** `sandbox/basics/tests/test_file_operations.py`

```python
"""Test file_operations.py helpers."""
import pytest
import logging
from pathlib import Path
from sandbox.basics.file_operations import (
    safe_read_text,
    safe_write_text,
    backup_file,
    cleanup_old_files,
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


def test_safe_read_text_logs_missing_file(tmp_path: Path, caplog):
    """Test da safe_read_text loguje missing file."""
    missing = tmp_path / "missing.txt"

    with caplog.at_level(logging.ERROR):
        result = safe_read_text(missing)

    assert result is None
    assert "File not found" in caplog.text
    assert str(missing) in caplog.text


def test_safe_write_text_creates_file(tmp_path: Path):
    """Test da safe_write_text kreira fajl."""
    test_file = tmp_path / "new.txt"
    success = safe_write_text(test_file, "content")

    assert success is True
    assert test_file.exists()
    assert test_file.read_text(encoding="utf-8") == "content"


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
    assert backup_path.suffix == ".txt"


def test_backup_file_missing_source(tmp_path: Path, caplog):
    """Test da backup_file loguje missing source."""
    missing = tmp_path / "missing.txt"
    backup_dir = tmp_path / "backups"

    with caplog.at_level(logging.ERROR):
        result = backup_file(missing, backup_dir)

    assert result is None
    assert "Source file not found" in caplog.text


def test_cleanup_old_files(tmp_path: Path):
    """Test da cleanup_old_files briše stare fajlove."""
    import time

    # Create old file (modify mtime)
    old_file = tmp_path / "old.log"
    old_file.touch()

    # Set mtime to 10 days ago
    ten_days_ago = time.time() - (10 * 86400)
    import os
    os.utime(old_file, (ten_days_ago, ten_days_ago))

    # Create new file
    new_file = tmp_path / "new.log"
    new_file.touch()

    deleted = cleanup_old_files(tmp_path, days=7, pattern="*.log")

    assert deleted == 1
    assert not old_file.exists()
    assert new_file.exists()
```

**Checkpoint:** Pokreni testove:

```bash
pytest sandbox/basics/tests/test_file_operations.py -v
```

---

## FAZA 3 (2h) — Test CSV Cleaner

### Zadatak 3.1: Kreiraj conftest.py (30min)

**Lokacija:** `sandbox/basics/tests/conftest.py`

```python
"""Shared pytest fixtures."""
import pytest
from pathlib import Path


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """Create sample CSV file sa whitespace."""
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


@pytest.fixture
def empty_csv(tmp_path: Path) -> Path:
    """Create empty CSV file sa samo headerom."""
    csv_path = tmp_path / "empty.csv"
    csv_path.write_text("name,age,city\n", encoding="utf-8")
    return csv_path
```

### Zadatak 3.2: Piši test_csv_cleaner.py (90min)

**Lokacija:** `sandbox/basics/tests/test_csv_cleaner.py`

```python
"""Test csv_cleaner_final.py functions."""
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


def test_detect_dialect_missing_file(tmp_path: Path):
    """Test da detect_dialect baca FileNotFoundError."""
    missing = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        detect_dialect(missing)


def test_read_rows(sample_csv: Path):
    """Test reading CSV rows."""
    dialect = detect_dialect(sample_csv)
    rows = read_rows(sample_csv, dialect)

    assert len(rows) == 3
    assert rows[0]["name"] == "Alice"
    assert rows[1]["name"] == "Bob"
    assert rows[2]["name"] == "  Charlie  "  # Not cleaned yet


def test_clean_rows_strips_whitespace(sample_csv: Path):
    """Test da clean_rows uklanja whitespace."""
    dialect = detect_dialect(sample_csv)
    rows = read_rows(sample_csv, dialect)
    cleaned, stats = clean_rows(rows)

    # Check last row (has whitespace)
    assert cleaned[-1]["name"] == "Charlie"
    assert cleaned[-1]["city"] == "Chicago"
    assert stats["cleaned_rows"] == 3


def test_clean_rows_empty_list():
    """Test da clean_rows hendluje praznu listu."""
    cleaned, stats = clean_rows([])

    assert cleaned == []
    assert stats["cleaned_rows"] == 0


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
    # Proveri da nema whitespace
    assert "  Charlie  " not in content


def test_write_rows_empty(tmp_path: Path, sample_csv: Path):
    """Test pisanja praznih rows."""
    dialect = detect_dialect(sample_csv)
    output = tmp_path / "empty_output.csv"

    write_rows(output, [], dialect)

    # Should create empty file or file with header only
    assert output.exists()
```

**Checkpoint:** Pokreni testove:

```bash
pytest sandbox/basics/tests/test_csv_cleaner.py -v
```

---

## FAZA 4 (2h) — Integration Tests

### Zadatak 4.1: Refaktoriši cli_with_types.py (45min)

Dodaj testable handler funkciju koja vraća bool (success/failure) umesto void.

**Dodaj u cli_with_types.py:**

```python
import logging
from sandbox.basics.csv_cleaner_final import (
    detect_dialect,
    read_rows,
    clean_rows,
    write_rows,
)

logger = logging.getLogger(__name__)

def cmd_process(args: ProcessArgs) -> bool:
    """Process komanda sa CSV cleaningom, vraća success status."""
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

### Zadatak 4.2: Integration test (75min)

**Lokacija:** `sandbox/basics/tests/test_cli_integration.py`

```python
"""Integration test: CLI → CSV → Logging."""
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


def test_cli_process_with_limit(tmp_path: Path, sample_csv: Path):
    """Test da limit ograničava broj redova."""
    output = tmp_path / "output.csv"

    args = Namespace(
        input_file=str(sample_csv),
        output_file=str(output),
        verbose=False,
        limit=2,  # Only first 2 rows
    )

    success = cmd_process(args)

    assert success is True
    assert output.exists()

    # Count rows in output
    import csv
    with output.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2


def test_cli_process_verbose_logging(sample_csv: Path, caplog):
    """Test da verbose flag uključuje INFO logging."""
    args = Namespace(
        input_file=str(sample_csv),
        output_file=None,
        verbose=True,
        limit=10,
    )

    with caplog.at_level(logging.INFO):
        cmd_process(args)

    # Should log processing info
    assert "Processing" in caplog.text
    assert "limit=10" in caplog.text
```

**Checkpoint:** Pokreni integration testove:

```bash
pytest sandbox/basics/tests/test_cli_integration.py -v
```

---

## Finalni Coverage Report

Pokreni sve testove sa coverage:

```bash
# Terminal coverage report
pytest --cov=sandbox.basics --cov-report=term-missing

# HTML coverage report (best for analysis)
pytest --cov=sandbox.basics --cov-report=html
xdg-open htmlcov/index.html
```

**Cilj:** Coverage >85% za sve module.

---

## Validation Checklist

-   [ ] `test_path_basics.py` sa 8+ testova
-   [ ] `test_file_operations.py` sa 8+ testova
-   [ ] `test_csv_cleaner.py` sa 7+ testova
-   [ ] `conftest.py` sa 3+ shared fixtures
-   [ ] `test_cli_integration.py` sa 4+ integration testova
-   [ ] Svi testovi prolaze: `pytest -v`
-   [ ] Coverage >85%: `pytest --cov=sandbox.basics --cov-report=term`
-   [ ] Svi error cases testirani (FileNotFoundError, permission errors, etc.)
-   [ ] Svi log messages testirani sa caplog

---

## Next Steps

Nakon uspešnog završetka:

1. Generiši HTML coverage report i pregledaj ga
2. Nađi module sa coverage <80% i dodaj testove
3. Kreiraj SUMMARY_DAN_07.md sa coverage statistikama
4. Pripremi se za Dan 8: Web Scraper projekat

**Srećno! 🚀**
