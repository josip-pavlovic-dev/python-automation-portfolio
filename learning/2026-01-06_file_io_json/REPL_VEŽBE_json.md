---
type: repl_exercises
time: 60 minutes
topics: [json]
---

# 🧪 REPL Vežbe — JSON

## FAZA 1 — Dump/Load (20 min)

1. Napravi dict i snimi u `data.json` sa `json.dump(..., ensure_ascii=False, indent=2)`.
2. Učitaj nazad sa `json.load` i proveri tip.

## FAZA 2 — String ↔ JSON (15 min)

3. `json.dumps` u string, ispiši; `json.loads` vrati u dict.
4. Napravi listu dict-ova i serijalizuj.

## FAZA 3 — Greške (15 min)

5. Probaj učitati nevalidan JSON, uhvati `json.JSONDecodeError`.
6. Napravi helper `safe_json(path)` koji vraća dict ili `None` na grešku (ali štampa warning).

## FAZA 4 — Mini integracija (10 min)

7. Uzmi CSV sa 2-3 reda (ručno napravi), koristi `csv.DictReader`, konvertuj u listu dict-ova i `json.dumps` sa `ensure_ascii=False`.

✅ Check: znaš dump/load, ensure_ascii, hvataš decode greške.
