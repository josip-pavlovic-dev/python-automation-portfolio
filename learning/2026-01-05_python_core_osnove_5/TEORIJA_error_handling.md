---
type: lecture
time: 100 minutes
topics: [try, except, else, finally, raise, custom exceptions]
---

# 📖 Teorija: Error Handling

## 1. Zašto hvatati greške?

-   Predvidive situacije (prazan fajl, pogrešan unos) → hvataj.
-   Programerske greške (typo, bug) → bolje da puknu (ne hvataj sve!).

## 2. Struktura try/except

```python
try:
    x = int(input("Unesi broj: "))
except ValueError:
    print("Nije broj!")
```

## 3. `else` i `finally`

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("Nema fajla")
else:
    data = f.read()
    print("Procitano")
finally:
    print("Zatvaram")
    try:
        f.close()
    except Exception:
        pass
```

-   `else` se izvršava ako nema greške u try bloku.
-   `finally` se izvršava uvek (zatvaranje resursa).

## 4. Hvataj specifično

```python
try:
    1 / 0
except ZeroDivisionError:
    print("Deljenje nulom")
```

-   Izbegavaj `except Exception:` bez potrebe (skriva bugove).

## 5. Podizanje greške

```python
def kvadrat(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x mora biti broj")
    return x * x
```

## 6. Custom exceptions

```python
class NegativeAmountError(ValueError):
    pass

def uplata(iznos):
    if iznos < 0:
        raise NegativeAmountError("Iznos ne sme biti negativan")
```

-   Nasledi od ugrađenih (`ValueError`, `RuntimeError`, ...).

## 7. Stack trace

-   Kada se desi greška, Python ispisuje stack trace (putanju poziva).
-   Čitaj najdonji poziv (prvi uzrok).

## 8. Česte greške

-   Hvatati previše (gutanje bugova).
-   Zaboravljen `finally` za resurse.
-   `except Exception as e: pass` (loše).
-   `raise` bez poruke → nejasan uzrok.

## 9. Mini kontrola

-   Kada koristiti `else` u try?
-   Kako podići custom grešku?
-   Zašto ne hvatati `Exception` bez logike?

Spreman za praksu u REPL-u.
