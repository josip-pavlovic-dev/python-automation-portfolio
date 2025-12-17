# 📅 DAN 3: CSV OSNOVE — Dialect, Sniffer i csv.excel (Dan 1 - CSV Fokus)

**Datum:** 2025-12-17
**Cilj:** Razumeti Dialect i Sniffer kroz praktične vežbe
**Rezultat:** Samstalno korišćenje csv.Dialect bez paničnog guglovanja
**Trajanje:** ~2h

---

# 🎯 Šta ćeš sutra raditi?

1. **FAZA 1 (30 min):** Setup - kreiraj test CSV fajlove
2. **FAZA 2 (45 min):** Teorija kroz terminal - eksperimentuj sa Sniffer
3. **FAZA 3 (45 min):** Praktika - napravi detect_dialect() funkciju

---

# 🚀 FAZA 1: Setup (30 min)

## 1.1 Naviguiraj do `sandbox/basics/`

```bash
cd /home/jole-pavlovic-dev/code/python-automation-lab/python-automation-portfolio/sandbox/basics
pwd  # Proverite gde ste
```

## 1.2 Kreiraj `data/` folder i test CSV fajlove

```bash
mkdir -p data
```

## 1.3 Pokreni Python terminal

```bash
python3
# ili
python
```

## 1.4 Kopirati PRVI kod iz `csv_repl_exercises.md` - DEO 1.2

```python
# Zameni sadržaj ispod:

import csv
from pathlib import Path

# Format 1: Standard (comma-delimited)
csv_standard = """name,age,city
Ana,25,Beograd
Marko,30,Novi Sad"""

# Format 2: Semicolon-delimited (Evropski standard)
csv_semicolon = """name;age;city
Ana;25;Beograd
Marko;30;Novi Sad"""

# Format 3: Tab-delimited (TSV)
csv_tabs = """name\tage\tcity
Ana\t25\tBeograd
Marko\t30\tNovi Sad"""

# Kreiraj fajlove
Path("data").mkdir(exist_ok=True)
Path("data/format_comma.csv").write_text(csv_standard)
Path("data/format_semicolon.csv").write_text(csv_semicolon)
Path("data/format_tabs.csv").write_text(csv_tabs)

print("✅ Test fajlovi kreirani!")

# Provera
import os
print("\nFajlovi u data/:")
for f in os.listdir("data"):
    print(f"  - {f}")
```

**Očekivani output:**

```
✅ Test fajlovi kreirani!

Fajlovi u data/:
  - format_comma.csv
  - format_semicolon.csv
  - format_tabs.csv
```

## 1.5 Provera: Pročitaj fajlove sa `cat`

```bash
# Exit iz Python terminal
exit()

# U terminalu:
cat data/format_comma.csv
cat data/format_semicolon.csv
cat data/format_tabs.csv
```

---

# 📖 FAZA 2: Teorija - Problem & Rešenje (45 min)

## 2.1 Problem: Pogrešan Dialect

Vrati se u Python:

```bash
python3
```

```python
import csv

# ❌ PROBLEM: Čitaj semicolon fajl sa default delimiter (comma)
print("❌ POGREŠAN PRIMER (zaboravio sam delimiter):")
with open("data/format_semicolon.csv", newline="") as f:
    reader = csv.reader(f)  # ← nema delimiter=";", koristi default ","
    for row in reader:
        print(f"  Red: {row}")
        print(f"  Kolone: {len(row)}")
        break  # Samo prvi red

print("\n" + "="*60)

# ✅ ISPRAVAN PRIMER: Koristi pravi delimiter
print("\n✅ ISPRAVAN PRIMER (sa delimiter=';'):")
with open("data/format_semicolon.csv", newline="") as f:
    reader = csv.reader(f, delimiter=";")  # ← Kazujem pravi separator
    for row in reader:
        print(f"  Red: {row}")
        print(f"  Kolone: {len(row)}")
        break
```

**Šta videš:**

```
❌ POGREŠAN PRIMER (zaboravio sam delimiter):
  Red: ['name;age;city']     ← CELA LINIJA JE JEDAN STRING!
  Kolone: 1                   ← trebalo bi 3!

============================================================

✅ ISPRAVAN PRIMER (sa delimiter=';'):
  Red: ['name', 'age', 'city']  ← RAZDELENO!
  Kolone: 3                      ← TAČNO!
```

