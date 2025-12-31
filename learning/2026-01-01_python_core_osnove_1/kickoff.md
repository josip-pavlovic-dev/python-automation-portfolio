---
type: kickoff
date: 2026-01-01
phase: python_core_day_1
linked_to: python-automation-portfolio
status: active
estimated_duration: 8 hours
---

# 🚀 Daily Kickoff — 2026-01-01 | Dan 1: Mentalni Model Pythona

## 🎯 Cilj Dana

> Razumeti **kako** Python razmišlja, **zašto** koristi uvlaku umesto zagrada, i **kako** se Python razlikuje od drugih jezika.

**Po završetku Dan 1, trebao bi da:**

✅ Razumeš pojmove: uvlaka, dvotačka, dinamičko tipiziranje, None, truthy/falsy
✅ Možeš da pokrneš kod u Python REPL-u bez greške
✅ Znaš šta će kod da ispiše PRE nego da ga pokrneš
✅ Razumeš razliku između `None`, `0`, `""`, `False`
✅ Znaš snake_case konvenciju

---

## 📋 Zadaci za Dan 1

### ✅ OBAVEZNI (Core)

-   [ ] 08:00-09:00: Pročitaj **START_HERE.md** (30 min) + Otvori REPL (30 min)
-   [ ] 09:00-11:00: Pročitaj **TEORIJA_mentalni_model.md** (2h)
-   [ ] 11:00-12:30: Uradi **REPL_VEŽBE_sintaksa_osnove.md** FAZA 1-3 (1.5h)
-   [ ] 13:30-15:00: Pročitaj **TEORIJA_tipiziranje_i_None.md** (1.5h)
-   [ ] 15:00-16:00: Uradi **REPL_VEŽBE_falsy_vs_truthy.md** FAZA 1-2 (1h)
-   [ ] 16:00-17:00: Rešiš **MINI_PROBLEMI.md** (zadaci 1-10) (1h)
-   [ ] 17:00-18:00: Napiši **summary.md** + refleksija (1h)

### 🎯 OPCIONALNI (Ako imaš vremena)

-   [ ] Pročitaj **NAJČEŠĆE_GREŠKE.md**
-   [ ] Rešiš sve MINI_PROBLEMI (zadaci 1-20)
-   [ ] Napravi svoj mali Projekt (vidi Bonus sekciju)

---

## ⏱️ Predložena Raspodela Vremena (8h)

```
08:00-09:00 | Ujutro Kickoff + START_HERE           | 1h
09:00-11:00 | TEORIJA mentalni model                | 2h
11:00-12:00 | REPL vežbe - Sintaksa FAZA 1-2        | 1h
12:00-13:00 | PAUZA - Ručak + Ostatak              | 1h
13:00-14:30 | TEORIJA tipiziranje i None           | 1.5h
14:30-15:30 | REPL vežbe - Falsy FAZA 1-2          | 1h
15:30-16:30 | MINI_PROBLEMI (10 zadataka)          | 1h
16:30-18:00 | Summary + Refleksija                 | 1.5h
────────────────────────────────────────────────────────
UKUPNO:                                             | 8h
```

---

## 📖 Materijali za Dan 1

### Teorija (čitaj)

1. **START_HERE.md** (30 min) - Brz pregled
2. **TEORIJA_mentalni_model.md** (2h) - Detaljno
3. **TEORIJA_tipiziranje_i_None.md** (1.5h) - Detaljno

### Praksa (radi)

1. **REPL_VEŽBE_sintaksa_osnove.md** (2h)
2. **REPL_VEŽBE_falsy_vs_truthy.md** (1.5h)
3. **MINI_PROBLEMI.md** (1h)

### Refleksija (napiši)

1. **summary.md** (1h) - Šta si naučio/naučila

---

## 💻 Pre nego što počneš

### Instalacija & Setup

```bash
# Provera da li je Python instaliran
python3 --version

# Trebalo bi nešto kao:
# Python 3.10.0 ili novije

# Otvori Python REPL
python3

# U REPL-u:
>>> x = 5
>>> print(x)
5
>>> exit()
```

Ako dobijash grešku `python3: command not found`:

-   Linux/Mac: `brew install python3` ili skini sa python.org
-   Windows: Skini Python sa <https://python.org> i markiraj "Add to PATH"

### Editor Setup

Otbori VS Code settings:

```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "[python]": {
        "editor.tabSize": 4,
        "editor.insertSpaces": true,
        "editor.formatOnSave": true,
        "editor.rulers": [88]
    }
}
```

---

## 🎓 Kako Uiti

### Preporuka 1: Pomodoro Teknika

```
25 min RAD + 5 min pauza
25 min RAD + 5 min pauza
25 min RAD + 15 min pauza (duža pauza)
```

### Preporuka 2: Aktivno čitanje

```
❌ Pasivno: Čitaj i pomisli "razumem"
✅ Aktivno: Čitaj → Eksperimentiši → Napiši beleške
```

### Preporuka 3: Ruci-na-tastaturasadržaj

```
❌ Loše: Kopirati kod iz materijala
✅ Dobro: Ručno ukucat kod (izbegavaj greške)
```

