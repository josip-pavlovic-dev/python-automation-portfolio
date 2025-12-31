---
type: quick_start
time: "30 min"
---

# ⚡ 30-Min Start — Dan 3: Kolekcije

## Šta dobijaš za 30 min

-   U glavi jasna razlika: lista vs tuple vs set vs dict
-   Znaš da napraviš kopiju liste bez shared reference
-   Znaš kako izgleda list/dict comprehension

---

## 1) Brzi mentalni modeli

-   **Lista**: kutija sa redom, promenljiva. `[1, 2, 3]` → možeš `append`, `pop`.
-   **Tuple**: kao lista, ali zaključano. Koristi se kao ključ u dict-u. `(lat, lon)`.
-   **Set**: vreća unikatnih stvari, bez redosleda. `{1, 2, 3}`.
-   **Dict**: mapa ključ → vrednost. `{"ime": "Ana", "godine": 30}`.

---

## 2) Slicing i kopije

```python
nums = [10, 20, 30, 40]
prvih_dva = nums[0:2]   # [10, 20]
poslednja_dva = nums[-2:]  # [30, 40]
kopija = nums[:]        # kopija liste (bez shared ref)
```

**Zašto kopija?** Ako proslediš `nums` i menjaš unutra, menja se i original. `nums[:]` izbegava to.

---

## 3) Comprehensions u 2 minuta

```python
kvadrati = [x * x for x in range(5)]            # lista
parni = {x for x in range(10) if x % 2 == 0}    # set
mapa_duzina = {ime: len(ime) for ime in ["ana", "marko"]}  # dict
```

-   Prvo napiši regularni for, onda ga skrati u comprehension.
-   Dodaj `if` na kraj da filtriraš.

---

## 4) Greške na koje paziš danas

-   `TypeError: unhashable type: 'list'` kad listu koristiš kao ključ u dict/set.
-   `KeyError` kad pristupiš `dikt["ne_postoji"]` bez `get` ili provere.
-   `IndexError` za `lst[100]` kad lista ima 5 elemenata.

---

## 5) Mini warmup (odmah u REPL)

```python
# Warmup 1: Lista → tuple → set
nums = [1, 2, 2, 3]
print(tuple(nums))
print(set(nums))

# Warmup 2: Dict osnovno
osoba = {"ime": "Ana", "god": 29}
print(osoba["ime"])
print(osoba.get("grad", "nema grada"))

# Warmup 3: Comprehension
imena = ["ana", "marko", "iva"]
velika = [ime.upper() for ime in imena]
print(velika)
```

---

✅ Spreman si. Otvori **kickoff.md** za plan dana.

## Hintovi za rad (tvoj nivo)

-   Lista vs tuple: tuple koristiš kada ne menjaš podatke; pokušaj izmenu tuple-a i posmatraj grešku.
-   Set koristi za uklanjanje duplikata i brzu proveru `in`; probaj `set([1,1,2])` i `2 in {1,2}`.
-   Dict: koristi `.get(key, default)` pre direktnog pristupa da izbegneš `KeyError`.
-   Comprehension piši tek posle regularne for-petlje; ako ne možeš da objasniš u jednoj rečenici, ostavi for.
