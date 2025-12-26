---
type: index
date: 2025-12-26
topic: Web Scraper v1 — Navigation
---

# 🗺️ DAN 8 — Materijali Pregled

Ovde vidis sve dostupne materijale za Dan 8 i kako se koriste.

---

## 📚 Fajlovi Objašnjeni

### 1. 🎯 [README.md](./README.md) — START HERE!

**Šta je to?** Pregled celog dana + očekivani rezultati

**Kad ga čitati?** PRVI — na početku dana (5 min)

**Šta sadrži?**

-   Šta radiš danas
-   Očekivani rezultat
-   Struktura materijala
-   Quick reference

**Sledeće:** Otvori [kickoff.md](./kickoff.md)

---

### 2. 🔴 [kickoff.md](./kickoff.md) — PLAN DANA

**Šta je to?** Detaljni timeline sa vremenskom raspodelom

**Kad ga čitati?** DRUGI — nakon README (5 min)

**Šta sadrži?**

-   8-satni timeline sa pauzama
-   3 linije kako da pristupim materijalu
-   Česte greške (izbegni!)
-   Motivacija

**Sledeće:** Čitaj [cheatsheet.md](./cheatsheet.md)

---

### 3. 📖 [cheatsheet.md](./cheatsheet.md) — REFERENCE

**Šta je to?** Quick reference za requests i BeautifulSoup

**Kad ga čitati?** TREĆI — pre nego što počneš vežbe (30 min)

**Šta sadrži?**

-   HTTP osnove
-   Status kodovi
-   Requests primeri (GET, error handling)
-   BeautifulSoup osnove
-   CSS selektori
-   Testiranje sa mock-ima
-   Česti problemi i rešenja

**Kako koristiti?**

-   Čitaj sekcije koje te zanimaju
-   Koristi kao reference tokom rada
-   Ako zaglavim → pronađi relevantnu sekciju

**Sledeće:** Otvori [web_scraper_setup_guide.md](./web_scraper_setup_guide.md)

---

### 4. 🕷️ [web_scraper_setup_guide.md](./web_scraper_setup_guide.md) — GLAVNI MATERIJAL

**Šta je to?** Detaljne vežbe sa korak-po-korak instrukcije

**Kad ga čitati?** ČETVRTI — ovo je main materijal (6h)

**Šta sadrži?**

**FAZA 1** (1.5h) — Requests + BeautifulSoup osnove

-   Instalacija
-   GET zahtev REPL praksa
-   HTML parsing REPL praksa
-   Kombinovani primeri

**FAZA 2** (1.5h) — Project struktura

-   Kreiranje direktorijuma
-   config.py setup
-   requirements.txt
-   Git setup

**FAZA 3** (2h) — Scraper core funkcije

-   scraper.py osnova
-   fetch_page() funkcija
-   Error handling
-   Logging setup

**FAZA 4** (2h) — Testing

-   conftest.py sa fixtures
-   test_scraper_basics.py sa 10+ testova
-   Coverage provera

**Kako koristiti?**

-   Prati sve 4 FAZE redom
-   Kopiraj primere u REPL
-   Uradi sve praktične vežbe
-   Testira posle svake faze

**Sledeće:** Koristi [tasks.md](./tasks.md) kao checklist

---

### 5. ✅ [tasks.md](./tasks.md) — CHECKLIST

**Šta je to?** Daily checklist za tracking napretka

**Kad ga čitati?** TOKOM RADA — kao referenca

**Šta sadrži?**

-   Checklist za FAZU 1
-   Checklist za FAZU 2
-   Checklist za FAZU 3
-   Checklist za FAZU 4
-   Finalni checklist
-   Bonus aktivnosti

**Kako koristiti?**

-   Zaokruži što završiš
-   Pogledaj na kraju svake faze
-   Proveri finalni checklist
-   Git commit na kraju

---

### 6. 💬 [chatlog.md](./chatlog.md) — Q&A

**Šta je to?** Česta pitanja i odgovori

**Kad ga čitati?** KAD ZAGLAVIM — ako imam pitanja

**Šta sadrži?**

-   Requests pitanja (text vs content, status codes, timeout)
-   BeautifulSoup pitanja (select, select_one, get_text)
-   Pytest pitanja (fixtures, caplog, exceptions)
-   Česte greške i rešenja
-   Saveti i trikovi

**Kako koristiti?**

-   Pronađi relevantno pitanje
-   Čitaj odgovor i primer
-   Koristi kod direktno
-   Ako tvoje pitanje nije ovde, pitaj!

---

## 🎯 PREPORUČENI REDOSLED ČITANJA

### Za Prve 30 Minuta

1. ✅ [README.md](./README.md) — 5 min
2. ✅ [kickoff.md](./kickoff.md) — 5 min
3. ✅ [cheatsheet.md](./cheatsheet.md) — 20 min

### Za FAZU 1 (1.5h)

4. 🕷️ [web_scraper_setup_guide.md](./web_scraper_setup_guide.md) — FAZA 1 sekcija
5. ✅ [tasks.md](./tasks.md) — FAZA 1 checklist
6. 💬 [chatlog.md](./chatlog.md) — ako zaglavim

### Za FAZU 2 (1.5h)

7. 🕷️ [web_scraper_setup_guide.md](./web_scraper_setup_guide.md) — FAZA 2 sekcija
8. ✅ [tasks.md](./tasks.md) — FAZA 2 checklist

### Za FAZU 3 (2h)

