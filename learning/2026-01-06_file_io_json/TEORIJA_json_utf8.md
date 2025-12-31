---
type: lecture
time: 100 minutes
topics: [json, utf8, serialization]
---

# 📖 Teorija: JSON + UTF-8

## 1. JSON ↔ Python

-   JSON object ↔ Python dict
-   JSON array ↔ list
-   string ↔ str, number ↔ int/float, true/false ↔ True/False, null ↔ None

## 2. Učitavanje

```python
import json
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

## 3. Upis

```python
with open("out.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

-   `ensure_ascii=False` da zadrži UTF-8 znakove.
-   `indent=2` za čitljivost.

## 4. string ↔ dict

```python
s = json.dumps(data, ensure_ascii=False)
data2 = json.loads(s)
```

## 5. Greške pri parsiranju

-   `json.JSONDecodeError` kada fajl nije validan JSON.
-   Uvek hvataj specifično ako radiš sa unosima korisnika.

## 6. Primer CSV → JSON (ideja)

```python
import csv, json
from pathlib import Path

rows = []
with open("ulaz.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

Path("out.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
```

## 7. Tipične greške

-   Zaboravljen `encoding` → �
-   Pisanje bez `ensure_ascii=False` → escape `\uXXXX`
-   Nevalidan JSON (zarez na kraju, jednostruki navodnici)

## 8. Mini kontrola

-   Kada koristiš `json.dumps` vs `json.dump`?
-   Kako uhvatiti loš JSON? (`except json.JSONDecodeError`)
-   Zašto `ensure_ascii=False`?

Spreman za REPL JSON vežbe.
