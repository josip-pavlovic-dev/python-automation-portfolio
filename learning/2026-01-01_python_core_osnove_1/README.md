---
type: readme
linked_to: python-automation-portfolio
status: active
phase: python_core_day_1
milestone: python_core_osnove
language: srpski
audience: početnik
generated_by: copilot
date: 2026-01-01
---

# 📘 Python Core Osnove — Dan 1: Mentalni Model & Sintaksa

## 🧭 Svrha foldera

Ovaj folder sadrži **obiman materijal** za prvi dan učenja Python Core osnova. Fokus je na:

1. **Mentalni model Pythona** — Kako Python "razmišlja"
2. **Sintaksa bez zagrada** — Uvlaka, dvotačka, indentation
3. **Dinamičko tipiziranje** — Šta znači da tipovi nisu deklarisani
4. **REPL vežbe** — Praktična iskustva u Python interpretatoru
5. **Sigurne putanje ka produbljivanju** — Kako se izbjegavaju greške početnika

---

## 🗂️ Struktura fajlova

```
2026-01-01_python_core_osnove_1/
├── README.md                          ← Ovaj fajl
├── START_HERE.md                      ← Brz početak (30 min)
├── TEORIJA_mentalni_model.md          ← Detaljno (2h)
├── TEORIJA_tipiziranje_i_None.md      ← Detaljno (1.5h)
├── REPL_VEŽBE_sintaksa_osnove.md      ← Praktična (2h)
├── REPL_VEŽBE_falsy_vs_truthy.md      ← Praktična (1.5h)
├── MINI_PROBLEMI.md                   ← 20+ malih zadataka
├── NAJČEŠĆE_GREŠKE.md                 ← Što izbegavati
├── kickoff.md                         ← Plan za dan
├── summary.md                         ← Refleksija nakon dana
└── chatlog.md                         ← Razgovori sa Copilot-om
```

---

## 🎯 Ciljevi Dana 1

Do kraja ovog dana trebao bi da:

✅ Razumeš **zašto** Python koristi uvlaku (ne zagrade)
✅ Znaš koja je razlika između `None`, `0`, `''`, `[]`
✅ Možeš da prediš šta će kod ispisati BEZ pokretanja
✅ Znaš što je `truthy` i `falsy` vrednovanje
✅ Možeš da pokrneš Python REPL i pisaš jednostavan kod
✅ Razumeš `snake_case` konvenciju

---

## 📊 Vremenska raspodela (8 sati)

| Vreme       | Aktivnost                          | Trajanje | Tip                    |
| ----------- | ---------------------------------- | -------- | ---------------------- |
| 08:00-09:00 | **START_HERE** + kickoff           | 1h       | Orientacija            |
| 09:00-11:00 | **TEORIJA_mentalni_model**         | 2h       | Čitanje + razmišljanje |
| 11:00-12:00 | **REPL_VEŽBE_sintaksa** (FAZA 1-2) | 1h       | Praktika               |
| 12:00-13:00 | **Pauza**                          | 1h       | Odmor                  |
| 13:00-14:30 | **TEORIJA_tipiziranje**            | 1.5h     | Čitanje                |
| 14:30-16:00 | **REPL_VEŽBE_falsy** (FAZA 1-3)    | 1.5h     | Praktika               |
| 16:00-17:00 | **MINI_PROBLEMI** (5-10 zadataka)  | 1h       | Vežba                  |
| 17:00-18:00 | **summary.md** + refleksija        | 1h       | Konsolidacija          |

**Pauziranje:** Svaki sat - 5 min istezanja, nakon 2h - 10 min odmora

---

## 💻 Potrebni alati

-   ✅ Python 3.10+ (`python --version` za proveru)
-   ✅ VS Code sa Python extension
-   ✅ Terminal (PowerShell, WSL, ili Linux)
-   ✅ Tekst editor za REPL vežbe

---

## 🚀 Kako početi

**Opcija 1: Brz pocetak (30 min)**

```bash
cd learning/2026-01-01_python_core_osnove_1
cat START_HERE.md
python3 -i  # Otvori Python REPL
```

**Opcija 2: Detaljno učenje (8h)**

```bash
# Čitaj u redosledu:
1. README.md (ovaj fajl)
2. START_HERE.md
3. kickoff.md
4. TEORIJA_mentalni_model.md
5. REPL_VEŽBE_sintaksa_osnove.md
... nastaviti
```

**Opcija 3: Ako ste iskusniji**

-   Preskočite START_HERE.md
-   Fokusirajte se na NAJČEŠĆE_GREŠKE.md
-   Rešite sve MINI_PROBLEME

