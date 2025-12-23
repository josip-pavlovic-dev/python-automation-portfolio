---
type: cheatsheet
topic: Pathlib — Quick Reference
date: 2025-12-22
language: bilingual
difficulty: beginner-intermediate
---

# 🧾 Pathlib Cheatsheet (Serbian objašnjenja, English code)

Kratki, uredni primeri za Dan 6 (Pathlib). Fokus na ispravnom indentu i sigurnim obrascima.

---

## Kreiranje i spajanje putanja

```python
from pathlib import Path

data = Path(__file__).parent / "data" / "users.csv"
temp = Path.home() / "tmp" / "demo.txt"
normalized = Path("~/data").expanduser().resolve()
```

---

## Čitanje i pisanje

### Tekst

```python
p = Path("notes.txt")
p.write_text("hello", encoding="utf-8")
content = p.read_text(encoding="utf-8")
```

---

### Binarno

```python
p = Path("data.bin")
p.write_bytes(b"hello")
data = p.read_bytes()
```

---

### Append (dodaj liniju)

```python
with p.open("a", encoding="utf-8", newline="") as f:
    f.write("new line\n")
```

---

### Safe overwrite (tmp pa replace)

```python
tmp = p.with_suffix(p.suffix + ".tmp")
tmp.write_text("new", encoding="utf-8")
tmp.replace(p)
```

---

## Traversal i filtriranje

```python
from pathlib import Path

list(Path("data").glob("*.csv"))
list(Path("data").rglob("*.json"))

cutoff = 1_700_000_000  # primer timestamp
recent_logs = [
    f for f in Path("logs").glob("*.log")
    if f.stat().st_mtime > cutoff
]

# Filter po ekstenziji i veličini (< 10 KB)
small_txt = [
    f for f in Path("data").rglob("*.txt")
    if f.stat().st_size < 10_000
]

# Filter po datumu izmene (mtime) i prefiksu imena
import time
week_ago = time.time() - 7 * 86400
weekly_exports = [
    f for f in Path("exports").glob("export_*.csv")
    if f.stat().st_mtime >= week_ago
]

# Kombinacija: samo fajlovi (ne dir), sa više ekstenzija
reports = [
    f for f in Path("reports").iterdir()
    if f.is_file() and f.suffix in {".csv", ".json"}
]
```

---

## Kopiranje / preimenovanje / brisanje

```python
src = Path("data/in.csv")
dst = Path("backup/in.csv")
dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_bytes(src.read_bytes())

dst.rename(dst.with_name("in_old.csv"))
dst.unlink(missing_ok=True)
```

---

## Metadata i atributi

```python
p.name
p.stem
p.suffix
p.suffixes
p.parent
p.parents[0]
p.stat().st_size
p.stat().st_mtime
```

---

## Bezbednost i error handling

```python
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def read_text_safe(path: Path) -> str:
    """Baci FileNotFoundError sa kontekstom ako fajl ne postoji."""
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def normalize_path(raw: str) -> Path:
    """Expand ~, zahteva suffix, vraća resolve() putanju."""
    path = Path(raw).expanduser()
    if not path.suffix:
        msg = f"Expected file with suffix, got: {path}"
        raise ValueError(msg)
    return path.resolve()


def safe_copy(src: Path, dst: Path) -> None:
    """Copy uz logovanje greške i prosl. exception."""
    try:
        dst.write_bytes(src.read_bytes())
    except Exception:
        logger.exception("copy failed", extra={"src": str(src), "dst": str(dst)})
        raise
```

---

### Symlink primer

```python
link = Path("latest.log")
target = Path("logs/app_2025-12-22.log")
if link.exists() or link.is_symlink():
    link.unlink()
link.symlink_to(target)
real = link.resolve()
```

---

## Test helpers (pytest)

```python
def test_roundtrip(tmp_path: Path):
    file = tmp_path / "out.txt"
    file.write_text("hi", encoding="utf-8")
    assert file.read_text(encoding="utf-8") == "hi"


def test_logs(caplog, tmp_path: Path):
    file = tmp_path / "x.txt"
    logger.info("writing %s", file)
    file.write_text("data", encoding="utf-8")
    assert "writing" in caplog.text
```

---

## Pitfalls (česte greške)

-   `Path("~/file")` ne expanduje `~` sam: koristi `Path("~/file").expanduser()`.
-   `Path("dir").glob("_.csv")` gleda samo prvi nivo; za rekursivno koristi `rglob("_.csv")`.
-   `Path.iterdir()` vraća i fajlove i foldere; proveri `f.is_file()` / `f.is_dir()` pre rada.
-   `Path.resolve()` bez `strict=False` može da pukne ako target ne postoji; default je barem na nekim sistemima.
-   Uvek koristi `encoding="utf-8"` pri čitanju/pisanju teksta.
-   Ne koristi `open()` bez `with` bloka da izbegneš curenje fajl deskriptora.
-   Prilikom pisanja, kreiraj roditeljske feldere sa `mkdir(parents=True, exist_ok=True)`.
-   Kod overwrite operacija koristi `temp fajl + replace()` da izbegneš delimično upisane fajlove.

---

## Tipovi (modern)

-   `Path | str` samo kada baš mora; prefer `Path` u interfejsima
-   Za generator funkcije koristi `Iterator[Path]` iz `collections.abc`

```python
from pathlib import Path
from collections.abc import Iterator
def find_txt_files(root: Path) -> Iterator[Path]:
    for p in root.rglob("*.txt"):
        yield p
```

---

## Dodatni primeri filtera

```python
# Kombinovani filter: suffix lista + mtime + veličina
import time
cutoff = time.time() - 30 * 86400  # 30 dana
valid_suffixes = {".csv", ".json"}
filtered_files = [
    f for f in Path("data").rglob("*")
    if f.is_file()
    and f.suffix in valid_suffixes
    and f.stat().st_mtime >= cutoff
    and f.stat().st_size <= 5_000_000  # max 5 MB
]
# Ignorisanje skrivenih fajlova
all_files = [
    f for f in Path("project").rglob("*")
    if f.is_file() and not any(part.startswith(".") for part in f.parts)
]

# Pronalaženje praznih direktorijuma
empty_dirs = [
    d for d in Path("data").rglob("*")
    if d.is_dir() and not any(d.iterdir())
]
```

---

```

```
