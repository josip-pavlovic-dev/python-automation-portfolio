---
type: lecture
time: 120 minutes
topics: [for, range, enumerate, loops, iteration]
---

# 📖 Teorija: `for` Petlja — Detaljno

## Sadržaj

1. Osnovna Struktura `for`
2. `range()` Funkcija — Tri Oblika
3. `enumerate()` — Indeks + Vrednost
4. Petlje Kroz Stringove
5. Petlje Kroz Liste
6. Nested Petlje — Petlja Unutar Petlje
7. Šta se Dešava Kad Petlja Počne
8. Česta Greška: Off-by-One

---

## 1. Osnovna Struktura `for`

```python
for PROMENLJIVA in NEŠTO_ITERIRAJUĆE:
    # Kod koji se ponavlja
    print(PROMENLJIVA)
```

**Čita se:** "Za svaki element iz NEŠTO_ITERIRAJUĆEG, primeni kod"

**Primer:**

```python
boje = ["crvena", "plava", "zelena"]

for boja in boje:
    print(boja)

# Output:
# crvena
# plava
# zelena
```

**Tok:**

1. Počni sa `boje[0]` → `"crvena"`

    - Postavi `boja = "crvena"`
    - Izvrši `print(boja)` → "crvena"

2. Nastavi sa `boje[1]` → `"plava"`

    - Postavi `boja = "plava"`
    - Izvrši `print(boja)` → "plava"

3. Nastavi sa `boje[2]` → `"zelena"`

    - Postavi `boja = "zelena"`
    - Izvrši `print(boja)` → "zelena"

4. Nema više elemenata → **Petlja završena**

---

## 2. `range()` Funkcija — Tri Oblika

### 2.1 `range(n)` — Od 0 do n-1

```python
for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4
```

**Napomena:** `range(5)` daje brojeve od **0 do 4** (ne do 5!)

---

### 2.2 `range(start, stop)` — Od start do stop-1

```python
for i in range(2, 8):
    print(i)

# Output: 2, 3, 4, 5, 6, 7
```

**Napomena:** Start je UKLJUČEN, stop je ISKLJUČEN.

---

### 2.3 `range(start, stop, step)` — Sa Korakom

```python
# Samo parni brojevi od 0 do 10
for i in range(0, 11, 2):
    print(i)

# Output: 0, 2, 4, 6, 8, 10
```

**Analiza:**

-   Start: `0`
-   Stop: `11` (ali se ide po 2, pa zadnji je 10)
-   Step: `2` (povećaj za 2 svaki put)

---

### 2.4 `range()` sa Negativnim Korakom

```python
# Unazad od 10 do 0
for i in range(10, -1, -1):
    print(i)

# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
```

---

## 3. `enumerate()` — Indeks + Vrednost

```python
voće = ["jabuka", "banana", "narandza"]

for indeks, voće_ime in enumerate(voće):
    print(f"{indeks}: {voće_ime}")

# Output:
# 0: jabuka
# 1: banana
# 2: narandza
```

**Zašto `enumerate()`?**

Nekad trebam **indeks** I **vrednost** istovremeno.

```python
# ❌ Loš način (bez enumerate)
voće = ["jabuka", "banana", "narandza"]
i = 0
for v in voće:
    print(f"{i}: {v}")
    i = i + 1

# ✅ Dobar način (sa enumerate)
for i, v in enumerate(voće):
    print(f"{i}: {v}")
```

---

## 4. Petlje Kroz Stringove

```python
reč = "Python"

for slovo in reč:
    print(slovo)

# Output:
# P
# y
# t
# h
# o
# n
```

---

## 5. Petlje Kroz Liste

```python
brojevi = [10, 20, 30, 40]

# Jednostavna petlja
for num in brojevi:
    print(num)

# Sa enumerate
for i, num in enumerate(brojevi):
    print(f"Indeks {i}: {num}")

# Output:
# Indeks 0: 10
# Indeks 1: 20
# Indeks 2: 30
# Indeks 3: 40
```

---

## 6. Nested Petlje — Petlja Unutar Petlje

```python
for i in range(3):
    print(f"Spoljašnja petlja: i = {i}")
    for j in range(2):
        print(f"  Unutrašnja petlja: j = {j}")
    print()

# Output:
# Spoljašnja petlja: i = 0
#   Unutrašnja petlja: j = 0
#   Unutrašnja petlja: j = 1
#
# Spoljašnja petlja: i = 1
#   Unutrašnja petlja: j = 0
#   Unutrašnja petlja: j = 1
#
# Spoljašnja petlja: i = 2
#   Unutrašnja petlja: j = 0
#   Unutrašnja petlja: j = 1
```

**Tok:**

1. `i = 0`
    - `j = 0` → štampa
    - `j = 1` → štampa
2. `i = 1`
    - `j = 0` → štampa
    - `j = 1` → štampa
3. `i = 2`
    - `j = 0` → štampa
    - `j = 1` → štampa

---

## 7. Praktičan Primer: Tablica Množenja

```python
# Tablica množenja 3x3
for i in range(1, 4):
    for j in range(1, 4):
        rezultat = i * j
        print(f"{i} × {j} = {rezultat}", end="  ")
    print()  # Nova linija nakon svakog reda

# Output:
# 1 × 1 = 1  1 × 2 = 2  1 × 3 = 3
# 2 × 1 = 2  2 × 2 = 4  2 × 3 = 6
# 3 × 1 = 3  3 × 2 = 6  3 × 3 = 9
```

---

## 8. Česta Greška: Off-by-One

```python
# ❌ LOŠE — Misliš da daje do 10
for i in range(10):
    print(i)

# Daje: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (samo do 9!)

# ✅ DOBRO
for i in range(11):
    print(i)

# Daje: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

---

## 📝 Rezime: `range()` Brza Referenca

| Kod                | Šta daje                      |
| ------------------ | ----------------------------- |
| `range(5)`         | 0, 1, 2, 3, 4                 |
| `range(2, 7)`      | 2, 3, 4, 5, 6                 |
| `range(0, 10, 2)`  | 0, 2, 4, 6, 8                 |
| `range(10, 0, -1)` | 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 |
| `range(5, 5)`      | (ništa)                       |

---

## 🎯 Sledeća Faza

Kreni sa **REPL vežbama za `for`** petlje!
