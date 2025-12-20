---
type: readme
date: 2025-12-18
linked_to: python-automation-portfolio
status: ready
---

# 📘 File Types + Type Annotations — Dan 5

**Tema:** Tipska sigurnost sa Type Annotations — Razumevanje CSV/JSON/CLI sa Python Type System
**Datum:** 2025-12-18
**Trajanje:** ~8 sati
**Status:** ✅ Ready to Go

---

## 🎬 BRZI START

**Sutra ujutro (First 10 min):**

1. Otvori: [`kickoff.md`](./kickoff.md) (5 min)
2. Čitaj: [`file_types_annotation_complete_exercises.md`](./file_types_annotation_complete_exercises.md) — INTRO (5 min)

**Narednih 8 sati (Main Learning):**

-   FAZA 1: Osnove Type Annotations (1.5h)
-   FAZA 2: CSV sa Type Annotations (1.5h)
-   FAZA 3: Argparse + CLI sa Tipima (1.5h)
-   FAZA 4-5: JSON + Kompleksne Tipizacije (1.5h)
-   FAZA 6: Integracija sa Tvojim Projektima (1.5h)
-   FAZA 7-8: Best Practices + Vežbe (1h)

---

## 🎯 CILJ DANA

**Što ćeš znati do kraja:**

✅ Šta su Type Annotations i zašto važne
✅ TypedDict za CSV i JSON
✅ Protocol klase za argparse args
✅ Modern Python imports sa `collections.abc`
✅ Kako da koristiš `mypy` za type checking
✅ Refaktorisati postojeći kod sa tipima

---

## 📊 Zašto Type Annotations?

```python
# ❌ BEZ TIPOVA — Linter NEMA POJMA
def process_csv(data):
    return data['name']  # Šta je data? Dict? List? ??

# ✅ SA TIPIMA — Linter ZNA ŠEŠTA
def process_csv(data: dict[str, str]) -> str:
    return data['name']  # OK — name je string
```

**Rezultat:**

-   🐛 Hvatanju greške pre nego što pokreneš kod
-   📖 Kod je samodokumentovan
-   🚀 IDE bolje sugeriše (autocomplete)
-   🏭 Production kod zahteva tipsku sigurnost

---

## 📁 Struktura Foldera

```
2025-12-18_file_types_annotations/
├── 📌 README.md                                     ← Ti si ovde
├── 🚀 kickoff.md                                    ← Start here
├── 📖 file_types_annotation_complete_exercises.md   ← 8h vežbi (GLAVNO)
├── 💡 cheatsheet.md (soon)                         ← Quick reference
├── 📝 chatlog.md (soon)                            ← Q&A
└── 📊 summary.md (soon)                            ← Što si naučio
```

---

## 🔗 Povezani Materijali (MORA DA PROČITAŠ PRE POČETKA)

1. **[scratch/docs/cheatsheet_csv_annotations.md](../../scratch/docs/cheatsheet_csv_annotations.md)** (15 min)

    - CSV sa Type Hints osnove
    - TypedDict primer
    - Path umesto stringova

2. **[scratch/docs/cheatsheet_modern_mypy_pylance.md](../../scratch/docs/cheatsheet_modern_mypy_pylance.md)** (20 min)
    - Moderni Python importi
    - Šta je `from __future__ import annotations`
    - Kada koristiti šta iz `typing` vs `collections.abc`

---

## 💻 Šta Ćeš Praktikovati

| Faza | Tema                         | Rezultat                                |
| ---- | ---------------------------- | --------------------------------------- |
| 1    | Osnove Type Annotations      | `mypy` radi na demo kodu                |
| 2    | CSV sa TypedDict             | `load_csv()` i `write_csv()` tipizovano |
| 3    | Argparse sa Protocol         | `basic_cli.py` refaktorisan             |
| 4-5  | JSON + Kompleksne Tipizacije | Generički tipovi razumljivi             |
| 6    | Integracija                  | `subcommands_cli.py` refaktorisan       |
| 7-8  | Best Practices               | Checklist + Mini projekat               |

---

## 🎓 Predznanje

**Trebalo bi da već znaš:**

-   ✅ Python `if __name__ == "__main__":` (Dan 1)
-   ✅ Argparse + subparsers (Dan 2 - CLI)
-   ✅ CSV reader/writer (Dan 0 - CSV Osnove)
-   ✅ Logging setup (Dan 2 - Logging)
-   ✅ JSON basics (iz cheatsheet)

---

## 🎯 Redosled Čitanja

