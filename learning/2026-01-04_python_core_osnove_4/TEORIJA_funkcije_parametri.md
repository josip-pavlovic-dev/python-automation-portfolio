---
type: lecture
time: 100 minutes
topics: [functions, params, defaults, args, kwargs, return]
---

# 📖 Teorija: Funkcije i Parametri

## 1. Definisanje funkcije

```python
def ime_funkcije(param1, param2):
    # blok
    return vrednost
```

-   `def` + ime + lista parametara + dvotačka
-   Blok indentiran

## 2. Parametri

| Vrsta      | Primer            | Opis                             |
| ---------- | ----------------- | -------------------------------- |
| Positional | `f(10, 20)`       | redosled bitan                   |
| Keyword    | `f(x=10, y=20)`   | imenuješ parametre               |
| Default    | `def f(x, y=5)`   | ima podrazumevanu vrednost       |
| \*args     | `def f(*args)`    | skuplja višak positional u tuple |
| \*\*kwargs | `def f(**kwargs)` | skuplja višak keyword u dict     |

## 3. Default parametri

```python
def pomnozi(x, faktor=2):
    return x * faktor
```

-   Default se procenjuje jedanput pri definiciji, ne svaki put!
-   Zato **ne koristi mutabilno** kao default.

### Mutabilni default problem

```python
def dodaj(item, lst=[]):
    lst.append(item)
    return lst

print(dodaj(1))  # [1]
print(dodaj(2))  # [1, 2]  # neočekivano
```

**Rešenje:**

```python
def dodaj(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

## 4. \*args i \*\*kwargs

```python
def zbir(*brojevi):
    return sum(brojevi)

print(zbir(1, 2, 3))  # 6
```

```python
def info(**podatak):
    print(podatak)

info(ime="Ana", grad="Bg")  # {'ime': 'Ana', 'grad': 'Bg'}
```

-   \*args = tuple, \*\*kwargs = dict
-   Možeš kombinovati: `def f(a, b=1, *args, **kwargs)`

## 5. Redosled parametara

```
obavezni → default → *args → keyword-only → **kwargs
```

Primer keyword-only:

```python
def podeli(x, y, *, zaokruzi_na=2):
    return round(x / y, zaokruzi_na)
```

## 6. Povratne vrednosti

```python
def f():
    return 10
```

-   Ako nema `return` → funkcija vraća `None`.
-   `return` prekida funkciju odmah.

## 7. Docstring

```python
def zbir(x: int, y: int) -> int:
    """Vrati zbir dva broja."""
    return x + y
```

Koristi za autosugestiju i dokumentaciju.

## 8. Lambda (kratko)

```python
duplo = lambda x: x * 2
```

-   Koristi samo kada je vrlo kratko; inače obična `def` je čitljivija.

## 9. Česte greške

-   Mutabilni default
-   Pogrešan redosled parametara
-   Vraćanje `None` jer `return` nedostaje
-   Mešanje positional/keyword (TypeError: got multiple values)

## 10. Mini kontrolna pitanja

-   Kako sprečiti mutabilni default bug?
-   Šta radi `*args`, šta radi `**kwargs`?
-   Kada koristiti keyword-only parametre?

Spreman za praksu? Idi na REPL vežbe.
