---
type: repl_exercises
time: 60 minutes
topics: [imports, type hints, scope]
---

# 🧪 REPL Vežbe — Import + Type Hints + Scope

## FAZA 1 — Type hints (20 min)

1. Napiši `def kvadrat(x: int) -> int` i pokreni; proveri `__annotations__`.
2. `def formatiraj(ime: str, aktivan: bool = True) -> str` → vrati string.
3. `def prvi(mozda: str | None) -> str | None` (Python 3.10 union operator).

## FAZA 2 — Scope (15 min)

4. Napravi `count = 0`; funkcija `inc()` sa `global count`; vidi promenu.
5. Ugnježdena funkcija sa `nonlocal` i bez njega; vidi razliku.

## FAZA 3 — Import lokalnog modula (25 min)

6. Napravi fajl `helper_math.py` u istoj fascikli:

```python
def duplo(x: int) -> int:
    return x * 2
```

7. U REPL-u probaj:

```python
import helper_math
print(helper_math.duplo(5))
from helper_math import duplo
print(duplo(6))
import helper_math as hm
print(hm.duplo(7))
```

8. Dodaj `if __name__ == "__main__": print("run")` u helper i pokreni `python helper_math.py` iz terminala da vidiš razliku.

✅ Check: znaš tri stila importa, osnovne hintove, `global`/`nonlocal` efekte.
