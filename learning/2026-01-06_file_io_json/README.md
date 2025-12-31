---
type: readme
date: 2026-01-06
phase: file_io_json
tier: 2
---

# 📘 Dan 6: File I/O + Pathlib + JSON

## 🧭 Svrha

-   Savladaj rad sa fajlovima (`open` + `with`), razlike tekst/binarno
-   Usvoji `pathlib.Path` umesto `os.path`
-   Nauči `json.load/dump` i UTF-8 disciplinu
-   Mini integracija: CSV → JSON konverzija

## 🗂️ Struktura

```
2026-01-06_file_io_json/
├── README.md
├── kickoff.md
├── START_HERE.md
├── TEORIJA_file_io_pathlib.md
├── TEORIJA_json_utf8.md
├── REPL_VEŽBE_pathlib_file.md
├── REPL_VEŽBE_json.md
├── MINI_PROBLEMI_dan6.md
├── summary.md
└── chatlog.md
```

## 🎯 Ciljevi

-   Koristiš `with open(..., encoding="utf-8")` bez razmišljanja
-   Znaš `Path` metode: `read_text`, `write_text`, `iterdir`, `glob`
-   Učitaš i upišeš JSON sa korektnim encodingom
-   Napraviš malu CSV→JSON skriptu (bez pandas)

## ⏱️ Raspodela (8h)

| Vreme       | Aktivnost               | Trajanje |
| ----------- | ----------------------- | -------- |
| 08:00-08:20 | START_HERE              | 20m      |
| 08:20-10:00 | TEORIJA_file_io_pathlib | 1h40     |
| 10:00-11:00 | REPL pathlib/file       | 1h       |
| 11:00-11:20 | Pauza                   | 20m      |
| 11:20-13:00 | TEORIJA_json_utf8       | 1h40     |
| 13:00-14:00 | REPL json               | 1h       |
| 14:00-15:00 | MINI_PROBLEMI_dan6      | 1h       |
| 15:00-16:00 | summary                 | 1h       |

## Ključni pojmovi

-   `with` kontekst menadžer, `open(..., newline="", encoding="utf-8")`
-   `Path` vs `os.path`, `Path.glob`, `Path.mkdir(exist_ok=True)`
-   JSON ↔ dict/list, `ensure_ascii=False`, `indent=2`

Kreći od START_HERE, zatim kickoff, pa teorija → REPL → problemi → summary. 🚀
