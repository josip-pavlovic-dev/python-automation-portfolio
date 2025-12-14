# QUICK START - Python Automation Portfolio

**Za brz start svakog dana!**

---

## 🚀 Kako Početi (Svaki Dan)

### 1. Otvori VS Code

```bash
cd ~/code/python-automation-lab/python-automation-portfolio
code .
```

---

### 2. Aktiviraj Virtual Environment

```bash
cd projects/01-web-scraper
source venv/bin/activate
```

**Znaš da je aktiviran kad vidiš:** `(venv)` u terminalu!

---

### 3. Proveri Python Setup

```bash
python --version  # Treba 3.10+
pip list  # Vidi instalirane pakete
```

---

### 4. Pokreni Scraper (Test)

```bash
python scraper.py
```

---

## 📁 Struktura Repo-a

```
python-automation-portfolio/
├── README.md                      # Portfolio overview (za klijente)
├── learning/                      # Tvoji dnevni materijali
│   ├── DAY_01_KICKOFF.md         # ← POČNI OVDE!
│   └── DAY_01_SUMMARY.md         # Popuni na kraju dana
├── projects/                      # Portfolio projekti
│   └── 01-web-scraper/           # ← TRENUTNI PROJEKAT
│       ├── scraper.py            # Glavni kod
│       ├── config.py             # Settings
│       ├── requirements.txt      # Dependencies
│       ├── README.md             # Projekat dokumentacija
│       ├── output/               # CSV fajlovi (scraped data)
│       ├── tests/                # Unit tests
│       └── venv/                 # Virtual environment
└── docs/                          # Dodatna dokumentacija
```

---

## 🔥 Današnji Fokus (Day 01)

**Fajl:** `learning/DAY_01_KICKOFF.md`

**Plan:**

1. ✅ Setup okruženje
2. ✅ Python refresh
3. ✅ Web scraping basics
4. ✅ Prvi scraper napisan
5. ✅ Git commit

**Gde kodiš:** `projects/01-web-scraper/`

---

## 💻 Česte Komande

### Git Workflow

```bash
git status                        # Proveri šta je promenjeno
git add .                         # Dodaj sve fajlove
git commit -m "opis promene"      # Commit
git push                          # Push na GitHub
git log --oneline -5              # Poslednjih 5 commitova
```

---

### Python

```bash
python scraper.py                 # Pokreni scraper
python -m pytest                  # Pokreni testove (kad budu)
pip install <paket>               # Instaliraj novi paket
pip freeze > requirements.txt     # Sačuvaj dependencies
```

---

### Virtual Environment

```bash
source venv/bin/activate          # Aktiviraj
deactivate                        # Deaktiviraj
```

---

## 🆘 Ako Nešto Pukne

### "ModuleNotFoundError"

```bash
# Reinstaliraj dependencies
pip install -r requirements.txt
```

---

### "Permission denied"

```bash
# Proveri da li je venv aktiviran
source venv/bin/activate
```

---

### "Scraper ne vraća podatke"

```bash
# Testni URL - quotes.toscrape.com
# Proveri internet konekciju
# Vidi da li je sajt dostupan u browseru
```

---

### Ako Zaglaviš 15+ Minuta

**PITAJ AI U VS CODE-U!** To je poenta! 🤖

---

## 📅 Weekly Overview

### Week 1 (Dec 13-20)

**Projekat:** Web Scraper Tool
**Goal:** MVP complete + advanced features

**Day 01:** Setup + osnovni scraper ✅
**Day 02:** CLI arguments + logging
**Day 03:** Class-based refactor + error handling
**Day 04:** Multiple site support
**Day 05:** Testing + documentation
**Day 06:** Polish + deployment prep
**Day 07:** Project 1 COMPLETE! 🎉

---

## 🎯 Dnevna Rutina

**09:00-10:00:** Pregled plana, kickoff za dan
**10:00-13:00:** Deep work session 1 (kodiranje)
**13:00-14:00:** Ručak + pauza
**14:00-17:00:** Deep work session 2 (kodiranje)
**17:00-18:00:** Testing + debugging
**18:00-19:00:** Dokumentacija + git commit
**19:00+:** Opciono - učenje novih koncepata

**Pauze:** Svaka 2h po 10-15min!

---

## 📞 Resources

**Learning Materials:** `learning/` folder
**Current Project:** `projects/01-web-scraper/`
**Portfolio README:** `README.md` (root)

**AI Mentor:** Dostupan u VS Code-u 24/7! Pitaj šta god ti nije jasno.

---

## ✅ Daily Checklist

Pre nego što ugasiš VS Code:

-   [ ] Kod testiran i radi?
-   [ ] Promena commitovana?
-   [ ] Summary fajl popunjen?
-   [ ] Plan za sutra jasan?
-   [ ] Virtual environment deaktiviran?

---

**REMEMBER:** All or nothing! Svaki dan je korak ka prvom klijentu! 💪

**First client goal:** Januar 31, 2026
**First income goal:** Mart 2026 (€500-1000)

**KRENIMO! 🚀**