9. 🕷️ [web_scraper_setup_guide.md](./web_scraper_setup_guide.md) — FAZA 3 sekcija
10. ✅ [tasks.md](./tasks.md) — FAZA 3 checklist

### Za FAZU 4 (2h)

11. 🕷️ [web_scraper_setup_guide.md](./web_scraper_setup_guide.md) — FAZA 4 sekcija
12. ✅ [tasks.md](./tasks.md) — FAZA 4 checklist
13. ✅ [tasks.md](./tasks.md) — FINALIZACIJA checklist

---

## 🚀 QUICK START (Za Impatientne)

Ako si već iskusan sa Python-om:

1. Otvori [cheatsheet.md](./cheatsheet.md) (5 min)
2. Otvori [tasks.md](./tasks.md) (reference)
3. Sledi [web_scraper_setup_guide.md](./web_scraper_setup_guide.md) (korak po korak)
4. Ako zaglavim → pogledaj [chatlog.md](./chatlog.md)

---

## 📁 ŠEMA MATERIJALA

```
learning/2025-12-26_web_scraper_v1/
├── README.md                       ← START HERE
├── kickoff.md                      ← Plan dana
├── cheatsheet.md                   ← Reference (requests + BS4)
├── web_scraper_setup_guide.md     ← GLAVNI MATERIJAL (sve 4 faze)
├── tasks.md                        ← Daily checklist
├── chatlog.md                      ← Q&A i greške
└── INDEX.md                        ← Ovaj fajl
```

---

## 🎓 ŠEME POVEZIVANJA SA PRETHODNIM DANIMA

```
DAN 5: Type Annotations
  └─→ `class ScrapedItem(TypedDict):`  (Dan 8 će koristiti TypedDict)

DAN 6: Pathlib
  └─→ `Path("output") / "data.csv"`  (Dan 8 koristi Path)

DAN 7: Error Handling + Testing
  └─→ `pytest`, `tmp_path`, `caplog`, try/except  (Dan 8 koristi sve)

DAN 8: WEB SCRAPER SETUP
  └─→ Requests, BeautifulSoup, Project struktura, Testiranje
```

---

## 📊 MATERIJAL STATISTIKA

| Fajl                       | Linije   | Trajanje   | Namena    |
| -------------------------- | -------- | ---------- | --------- |
| README.md                  | 150      | 5 min      | Overview  |
| kickoff.md                 | 200      | 5 min      | Timeline  |
| cheatsheet.md              | 500      | 30 min     | Reference |
| web_scraper_setup_guide.md | 800      | 6h         | Glavno    |
| tasks.md                   | 300      | tokom      | Checklist |
| chatlog.md                 | 400      | po potrebi | Q&A       |
| **TOTAL**                  | **2350** | **8h**     | **Dan 8** |

---

## 🔄 KAKO KORISTIŠ MATERIJAL TOKOM DANA

### Primer: Rad sa FAZA 1

```
09:00 — Zapocni dan
├─ Pročitaj README.md (5 min)
├─ Pročitaj kickoff.md (5 min)
└─ Pročitaj cheatsheet.md (20 min)

09:30 — Kreni sa FAZA 1
├─ Otvori web_scraper_setup_guide.md, pronađi FAZA 1
├─ Prati Korak 1.1, 1.2, 1.3, 1.4
├─ Kopiraj primere u REPL
├─ Eksperimentiraj
└─ Kad završiš FAZU 1:
   └─ Zaokruži FAZA 1 u tasks.md

10:45 — Pauza (15 min)

11:00 — Kreni sa FAZA 2
└─ Ista struktura kao FAZA 1

... itd za FAZU 3 i 4

17:30 — DAN 8 GOTOV! ✅
└─ Finalizacija checklist u tasks.md
└─ Git commit
```

---

## 💡 SAVETI KAKO UČITI

1. **Čitaj aktivno** — kopiraj primere u REPL, eksperimentiraj
2. **Ne preskakaj** — čak i ako misliš da znaš, čitaj sekcije
3. **Pracuj FAZE redom** — svaka FAZA gradi na prethodnoj
4. **Testiraj** — pokreni primere, proveri output
5. **Ako zaglavim** — pronađi odgovor u [chatlog.md](./chatlog.md)
6. **Loguj napredak** — zaokruži checklist-e u [tasks.md](./tasks.md)
7. **Commituj često** — git commit nakon svake FAZE

---

## 🎯 OČEKIVANI REZULTAT NA KRAJU

Na kraju Dana 8, trebalo bi:

```bash
# Struktura
projects/01-web-scraper/
├── config.py              ✅
├── scraper.py             ✅
├── requirements.txt       ✅
├── tests/
│   ├── conftest.py       ✅
│   └── test_scraper_basics.py ✅
├── logs/app.log          ✅
└── output/

# Testovi
$ pytest tests/ -v
10+ passed  ✅

# Coverage
$ pytest --cov=scraper tests/
>85% coverage  ✅

# Git
$ git log --oneline
Day 8: Web Scraper Setup Complete  ✅
```

---

## 📞 AKO NEŠTO NEDOSTAJE?

Ako radiš kroz materijal i nešto ti nije jasno:

1. Pronađi relevantnu sekciju u [cheatsheet.md](./cheatsheet.md)
2. Pogledaj [chatlog.md](./chatlog.md) za često pitanja
3. Ako nisu tu → kreiraj issue ili pitaj direktno

---

**Sada — kreni sa [README.md](./README.md)! 🚀**

Malo po malo, korak po korak, biće to brzo. Srećno! 💪

---
