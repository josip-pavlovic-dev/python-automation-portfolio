---
type: theory
date: 2026-01-01
estimated_time: 2 hours
difficulty: beginner
linked_to: L01_mentalni_model_pythona
---

# 📖 TEORIJA: Mentalni Model Pythona & Sintaksa

**Čas 1 od Dana 1 - Trajanje: ~2 sata**

Cilj: Razumeti **kako** Python razmišlja i **zašto** koristi uvlaku umesto zagrada.

---

## 1️⃣ INTERPRETIRANI JEZIK vs KOMPAJLIRANI

### Šta je razlika?

**Kompajlirani jezici (C, Java, C#):**

```
Tvoj kod (.java)
    ↓
Kompajler (prevođač)
    ↓
Mašinski kod (.exe)
    ↓
Kompjuter izvršava
```

**Interpretovani jezici (Python, JavaScript):**

```
Tvoj kod (.py)
    ↓
Interpreter (tumač)
    ↓
Tumač čita red-po-red i ODMAH izvršava
```

**Praktična razlika:**

```python
# Python - greške se vide tek kada se kod pokrene
x = "pet"
print(x + 5)  # ← GREŠKA! Tek kada Python čita red
TypeError: can only concatenate str (not "int") to str

# Java - greške se pronalaze PRE pokretanja
String x = "pet";
int y = x + 5;  // ← GREŠKA pri kompajliranju!
Type mismatch: cannot convert from String to int
```

**Zaključak:** Python je fleksibilniji, ali ako dodeliš pogrešan tip, saznaćeš tek tokom pokretanja.

---

## 2️⃣ DINAMIČKO TIPIZIRANJE — Python ne želi da zna tip unapred

### Šta znači "dinamičko"?

```python
x = 5              # Python: "Ok, x je int"
x = "pet"          # Python: "Sad je x str"
x = [1, 2, 3]      # Python: "Sad je x list"
x = {"key": 42}    # Python: "Sad je x dict"

print(type(x))     # <class 'dict'>
```

Python **dinamički** određuje tip tokom izvršavanja koda.

### Kako to da izgleda u drugim jezicima (statičko tipiziranje)

```java
// Java - moraš prvo reći tip
int x = 5;
x = "pet";        // ← GREŠKA! x je int, ne String!

String name = "Ana";
name = 42;        // ← GREŠKA! name je String, ne int!
```

### Zašto je dinamičko tipiziranje dobro?

✅ **Brže pisanje koda** - ne pisuš `int`, `String`, itd.
✅ **Fleksibilnije** - ista funkcija radi sa različitim tipima
✅ **Manje koda** - nema deklaracija tipova

### Zašto je dinamičko tipiziranje loše?

❌ **Greške tek pri pokretanju** - sintaksna greška se vidi tek kada pokreneš kod
❌ **Teže debugovanje** - ne znaš šta je tip dok ne pokreneš
❌ **Sporije** - tumač mora da Figure Out tipove tokom rada

**Zaključak:** Dinamičko tipiziranje je "brže za male programe, sporije za velike". Python je dobar za automatizaciju, ne za sistemsko programiranje.

---

## 3️⃣ UVLAKA (INDENTATION) — Zašto Python koristi razmake?

### Istorija

**Stariji jezici (C, Java):**

```c
// Zagrade pokazuju gde počinje i gde se završava blok
if (x > 5) {
    printf("Veće od 5");
    printf("Dalje...");
}
```

Problem: Zagrade čine kod nečitljivim (posebno sa gnezdenim zagraduama):

```java
if (a > 0) {
    if (b > 0) {
        if (c > 0) {
            System.out.println("Sve je pozitivno");
        }
    }
}
```

**Guido van Rossum (tvorca Python-a) je rekao:** "Zašto bi pisao `{` i `}` kada već pisuš uvlaku?"

Zato je Python rekao: **Koristimo SAMO uvlaku, bez zagrada.**

```python
if a > 0:
    if b > 0:
        if c > 0:
            print("Sve je pozitivno")
```

### Python Pravilo: Dvotačka + Uvlaka

```python
# ❌ LOŠE - bez dvotačke
if x > 5
    print(x)

# ✅ ISPRAVNO - sa dvotačkom
if x > 5:
    print(x)

# ❌ LOŠE - bez uvlake
if x > 5:
print(x)

# ✅ ISPRAVNO - sa uvlakom
if x > 5:
    print(x)
```

### Šta se računa kao "uvlaka"?

**Pravilo:** Python očekuje **4 razmaka** (ili 1 tab, ali razlika može biti fatal):

```python
# ✅ ISPRAVNO - 4 razmaka
if x > 5:
    print(x)      # 4 razmaka

# ❌ POGREŠNO - 2 razmaka
if x > 5:
  print(x)        # 2 razmaka - IndentationError!

# ❌ NAJGORE - mešanje tabova i razmaka
if x > 5:
    print(x)      # 4 razmaka (OK)
	print(y)      # 1 tab (PROBLEM!)
# IndentationError: unexpected indent
```

**Savvet:** VS Code Settings → Tab Size: 4, Insert Spaces: ON

---

## 4️⃣ BLOKOVI KODA — Šta se štiti uvlakom?

### `if` blok

```python
if x > 5:
    print("Veće")      # ← Dio bloka
    y = x * 2          # ← Dio bloka
print("Završeno")      # ← NIJE dio bloka (nema uvlake)
```

### `for` blok

```python
for i in range(3):
    print(i)           # ← Dio bloka
    print("---")       # ← Dio bloka
print("Gotovo")        # ← NIJE dio bloka
```

### `while` blok

```python
while x > 0:
    print(x)           # ← Dio bloka
    x -= 1             # ← Dio bloka
print("Završeno")      # ← NIJE dio bloka
```

### `def` (funkcija) blok

```python
def greet(name):
    print(f"Pozdrav, {name}")  # ← Dio funkcije
    return name                # ← Dio funkcije

greet("Ana")  # ← NIJE dio funkcije (nema uvlake)
```

### Gnezdeni blokovi (blokovi u blokovima)

```python
for i in range(3):              # ← Nivo 0
    if i % 2 == 0:              # ← Nivo 1 (4 razmaka)
        print(f"{i} je paran")   # ← Nivo 2 (8 razmaka)
    else:                        # ← Nivo 1 (4 razmaka)
        print(f"{i} je neparan") # ← Nivo 2 (8 razmaka)
print("Gotovo")                  # ← Nivo 0
```

**Zaključak:** Dubina uvlake pokazuje dubinu gnezdenja.

---

## 5️⃣ NEMA ZAGRADA, ALE SU ZAGRADE ZA POZIVE FUNKCIJA

⚠️ **Važno razumevanje:**

```python
# Nema zagrada za kontrolu toka (if, for, while, def, class)
if x > 5:     # ← NEMA zagrada
    print(x)

for i in range(5):  # ← range() ima zagrade jer je FUNKCIJA
    print(i)

def my_func():  # ← NEMA zagrada za samu def, ali zagrade za parametre
    pass

# ALI zagrade su za pozive funkcija (obavezno!)
print(x)      # ← zagrade su za poziv print()
my_func()     # ← zagrade su za poziv my_func()
len([1, 2])   # ← zagrade su za poziv len()
```

**Razlika:**

-   `if`, `for`, `while` - **NE trebaju zagrade**
-   Pozivi funkcija - **MORAJU zagrade**

---

## 6️⃣ None, True, FALSE — Specijalne vrednosti

### None = Odsustvo vrednosti

```python
x = None     # x postoji, ali nema vrednosti

# Primer: funkcija bez return vrednosti
def do_something():
    print("Nešto")
    # nema return - vraća None

result = do_something()
print(result)  # None
```

### True i False

```python
is_active = True
is_deleted = False

if is_active:
    print("Aktivno")
```

### Šta je razlika između `None`, `0`, `""`, `False`?

| Vrednost | Tip      | Značenje       | Primena                            |
| -------- | -------- | -------------- | ---------------------------------- |
| `None`   | NoneType | Nema vrednosti | Inicijalizacija, nedostaje podatak |
| `0`      | int      | Nula           | Brojanje, matematika               |
| `""`     | str      | Prazna niska   | Tekst bez znakova                  |
| `False`  | bool     | Logička laž    | Boolean logika                     |
| `[]`     | list     | Prazan niz     | Nema elemenata                     |

**Primer koga nije razumelo:**

```python
x = None
y = 0
z = ""

if x:      # ← None je FALSY (False ponašanje)
    print("x je truthy")
else:
    print("x je falsy")  # ← Ispisuje se OVO

if y:      # ← 0 je FALSY
    print("y je truthy")
else:
    print("y je falsy")  # ← Ispisuje se OVO

if z:      # ← "" je FALSY
    print("z je truthy")
else:
    print("z je falsy")  # ← Ispisuje se OVO
```

---

## 7️⃣ TRUTHY & FALSY — Kako Python evaluira ne-boolean vrednosti

### FALSY vrednosti (tretiraju se kao False)

```python
0          # int
0.0        # float
""         # prazna niska
[]         # prazan list
{}         # prazan dict
()         # prazna tuple
None       # odsustvo vrednosti
set()      # prazan set
False      # boolean False
```

### TRUTHY vrednosti (tretiraju se kao True)

```python
1          # bilo koji broj osim 0
"a"        # bilo koja niska osim ""
[1]        # bilo koji neprazan list
{"a": 1}   # bilo koji neprazan dict
(1,)       # bilo koja neprazna tuple
True       # boolean True
```

### Praktični primeri

```python
# ❌ Loše - eksplicitno
users = []
if len(users) > 0:
    print("Ima korisnika")

# ✅ Dobro - koristi truthy/falsy
users = []
if users:  # prazan list je falsy
    print("Ima korisnika")

# ❌ Loše - eksplicitno
text = ""
if text == "":
    print("Tekst je prazan")

# ✅ Dobro - koristi truthy/falsy
text = ""
if not text:  # "" je falsy, not "" je True
    print("Tekst je prazan")
```

---

## 8️⃣ KOMENTARI — Kako dokumentovati kod

### Jednoredi komentar

```python
x = 5  # Ovo je jednoredi komentar
```

### Viseredi komentar

```python
"""
Ovo je viseredi komentar.
Koristi se za dokumentovanje funkcija i klasa.
"""

def calculate_sum(a, b):
    """
    Sabira dva broja.

    Args:
        a: Prvi broj
        b: Drugi broj

    Returns:
        Zbir a i b
    """
    return a + b
```

---

## 9️⃣ SNAKE_CASE — Konvencija za imena

Python koristi `snake_case` (donje crtice) umesto `camelCase`:

```python
# ✅ Ispravno - snake_case
my_variable = 5
def calculate_sum(a, b):
    return a + b

class UserProfile:  # Klase koriste PascalCase
    pass

user_profile = UserProfile()  # Instance koriste snake_case

# ❌ Izbegavati - camelCase
myVariable = 5
def calculateSum(a, b):
    return a + b

userProfile = UserProfile()  # Tehnički radi, ali izbegavaj

# ❌ Čak i gore - SCREAMING_SNAKE_CASE (samo za konstante)
PI = 3.14159  # Konstanta
MAX_USERS = 100
DEBUG_MODE = True
```

---

## 🔟 REPL vs SKRIPTA

### REPL (Interactive Mode)

```bash
$ python3
Python 3.12.0 (main, ...)
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 5
>>> print(x)
5
>>> exit()
```

**Prednosti:**

-   Trenutni feedback
-   Brz eksperiment
-   Dobar za učenje

**Mane:**

-   Bez memorije između pokretanja
-   Ne možeš da sačuvaš kod

### Skripta (Script Mode)

```python
# my_script.py
x = 5
print(x)
```

```bash
$ python3 my_script.py
5
```

**Prednosti:**

-   Kod je sačuvan
-   Možeš da ga pokreneš više puta
-   Može biti deo projekta

**Mane:**

-   Sporiji za brz eksperiment
-   Moraš da koristiš editor + terminal

---

## ✅ CHECKLIST — Šta trebam da znam

-   [ ] Razumem zašto Python koristi uvlaku
-   [ ] Znam šta je "blok koda" i kako se definiše
-   [ ] Znam razliku između `None`, `0`, `""`, `False`
-   [ ] Znam šta je truthy i falsy vrednovanje
-   [ ] Mogu da napravim if/for bez zagrada
-   [ ] Razumem snake_case konvenciju
-   [ ] Mogu da pokrenm kod u REPL-u

---

## 🎯 Sumiran-Pouka

| Tema          | Ključna Ideja                        |
| ------------- | ------------------------------------ |
| Uvlaka        | Definiše blok umesto zagrada         |
| Dvotačka      | Signalizira početak bloka            |
| Dinamički tip | Tipovi se određuju tokom izvršavanja |
| None          | Nije 0, nije "" - odsustvo vrednosti |
| Truthy/Falsy  | Python evaluira ne-boolean vrednosti |
| snake_case    | Koristi donje crtice za imena        |

---

## 🔗 Dalje

**Čitaj:** [`REPL_VEŽBE_sintaksa_osnove.md`](REPL_VEŽBE_sintaksa_osnove.md) za praktičnu primenu

Ili ako želiš vise teorije: [`TEORIJA_tipiziranje_i_None.md`](TEORIJA_tipiziranje_i_None.md)

Sretno! 🚀
