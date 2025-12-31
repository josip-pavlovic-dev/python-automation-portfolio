---
type: lecture
time: 120 minutes
topics: [if, elif, else, boolean operators, comparison]
---

# 📖 Teorija: `if/elif/else` — Detaljno

## Sadržaj

1. Osnovna Struktura `if`
2. `elif` — Više Opcija
3. `else` — Kada Ništa Nije Tačno
4. Uslovi: Poređenja
5. Logički Operatori: `and`, `or`, `not`
6. Truthy/Falsy u Uslovima
7. Nested `if` — `if` Unutar `if`
8. Česta Greška: Indentacija
9. Česta Greška: `=` vs `==`

---

## 1. Osnovna Struktura `if`

```python
if USLOV:
    # Kod koji se izvršava ako je uslov True
    print("Uslov je istinit!")
```

**Komponente:**

| Deo     | Šta je                         | Primer       |
| ------- | ------------------------------ | ------------ |
| `if`    | Ključna reč                    | `if`         |
| `USLOV` | Nešto što može biti True/False | `x > 5`      |
| `:`     | Dvotačka (OBAVEZNA!)           | `:`          |
| Blok    | Indentirano                    | `print(...)` |

**Tok izvršavanja:**

```python
x = 10

if x > 5:           # ← Python čita: Je li x > 5?
    print("DA!")    # ← Ako DA, izvrši ovaj red
                    # ← Ako NE, preskoči
```

---

## 2. `elif` — Više Opcija

```python
if USLOV1:
    # Ako je USLOV1 True
    kod()
elif USLOV2:
    # Ako je USLOV1 False ALI USLOV2 True
    kod()
elif USLOV3:
    # Ako su USLOV1 i USLOV2 False ALI USLOV3 True
    kod()
```

**Primer iz stvarnog sveta:**

```python
vreme = 10  # AM

if vreme < 12:
    poruka = "Dobro jutro!"
elif vreme < 18:
    poruka = "Dobar dan!"
elif vreme < 21:
    poruka = "Dobar veče!"
else:
    poruka = "Dobar noć!"

print(poruka)  # Dobro jutro!
```

**Tok:**

1. `if vreme < 12:` → `10 < 12` → **TRUE** ✓
2. Izvršava se `poruka = "Dobro jutro!"`
3. Preskaču se ALL ostali `elif` i `else` (čak i ako bi bili istiniti!)

---

## 3. `else` — Ako Ništa Nije Tačno

```python
if USLOV:
    kod_ako_je_true()
else:
    kod_ako_je_false()
```

**Primer:**

```python
age = 15

if age >= 18:
    print("Možeš da glasaš!")
else:
    print("Nisi star/a dovoljno")

# Output: Nisi star/a dovoljno
```

**Napomena:** `else` nema svog uslova — uvek se izvršava ako su SVI prethodni uslovi bili False.

---

## 4. Uslovi: Poređenja

```python
x = 10
y = 20
```

| Operator | Čita se           | Primer    | Rezultat |
| -------- | ----------------- | --------- | -------- |
| `==`     | Jednako           | `x == 10` | True     |
| `!=`     | Nije jednako      | `x != 20` | True     |
| `>`      | Veće od           | `x > 5`   | True     |
| `<`      | Manje od          | `x < 5`   | False    |
| `>=`     | Veće ili jednako  | `x >= 10` | True     |
| `<=`     | Manje ili jednako | `y <= 30` | True     |

**Važno: `==` je POREĐENJE, `=` je DODELA!**

```python
# ❌ LOŠE
if x = 10:     # SyntaxError!

# ✅ DOBRO
if x == 10:    # Poređenje
```

---

## 5. Logički Operatori: `and`, `or`, `not`

### 5.1 `and` — Oba Moraju Biti True

```python
temperatura = 25
humidnost = 65

if temperatura > 20 and humidnost < 70:
    print("Uslovi su idealni za odmor!")
else:
    print("Nije idealno")

# Output: Uslovi su idealni za odmor!
```

**Tabela Istine:**

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

---

### 5.2 `or` — Bar Jedan Mora Biti True

```python
voznja = 150  # km/h

if voznja < 30 or voznja > 130:
    print("OPASNO!")
else:
    print("Bezbedno")

# Output: OPASNO!
```

**Analiza:**

-   `voznja < 30` → `150 < 30` → False
-   `voznja > 130` → `150 > 130` → **True**
-   `False or True` → **True** ✓

**Tabela Istine:**

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

### 5.3 `not` — Obrni Rezultat

```python
je_kisa = True

if not je_kisa:
    print("Možeš da izađeš!")
else:
    print("Ostani unutra")

# Output: Ostani unutra
```

**Tabela Istine:**

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

---

## 6. Truthy/Falsy u Uslovima

Prethodno si naučio da `True` i `False` postoje. Ali Python tretira i DRUGE vrednosti kao "true" ili "false" u `if` bloku.

**Falsy vrednosti** (Python tretira kao False):

```python
if 0:           # False (nula je falsy)
    print("X")

if "":          # False (prazan string je falsy)
    print("X")

if []:          # False (prazna lista je falsy)
    print("X")

if None:        # False (None je falsy)
    print("X")
```

**Truthy vrednosti** (Python tretira kao True):

```python
if 1:           # True (bilo koji broj != 0)
    print("✓")  # Štampa se!

if "hello":     # True (neprazan string)
    print("✓")  # Štampa se!

if [1, 2, 3]:   # True (neprazna lista)
    print("✓")  # Štampa se!
```

---

## 7. Nested `if` — `if` Unutar `if`

```python
korisnik = "admin"
lozinka = "tajno123"
je_konekcija = True

if korisnik == "admin":
    print("Korisnik je pronađen")

    if lozinka == "tajno123":
        print("  Lozinka je ispravna")

        if je_konekcija:
            print("    Konekcija je OK")
            print("    ✓ Prijavljen!")
        else:
            print("    Nema konekcije")
    else:
        print("  Lozinka je POGREŠNA")
else:
    print("Korisnik ne postoji")

# Output:
# Korisnik je pronađen
#   Lozinka je ispravna
#     Konekcija je OK
#     ✓ Prijavljen!
```

**Napomena:** Svaki nivo `if` ima vlastitu indentaciju (+4 razmaka).

---

## 8. Česta Greška: Indentacija

```python
# ❌ POGREŠNO — print je izvan if bloka
if x > 5:
print("x je veći od 5")  # IndentationError!

# ✅ DOBRO — print je indentovan
if x > 5:
    print("x je veći od 5")
```

---

## 9. Česta Greška: `=` vs `==`

```python
# ❌ POGREŠNO
if x = 10:    # SyntaxError! = je dodela, ne poređenje
    print("X")

# ✅ DOBRO
if x == 10:   # == je poređenje
    print("X")
```

---

## 📝 Rezime

| Koncept              | Primer                              |
| -------------------- | ----------------------------------- |
| `if`                 | `if x > 5:` — Proverava jedan uslov |
| `elif`               | `elif x > 0:` — Alternativni uslov  |
| `else`               | `else:` — Ako ništa nije tačno      |
| `and`                | `if x > 0 and x < 10:` — OBA uslov  |
| `or`                 | `if x < 0 or x > 10:` — BAR JEDAN   |
| `not`                | `if not x:` — OBRNI                 |
| `==`                 | Poređenje (je li jednako?)          |
| `!=`                 | Poređenje (nije li jednako?)        |
| `>`, `<`, `>=`, `<=` | Numerička poređenja                 |

---

## 🎯 Sledeća Faza

Vrati se na **kickoff.md** i kreni sa **REPL vežbama**!
