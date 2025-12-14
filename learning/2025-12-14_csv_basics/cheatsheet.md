---
type: cheatsheet
topic: CSV basics (csv module)
date: 2025-12-14
linked_to: python-automation-portfolio
language: bilingual
status: draft
difficulty: beginner
audience: myself
recommended_by: codex
---

# 📘 Cheatsheet: CSV basics (csv module)

## ✅ Key Concepts

-   `csv.reader` | čita redove kao liste stringova; koristi `newline=""` pri otvaranju fajla.
-   `csv.DictReader` | čita redove kao dict (ključevi iz header-a); prazne kolone daju `None`.
-   `csv.writer` | piše liste; `writerows` za više redova odjednom; `newline=""` obavezno.
-   `csv.DictWriter` | piše dict-ove uz `fieldnames`; zovi `writeheader()` pre `writerow(s)`.
-   `delimiter` | default je `,`; pogrešan delimiter daje ceo red u jednoj koloni.
-   `encoding` | koristite `utf-8`; pogrešan encoding baca `UnicodeDecodeError`.

---

## 📌 Code Example

```python
from pathlib import Path
import csv

path = Path("sample.csv")

# Read as dicts
with path.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=",")
    rows = list(reader)

# Write as dicts
out_path = Path("out.csv")
headers = reader.fieldnames or []
with out_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)
```

---

## 💡 Explanation

`newline=""` sprečava duple prazne redove na Windows-u i generalno je preporuka uz `csv` modul. `DictReader` koristi header prvi red; ako red ima manje kolona, nedostajući ključevi dobiju `None`. Ako dobiješ ceo red kao jedan string, proveri `delimiter`.

---

## 📥 Related Topics

-   Path vs string putanje | Portabilne putanje, nema `\\` problema
-   Error handling | `FileNotFoundError`, `UnicodeDecodeError`, `ValueError` (DictWriter missing key)
-   Large CSV strategije | Stream čitanje red po red vs `list(reader)`
