---
type: cheatsheet
linked_to: 2025-12-23_testing_advanced
date: 2025-12-23
status: draft
---

# 🧾 Pytest Cheatsheet

## Basic layout

```python
# file: tests/test_example.py
def test_add():
    assert 1 + 1 == 2
```

Run: `pytest -q`

---

## Parametrize

```python
import pytest
@pytest.mark.parametrize("raw,expected", [("1", 1), ("2", 2)])
def test_to_int(raw, expected):
    assert int(raw) == expected
```

---

## Fixtures

```python
@pytest.fixture
def sample_path(tmp_path: Path) -> Path:
    file = tmp_path / "data.txt"
    file.write_text("hi", encoding="utf-8")
    return file

def test_read(sample_path: Path):
    assert sample_path.read_text(encoding="utf-8") == "hi"
```

---

## Monkeypatch

```python
def test_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "test")
```

---

## caplog / capsys

```python
def test_logs(caplog):
    logger.info("hello")
    assert "hello" in caplog.text
```

---

## Markers

```python
import pytest
@pytest.mark.slow
def test_big():
    ...
```

Run subset: `pytest -m "not slow"`

---

## Failure patterns

-   Arrange/Act/Assert jasno
-   Jedan assert po ideji (više je ok ako je vezano)
-   Bez print u testu

---

## Coverage quick

```
pytest --maxfail=1 -q --cov=sandbox --cov=projects/01-web-scraper
```

---
