---
type: repl_exercises
time: 120 minutes
phases: 5
focus: for, range, enumerate, nested loops
---

# 🧪 REPL Vežbe: `for` Petlje, `range()`, `enumerate()`

## 🎯 Cilj

Do kraja ovih vežbi moraš da se oseti kao kuća u `for` petljama. Koristi REPL!

---

## FAZA 1: `range()` — Brzo Zagrevanje

### Vežba 1.1: Brojanje od 0 do 9

```python
# Štampaj brojeve od 0 do 9
for i in range(10):
    print(i)
```

**Očekivani rezultat:**

```
0
1
2
...
9
```

**Provera:** Da li vidim brojeve od 0 do 9 (uključujući 9)?

---

### Vežba 1.2: Brojanje sa `range(start, stop)`

```python
# Štampaj brojeve od 3 do 8
for i in range(3, 9):
    print(i)
```

**Provera:** Da li se počinje od 3 i staje PRE 9? (3,4,5,6,7,8)

---

### Vežba 1.3: Samo Parni Brojevi

```python
# Štampaj samo parne brojeve od 0 do 20
for i in range(0, 21, 2):
    print(i)
```

**Provera:** Da li vidim samo parne? (0,2,4,6,...)

---

### Vežba 1.4: Unazad

```python
# Brojanje unazad od 10 do 1
for i in range(10, 0, -1):
    print(i)
```

**Provera:** 10, 9, 8, ..., 2, 1?

---

## FAZA 2: Petlje Kroz Liste i Stringove

### Vežba 2.1: Petlja Kroz Listu

```python
voće = ["jabuka", "banana", "narandza", "limun"]

for item in voće:
    print(item)
```

**Provera:** Štampa se svako voće u novom redu?

---

### Vežba 2.2: Petlja Kroz String

```python
reč = "PYTHON"

for slovo in reč:
    print(slovo)
```

**Provera:** P, Y, T, H, O, N?

---

### Vežba 2.3: `enumerate()` — Indeks + Vrednost

```python
boje = ["crvena", "plava", "zelena"]

for indeks, boja in enumerate(boje):
    print(f"{indeks}: {boja}")
```

**Očekivani rezultat:**

```
0: crvena
1: plava
2: zelena
```

---

### Vežba 2.4: `enumerate()` sa `range()`

```python
for i, num in enumerate(range(5, 10)):
    print(f"Pozicija {i}: broj {num}")
```

**Očekivani rezultat:**

```
Pozicija 0: broj 5
Pozicija 1: broj 6
Pozicija 2: broj 7
Pozicija 3: broj 8
Pozicija 4: broj 9
```

---

## FAZA 3: Logika Unutar Petlje

### Vežba 3.1: `if` Unutar `for`

```python
# Štampaj samo brojeve veće od 5
brojevi = [2, 5, 8, 3, 10, 1, 15]

for num in brojevi:
    if num > 5:
        print(num)
```

**Očekivani rezultat:** 8, 10, 15

---

### Vežba 3.2: Brojanje Parnih i Neparnih

```python
# Prebrojaj parne i neparne brojeve do 20
brojevi = list(range(1, 21))
parni = 0
neparni = 0

for num in brojevi:
    if num % 2 == 0:
        parni = parni + 1
    else:
        neparni = neparni + 1

print(f"Parni: {parni}, Neparni: {neparni}")
```

**Očekivani rezultat:** Parni: 10, Neparni: 10

---

### Vežba 3.3: Sumiranje

```python
# Saberi sve brojeve od 1 do 100
suma = 0

for i in range(1, 101):
    suma = suma + i

print(f"Suma: {suma}")
```

**Očekivani rezultat:** Suma: 5050

**Napomena:** Postoji formula (1+100)\*100/2 = 5050, ali ovde koristimo petlju!

---

## FAZA 4: Nested Petlje (Petlja Unutar Petlje)

### Vežba 4.1: Tablica Množenja 3x3

```python
# Prosta tablica množenja
for i in range(1, 4):
    for j in range(1, 4):
        rezultat = i * j
        print(f"{i}×{j}={rezultat}", end="  ")
    print()  # Nova linija
```

**Očekivani rezultat:**

```
1×1=1  1×2=2  1×3=3
2×1=2  2×2=4  2×3=6
3×1=3  3×2=6  3×3=9
```

---

### Vežba 4.2: Tablica Množenja sa `enumerate()`

```python
# Tablica sa rednim brojevima
karakteri = ["A", "B", "C"]
brojevi = [1, 2, 3]

for red, char in enumerate(karakteri):
    for col, num in enumerate(brojevi):
        print(f"[{char}{num}]", end="  ")
    print()
```

**Očekivani rezultat:**

```
[A1]  [A2]  [A3]
[B1]  [B2]  [B3]
[C1]  [C2]  [C3]
```

---

### Vežba 4.3: Piramida

```python
# Napravi piramidu sa zvezdama
for red in range(1, 6):
    print("*" * red)
```

**Očekivani rezultat:**

```
*
**
***
****
*****
```

---

## FAZA 5: Eksperimenti

### Vežba 5.1: Pronađi Prvo Pojavljivanje

```python
# Pronađi prvi broj veći od 10
brojevi = [2, 5, 8, 15, 3, 20]
pronađen = False

for num in brojevi:
    if num > 10:
        print(f"Pronađen: {num}")
        pronađen = True
        break  # Prestani čim pronađeš

if not pronađen:
    print("Nije pronađen")
```

---

### Vežba 5.2: Preskakanje Neparnih

```python
# Štampaj samo parne brojeve (sa continue)
for i in range(1, 11):
    if i % 2 != 0:  # Ako je neparan
        continue     # Preskoči
    print(i)
```

**Očekivani rezultat:** 2, 4, 6, 8, 10

---

### Vežba 5.3: Kombinovani Uslov

```python
# Nađi sve brojeve između 5 i 15 koji se daju sa 3
for i in range(5, 16):
    if i % 3 == 0:
        print(i)
```

**Očekivani rezultat:** 6, 9, 12, 15

---

## ✅ Čeklist — Završetku Ove Faze

-   [ ] Sve FAZA 1 vežbe rade (range sa različitim oblicima)
-   [ ] FAZA 2 radi (enumerate, stringovi, liste)
-   [ ] FAZA 3 radi (if logika, brojanje, sumiranje)
-   [ ] FAZA 4 radi (nested petlje, tablica, piramida)
-   [ ] FAZA 5 radi (break, continue, kombinovani uslovi)

---

## 🎯 Ako Nešto Ne Radi

**Problem:** "Dobijam beskonačnu petlju!"

-   Pritisni `Ctrl+C` da prekinuš
-   Proveri da li se promenljiva menja u petlji

**Problem:** "Off-by-One greška (brojim do 9 umesto do 10)"

-   Zapamti: `range(10)` daje 0-9, ne 0-10
-   Koristi `range(11)` ako trebas do 10

**Problem:** "`enumerate()` mi je čudan"

-   Testira: `for i, x in enumerate(['a', 'b']):`
-   Trebam TWO promenljive (indeks i vrednost)

---

## 🚀 Sledeća Faza

Kreni sa **REPL vežbama za `while`** petlje!
