---
type: lecture
time: 90 minutes
topics: [while, break, continue, pass, loop control]
---

# 📖 Teorija: `while`, `break`, `continue`, `pass`

## Sadržaj

1. `while` Petlja — Osnova
2. `break` — Prekini Petlju
3. `continue` — Preskoči Iteraciju
4. `pass` — Ništa Ne Radi
5. Beskonačna Petlja
6. Razlika: `for` vs `while`

---

## 1. `while` Petlja — Osnova

```python
while USLOV:
    # Kod koji se ponavlja DOKLE JE USLOV True
    print("Ponavljam se")
```

**Čita se:** "Dok je uslov istinit, ponavljaj kod"

**Primer:**

```python
broj = 0

while broj < 5:
    print(broj)
    broj = broj + 1

# Output: 0, 1, 2, 3, 4
```

**Tok:**

1. `broj = 0`, uslov je `0 < 5` → **True** ✓

    - Štampa: `0`
    - `broj` postaje `1`

2. `broj = 1`, uslov je `1 < 5` → **True** ✓

    - Štampa: `1`
    - `broj` postaje `2`

3. `broj = 2`, uslov je `2 < 5` → **True** ✓

    - Štampa: `2`
    - `broj` postaje `3`

4. `broj = 3`, uslov je `3 < 5` → **True** ✓

    - Štampa: `3`
    - `broj` postaje `4`

5. `broj = 4`, uslov je `4 < 5` → **True** ✓

    - Štampa: `4`
    - `broj` postaje `5`

6. `broj = 5`, uslov je `5 < 5` → **False** ✗
    - Petlja se prekida

---

## 2. `break` — Prekini Petlju

```python
while True:  # BESKONAČNA petlja!
    broju = input("Unesi broj ili 'stop': ")
    if broj == "stop":
        break  # IZLAZI iz petlje
    print(f"Unešao si: {broj}")

print("Petlja je gotova!")
```

**Tok:**

-   Korisnik unese `"stop"` → `if broj == "stop":` → **True**
-   `break` → IZLAZI iz `while` petlje
-   Ostatak koda (`print(f"Unešao si...")`) se ignoriše

---

## 3. `continue` — Preskoči Iteraciju

```python
broj = 0

while broj < 10:
    broj = broj + 1

    if broj == 5:
        continue  # PRESKOČI ostatak ovog kruga

    print(broj)

# Output: 1, 2, 3, 4, 6, 7, 8, 9, 10
```

**Napomena:** Broj 5 se NE štampa jer se `continue` izvršio.

---

## 4. `pass` — Ništa Ne Radi

```python
broj = 0

while broj < 5:
    broj = broj + 1

    if broj == 3:
        pass  # Ništa! Samo nastavi
    else:
        print(broj)

# Output: 1, 2, 4, 5
```

**Zašto `pass`?**

Ponekad Python sintaksa zahteva nešto, ali ti još ne znaš šta da napraviš.

```python
# ❌ POGREŠNO — Sintaksna greška
if x > 5:
    # Još nisam siguran što da stavim

# ✅ DOBRO — Koristi pass kao placeholder
if x > 5:
    pass  # TODO: Napiši kod kasnije
```

---

## 5. Beskonačna Petlja

```python
# ⚠️ OPASNO — Beskonačna petlja!
while True:
    print("Ovo će se ponavljati zauvek!")

# Zaustavi sa Ctrl+C u terminalu
```

**Beskonačna petlja je OK ako imaš `break`:**

```python
while True:
    unos = input("Unesi broj ili 'stop': ")
    if unos == "stop":
        break
    print(f"Unešao si: {unos}")
```

---

## 6. Razlika: `for` vs `while`

| Aspekt         | `for`                               | `while`                            |
| -------------- | ----------------------------------- | ---------------------------------- |
| Kada koristiti | Znaš koliko puta će petlja biti     | Ne znaš koliko puta će biti        |
| Kontrola       | Automatska (sa `range()`)           | Ručna (promenljive)                |
| Primer         | `for i in range(5):`                | `while x < 10:`                    |
| Sigurnost      | Teže je napraviti beskonačnu petlju | Lako je accident beskonačne petlje |

**Primer: `for` (Znam koliko puta)**

```python
# Štampaj brojeve 1-10
for i in range(1, 11):
    print(i)
```

**Primer: `while` (Ne znam koliko puta)**

```python
# Pitaj korisnika dok ne unese validan broj
while True:
    unos = input("Unesi broj od 1 do 10: ")
    if unos.isdigit() and 1 <= int(unos) <= 10:
        print(f"Odličan izbor: {unos}")
        break
    print("Nevažeći unos!")
```

---

## 📝 Rezime

| Ključna reč    | Šta radi                                |
| -------------- | --------------------------------------- |
| `while USLOV:` | Ponavljaj dok je uslov True             |
| `break`        | IZLAZI iz petlje odmah                  |
| `continue`     | PRESKOČI ostatak ovog kruga, kreni novi |
| `pass`         | Ništa — samo placeholder                |

---

## 🎯 Sledeća Faza

Kreni sa **REPL vežbama za `while`** i `break`/`continue`!