```
1. ← TI SI OVDE (README.md) — 5 min
2. kickoff.md — 5 min (dnevni plan)
3. file_types_annotation_complete_exercises.md — 8h (GLAVNI RAD)
   └─ Čitaj FAZU PO FAZU, praktikovanjem
4. chatlog.md (sutra) — Q&A ponavljivanje
5. summary.md (sutra) — Što si naučio
```

---

## 🧩 Kako Se Ovo Uklapá U Tvoj Plan?

```
DAN 1-4: Foundation
├─ Terminal (Dan 1-2)
├─ CSV Osnove (Dan 0 — već urađeno)
├─ CLI + Logging (Dan 2)
└─ Type Annotations (DAN 5 — SADA)

DAN 5: ← TI SI OVDE
├─ File Types
├─ Type Annotations
└─ Type Safety za Automation

DAN 6-7: Advanced
├─ Pathlib + File I/O
├─ Testing + Pytest
└─ Error Handling

DAN 8+: PROJEKTI
├─ Web Scraper v1 (sa tipima!)
├─ CSV Cleaner v2
└─ Automation Tools
```

---

## ✨ Šta Će Se Promeniti u Tvojem Kodu?

**Pre (bez tipova):**

```python
def load_users(path):
    # ??? Šta je path? Šta vraćam? ??
    with open(path) as f:
        reader = csv.DictReader(f)
        return list(reader)
```

**Posle (sa tipima):**

```python
def load_users(path: Path) -> list[UserRecord]:
    """Učitaj korisnike sa tipskom sigurnošću"""
    users: list[UserRecord] = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user: UserRecord = {
                'name': row['name'],
                'age': int(row['age']),
                'city': row['city']
            }
            users.append(user)
    return users
```

**Benefiti:**

-   🐛 mypy proverava PRE nego što pokreneš
-   📖 Čitljivo — svako vidi šta je `UserRecord`
-   🚀 IDE sugeriše `.name` i `.age` automatski
-   🏆 Production-ready kod

---

## 🧠 Top 3 Stvari za Pamćenje

1. **Type Annotations nisu runtime** — Python ih ignoriše! ALI Pylance proverava pre nego što pokreneš.
2. **TypedDict je tvoj best friend** — Koristi ga za svi redove iz CSV/JSON
3. **Modern Python:** `list[T]`, `dict[K, V]`, `X | None` (ne `List[T]`, `Dict[K, V]`, `Optional[X]`)

---

## 🚀 KRENI SADA

**Sledeći 5 Minuta:**

-   [ ] Otvori: [`kickoff.md`](./kickoff.md)

**Narednih 30 Minuta:**

-   [ ] Čitaj: [cheatsheet_csv_annotations.md](../../scratch/docs/cheatsheet_csv_annotations.md)
-   [ ] Čitaj: [cheatsheet_modern_mypy_pylance.md](../../scratch/docs/cheatsheet_modern_mypy_pylance.md)

**Narednih 8 Sati:**

-   [ ] Kreni sa: [`file_types_annotation_complete_exercises.md`](./file_types_annotation_complete_exercises.md) — FAZA 1

---

## 📞 Ako se Zaglaviš

1. **Greška u FAZI X?** → Pogledaj error u `mypy` output-u
2. **Ne razumeš TypedDict?** → Vrati se na [cheatsheet_csv_annotations.md](../../scratch/docs/cheatsheet_csv_annotations.md)
3. **Pylance se žali?** → Proveri import — trebaš li `Protocol` iz `typing`?
4. **15+ min zaglavljen?** → Pitaj AI sa konkretnom greskom ili kodom

---

## ✅ Checklist — Šta Si Urađio?

**Dan Završen Kada:**

-   [ ] Završio si sve FAZE 1-8 iz `file_types_annotation_complete_exercises.md`
-   [ ] `mypy --strict sandbox/basics/` - bez greške
-   [ ] Refaktorisao si `basic_cli.py` i `subcommands_cli.py` sa tipima
-   [ ] Razumeš razliku TypedDict vs Protocol
-   [ ] Spreman si za Pathlib + File I/O (Dan 6)

---

## 🎓 Znanje Koje Možeš SADA Koristiti

Završio si Dan 5, imaš:

✅ **Type Safety** — Više nikada ne gubiš vreme na "TypeError: 'NoneType' object is not subscriptable"
✅ **Self-Documenting Code** — Svako zna šta je `UserRecord`
✅ **IDE Power** — Pylance ti sugeriše atribute
✅ **Production Ready** — Tvoj kod je kao u pravim Python projektima
✅ **Spreman za Web Scraper** — Sa tipskom sigurnošću!

---

**Počni sa [`kickoff.md`](./kickoff.md)! 🔥**

---
