---
type: repl_exercises
date: 2026-01-01
estimated_time: 2 hours
difficulty: beginner
part: 1
---

# 💻 REPL VEŽBE — Sintaksa & Uvlaka Osnove

**Trajanje:** ~2 sata
**Deo:** 1 od 2 (Sintaksa osnove + Falsy)

---

## 🎯 Cilj

Praktično eksperimentisati sa Python REPL-om kako bi razumeo:

-   Dvotačka (`:`) i uvlaka
-   Razlika između bloka i ne-bloka
-   Print sa f-stringom
-   Kako Python evaluira uslov

---

## 🔥 Kako početi

1. Otvori terminal:

```bash
python3
```

2. Trebalo bi da vidiš:

```
Python 3.12.0 (main, Oct  2 2023, 00:00:00)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

3. Kopiraj kod iz faza ispod (ILI još bolje - ručno ukucat)

---

## FAZA 1: Jednostavna if Naredba

### Vežba 1.1: If bez uvlake (GREŠKA)

```python
>>> if 5 > 3:
...
```

Pauziraj! Python očekuje uvlaku. Dodaj 4 razmaka:

```python
>>> if 5 > 3:
...     print("Pet je veće od tri")
...
```

Sada ukucaj praznu liniju (samo ENTER) da završiš blok:

```python
>>> if 5 > 3:
...     print("Pet je veće od tri")
...
Pet je veće od tri
```

**Šta se desilo:** Python je izvršio `print` jer je uslov `5 > 3` istinit.

---

### Vežba 1.2: Else naredba

```python
>>> x = 2
>>> if x > 5:
...     print("x je veće od 5")
... else:
...     print("x je manje ili jednako 5")
...
x je manje ili jednako 5
```

**Šta se desilo:** `x = 2` je manje od 5, tako da se izvršio else blok.

---

### Vežba 1.3: Elif (ako drugih slučajeva)

```python
>>> age = 17
>>> if age < 13:
...     print("Dete")
... elif age < 18:
...     print("Tinejdžer")
... else:
...     print("Odrasla osoba")
...
Tinejdžer
```

**Šta se desilo:** `age = 17` zadovoljava `age < 18`, tako da se ispisuje "Tinejdžer".

---

### Vežba 1.4: Ugneždeni if (if u if-u)

```python
>>> x = 10
>>> y = 5
>>> if x > 5:
...     print("X je veće od 5")
...     if y > 3:
...         print("  A Y je veće od 3")
...     else:
...         print("  A Y je manje od 3")
...
X je veće od 5
  A Y je veće od 3
```

**Šta se desilo:** Oba uslova su ispunjena, tako da se izvršio ugneždeni if.

**Obrati pažnju:** Ugneždeni `if` ima 8 razmaka (dva puta 4)!

---

## FAZA 2: For Petlja

### Vežba 2.1: Jednostavna for petlja

```python
>>> for i in range(3):
...     print(i)
...
0
1
2
```

**Šta se desilo:** `range(3)` generiše 0, 1, 2. Svaki se ispisuje.

---

### Vežba 2.2: For sa računanjem

```python
>>> for i in range(3):
...     print(f"Iteracija {i + 1}")
...
Iteracija 1
Iteracija 2
Iteracija 3
```

**Šta se desilo:** `f"..."` je f-string. `{i + 1}` se evaluira unutar stringa.

---

### Vežba 2.3: For petlja sa listom

```python
>>> fruits = ["jabuka", "banana", "narandža"]
>>> for fruit in fruits:
...     print(fruit)
...
jabuka
banana
narandža
```

**Šta se desilo:** For petlja iterira kroz svaki element liste.

---

### Vežba 2.4: For sa enumerate()

```python
>>> fruits = ["jabuka", "banana", "narandža"]
>>> for i, fruit in enumerate(fruits):
...     print(f"{i}: {fruit}")
...
0: jabuka
1: banana
2: narandža
```

**Šta se desilo:** `enumerate()` daje (indeks, vrednost).

---

### Vežba 2.5: For sa if unutar

```python
>>> for i in range(5):
...     if i % 2 == 0:
...         print(f"{i} je paran")
...     else:
...         print(f"{i} je neparan")
...
0 je paran
1 je neparan
2 je paran
3 je neparan
4 je paran
```

**Šta se desilo:** Kombinovao sam `for` i `if` sa ugneždenom strukturom.

---

## FAZA 3: While Petlja

### Vežba 3.1: Jednostavna while petlja

```python
>>> x = 3
>>> while x > 0:
...     print(x)
...     x -= 1
...
3
2
1
```

**Šta se desilo:** While se ponavlja dok je `x > 0` istinito. Svaki put `-= 1`.

---

### Vežba 3.2: While sa break

```python
>>> x = 0
>>> while True:
...     print(x)
...     x += 1
...     if x > 3:
...         break
...
0
1
2
3
```

**Šta se desilo:** `break` prekida petlju čim je `x > 3`.

---

### Vežba 3.3: While sa continue

```python
>>> x = 0
>>> while x < 5:
...     x += 1
...     if x == 3:
...         continue
...     print(x)
...
1
2
4
5
```

**Šta se desilo:** `continue` preskače ostatak bloka i ide na sledeću iteraciju. Broj 3 se ne ispisuje.

---

## FAZA 4: Funkcije sa if/for

### Vežba 4.1: Funkcija sa if

```python
>>> def is_even(n):
...     if n % 2 == 0:
...         return True
...     else:
...         return False
...
>>> is_even(4)
True
>>> is_even(5)
False
```

**Šta se desilo:** Funkcija vraća True ako je broj paran.

---

### Vežba 4.2: Funkcija sa for petljom

```python
>>> def sum_numbers(n):
...     total = 0
...     for i in range(1, n + 1):
...         total += i
...     return total
...
>>> sum_numbers(5)
15
```

**Šta se desilo:** Sabira sve brojeve od 1 do n (1+2+3+4+5 = 15).

---

### Vežba 4.3: Funkcija sa for i if

```python
>>> def count_evens(numbers):
...     count = 0
...     for num in numbers:
...         if num % 2 == 0:
...             count += 1
...     return count
...
>>> count_evens([1, 2, 3, 4, 5, 6])
3
```

**Šta se desilo:** Broji koliko ima parnih brojeva. Odgovor: 3 (2, 4, 6).

---

## FAZA 5: Greške i Eksperimentisanje

### Vežba 5.1: SyntaxError - zaboravljena dvotačka

```python
>>> if 5 > 3
...
  File "<stdin>", line 1
    if 5 > 3
           ^
