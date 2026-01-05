---
type: quick_start
date: 2026-01-01
estimated_time: 30 min
difficulty: beginner
---

# 🚀 START HERE — 30 Minuta do Prvog Razumevanja

**Cilj:** Brz pregled ključnih ideja. Za detalje, čitaj ostale fajlove.

---

## ❓ Šta je Python?

**Python = Jezik koji se čita kao pseudo-kod**

```python
# C / Java (komplikovano)
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

# Python (jednostavno)
for i in range(5):
    print(i)
```

---

## 🎯 Suština Python osnova (Dan 1)

### 1️⃣ **Uvlaka umesto zagrada**

Python koristi **4 razmaka** za definisanje blokova (ne `{}`):

```python
# ✅ ISPRAVNO
if x > 5:
    print("Veće od 5")      # Uvlaka od 4 razmaka
    print("Dalje...")

# ❌ POGREŠNO
if x > 5:
print("Veće od 5")          # GREŠKA - nedostaje uvlaka
```

**Zašto?** Python je dizajniran da bude čitljiv. Zagrade prave kod nečitljivim.

---

### 2️⃣ **Dvotačka (`:`) signalizira blok**

Posle `if`, `for`, `while`, `def`, `class` **uvek** dolazi dvotačka:

```python
if x > 5:      # ← dvotačka
    print(x)   # ← uvlaka

for i in range(5):  # ← dvotačka
    print(i)        # ← uvlaka

def my_func():  # ← dvotačka
    return 42   # ← uvlaka
```

---

### 3️⃣ **Dinamičko tipiziranje**

Python ne zahteva da deklarišeš tipove - on čini automatski:

```python
# Java (statičko tipiziranje)
int x = 5;
String name = "Ana";

# Python (dinamičko tipiziranje)
x = 5              # Python zna: ovo je int
name = "Ana"       # Python zna: ovo je str

# Čak i možeš da promeni tip (ne preporučuje se za početnike):
x = 5              # int
x = "pet"          # sada je str
```

---

### 4️⃣ **None = odsustvo vrednosti**

`None` nije `0`, nije `""` - to je **"nema vrednosti"**:

```python
x = None           # x postoji, ali nema vrednosti

if x is None:      # Provera da li je None
    print("Nema vrednosti")

# Razlika:
None   # Nema vrednosti
0      # Ima vrednosti, ali je 0
""     # Ima vrednosti, ali je prazna niska
[]     # Ima vrednosti, ali je prazan niz
```

---

### 5️⃣ **Truthy vs Falsy — Kako Python evaluira vrednosti**

Python tretira NEKI vrednosti kao "istinite" (truthy) a neke kao "lažne" (falsy):

```python
# FALSY vrednosti (Python ih tretira kao False):
if 0:           # False (nula je falsy)
if "":          # False (prazna niska je falsy)
if None:        # False (None je falsy)
if []:          # False (prazan niz je falsy)
if {}:          # False (prazan dict je falsy)

# TRUTHY vrednosti (Python ih tretira kao True):
if 1:           # True
if "tekst":     # True
if [1, 2, 3]:   # True
if {"key": "value"}:  # True
```

**Praktična primena:**

```python
users = []  # prazna lista

# ❌ Loše:
if len(users) > 0:
    print("Ima korisnika")

# ✅ Dobro (koristi falsy):
if users:  # prazna lista je falsy
    print("Ima korisnika")
```

---

### 6️⃣ **snake_case — Konvencija za imena**

Python koristi `snake_case` za imena (ne `camelCase`):

```python
# ✅ Ispravno (snake_case)
my_variable = 5
def calculate_sum(a, b):
    return a + b

class MyClass:
    pass

# ❌ Python stil, ali loše (camelCase)
myVariable = 5  # Tehnički radi, ali izbegavaj
def calculateSum():
    pass
```

---

## 💻 Prvi Kod - Pokrenuti u REPL-u

Otvori terminal i pokreni:

```bash
python3
```

Tada, ukucaj redosled:

```python
# Promenljiva
x = 10

# Provera
if x > 5:
    print("x je veće od 5")
else:
    print("x je manje od 5")

# Petlja
for i in range(3):
    print(f"Iteracija {i}")

# Truthy test
empty_list = []
if empty_list:
    print("Lista ima elemente")
else:
    print("Lista je prazna")
```

**Očekivani rezultat:**

