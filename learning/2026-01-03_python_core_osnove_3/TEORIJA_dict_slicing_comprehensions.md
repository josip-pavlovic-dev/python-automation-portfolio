---
type: lecture
time: 100 minutes
topics: [dict, slicing, comprehension, copy, errors]
---

# 📖 Teorija: Rečnici, Slicing, Comprehensions

## 1. Dict (ključ → vrednost)

```python
osoba = {
    "ime": "Ana",
    "godine": 29,
    "grad": "Beograd",
}
```

-   Ključevi moraju biti hashable (`str`, `int`, `tuple`...), vrednosti mogu biti bilo šta.
-   Ne garantuje red u starijim verzijama Pythona, ali 3.7+ čuva red unosa.

### Glavne operacije

| Operacija    | Primer                         | Napomena            |
| ------------ | ------------------------------ | ------------------- |
| Čitanje      | `osoba["ime"]`                 | `KeyError` ako nema |
| Bez greške   | `osoba.get("telefon", "nema")` | default vrednost    |
| Dodaj/izmeni | `osoba["grad"] = "Novi Sad"`   | kreira ili menja    |
| `update`     | `osoba.update({"godine": 30})` | višestruke izmene   |
| `pop`        | `osoba.pop("godine", None)`    | ukloni i vrati      |
| Ključevi     | `osoba.keys()`                 | view objekat        |
| Vrednosti    | `osoba.values()`               | view                |
| Parovi       | `osoba.items()`                | tuple (key, value)  |

### Iteracije

```python
for key in osoba:
    print(key, osoba[key])

for key, val in osoba.items():
    print(key, val)
```

### Ugnježdeni dict

```python
korisnik = {
    "ime": "Ana",
    "adres": {"grad": "Bg", "ulica": "Main 1"},
}
print(korisnik["adres"]["grad"])  # Bg
```

### Tipične greške

-   `KeyError`: reši sa `get` ili `in` proverom.
-   Mutabilne vrednosti dele referencu.

---

## 2. Slicing (podsekcije sekvenci)

Radi na listama, stringovima, tupleovima.

```python
nums = [10, 20, 30, 40, 50]
print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[::2])   # [10, 30, 50]
print(nums[::-1])  # obrnuto
```

### Kopiranje liste

```python
orig = [1, 2, 3]
copy = orig[:]       # plitka kopija
copy2 = orig.copy()  # isto
```

### Plitka vs duboka kopija

```python
import copy

nested = [[1, 2], [3, 4]]
shallow = nested[:]           # spolja kopija, unutra reference
shallow[0][0] = 99            # menja nested too!

deep = copy.deepcopy(nested)  # odvojena struktura
```

-   Ako imaš ugnježdene mutable elemente, `deepcopy` je bezbedniji.

---

## 3. Comprehensions (list/dict/set)

### List comprehension

```python
kvadrati = [x * x for x in range(5)]            # [0,1,4,9,16]
parni = [x for x in range(10) if x % 2 == 0]    # filtriranje
```

### Dict comprehension

```python
imena = ["ana", "marko", "iva"]
duzine = {ime: len(ime) for ime in imena}
```

### Set comprehension

```python
unikatni = {c for c in "bananaa"}  # {'b','a','n'}
```

### Kada koristiti

-   Kada imaš kratku transformaciju/filtriranje koje je čitljivo u jednoj liniji.
-   Nemoj preterivati sa ugnježdenim comprehensions (čitajnost trpi).

---

## 4. Dict + Comprehension — primeri

```python
ocene = {"ana": 95, "ivana": 72, "marko": 60}

a_ili_b = {ime: oc for ime, oc in ocene.items() if oc >= 80}
# {'ana': 95}

sa_bonusom = {ime: oc + 5 for ime, oc in ocene.items()}
# {'ana': 100, 'ivana': 77, 'marko': 65}
```

---

## 5. Error checklist

-   `KeyError`: koristi `dict.get` ili `if key in dict`.
-   `TypeError: unhashable type`: ne koristi list/set/dict kao ključ ili element seta.
-   `IndexError` u slicingu je ređi (slicing je bezbedan), ali direktan indeks može pasti.

---

## 6. Kada koristiti dict

-   Kada ti treba brzo preslikavanje ključ → vrednost.
-   Kada treba brzo membership po ključu (`in dict` je O(1) u proseku).
-   Kada treba da grupišeš podatke po kategorijama (vidi mini probleme).

Spreman za REPL? Pređi na vežbe za dict + comprehensions. 🚀