---

## 📚 Logika učenja

### Tiers znanja

```
TIER 0 (Sada)
└─ Šta je Python, kako se pokreće REPL
   └─ TEORIJA_mentalni_model.md

TIER 1 (Posle 2h)
└─ Kako Python koristi uvlaku i šta znači
   └─ REPL_VEŽBE_sintaksa_osnove.md

TIER 2 (Posle 4h)
└─ Dinamičko tipiziranje, None, truthy/falsy
   └─ TEORIJA_tipiziranje_i_None.md
   └─ REPL_VEŽBE_falsy_vs_truthy.md

TIER 3 (Posle 6h)
└─ Mini problemi koje možeš da rešiš bez pomoći
   └─ MINI_PROBLEMI.md

TIER 4 (Posle 8h)
└─ Refleksija i pregled
   └─ summary.md
```

---

## 🎓 Key Concepts — Ključni koncepti

| Koncept                   | Objašnjenje                               | Primer                      |
| ------------------------- | ----------------------------------------- | --------------------------- |
| **Uvlaka**                | Python koristi razmake za blokove         | `if x > 5:` + 4 razmaka     |
| **Dvotačka**              | Signalizira početak bloka                 | `if`, `for`, `def`, `class` |
| **Dinamičko tipiziranje** | Tipovi se određuju tokom izvršavanja      | `x = 5`, zatim `x = "pet"`  |
| **None**                  | Odsustvo vrednosti                        | `result = None`             |
| **Truthy/Falsy**          | Kako Python evaluira ne-boolean vrednosti | `if []`: je False           |
| **snake_case**            | Konvencija za imena                       | `my_var`, `calculate_sum()` |

---

## ⚠️ Česte greške POČETNIKA

| Greška                   | Šta se desi        | Kako popraviti                                |
| ------------------------ | ------------------ | --------------------------------------------- |
| Mešanje tabova i razmaka | `IndentationError` | Koristi samo razmake (Settings → Tab Size: 4) |
| Zaboravljena dvotačka    | `SyntaxError`      | `if x > 5` → `if x > 5:`                      |
| `None` vs `''`           | Logička greška     | `None` je odsustvo, `''` je prazna niska      |
| Beskonačna petlja        | Kod se zaglavlio   | Uvek imaj `break` ili promeni uslov           |

---

## 📋 Checklist pre nego što kreneš

-   [ ] Instalirao sam Python 3.10+
-   [ ] Terminal se pokreće bez greške
-   [ ] Vidim Python verziju: `python --version`
-   [ ] Mogu da otvorim REPL: `python` (ili `python3`)
-   [ ] Mogu da izađem iz REPL-a: `exit()`
-   [ ] Razumem šta je folder `learning/`
-   [ ] Spreman sam za 8 sati intenzivnog učenja

---

## 🤝 Ako se zaglavim...

**Šta da uradim ako ne razumem nešto:**

1. **Prvo:** Ponovi lekciju (čitaj sporije, učini pauzu)
2. **Drugo:** Uradi MINI_PROBLEME slične na vežbi
3. **Treće:** Otvori Python REPL i eksperimentiši
4. **Četvrto:** Pitaj Copilota ali sa specifičnim primerom
5. **Peto:** Odedi na sledeću lekciju (ponekad razumevanje dolazi kasnije)

**Nema žurbe - bolje je biti siguran nego brz.**

---

## 📖 Dodatni Resursi (opsiono)

-   Python official: https://python.org/
-   Real Python: https://realpython.com/ (EN)
-   Learn Python the Hard Way: https://learnpythonthehardway.com/ (EN)
-   Automate the Boring Stuff: https://automatetheboringstuff.com/ (EN)

---

## 💪 Motivacija

```
DAN 1 (Sada):      "Šta je to uvlaka? Zašto je važna?"
DAN 2 (Sutra):     "Ok, razumem kontolu toka..."
DAN 3-5 (Nedelja): "Sad mogu da napravim male skripte!"
NEDELJA 2:         "Mogu da čitam kod bez paničnog guglovanja"
MESEC:             "Python Core je moj! Spreman sam za module."
```

**Ključ:** Konzistentnost, ponavljanje, praksa.

---

## 📞 Kontakt & Povratna Informacija

Ako imate pitanja ili sugestije za poboljšanje materijala:

-   Napomeni u `chatlog.md`
-   Napravi issue u projektu
-   Pokrenite diskusiju sa mentorem

---

**Čitaj dalje:** [`START_HERE.md`](START_HERE.md)

Sretno! 🚀
