---
type: lecture
time: 100 minutes
topics: [type hints, scope, imports]
---

# 📖 Teorija: Type Hints, Scope, Importi

## 1. Type hints (osnova)

```python
def zbir(x: int, y: int) -> int:
    return x + y
```

-   Nisu obavezni u runtime-u, pomažu linteru i čitljivosti.
-   Uobičajeni hintovi: `int`, `str`, `float`, `bool`, `list[str]`, `dict[str, int]`, `tuple[int, int]`.

### Optional i Union

```python
from typing import Optional, Union

def mozda(x: Optional[int]) -> Union[int, None]:
    return x
```

### Callable i Any (kratko)

```python
from typing import Callable, Any

def primeni(fn: Callable[[int], int], x: int) -> int:
    return fn(x)
```

## 2. Scope (LEGB)

-   **L**ocal: unutar funkcije
-   **E**nclosing: ugnježdene funkcije
-   **G**lobal: modul
-   **B**uiltin: Python builtins

```python
x = 10  # global

def spolja():
    y = 20  # enclosing
    def unutra():
        z = 30  # local
        return x + y + z
    return unutra()
```

### `global` i `nonlocal`

```python
count = 0

def inc():
    global count
    count += 1
```

```python
def spolja():
    val = 0
    def unutra():
        nonlocal val
        val += 1
        return val
    return unutra()
```

-   Koristi ih štedljivo; često je bolji povrat vrednosti.

## 3. Importi i moduli

### Tri osnovna obrasca

```python
import math
print(math.sqrt(9))
```

```python
from math import sqrt
print(sqrt(9))
```

```python
import math as m
print(m.sqrt(9))
```

-   Izbegavaj `from module import *` (zamagljuje namespace).

### Import sopstvenih modula

Struktura:

```
projekt/
    main.py
    utils/
        __init__.py
        math_util.py
```

`main.py`:

```python
from utils.math_util import zbir
```

### `if __name__ == "__main__":`

-   Čuva kod koji se izvršava samo kad pokreneš fajl direktno.

```python
def main():
    print("Pokrenuto")

if __name__ == "__main__":
    main()
```

## 4. Tipične greške

-   Circular import (modul uvozi modul koji uvozi prvi) → refaktoriši.
-   Ne postoji `__init__.py` u paketu → import fail (u nekim starijim strukturama).
-   Hintovi pogrešnog tipa (npr. `list` vs `list[str]`).
-   `global` korišćen umesto povratne vrednosti.

## 5. Mini kontrolna pitanja

-   Kada koristiti `Optional`?
-   Kako rešiti mutabilne deljene promenljive bez `global`? (prosledi kao parametar)
-   Tri načina importa? Kada koji?

Spreman za REPL import/hint vežbe.
