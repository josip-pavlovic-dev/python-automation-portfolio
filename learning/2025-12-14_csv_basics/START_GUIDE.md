# 🚀 START GUIDE — CSV Basics (Day 01)

## ✅ Šta sam ti kreirao

📁 **Test fajlovi u `sandbox/basics/`:**

-   `sample.csv` — čist, standardan CSV (4 kolone, 3 reda)
-   `dirty_sample.csv` — prljav CSV (`;` delimiter, whitespace, prazni redovi)
-   `products.csv` — dodatni primer (proizvodi sa cenom)

📁 **Kod fajlovi:**

-   `csv_cleaner.py` — skeleton verzija (možeš proširiti)
-   `csv_cleaner_final.py` — finalna verzija sa komentarima

📁 **Dnevni folder `learning/2025-12-14_csv_basics/`:**

-   `kickoff.md` — plan dana
-   `tasks.md` — checklist
-   `cheatsheet.md` — CSV referenca
-   `chatlog.md` — današnji razgovori
-   `summary.md` — popuni na kraju dana

---

## 🎯 Strategija za danas (8-10h)

### FAZA 1: REPL Warm-up (09:00-10:30) — 1h 30min

**Cilj:** Razumeti `csv.reader`, `DictReader`, `delimiter`, `newline=""`, encoding greške.

**Akcija:**

1. Otvori terminal u root-u projekta
2. Pokreni Python REPL: `python`
3. Radi korak po korak prema [`scratch/repl_sessions/csv_repl_plan.md`](scratch/repl_sessions/csv_repl_plan.md)

**Konkretni koraci:**

```python
# KORAK 1 — Učitaj modul i help (5 min)
import csv
help(csv)  # čitaj dokumentaciju
dir(csv)   # vidi funkcije

# KORAK 2 — Čitanje sample.csv (10 min)
with open("sandbox/basics/sample.csv", newline="") as f:
    reader = csv.reader(f)
    rows = list(reader)
    print(rows)
    print(type(rows[0]))  # list

# KORAK 3 — DictReader (15 min)
with open("sandbox/basics/sample.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row, type(row))  # dict

# KORAK 4 — Pisanje novog CSV (15 min)
data = [
    ["ime", "godine"],
    ["Nikola", 32],
    ["Ivana", 27]
]
with open("sandbox/basics/out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Proveri šta si kreirao
with open("sandbox/basics/out.csv") as f:
    print(f.read())

# KORAK 5 — DictWriter (20 min)
with open("sandbox/basics/people.csv", "w", newline="") as f:
    fieldnames = ["ime", "godine", "grad"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"ime": "Milan", "godine": 40, "grad": "Kragujevac"})
    writer.writerow({"ime": "Sara", "godine": 22, "grad": "Subotica"})

# KORAK 6 — Edge: pogrešan delimiter (10 min)
with open("sandbox/basics/dirty_sample.csv", newline="") as f:
    reader = csv.reader(f, delimiter=",")  # pogrešan delimiter
    print(list(reader))  # sve u jednoj koloni

with open("sandbox/basics/dirty_sample.csv", newline="") as f:
    reader = csv.reader(f, delimiter=";")  # ispravan delimiter
    print(list(reader))

# KORAK 7 — Edge: bez newline="" (10 min)
# Windows bug — probaj bez newline=""
with open("sandbox/basics/test_bad.csv", "w") as f:  # BEZ newline=""
    writer = csv.writer(f)
    writer.writerow(["test", "123"])
    writer.writerow(["test2", "456"])

with open("sandbox/basics/test_bad.csv") as f:
    print(repr(f.read()))  # vidi duplo \n\n

# KORAK 8 — Error: fajl ne postoji (5 min)
try:
    with open("sandbox/basics/nonexistent.csv", newline="") as f:
        reader = csv.reader(f)
except FileNotFoundError as e:
    print(f"Error: {e}")
```

**✅ Checklist:**

-   [ ] `csv.reader` vraća liste
-   [ ] `DictReader` vraća dict-ove
-   [ ] `newline=""` je obavezan
-   [ ] Pogrešan delimiter daje jednu kolonu
-   [ ] `FileNotFoundError` kad fajl ne postoji

**⏱️ Vreme:** Max 1h 30min. Ako zaglaviš, javi.

---

### FAZA 2: Helper funkcije (10:30-11:30) — 1h

**Cilj:** Napisati `load_csv` i `write_csv` sa `Path` i `DictReader/DictWriter`.

**Akcija:**

1. Otvori `sandbox/basics/python_refresh.py`
2. Dodaj funkcije na kraju fajla

**Kod:**

```python
from pathlib import Path
import csv


def load_csv(path: Path) -> list[dict[str, str]]:
    """Load CSV as list of dicts using DictReader."""
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_csv(path: Path, rows: list[dict[str, str]], headers: list[str]) -> None:
    """Write list of dicts to CSV using DictWriter."""
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


# Test funkcija
if __name__ == "__main__":
    test_path = Path("sandbox/basics/sample.csv")
    data = load_csv(test_path)
    print(f"Loaded {len(data)} rows:")
    for row in data:
        print(row)

    # Snimi nazad
    out_path = Path("sandbox/basics/copy.csv")
    headers = list(data[0].keys()) if data else []
    write_csv(out_path, data, headers)
    print(f"Saved to {out_path}")
```

