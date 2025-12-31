---
type: repl_exercises
time: 90 minutes
topics: [dict, comprehension, slicing, shallow_copy]
---

# 🧪 REPL Vežbe — Dict, Slicing, Comprehensions

## FAZA 1 — Dict osnove (20 min)

1. Čitanje i `get`

```python
osoba = {"ime": "Ana", "god": 29}
print(osoba["ime"])
print(osoba.get("grad", "nema"))
```

2. Dodavanje i update

```python
osoba["grad"] = "Bg"
osoba.update({"god": 30, "telefon": "123"})
print(osoba)
```

3. Iteracija

```python
for k in osoba:
    print(k, osoba[k])

for k, v in osoba.items():
    print(k, v)
```

---

## FAZA 2 — Slicing + kopije (15 min)

4. Kopija dict-a

```python
orig = {"a": [1,2], "b": [3,4]}
kopija = orig.copy()      # plitka kopija
kopija["a"][0] = 99
print(orig)   # vidi da se promenilo

import copy
deep = copy.deepcopy(orig)
deep["a"][1] = 77
print(orig)   # sada ostaje netaknut
```

5. Slicing stringa i liste (podsetnik)

```python
tekst = "python"
print(tekst[1:4])
nums = [0,1,2,3,4,5]
print(nums[2:5])
print(nums[::-1])
```

---

## FAZA 3 — List comprehensions (20 min)

6. Kvadrati + filtriranje

```python
kv = [x*x for x in range(8)]
parni_kv = [x for x in kv if x % 2 == 0]
print(kv)
print(parni_kv)
```

7. Normalizuj stringove

```python
imena = [" ana ", "MARKO", "IvA"]
cisti = [ime.strip().lower() for ime in imena]
print(cisti)
```

---

## FAZA 4 — Dict comprehensions (20 min)

8. Duzine reci

```python
reci = ["ana", "program", "set"]
duzine = {rec: len(rec) for rec in reci}
print(duzine)
```

9. Filtriraj ocene

```python
ocene = {"ana": 95, "ivana": 72, "marko": 60}
iznad_80 = {ime: oc for ime, oc in ocene.items() if oc >= 80}
print(iznad_80)
```

10. Obrni dict (ako su vrednosti unikatne)

```python
mapa = {"rs": "serbian", "en": "english"}
obrni = {v: k for k, v in mapa.items()}
print(obrni)
```

---

## FAZA 5 — Set comprehension (15 min)

11. Jedinstveni karakteri

```python
tekst = "kompletan"
uniq = {c for c in tekst}
print(uniq)
```

12. Samo parni brojevi

```python
parni = {x for x in range(20) if x % 2 == 0}
print(parni)
```

---

## FAZA 6 — Mini izazovi (15 min)

13. Napravi dict koji mapira broj → njegov kvadrat za 1..10 (dict comprehension).
14. Iz liste tuplova `[("ana", 2), ("mila", 3)]` napravi dict imena → broj_pojavljivanja.
15. Ukloni sve duplikate iz liste stringova i zadrži ih u set-u; ispiši veličinu seta.

---

## ✅ Checklista

-   [ ] Razumeš plitku vs duboku kopiju dict-a sa listama unutra
-   [ ] Možeš da napišeš dict comprehension sa uslovom
-   [ ] Znaš `get` i `items()` bez guglanja
