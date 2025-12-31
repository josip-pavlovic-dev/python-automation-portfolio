---
type: quick_start
time: "30 min"
---

# ⚡ 30-Min Start — Dan 4: Funkcije

## Brzi mentalni model

-   Funkcija = paket koda + ulazi + izlaz
-   Parametri: positional, keyword, default, \*args (tuple), \*\*kwargs (dict)
-   Nikad mutabilni default (`[]`, `{}`) → koristi `None`
-   `return` završava funkciju; bez `return` → `None`

## Mikro primer (otkucaj u REPL)

```python
def pozdravi(ime: str, jezik: str = "sr") -> str:
    if jezik == "sr":
        return f"Zdravo, {ime}!"
    return f"Hello, {ime}!"

print(pozdravi("Ana"))
print(pozdravi("Ana", "en"))
```

## \*args / \*\*kwargs u 2 min

```python
def zbir(*brojevi: int) -> int:
    return sum(brojevi)

print(zbir(1, 2, 3))  # 6

def prikaz(**opcije):
    print(opcije)

prikaz(boja="plava", veličina=42)
```

## Mutabilni default bug

```python
def dodaj(item, lst=[]):  # ⚠️ B U G
    lst.append(item)
    return lst

print(dodaj(1))  # [1]
print(dodaj(2))  # [1, 2]  (neočekivano)
```

**Ispravno:**

```python
def dodaj(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

## Type hints brzi primer

```python
def kvadrat(x: int) -> int:
    return x * x
```

✅ Spreman si; idi na kickoff za dnevni plan.

## Hintovi za rad (tvoj nivo)

-   Namerno napravi mutabilni default bug (lista), zatim ga ispravi sentinelom `None` da upamtiš obrazac.
-   `*args/**kwargs` odštampaj u funkciji `log_call` da vidiš strukturu; koristi keyword-only kada želiš eksplicitnost.
-   Scope: razlikuj lokalno vs globalno; izbegavaj `global` osim za primer.
-   Import modeli: napravi mali `utils.py`, uvezi ga apsolutno i relativno da vidiš razliku.
-   Type hints dodaj u 2-3 funkcije i razmisli šta se dešava ako proslediš pogrešan tip.
