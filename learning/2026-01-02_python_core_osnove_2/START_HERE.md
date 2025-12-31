---
type: quick_start
time: "30 min"
---

# ⚡ 30-Minute Start — Dan 2: Kontrola Toka

## 🎯 Šta ćeš naučiti do 9:00

Skočićeš direktno u REPL (Interactive Python) i razumeći **kako Python DONOSI ODLUKE**.

---

## 1️⃣ Kako Python Bira Između 2 Opcije

```python
# Kod 1: Klasičan if/else
x = 10

if x > 5:
    print("x je veći od 5")
else:
    print("x je manji ili jednak 5")

# Output: x je veći od 5
```

**Analiza:**

-   Python **čita** `if x > 5:`
-   **Proverava** da li je `10 > 5` (DA!)
-   **Izvršava** prvi blok (`print("x je veći od 5")`)
-   **Preskaće** drugi blok (`else`)

---

## 2️⃣ Tri Opcije — `if/elif/else`

```python
# Kod 2: Tri grana
rezultat = 75

if rezultat >= 90:
    print("A - Odličan!")
elif rezultat >= 80:
    print("B - Dobar")
elif rezultat >= 70:
    print("C - Zadovoljavajući")
else:
    print("F - Neuspešan")

# Output: C - Zadovoljavajući
```

**Kako radi:**

1. `if rezultat >= 90:` → NE (75 nije >= 90)
2. `elif rezultat >= 80:` → NE (75 nije >= 80)
3. `elif rezultat >= 70:` → DA! (75 jest >= 70)
4. Izvršava: `print("C - Zadovoljavajući")`
5. Preskaće sve ostale

**Važno:** Python **STAJE** čim nađe `True` `elif`. Ostali se ignoriše.

---

## 3️⃣ Kombinovanje Uslova: `and`, `or`, `not`

```python
# Kod 3: Dva uslova ISTOVREMENO (and)
temperatura = 25
humidnost = 60

if temperatura > 20 and humidnost < 70:
    print("Uslovi su idealni!")
else:
    print("Nije idealno")

# Output: Uslovi su idealni!
```

| Operator | Čita se | Prim                  |                        |
| -------- | ------- | --------------------- | ---------------------- |
| `and`    | I/i     | Oba uslov mora biti T | `if x > 0 and x < 10:` |
| `or`     | ILI     | Bar jedan mora biti T | `if x < 0 or x > 100:` |
| `not`    | NE      | Obrni rezultat        | `if not x:`            |

---

## 4️⃣ `range()` — Generisanje Brojeva

```python
# Kod 4: for petlja sa range()
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

**Čita se:** "Za svaki broj `i` od 0 do 4..."

**Tri oblika `range()`:**

```python
range(5)           # 0, 1, 2, 3, 4 (STAJE PRE 5)
range(2, 8)        # 2, 3, 4, 5, 6, 7
range(0, 20, 3)    # 0, 3, 6, 9, 12, 15, 18 (STEP 3)
```

---

## 5️⃣ `break` — Izlaz iz Petlje

```python
# Kod 5: Skok iz petlje
for i in range(10):
    if i == 5:
        break  # IZLAZI IZ PETLJE
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

Kada `i` postane 5:

-   `if i == 5:` → True
-   `break` → PREKINUTI petlju
-   Ostatak petlje se ignoriše

---

## 6️⃣ `continue` — Preskoči Ovaj Red

```python
# Kod 6: Preskoči neke iteracije
for i in range(5):
    if i == 2:
        continue  # PRESKOČI OVAJ RED
    print(i)

# Output:
# 0
# 1
# 3
# 4
```

Kada `i` postane 2:

-   `if i == 2:` → True
-   `continue` → PRESKOČI `print(i)`
-   Nastavi sa sledećom iteracijom (3)

---

## 🧪 Vežba #1: Testiraj u REPL-u

**Čim otvoriš REPL, uradi ova 3 vežbe:**

```python
# VEŽBA 1.1: Ako sada
trenutni_sat = 14

if trenutni_sat < 12:
    print("Dobro jutro!")
elif trenutni_sat < 18:
    print("Dobar dan!")
else:
    print("Dobra noć!")

# VEŽBA 1.2: Broj nije u lošem rasponu
broj = 50

if broj < 0 or broj > 100:
    print("Broj je van raspona!")
else:
    print("Broj je OK")

# VEŽBA 1.3: Štampaj samo parne brojeve
for num in range(10):
    if num % 2 == 0:
        print(num)
```

---

## ✅ Čeklist za 9:00

-   [ ] Razumeš `if/elif/else` strukturu
-   [ ] Znaš `and`, `or`, `not`
-   [ ] Testirao si `range()` sa različitim brojevima
-   [ ] Testirao si `break` i `continue`
-   [ ] Urađio si sve 3 VEŽBE iznad

## Hintovi za rad (tvoj nivo)

-   Nacrtaj mini tablu odluke (broj <0, =0, >0) i testiraj svaku granu u REPL-u.
-   `range` proveravaj sa `list(range(...))` da vizuelno vidiš izlaz; menjaj step i start/stop.
-   `enumerate` uporedi sa petljom bez enumerate; zapiši koja je čitljivija i zašto.
-   `while` napravi sa korisničkim unosom i `quit` prekidom; koristi `break`/`continue` da osetiš razliku.
-   Mini problemi: kreni od lakših, posle svakog napiši jednu rečenicu šta si naučio.

---

**Sledeće:** Čitaj **kickoff.md** za detaljni plan dana
