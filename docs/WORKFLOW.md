# 🧭 WORKFLOW.md — Radni Tok za Python Automation Portfolio

## 🎯 Cilj fajla

Ovaj dokument opisuje kako radim svakodnevno na svom Python automation portfoliju koristeći VS Code + GitHub Copilot Pro i Copilot za Windows u Edge-u.

---

## 🛠️ Okruženje

-   **Editor:** VS Code (WSL2 + Ubuntu 24.04)
-   **AI Mentori:**
    -   GitHub Copilot Pro (kod review, sugestije, inline pomoć)
    -   Copilot za Windows (Edge sidebar — planiranje, debugging, refleksija)
-   **Repo:** `python-automation-portfolio`
-   **Virtuelno okruženje:** `projects/01-web-scraper/venv`

---

## 📁 Struktura Projekta

```

python-automation-portfolio/
├── learning/ # Dnevni materijali, planovi, refleksije
│ └── 2025-12-14_csv_basics/ # ← TRENUTNI DAN
│     ├── kickoff.md # Plan rada za dan
│     ├── tasks.md # Lista zadataka
│     ├── cheatsheet.md # Tehnička referenca za csv modul
│     ├── summary.md # Refleksija i zaključak nakon dana
│     └── README.md # Pregled dnevnog foldera
│
├── sandbox/ # Eksperimenti i helper skripte
│ └── basics/ # Python osnove, CSV helperi
│     ├── python_refresh.py # Helper funkcije za CSV
│     └── csv_cleaner.py # Mini CSV Cleaner alat
│
├── projects/ # Portfolio projekti
│ └── 01-web-scraper/ # Trenutni projekat
│     ├── scraper.py # Glavni kod web scrapera
│     ├── config.py # Konfiguracija scrapera
│     ├── requirements.txt # Dependencies
│     ├── README.md # Dokumentacija projekta
│     ├── output/ # Scraped CSV fajlovi
│     ├── tests/ # Unit testovi
│     └── venv/ # Virtuelno okruženje
│
├── docs/ # Dodatna dokumentacija
│    ├── ROADMAP_3_MONTHS.md # Ciljevi i timeline
│    └── WORKFLOW.md # ← ovaj fajl
│
├── QUICK_START.md # Brzi start svakog dana
├── README.md # Portfolio overview
└── .gitignore # Git ignore fajl

```

---

## 🚀 Dnevna Rutina

**09:00-10:00** Kickoff + planiranje
**10:00-13:00** Deep work session 1
**13:00-14:00** Pauza
**14:00-17:00** Deep work session 2
**17:00-18:00** Testiranje + debugging
**18:00-19:00** Dokumentacija + commit
**19:00+** Opciono učenje

**Pauze:** Svaka 2h po 10-15min

---

## 🤖 AI Workflow

### GitHub Copilot Pro (VS Code)

-   Inline sugestije dok pišem kod
-   Refaktor i komentari
-   Pokretanje testova i debugging
-   Workspace context za pitanja o codebase-u

### Copilot za Windows (Edge)

-   Planiranje i retrospektive
-   Debugging sesije (kada zaglavim)
-   Pisanje README, commit poruka, refleksija
-   Vizualizacija roadmap-a i dnevnih ciljeva

---

## 📅 Dnevni Kickoff

Koristim `DAILY_KICKOFF_PROMPT.md` template:

```text
Hi! I'm Jole Pavlović, Python automation developer...

**Current Project:** Web Scraper Tool
**Day:** 01 - 14.12.2025
**Today's Goal:** Implement CLI + logging

@file scraper.py
@file config.py
@file DAY_01_KICKOFF.md
```

---

## 🧪 Testiranje i Debugging

-   Pokreni testove: `python -m pytest`
-   Ako scraper ne radi:
    -   Proveri URL
    -   Aktiviraj venv
    -   Pitaj Copilot (Edge) za pomoć

---

## 📈 Praćenje Napretka

-   Svaki dan commitujem sa jasnim porukama
-   Popunjavam `summary.md` na kraju dana
-   Reflektujem u Copilot chatu (Edge)
-   Pratim roadmap ciljeve iz `ROADMAP_3_MONTHS.md`

---

## 🆘 Ako zaglavim

-   Ako ne rešim problem za 15+ min:
    -   Pokrećem debugging sesiju u Edge Copilotu
    -   Koristim `Debugging Session` template
    -   Pitam konkretno: kod, očekivano, greška

---

## 🧠 Motivacija

-   Cilj: prvi klijent do 31.01.2026
-   Fokus: praktični alati za realne probleme
-   AI mentor dostupan 24/7
-   Svaki dan = korak ka slobodi i prihodima

---

```

---

## 🔍 Predlog za pretragu u Edge Copilotu

Pošto si u Edge sidebaru, koristi **Technology** kao odeljak za pretragu. Tu se nalaze sve relevantne stranice o VS Code, Copilot, workspace context i AI integraciji.

---
```
