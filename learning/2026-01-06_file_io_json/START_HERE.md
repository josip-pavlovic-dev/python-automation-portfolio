---
type: quick_start
time: "30 min"
---

# ⚡ 30-Min Start — Dan 6: File I/O + JSON

## Brzi modeli

-   Koristi `with open(path, mode, encoding="utf-8")` → auto zatvaranje
-   `Path` je moderniji od `os.path`; koristi `Path("data/file.txt")`
-   JSON = dict/list serijalizacija; `json.load` iz fajla, `json.dump` u fajl

## Warmup (REPL)

```python
from pathlib import Path

p = Path("demo.txt")
p.write_text("hello", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
```

```python
import json
sample = {"ime": "Ana", "god": 30}
with open("sample.json", "w", encoding="utf-8") as f:
    json.dump(sample, f, ensure_ascii=False, indent=2)
```

✅ Spreman; idi na kickoff.

## Hintovi za rad (tvoj nivo)

-   Pathlib: `Path("demo.txt").write_text(..., encoding="utf-8")`, zatim `read_text` da potvrdiš sadržaj.
-   Mode i encoding: namerno otvori sa pogrešnim encodingom da vidiš grešku i zapamtiš zašto `encoding="utf-8"`.
-   JSON: koristi `json.dumps(..., ensure_ascii=False, indent=2)` u REPL-u, zatim `json.loads` da proveriš runde trip.
-   Mini CSV→JSON: pročitaj male CSV redove, konvertuj u listu dict-ova, upiši u JSON; posle svakog koraka otvori fajl i proveri.