```
x je veće od 5
Iteracija 0
Iteracija 1
Iteracija 2
Lista je prazna
```

Izlaz iz REPL-a: `exit()`

---

## 📊 Brz Pregled Koncepata

| Koncept       | Primer              | Ključna Lekcija                      |
| ------------- | ------------------- | ------------------------------------ |
| Uvlaka        | `if x:` + 4 razmaka | Definiše blok                        |
| Dvotačka      | `if x:`             | Signalizira blok                     |
| Dinamički tip | `x = 5; x = "pet"`  | Tipovi se određuju tokom rada        |
| None          | `x = None`          | Nije 0, nije "" - odsustvo vrednosti |
| Truthy        | `if []:`→ False     | Prazna [] je falsy                   |
| snake_case    | `my_var`            | Koristi donje crtice                 |

---

## ⚠️ Tri Najčešće Greške Početnika

### ❌ Greška 1: Zaboravljena dvotačka

```python
if x > 5      # ← GREŠKA! Nedostaje :
    print(x)
# SyntaxError: expected ':'
```

**Ispravka:** `if x > 5:`

---

### ❌ Greška 2: Mešanje tabova i razmaka

```python
if x > 5:
	print(x)    # ← TAB (problem!)
    print(y)    # ← RAZMAK (problem!)
# IndentationError: unexpected indent
```

**Ispravka:** Koristi Settings → Tab Size: 4 (samo razmake)

---

### ❌ Greška 3: Zbunjivanje None sa 0

```python
x = None
if x == 0:          # LOŠE - None nije 0!
    print("nula")

if x is None:       # ISPRAVNO
    print("nema vrednosti")
```

---

## 🎯 Šta Trebam da Znam do Kraja Dana

✅ **Razumeš zašto** Python koristi uvlaku
✅ **Znaš razliku** između `None`, `0`, `''`, `[]`
✅ **Možeš da prediš** šta će kod da ispiše
✅ **Znaš što je truthy** i šta je falsy
✅ **Možeš da napišeš** jednostavan `if/for` kod

---

## 🔗 Šta je Sledeće?

1. **Čitaj:** [`TEORIJA_mentalni_model.md`](TEORIJA_mentalni_model.md) (2h)
2. **Uradi:** [`REPL_VEŽBE_sintaksa_osnove.md`](REPL_VEŽBE_sintaksa_osnove.md) (2h)
3. **Razmisli:** [`NAJČEŠĆE_GREŠKE.md`](NAJČEŠĆE_GREŠKE.md) (30 min)

---

## 💡 Saveti za Učenje

1. **Pokretaj kod!** Čitanje nije dovoljno - moraš da vidiš šta se dešava
2. **Eksperimentiši** - što gore kod funkcionira, proba da ga prekiniš
3. **Ponavljaj** - prvi dan je za upoznavanje, ne za savladavanje
4. **Čini pauze** - mozak se najbolje uči sa pauzama (Pomodoro: 25 min + 5 min pauza)

## Hintovi za rad (tvoj nivo)

-   U REPL-u svaki koncept odmah isprobaj (promenljiva, sabiranje, string + int greška, None provera).
-   Truthy/falsy: testiraj `bool("")`, `bool("0")`, `bool([])`, `bool([0])` i zapiši pravilo (prazno je False, neprazno True).
-   Uvlaka/dvotačka: namerno izbaci uvlaku da vidiš SyntaxError; zapamti 4 razmaka.
-   Mini problemi radi kao kratke funkcije; cilj je da ne ponoviš istu grešku dva puta.

---

## ✋ Ako Se Zaglavim

**Q: Šta znači "SyntaxError: unexpected indent"?**
A: Mešaš tabove i razmake. Otvori Settings → Tab Size: 4 i koristi samo razmake.

**Q: Zašto `None is None` je True, ali `None == None` je i True?**
A: Oba rade, ali `is` poredi memorijsku lokaciju, `==` poredi vrednost. Za None, koristi `is`.

**Q: Mogu li da ombijem `camelCase` umesto `snake_case`?**
A: Tehnički - da, ali to se smatra lošim stilom u Python zajednici.

---

## 🚀 Spreman?

**Čitaj dalje:** [`kickoff.md`](kickoff.md) za detaljni plan Dana 1

Ili ako ste spremni: [`TEORIJA_mentalni_model.md`](TEORIJA_mentalni_model.md)

Sretno! 🎓