SyntaxError: expected ':'
```

**Ispravka:** Dodaj `:`

```python
>>> if 5 > 3:
...     print("OK")
...
OK
```

---

### Vežba 5.2: IndentationError - loša uvlaka

```python
>>> if 5 > 3:
...   print("OK")  # Samo 2 razmaka!
...
  File "<stdin>", line 2
    print("OK")
    ^
IndentationError: unexpected indent
```

**Ispravka:** Koristi 4 razmaka

```python
>>> if 5 > 3:
...     print("OK")  # 4 razmaka
...
OK
```

---

### Vežba 5.3: Što ako koristiš pogrešan operator?

```python
>>> x = 5
>>> if x = 5:  # = je dodela, ne poređenje!
...
  File "<stdin>", line 1
    if x = 5:
         ^
SyntaxError: invalid syntax
```

**Ispravka:** Koristi `==` za poređenje

```python
>>> if x == 5:  # == je poređenje
...     print("OK")
...
OK
```

---

## 🎯 EKSPERIMENTI - Probaj Sam

### Eksperiment 1: Šta se desi ako je else bez if?

```python
>>> else:
...     print("Nešto")
...
IndentationError: unexpected indent
```

**Zaključak:** `else` mora da ide sa `if`.

---

### Eksperiment 2: Šta se desi ako nemaš `break` u while?

```python
>>> x = 0
>>> while True:
...     print("Beskonačno")
...     # CTRL+C da zaustaviš!!!
```

**Zaključak:** Beskonačne petlje se zaustavijaju sa CTRL+C.

---

### Eksperiment 3: Šta se desi ako koristiš pogrešan `+=`?

```python
>>> x = 5
>>> x = x + 1
>>> print(x)
6

>>> x += 1  # Isto kao x = x + 1
>>> print(x)
7
```

**Zaključak:** `+=` je skraćenica za `= +`.

---

## ✅ CHECKLIST - Šta Trebam da Znam

-   [ ] Razumem dvotačku i uvlaku
-   [ ] Mogu da napravim if/elif/else bez greške
-   [ ] Mogu da napravim for petlju
-   [ ] Mogu da napravim while petlju sa break
-   [ ] Mogu da napravim funkciju sa for/if
-   [ ] Znam šta su `SyntaxError` i `IndentationError`
-   [ ] Znam razliku između `=` i `==`

---

## 💾 Što da Sačuvaš

Kreiraj fajl `repl_dan1_veze.py` sa kođom koju si najpre savladao/savladala:

```python
# Dan 1 - Moje Vežbe

# Vežba 1: If/else
def is_positive(n):
    if n > 0:
        return "Pozitivno"
    else:
        return "Negativno"

print(is_positive(5))

# Vežba 2: For petlja
for i in range(1, 4):
    print(f"Broj: {i}")

# Vežba 3: Funkcija sa for
def multiply_by_two(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    return result

print(multiply_by_two([1, 2, 3]))
```

Pokreni:

```bash
python3 repl_dan1_veze.py
```

---

## 🔗 Dalje

Čitaj: [`REPL_VEŽBE_falsy_vs_truthy.md`](REPL_VEŽBE_falsy_vs_truthy.md)

Sretno! 🚀
