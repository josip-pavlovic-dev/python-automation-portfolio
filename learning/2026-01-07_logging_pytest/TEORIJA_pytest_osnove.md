---
type: lecture
time: 100 minutes
topics: [pytest, assert, tests]
---

# 📖 Teorija: Pytest Osnove

## 1. Struktura

-   Test fajl: `test_*.py`
-   Test funkcija: `def test_nešto():`
-   Koristi plain `assert`

## 2. Primer

```python
# calc.py
def add(a, b):
    return a + b
```

```python
# test_calc.py
from calc import add

def test_add():
    assert add(2, 3) == 5
```

Pokreni: `pytest -q`

## 3. Assercije

```python
assert x == 10
assert "py" in "python"
assert lista  # truthy/falsy
```

## 4. Fixtures (kratko)

```python
import pytest

@pytest.fixture
def sample_nums():
    return [1, 2, 3]

def test_sum(sample_nums):
    assert sum(sample_nums) == 6
```

## 5. Parametrizacija (kratko)

```python
import pytest

@pytest.mark.parametrize("a,b,res", [(1,2,3), (2,2,4)])
def test_add(a, b, res):
    assert a + b == res
```

## 6. Čitanje greške

-   Pytest ispisuje gde je `assert` pao i konkretne vrednosti.
-   Gledaj stack trace i diff.

## 7. Česte greške

-   Pogrešan naziv fajla/funkcije (pytest ne vidi).
-   Import problemi (relative path) — koristi PYTHONPATH ili strukturu paketa.

## 8. Mini kontrola

-   Kako pokrenuti samo jedan test fajl? (`pytest test_calc.py`)
-   Kako parametrize? (`@pytest.mark.parametrize`)
-   Kada koristiti fixture? (deljeni setup)

Spreman za REPL pytest vežbe.
