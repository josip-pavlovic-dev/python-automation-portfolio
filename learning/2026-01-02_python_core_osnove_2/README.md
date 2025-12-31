---
type: readme
date: 2026-01-02
phase: python_core_day_2
milestone: python_core_osnove
---

# 📘 Python Core Osnove — Dan 2: Kontrola Toka (Detaljno)

## 🧭 Svrha

Dan 2 je **DUBOKO** zagrevanje u kontroli toka:

-   `if/elif/else` sa kompleksnim uslovima
-   `for` sa `range()`, `enumerate()`, slicing
-   `while` sa naprednim pattern-ima
-   `break`, `continue`, `pass`
-   Kombinovanje (nested loops, nested conditionals)

---

## 🗂️ Struktura Materijala

```
2026-01-02_python_core_osnove_2/
├── README.md                          ← Ovaj fajl
├── kickoff.md                         ← Plan za dan
├── START_HERE.md                      ← Brz pregled
├── TEORIJA_if_elif_else_detaljno.md   ← 2h čitanja
├── TEORIJA_for_petlja_detaljno.md     ← 2h čitanja
├── TEORIJA_while_break_continue.md    ← 1.5h čitanja
├── REPL_VEŽBE_for_range_enumerate.md  ← 2h praktike
├── REPL_VEŽBE_while_advanced.md       ← 1.5h praktike
├── MINI_PROBLEMI_dan2.md              ← 20+ zadataka
├── summary.md                         ← Refleksija
└── chatlog.md                         ← Razgovori
```

---

## 🎯 Ciljevi Dana 2

✅ Razumeš kompleksne uslove (`and`, `or`, `not`)
✅ Znaš sve varijednost `range()` funkcije
✅ Znaš šta je `enumerate()` i kada je koristiti
✅ Možeš da napraviš nested for petlje bez greške
✅ Razumeš `break` i `continue` u svim kontekstima
✅ Možeš da rešiš kompleksnije probleme sa petljama

---

## ⏱️ Raspodela (8 sati)

| Vreme       | Aktivnost                     | Trajanje |
| ----------- | ----------------------------- | -------- |
| 08:00-09:00 | kickoff + START_HERE          | 1h       |
| 09:00-11:00 | TEORIJA if/elif/else detaljno | 2h       |
| 11:00-12:00 | REPL vežbe if/else            | 1h       |
| 12:00-13:00 | PAUZA                         | 1h       |
| 13:00-15:00 | TEORIJA for detaljno          | 2h       |
| 15:00-16:00 | REPL vežbe for                | 1h       |
| 16:00-17:00 | MINI_PROBLEMI                 | 1h       |
| 17:00-18:00 | summary                       | 1h       |

---

## 📚 Ključni Koncepti

| Koncept       | Šta je                             | Primer                                    |
| ------------- | ---------------------------------- | ----------------------------------------- |
| `and`         | Oba uslova mora biti istinito      | `if x > 0 and x < 10:`                    |
| `or`          | Bar jedan uslov mora biti istinito | `if x < 0 or x > 100:`                    |
| `not`         | Negacija                           | `if not x:`                               |
| `in`          | Provera članstva                   | `if 5 in [1,2,5]:`                        |
| `range()`     | Generiše brojeve                   | `range(5)` → 0,1,2,3,4                    |
| `enumerate()` | Indeks + vrednost                  | `enumerate(['a','b'])` → (0,'a'), (1,'b') |
| `break`       | Prekini petlju                     | `if x == 5: break`                        |
| `continue`    | Preskoči                           | `if x % 2: continue`                      |

---

## 🔗 Dalje

Čitaj: **kickoff.md**

Sretno! 🚀
