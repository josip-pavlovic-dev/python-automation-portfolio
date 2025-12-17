# 📌 SUMMARY DAN 03

**Datum:** 2025-12-16
**Tema:** CSV Osnove - Dialect, Sniffer i csv.excel
**Status:** ✅ Kompletno + Spreman za praksu sutra

---

## 🎯 Problem koji sam rešio

```
❌ PRE:
"Nije mi jasno značenje Dialect, Sniffer i csv.excel"
"Imam osećaj da mi treba jača teorijska osnova"
"Ne mogu da počnem samostalno sa kodiranjem"


✅ SADA:
"Razumem šta je Dialect - recept za format"
"Znam kako koristi csv.Sniffer za auto-detektovanje"
"Znam kako padnem na csv.excel ako Sniffer ne uspe"
"Imam konkretan plan za narednih 14 dana"
"Znam šta tačno treba da učim"
```

---

## 📚 Materijal za učenje

### 1. [`csv_repl_exercises.md`](../../scratch/repl_sessions/csv_repl_exercises.md) ⭐ GLAVNI MATERIJAL ZA UČENJE

-   **DEO 1 (2h):** Teorija Dialect + praktični primeri
-   **DEO 2 (2h):** csv.Sniffer detektovanje + edge cases
-   **DEO 3 (2h):** Kompletan csv_cleaner.py sa komentarima
-   **Format:** REPL-ready - Svaka linija je testirana
-   **Rezultat:** Posle 6h, savršeno razumeš sve tri koncepta

### 2. [`DAY_03_CSV_BASICS.md`](../../learning/DAY_03_CSV_BASICS.md) ⭐ SUTRA RADIŠ OVO

-   **FAZA 1 (30 min):** Setup test CSV fajlove
-   **FAZA 2 (45 min):** Praktični primeri - vidim šta se dešava
-   **FAZA 3 (45 min):** Napravi svoju `detect_dialect()` funkciju
-   **Format:** Konkretne instrukcije, očekivani output
-   **Rezultat:** Sutra večeras, `detect_dialect()` radi!

### 3. [`BAZA_POTREBNA.md`](../../learning/BAZA_POTREBNA.md) ⭐ ODGOVOR NA GLAVNO PITANJE

-   **Koja baza ti trebá?** 4 Tiers znanja (Terminal, Python Core, Modules, Frameworks)
-   **14-danac plan** - Tačan redosled učenja
-   **Što dalje?** Jasna prioriteta šta da radiš kada
-   **Format:** Hierarchical - Od fundamentals do projects

### 4. [`FOUNDATION_14_DAYS.md`](../../learning/FOUNDATION_14_DAYS.md) ⭐ MASTER PLAN

-   **Piramida znanja** - Šta se gradi na čemu
-   **Nedelja 1** - Terminal + Python Core + CSV
-   **Nedelja 2** - Modules + Testing
-   **Nedelja 3** - Web scraping + Integration
-   **Format:** Strategija + Resursi + Motivacija

### 5. [`chatlog_csv_cleaner_2025_12_17.md`](../../scratch/chatlog/chatlog_csv_cleaner_2025_12_17.md) ⭐ DANASNJI RAZGOVOR

-   **Q&A format** - 5 ključnih pitanja sa odgovorima
-   **Tehnički napomene** - Ključni kod fragmenti
-   **Next steps** - Šta radiš sutra
-   **Format:** Arhiviran za kasnije čitanje

---

## 🔥 TOP 3 STVARI KOJE TREBAŠ ZAPAMTITI

### 1️⃣ Dialect = Recept za CSV

```python
CSV fajl može biti:
- name,age,city        (comma)
- name;age;city        (semicolon)
- name\tage\tcity      (tabs)

Ako koristiš POGREŠAN Dialect:
→ POGREŠNI REZULTATI bez greške! ⚠️

Rešenje: csv.Sniffer().sniff(sample)
```

---

### 2️⃣ Fallback strategy: Try → csv.excel

```python
try:
    dialect = csv.Sniffer().sniff(sample)
except Exception:
    dialect = csv.excel  # ← Nikad padni
```

---

### 3️⃣ Svaka skripta = Praksa + Ponavljanje

```
DAN 1: Čitam teoriju (30 min)
DAN 1: Kodiram primere (90 min)
DAN 2: Ponavljam kod bez greške
→ ZAPAMĆENO! ✅
```

---

## 🚀 Šta Radiš Sutra (Dan 4)

```
JUTRO:
1. Otvori DAY_03_CSV_BASICS.md
2. Setup test CSV fajlove (FAZA 1)

PREDPODNE:
3. Praktični primeri sa Sniffer (FAZA 2)
4. Testiraj sa 3 različita formata

POSLE PODNE:
5. Napravi detect_dialect() funkciju (FAZA 3)
6. Testiraj sa fallback mehanizmom

VEČERAS:
7. ✅ detect_dialect() radi savršeno
8. Spreman za DAY 4 - read_rows() i write_rows()

REZULTAT: +2h rada = Svladao CSV Dialect! 🎉
```