**Lekcija:** Ako ne znaš Dialect, Python će ti dati POGREŠNE podatke bez greške! ⚠️

## 2.2 Rešenje 1: csv.excel Dialect

```python
import csv

# Istražiti csv.excel
print("Atributi csv.excel Dialect-a:")
print(f"  delimiter: {repr(csv.excel.delimiter)}")
print(f"  quotechar: {repr(csv.excel.quotechar)}")
print(f"  lineterminator: {repr(csv.excel.lineterminator)}")
print(f"  doublequote: {csv.excel.doublequote}")

# Koristi csv.excel
print("\n" + "="*60)
print("\n✅ Korišćenje csv.excel:")
with open("data/format_comma.csv", newline="") as f:
    reader = csv.reader(f, dialect=csv.excel)
    for row in reader:
        print(f"  {row}")
```

**Output:**

```
Atributi csv.excel Dialect-a:
  delimiter: ','
  quotechar: '"'
  lineterminator: '\r\n'
  doublequote: True

============================================================

✅ Korišćenje csv.excel:
  ['name', 'age', 'city']
  ['Ana', '25', 'Beograd']
  ['Marko', '30', 'Novi Sad']
```

## 2.3 Rešenje 2: csv.Sniffer - Automatska detekcija

```python
import csv

# OSNOVNA UPOTREBA - Sniffer detektuje format
print("🔍 CSV SNIFFER - Automatska detekcija\n")

test_samples = {
    "Comma": "name,age,city\nAna,25,Beograd\nMarko,30,Novi Sad",
    "Semicolon": "name;age;city\nAna;25;Beograd\nMarko;30;Novi Sad",
    "Tabs": "name\tage\tcity\nAna\t25\tBeograd\nMarko\t30\tNovi Sad",
}

for format_name, sample in test_samples.items():
    print(f"\n{format_name}:")
    print(f"  Sample: {sample[:30]}...")

    try:
        dialect = csv.Sniffer().sniff(sample)
        print(f"  ✅ Detektovan delimiter: {repr(dialect.delimiter)}")
    except Exception as e:
        print(f"  ❌ Greška: {e}")
```

**Output:**

```
🔍 CSV SNIFFER - Automatska detekcija

Comma:
  Sample: name,age,city
Ana,25,Beograd
M...
  ✅ Detektovan delimiter: ','

Semicolon:
  Sample: name;age;city
Ana;25;Beograd
M...
  ✅ Detektovan delimiter: ';'

Tabs:
  Sample: name	age	city
Ana	25	Beograd
M...
  ✅ Detektovan delimiter: '\t'
```

**Wow!** Sniffer je automatski pogadio sve tri! 🎉

---

# 💻 FAZA 3: Praktika - Napravi detect_dialect() (45 min)

## 3.1 Šablonica

```python
import csv
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from csv import Dialect

def detect_dialect(csv_path: Path) -> type["Dialect"]:
    """
    Detektuj CSV format ili padni na csv.excel.

    Args:
        csv_path: Path do CSV fajla

    Returns:
        Dialect (detektovan ili csv.excel ako neuspe)
    """
    # Korak 1: Uzmi prvih 2048 karaktera
    sample = csv_path.read_text(encoding="utf-8", errors="ignore")[:2048]

    # Korak 2: Pokušaj Sniffer
    try:
        detected = csv.Sniffer().sniff(sample)
        print(f"✅ Detektovan: delimiter={repr(detected.delimiter)}")
        return detected
    except Exception as e:
        print(f"⚠️  Sniffer neuspešan ({type(e).__name__}), koristim csv.excel")
        return csv.excel

# TEST sa svim formatima
print("="*60)
print("TESTIRANJE detect_dialect()")
print("="*60)

test_files = [
    Path("data/format_comma.csv"),
    Path("data/format_semicolon.csv"),
    Path("data/format_tabs.csv"),
]

for file_path in test_files:
    print(f"\n📄 {file_path}:")
    dialect = detect_dialect(file_path)

    # Koristi pronađeni dialect za čitanje
    with open(file_path, newline="") as f:
        reader = csv.reader(f, dialect=dialect)
        for i, row in enumerate(reader):
            if i == 0:  # Samo header
                print(f"   Header: {row}")
            else:
                break
```

