---
type: repl_exercises
time: 90 minutes
topics: [list, tuple, set, slicing]
---

# 🧪 REPL Vežbe — Liste, Tuple, Set

## Pravila

-   Kucaj u REPL-u, menjaj vrednosti, posmatraj razliku mutabilno/imutabilno.
-   Posle svakog primera: predvidi output pre enter.

---

## FAZA 1 — Liste (20 min)

1. Dodavanje i brisanje

```python
nums = [10, 20, 30]
nums.append(40)
nums.insert(1, 15)
print(nums)
nums.pop()
nums.remove(20)
print(nums)
```

2. Slicing i kopije

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])   # ?
print(nums[:3])    # ?
print(nums[::2])   # ?
copy_ref = nums
copy_slice = nums[:]
copy_ref[0] = 99
print(nums)        # vidi razliku
print(copy_slice)
```

3. Sortiranje

```python
vals = [5, 1, 7, 3]
vals.sort()
print(vals)
vals.sort(reverse=True)
print(vals)
```

---

## FAZA 2 — Tuple (15 min)

4. Unpacking

```python
p = ("Ana", 29, "Bg")
ime, godine, grad = p
print(ime, godine, grad)
```

5. Tuple kao ključ

```python
koordinate = {(44.8, 20.5): "Bg", (45.2, 19.8): "Ns"}
print(koordinate[(44.8, 20.5)])
```

6. Greška sa listom u setu

```python
s = set()
try:
    s.add([1,2,3])
except Exception as e:
    print(type(e), e)
```

---

## FAZA 3 — Set (20 min)

7. Unikatnost

```python
s = {1, 2, 2, 3, 3, 3}
print(s)
```

8. Operacije skupova

```python
a = {1,2,3}
b = {3,4,5}
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)
```

9. `remove` vs `discard`

```python
s = {1,2,3}
s.discard(4)   # ?
try:
    s.remove(4)
except Exception as e:
    print(type(e), e)
```

---

## FAZA 4 — Kombinacije (20 min)

10. Lista → set → lista (uklanjanje duplikata, ali red može da se promeni)

```python
nums = [1,2,2,3,3,4]
jedinstveni = list(set(nums))
print(jedinstveni)
```

11. Brojanje frekvencija bez dict (set + count)

```python
tekst = "banana"
unikatni = set(tekst)
for slovo in unikatni:
    print(slovo, tekst.count(slovo))
```

12. Tuple lista → filtriraj by index

```python
parovi = [("ana", 25), ("marko", 40), ("iva", 19)]
zreliji = []
for ime, god in parovi:
    if god >= 25:
        zreliji.append(ime)
print(zreliji)
```

---

## FAZA 5 — Mini izazovi (15 min)

13. Napravi kopiju liste i obrni je bez `reverse()` (koristi slicing).
14. Zameni sve negativne brojeve u listi sa 0 (in-place).
15. Napravi set svih reči u stringu "ovo je je test".

---

## ✅ Checklista

-   [ ] Razlika reference vs kopija na listi
-   [ ] Tuple unpacking i tuple kao ključ
-   [ ] Set operacije i razlika `remove`/`discard`
