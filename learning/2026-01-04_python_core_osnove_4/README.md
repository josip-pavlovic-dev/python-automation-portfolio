---
type: readme
date: 2026-01-04
phase: python_core_day_4
milestone: python_core_osnove
---

# 📘 Dan 4: Funkcije + Type Hints + Importi

## 🧭 Svrha

-   Ovladavanje pisanjem funkcija (parametri, default, \*args/\*\*kwargs)
-   Jasnoća povratnih vrednosti (`return` vs `None`), docstring
-   Type hints kao dokumentacija i pomoć linterima
-   Scope (LEGB) i česte greške sa mutabilnim default-ovima
-   Osnove modula i `import` obrazaca

## 🗂️ Struktura

```
2026-01-04_python_core_osnove_4/
├── README.md
├── kickoff.md
├── START_HERE.md
├── TEORIJA_funkcije_parametri.md
├── TEORIJA_type_hints_scope_import.md
├── REPL_VEŽBE_funkcije.md
├── REPL_VEŽBE_import_typehint.md
├── MINI_PROBLEMI_dan4.md
├── summary.md
└── chatlog.md
```

## 🎯 Ciljevi

-   Napišeš funkciju sa default i \*args/\*\*kwargs bez greške
-   Znaš razliku `return x` vs `return None` vs bez `return`
-   Znaš da ne koristiš mutabilni default (`[]`, `{}`)
-   Dodaješ osnovne type hints na funkcije
-   Znaš tri oblika importa i kada koji koristiti

## ⏱️ Raspodela (8h)

| Vreme       | Aktivnost                       | Trajanje |
| ----------- | ------------------------------- | -------- |
| 08:00-08:20 | START_HERE                      | 20m      |
| 08:20-10:00 | TEORIJA_funkcije_parametri      | 1h40     |
| 10:00-11:00 | REPL funkcije                   | 1h       |
| 11:00-11:20 | Pauza                           | 20m      |
| 11:20-13:00 | TEORIJA_type_hints_scope_import | 1h40     |
| 13:00-14:00 | REPL import + hints             | 1h       |
| 14:00-15:00 | MINI_PROBLEMI_dan4              | 1h       |
| 15:00-16:00 | summary                         | 1h       |

## Ključni pojmovi

-   Parametri: positional, keyword, default, \*args, \*\*kwargs
-   Scope: LEGB, `nonlocal`, `global`
-   Type hints: `def f(x: int) -> str:`
-   Import: `import mod`, `from mod import f`, `import mod as m`
-   Mutabilni default = bug (`def f(x=[]): ...`)

Kreći od START_HERE, pa kickoff plan, zatim teorija → REPL → problemi → summary.🚀