---

## 📊 14 Dana Priprema

| Nedelja | Dan   | Fokus             | Rezultat                   |
| ------- | ----- | ----------------- | -------------------------- |
| 1       | 1-2   | Terminal + Git    | Mogu da radim sa fajlovima |
| 1       | 3-4   | **CSV Osnove**    | **detect_dialect() ✅**    |
| 1       | 5-6   | CSV read/write    | csv_cleaner.py osnova      |
| 1       | 7     | Pathlib + Logging | Refaktuj sa Path i logging |
| 2       | 8     | Pytest            | Testiram svoj kod          |
| 2       | 9-10  | Requests + BS     | Web scraper osnove         |
| 2       | 11-14 | Integration       | Kompletan projekat         |

**Tvoja lokacija:** Dan 3 → Sutra počinješ sa FAZA 1 setup-a

---

## ✅ Checklist — Šta si Naučio Danas

-   [x] Razumem šta je Dialect
-   [x] Razumem šta je csv.Sniffer
-   [x] Razumem šta je csv.excel
-   [x] Znam kako čitati CSV bilo kog formata
-   [x] Znam kako pisati standardan CSV
-   [x] Imam 6h teorije + prakse (DEO 1-3)
-   [x] Imam konkretan plan za sutra
-   [x] Imam odgovore na sva pitanja
-   [x] Znam koja baza mi trebá (4 Tiers)
-   [x] Znam šta da radim nedelje dana

---

## 🎓 Znanje Koje Možeš Koristiti SADA

```python
# ✅ Mogu da koristim ovo bez paničnog guglovanja:

# 1. Detektuj format
dialect = csv.Sniffer().sniff(sample)

# 2. Čitaj CSV
with open(file, newline="") as f:
    reader = csv.reader(f, dialect=dialect)

# 3. Piši CSV
with open(file, "w", newline="") as f:
    writer = csv.writer(f, dialect=csv.excel)

# 4. Fallback ako neuspe
try:
    dialect = csv.Sniffer().sniff(sample)
except Exception:
    dialect = csv.excel

# 5. Čitaj bilo kog CSV-a
rows = []
with open(file, newline="", encoding="utf-8") as f:
    dialect = csv.Sniffer().sniff(f.read(2048))
    f.seek(0)
    reader = csv.reader(f, dialect=dialect)
    rows = list(reader)
```

**To je to! Spreman si! 🚀**

---

## 💪 Motivacija za Sutra

```
SADA:        "Ne razumem Dialect..."
SUTRA UJUTRO: "Kreiram test CSV fajlove"
SUTRA POPODNE: "Sniffer detektuje sve formate!"
SUTRA VEČE:    "Napisao sam detect_dialect()!"
SLEDECA NEDELJA: "Kompletan csv_cleaner sa testovima!"
SLEDECI MESEC:   "Kreiram nove projekte bez paničnog guglovanja"
```

**Razlika?** Sistem učenja + Praksa + Ponavljanje.

---

## 📖 Kako Koristiti Materijale

```
1️⃣ PRVO: Pročitaj chatlog_csv_cleaner.md (Opšta slika)
2️⃣ DRUGO: Pročitaj csv_repl_exercises.md DEO 1 (Teorija)
3️⃣ TREĆE: Pokreni DAY_03_CSV_BASICS.md (Praksa)
4️⃣ ČETVRTO: Referenca → BAZA_POTREBNA.md (Šta dalje)
5️⃣ PETO: Ponavljaj i eksperimentiši
```

---

## 🎯 Finalna Poruka

**Pitao si:** "Koja je to baza potrebna?"

**Odgovor:** Ista koju ti dajem u FOUNDATION_14_DAYS.md

**Ključna razlika:** Nije količina znanja, već **redosled**.

**Tvoj redosled:**

1. Terminal (foundation)
2. Python Core (basics)
3. **CSV Module** (osnova za sve) ← TI STE OVDE
4. Pathlib, JSON, Logging
5. Requests, BeautifulSoup
6. Real projects

**Rezultat:** Posle 14 dana, spreman za **bilo koji projekat**!

---

## 🚀 POČNI SUTRA

**File:** [`learning/DAY_03_CSV_BASICS.md`](../../learning/DAY_03_CSV_BASICS.md)

**Vreme:** ~2h (FAZA 1-3)

**Rezultat:** `detect_dialect()` radi!

**Sledeći dan:** read_rows() i write_rows()

---

**Sretno! 💪**

P.S. Ako nešto nije jasno, vraćam se na čat svaki dan. Ovo nije "završili smo" - ovo je **početak sistema učenja**.

Kreni sutra, redosled je precizan, svaki dan je planiran. ✅

---
