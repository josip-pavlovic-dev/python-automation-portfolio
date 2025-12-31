---
type: readme
date: 2026-01-07
phase: logging_pytest
tier: 2
---

# 📘 Dan 7: Logging + Pytest Osnove

## 🧭 Svrha

-   Nauči `logging.basicConfig`, nivoe i format
-   Dodaj logger u male skripte (umesto `print`)
-   Pytest: `test_` funkcije, `assert`, pokretanje `pytest -q`
-   Mini integracija: mala funkcija + test + logger

## 🗂️ Struktura

```
2026-01-07_logging_pytest/
├── README.md
├── kickoff.md
├── START_HERE.md
├── TEORIJA_logging.md
├── TEORIJA_pytest_osnove.md
├── REPL_VEŽBE_logging.md
├── REPL_VEŽBE_pytest.md
├── MINI_PROBLEMI_dan7.md
├── summary.md
└── chatlog.md
```

## 🎯 Ciljevi

-   Postavi `basicConfig` sa formatom i nivoom
-   Koristi `logger.debug/info/warning/error/critical`
-   Napišeš 3-4 pytest testa sa `assert`
-   Razumeš failure output i kako ga čitati

## ⏱️ Raspodela (8h)

| Vreme       | Aktivnost             | Trajanje |
| ----------- | --------------------- | -------- |
| 08:00-08:20 | START_HERE            | 20m      |
| 08:20-10:00 | TEORIJA_logging       | 1h40     |
| 10:00-11:00 | REPL logging          | 1h       |
| 11:00-11:20 | Pauza                 | 20m      |
| 11:20-13:00 | TEORIJA_pytest_osnove | 1h40     |
| 13:00-14:00 | REPL pytest           | 1h       |
| 14:00-15:00 | MINI_PROBLEMI_dan7    | 1h       |
| 15:00-16:00 | summary               | 1h       |

## Ključni pojmovi

-   `logging.basicConfig(level=logging.INFO, format=...)`
-   Logger po modulu: `logger = logging.getLogger(__name__)`
-   Pytest: funkcije `test_*`, plain `assert`, fixture `tmp_path` (osnova)
-   Čitanje izlaza `pytest -q`

Kreći od START_HERE, kickoff, pa teorija → REPL → problemi → summary. 🚀