### Preporuka 4: Pravaj greške

```
❌ Loše: Biti uplašen od greške
✅ Dobro: "Šta će se desiti ako mi dodam pogrešan tip?"
```

---

## ⚠️ Česte Greške Početnika (Izbjegavati)

| Greška                   | Primer                         | Rešenje                                |
| ------------------------ | ------------------------------ | -------------------------------------- |
| Zaboravljena dvotačka    | `if x > 5:` → `if x > 5`       | Uvek `:` posle if/for/while/def        |
| Mešanje tabova i razmaka | Tab + Space                    | Settings: Tab Size 4, Insert Spaces ON |
| None vs 0 vs ""          | `if None:` thinking je `if 0:` | None je odsustvo, 0 je broj            |
| Beskračičan kod          | `for i in range(10000000):`    | Uvek imaj `break` u while              |

---

## 🚨 Ako Se Zaglavim

### Scenario 1: "Ne razumem zadatak"

```
1. Ponovi zadatak i pročitaj ga sporije
2. Pogledaj primer iz materijala
3. Pokreni u REPL-u i eksperimentiši
4. Ako je sveće nego 15 min - preskočiti na sledeće
```

### Scenario 2: "Kod ne radi, dobijam grešku"

```
1. Pročitaj celu grešku (važna je poslednja linija)
2. Potraži grešku u NAJČEŠĆE_GREŠKE.md
3. Pokreni kod liniju-po-liniju u REPL-u
4. Ako ne razumeš - napisi grešku u chatlog.md i pitaj Copilota
```

### Scenario 3: "Zasnujem se od veoma teorije"

```
1. Preskoči teoriju, idi na REPL_VEŽBE
2. Kod je bolji učilac nego teorija
3. Teorija će biti jasna kada vidiš kod u akciji
```

---

## 📝 Što treba da napišeš/sačuvaš

### 1. Beleške (opsionalno)

```markdown
# Dan 1 Beleške

## Uvlaka

-   Python koristi 4 razmaka
-   Definiše blok umesto zagrada

## Truthy/Falsy

-   [] je falsy
-   [1,2,3] je truthy

## Moja Greška

-   Zaboravio sam : posle if
```

### 2. REPL Vežbe (obavezno)

```python
# Trebalo bi da napraviš/pratiš kod iz REPL_VEŽBE fajlova
# NEMOJ da kopiraš - ručno ukucat!
```

### 3. MINI_PROBLEMI (obavezno)

```python
# Rešenja zadataka iz MINI_PROBLEMI.md
# Radi direktno u REPL-u ili u test.py fajlu
```

### 4. summary.md (obavezno)

```markdown
# Summar Dan 1

## Šta sam naučio/naučila

1. Uvlaka definiše blok
2. None nije 0
   ...

## Greške koje sam pravio/prajila

1. Zaboravio/zaboravila sam :
2. Mešao/mesala sam tab i space

## Pitanja za sutra

1. Kako da proverim tip promenljive?
2. Šta je reason ako imaj return u funkciji?
```

---

## 🎯 Očekivani Output Dan 1

Na kraju Dana 1, trebalo bi da imaš:

```
2026-01-01_python_core_osnove_1/
├── README.md
├── START_HERE.md
├── TEORIJA_mentalni_model.md
├── TEORIJA_tipiziranje_i_None.md
├── REPL_VEŽBE_sintaksa_osnove.md
├── REPL_VEŽBE_falsy_vs_truthy.md
├── MINI_PROBLEMI.md
├── NAJČEŠĆE_GREŠKE.md
├── summary.md                ← NAPIŠI OVAJ
└── test_dan1.py             ← OPCIONALNO: Tvoja REPL vežba
```

---

## 💡 Saveti za Uspeh

1. **Brzina je neprijateljska** - Bolje je biti spor i precizan
2. **Ponavljanje je ključ** - Ponovi nakon 1h, 24h, 1 nedelje
3. **Nauči kroz greške** - Bez grešaka nema učenja
4. **Pitaj se "zašto"** - Zašto Python radi na ovaj način?
5. **Pravi male projekte** - Provjeri MINI_PROBLEMI

---

## 🔗 Šta je Dalje (Dan 2)

Dan 2 će biti: **Kontrola Toka - if/elif/else, for/while, range, enumerate**

Spremi se!

---

## ✅ Checklist Pre Nego Što Kreneš

-   [ ] Python je instaliran (`python3 --version`)
-   [ ] Mogu da otvorim REPL (`python3`)
-   [ ] Mogu da zatvorim REPL (`exit()`)
-   [ ] VS Code je otboren
-   [ ] Imaš 8 sati za fokusirani rad (bez ometanja!)
-   [ ] Spreman/Spremna si da napraviš greške (to je dobro!)

---

## 🚀 LET'S GO

Prvo čitaj: **START_HERE.md**

Nakon toga: **TEORIJA_mentalni_model.md**

Sretno! 🎓

---

**Vreme:** 2026-01-01
**Trajanje:** 8 sati
**Težina:** Početnik
**Status:** Spreman sam!
