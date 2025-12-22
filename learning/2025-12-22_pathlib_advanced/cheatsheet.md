---
type: cheatsheet
topic: Pathlib — Quick Reference
date: 2025-12-22
language: bilingual
difficulty: beginner-intermediate
---

# 🧾 Pathlib Cheatsheet (Serbian objašnjenja, English code)

## Kreiranje i join

# Binarno

data = p.read_bytes()
p.write_bytes(b"hello")

# Append lines

with p.open("a", encoding="utf-8", newline="") as f:
f.write("new line\n")

# Safe overwrite (tmp file then replace)

tmp = p.with_suffix(p.suffix + ".tmp")
tmp.write_text("new", encoding="utf-8")
tmp.replace(p)

```python
from pathlib import Path
data = Path(__file__).parent / "data" / "users.csv"
temp = Path.home() / "tmp" / "demo.txt"
normalized = Path("~/data").expanduser().resolve()
```

---

## Inspekcija

small = [f for f in Path("data").rglob("*.json") if f.stat().st_size < 1024]

```python
p.name; p.stem; p.suffix; p.suffixes
p.parent; p.parents[0]; p.parents[1]
p.stat().st_size; p.stat().st_mtime
```

---

## Čitanje / Pisanje

def ensure_dir(path: Path) -> Path:
path.mkdir(parents=True, exist_ok=True)
return path

```python
p.write_text("hello", encoding="utf-8")
with p.open("w", encoding="utf-8", newline="") as f:
    f.write("line")
```

---

## Traversal i filtriranje

```python
list(Path("data").glob("*.csv"))
list(Path("data").rglob("*.json"))
recent = [f for f in Path("logs").glob("*.log") if f.stat().st_mtime > cutoff]
```

src = Path("data/in.csv")
dst = Path("backup/in.csv")
dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_bytes(src.read_bytes())

dst.rename(dst.with_name("in_old.csv"))
dst.unlink(missing_ok=True)

---

## Bezbednost + error handling

```python
def read_text_safe(path: Path) -> str:
link = Path("latest.log")
target = Path("logs/app_2025-12-22.log")
if link.exists() or link.is_symlink():
    link.unlink()
link.symlink_to(target)
real = link.resolve()
    if not path.exists():
        raise FileNotFoundError(path)
```

---

## Test helpers (pytest)

    file = tmp_path / "out.txt"
    file.write_text("hi", encoding="utf-8")
    assert file.read_text(encoding="utf-8") == "hi"

```python
    file = tmp_path / "out.txt"
    file.write_text("hi", encoding="utf-8")
    assert file.read_text(encoding="utf-8") == "hi"
```

    file = tmp_path / "x.txt"
    logger.info("writing %s", file)
    file.write_text("data", encoding="utf-8")
    assert "writing" in caplog.text

---

```python
import logging
logger = logging.getLogger(__name__)
def normalize_path(raw: str) -> Path:
    path = Path(raw).expanduser()
    if not path.suffix:
        msg = f"Expected file with suffix, got: {path}"
        raise ValueError(msg)
    return path.resolve()

def safe_copy(src: Path, dst: Path) -> None:
        dst.write_bytes(src.read_bytes())
    except Exception:
        logger.exception("copy failed", extra={"src": str(src), "dst": str(dst)})
        raise
mode = oct(Path("data.csv").stat().st_mode)
mtime = Path("data.csv").stat().st_mtime
```

---

## Tipovi (modern)

-   `Path | str` samo kad mora; prefer `Path`
-   Koristi `Iterator[Path]` iz `collections.abc` za generator funkcije