**Očekivani output:**

```
============================================================
TESTIRANJE detect_dialect()
============================================================

📄 data/format_comma.csv:
✅ Detektovan: delimiter=','
   Header: ['name', 'age', 'city']

📄 data/format_semicolon.csv:
✅ Detektovan: delimiter=';'
   Header: ['name', 'age', 'city']

📄 data/format_tabs.csv:
✅ Detektovan: delimiter='\t'
   Header: ['name', 'age', 'city']
```

## 3.2 Bonus: Test sa Fallback

```python
# Kreiraj "čudan" fajl koji će zbuniti Sniffer
weird_file = Path("data/weird.csv")
weird_file.write_text("a,b,c")  # Samo jedan red - Sniffer će se zbuniti

print("\n" + "="*60)
print("EDGE CASE: Šta ako Sniffer ne uspe?\n")
print("📄 data/weird.csv:")
dialect = detect_dialect(weird_file)
print(f"   Fallback dialect: {repr(dialect.delimiter)}")
```

**Output:**

```
============================================================
EDGE CASE: Šta ako Sniffer ne uspe?

📄 data/weird.csv:
⚠️  Sniffer neuspešan (Error), koristim csv.excel
   Fallback dialect: ','
```

---

# 🎯 Checklist za Dan 3

-   [ ] **FAZA 1:** Kreiraj test CSV fajlove u `data/` folder
-   [ ] **FAZA 2:** Razumem razliku između pogrešnog i ispravljenog readera
-   [ ] **FAZA 2:** Razumem šta su atributi csv.excel (delimiter, quotechar, lineterminator)
-   [ ] **FAZA 2:** Vidim kako Sniffer automatski detektuje 3 različita formata
-   [ ] **FAZA 3:** Napisao sam `detect_dialect()` funkciju i testirao je
-   [ ] **FAZA 3:** Razumem fallback mehanizam (Sniffer → csv.excel)

---

# 📝 Šta da zapamtiš

```python
# 1. CSV može biti u BILO KOJEM formatu:
#    comma, semicolon, tabs, pipes...

# 2. Ako ne znaš format → POGREŠNI REZULTATI (bez greške!)
#    name;age;city  →  ['name;age;city']  ❌

# 3. Rešenja:
#    a) csv.excel - safe fallback, standard format
#    b) csv.Sniffer - automatska detekcija
#    c) detect_dialect() - kombinuj oba

# 4. Uvek koristi try/except + fallback:
try:
    dialect = csv.Sniffer().sniff(sample)
except Exception:
    dialect = csv.excel
```

---

# 🔗 Sledeći korak (Dan 4)

Sutra ćeš:

-   Naučiti `read_rows()` i `clean_rows()` funkcije
-   Integrirati `detect_dialect()` u kompletan workflow
-   Pisati i čitati CSV fajlove sa različitim formatima
-   **Rezultat:** Kompletan `csv_cleaner.py` kod

---

# 💡 Ako se zaglaviš

**Pitanja koja si možda postavio:**

**P: Zašto `encoding="utf-8, errors="ignore"`?**
O: UTF-8 čita sve znakove (€, ć, š). `errors="ignore"` zamenjuje nečitljive znakove sa ''

**P: Šta je `[:2048]`?**
O: Uzmi samo prva 2048 karaktera (dovoljno za Sniffer). Veći fajlovi mogu biti spori

**P: Zašto `newline=""`?**
O: CSV modul needs control over line termination. Bez toga, dobijas prazne redove!

**P: TYPE_CHECKING šta radi?**
O: Python IDE zna tip ali se ne importuje na runtime. Sprečava cirkularni import

---

## 🎬 Pokreni sada

```bash
# Terminal:
cd ~/code/python-automation-lab/python-automation-portfolio/sandbox/basics
python3

# Kopira kod iz Faze 1, 2, 3 i pokreni!
```

**Kreni! 🚀**
