---
type: readme
date: 2026-01-03
phase: python_core_day_3
milestone: python_core_osnove
---

# 📘 Python Core Osnove — Dan 3: Kolekcije

## 🧭 Svrha

Danas gradiš čvrst osećaj za kolekcije i kako da ih koristiš bez guglanja:

-   `list`, `tuple`, `set`, `dict` — kada i zašto
-   Slicing i copy vs reference
-   `in`, `len`, membership i pretraga
-   Komprehencije (list/dict/set) kao čitljiviji for
-   Mutabilnost, hashability, tipične greške

---

## 🗂️ Struktura Materijala

```
2026-01-03_python_core_osnove_3/
├── README.md
├── kickoff.md
├── START_HERE.md
├── TEORIJA_liste_tuple_set.md
├── TEORIJA_dict_slicing_comprehensions.md
├── REPL_VEŽBE_liste_tuple_set.md
├── REPL_VEŽBE_dict_comprehensions.md
├── MINI_PROBLEMI_dan3.md
├── summary.md
└── chatlog.md
```

---

## 🎯 Ciljevi Dana 3

✅ Razlikuješ listu, tuple i set po mutabilnosti i duplikatima
✅ Možeš da presečeš listu (`lst[1:4]`) i napraviš kopiju bez bugova
✅ Znaš kada koristiti `dict` i kako iterirati po `items()`
✅ Pišeš list/dict/set comprehension bez gubitka čitljivosti
✅ Znaš gde može da se desi `KeyError`, `IndexError`, `TypeError` (unhashable)

---

## ⏱️ Raspodela (8 sati)

| Vreme       | Aktivnost                           | Trajanje |
| ----------- | ----------------------------------- | -------- |
| 08:00-08:20 | START_HERE + plan                   | 20m      |
| 08:20-10:00 | TEORIJA_liste_tuple_set             | 1h40     |
| 10:00-11:00 | REPL liste/tuple/set                | 1h       |
| 11:00-11:20 | Pauza                               | 20m      |
| 11:20-13:00 | TEORIJA_dict_slicing_comprehensions | 1h40     |
| 13:00-14:00 | REPL dict + comprehensions          | 1h       |
| 14:00-15:00 | MINI_PROBLEMI_dan3                  | 1h       |
| 15:00-16:00 | summary                             | 1h       |

---

## 📚 Ključni Koncepti (brzi pregled)

| Koncept       | Zašto                | Primer                          |
| ------------- | -------------------- | ------------------------------- |
| Lista         | Mutabilna, čuvaj red | `[1, 2, 3]`                     |
| Tuple         | Imutabilan, hashable | `(10, 20)` kao ključ rečnika    |
| Set           | Unikatne vrednosti   | `{1, 2, 2, 3}` → `{1, 2, 3}`    |
| Dict          | Ključ → vrednost     | `{"ime": "Ana"}`                |
| Slicing       | Podsekcija           | `nums[1:4]`, `nums[:]` (kopija) |
| Comprehension | Kraći for            | `[x*x for x in range(5)]`       |

---

## 🔗 Dalje

Kreni od **START_HERE.md**, zatim **kickoff.md** za dnevni plan, pa redom teorija → REPL → problemi → summary. Srećno! 🚀