**Test:**

```bash
cd /home/jole-pavlovic-dev/code/python-automation-lab/python-automation-portfolio
python sandbox/basics/python_refresh.py
```

**✅ Checklist:**

-   [ ] `load_csv` radi sa `Path`
-   [ ] `write_csv` kreira fajl sa headerom
-   [ ] Test u `if __name__ == "__main__":` radi

**⏱️ Vreme:** Max 1h.

---

### FAZA 3: CSV Cleaner v0 (11:45-13:00) — 1h 15min

**Cilj:** Kreirati `csv_cleaner.py` koji čisti `dirty_sample.csv`.

**Akcija:**

1. Otvori `sandbox/basics/csv_cleaner.py` (već postoji skeleton)
2. Testiraj na `dirty_sample.csv`
3. Rezultat: `clean.csv` sa trimovanim vrednostima, bez praznih redova

**Test:**

```bash
python sandbox/basics/csv_cleaner.py
```

**Očekivani output:**

```
Input rows: 7
Output rows: 4
Skipped empty: 2
Saved to: clean.csv
```

**Proveri clean.csv:**

```bash
cat sandbox/basics/clean.csv
```

Treba da vidiš:

```
ime,prezime,godine,grad
Ana,Petrović,25,Beograd
Marko,Jovanović,30,Novi Sad
Jelena,Nikolić,28,
Stefan,Stojanović,35,Subotica
```

**✅ Checklist:**

-   [ ] Trimovane su sve ćelije (nema leading/trailing whitespace)
-   [ ] Delimiter normalizovan na `,`
-   [ ] Prazni redovi skipnuti
-   [ ] Statistika ispisana

**⏱️ Vreme:** Max 1h 15min.

---

### 🍔 PAUZA (13:00-14:00)

---

### FAZA 4: Web Scraper Primer (14:00-16:00) — 2h

**Cilj:** Pokrenuti postojeći scraper i proveriti output.

**Akcija:**

```bash
cd projects/01-web-scraper
source venv/bin/activate
python scraper.py
```

**Proveri output:**

```bash
head -n 5 output/scraped_quotes.csv
```

**✅ Checklist:**

-   [ ] Scraper se izvršio bez greške
-   [ ] Fajl postoji u `output/scraped_quotes.csv`
-   [ ] Ima ~20 redova (2 strane × 10 citata)

**Optional (ako stigneš):**

-   Dodaj `Path` za output putanje u `scraper.py`
-   Dodaj proveru `timeout` i `headers` u `config.py`

**⏱️ Vreme:** Max 2h (ako radiš refaktor).

---

### FAZA 5: README + Git Commit (16:00-17:00) — 1h

**Akcija:**

1. Kratko update README.md (dodaj paragraf o CSV Cleaner v0)
2. Git commit

**Git komande:**

```bash
git status
git add sandbox/basics/csv_cleaner.py sandbox/basics/dirty_sample.csv sandbox/basics/sample.csv
git add learning/2025-12-14_csv_basics/
git commit -m "feat(day01): csv basics foundations + CSV Cleaner v0

- Add sample CSV files for testing
- Implement CSV Cleaner v0 (trim, normalize delimiter, skip empty)
- Add helper functions load_csv/write_csv with Path
- REPL warm-up completed: csv.reader, DictReader/DictWriter
- Daily folder structure created"
git push
```

**✅ Checklist:**

-   [ ] Commit message jasan
-   [ ] Svi novi fajlovi dodati
-   [ ] Push na GitHub

---

### FAZA 6: Reflection (17:00-17:30) — 30min

**Akcija:**

1. Popuni `learning/2025-12-14_csv_basics/summary.md`
2. Šta si naučio? Šta je bilo konfuzno?
3. 3 cilja za sutra

---

## 🆘 Ako zaglaviš

### Problem: FileNotFoundError

**Rešenje:** Proveri putanju. Ako si u root-u, koristi `sandbox/basics/sample.csv`.

### Problem: csv.reader vraća prazan list

**Rešenje:** Iterator je potrošen. Koristi `rows = list(reader)` odmah.

### Problem: Delimiter ne radi

**Rešenje:** Proveri da li je delimiter `,` ili `;`. Koristi `delimiter=";"`

### Problem: Encoding error

**Rešenje:** Dodaj `encoding="utf-8"` u `open()`.

### Ako si zaglavljen 15+ min

**Javi mi ovde sa:**

-   Kod koji si probao
-   Error poruka
-   Šta očekuješ vs šta dobijaš

---

## 💪 Motivacija

Danas radiš **fundamentals**. CSV modul je osnova za:

-   Scraping output (web scraper → CSV)
-   Data cleaning (input → clean → output)
-   Excel automation (čitanje/pisanje CSV)
-   PDF extraction (PDF → CSV)

Ovaj dan je **temelj** za sve dalje projekte. Uzmi polako, razumi svaki korak.

**Srećno! 🚀**
