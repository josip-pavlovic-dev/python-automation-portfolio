---
type: summary
linked_to: 2025-12-17_terminal_git_basics
status: complete
date: 2025-12-17
topic: Terminal i Git Osnove
author: jole-pavlovic-dev
---

# 📊 SUMMARY — Što si Naučio (Dan 1-2)

## Dan 1: Terminal Osnove (8 sati)

### ✅ FAZA 1: Navigation (2h)

-   `pwd` - Gde sam?
-   `cd /path` - Idi tamo
-   `ls`, `ls -la`, `ls -l` - Vidim što je
-   `cd ..` - Idi gore
-   `cd -` - Nazad gde sam bio

**Rezultat:** Mogu slobodno da se krećem kroz direktorijume ✅

---

### ✅ FAZA 2: File Operations (3h)

-   `mkdir folder` - Kreiraj
-   `touch file.txt` - Kreiraj fajl
-   `cp file.txt copy.txt` - Kopiraj
-   `mv file.txt newname.txt` - Preimenuj
-   `rm file.txt` - Obriši

**Rezultat:** Fajlove kreiram, brišem, kopiram bez problema ✅

---

### ✅ FAZA 3: Reading & Searching (3h)

-   `cat file.txt` - Ceo sadržaj
-   `head -n 10 file.txt` - Prvih 10 linija
-   `tail -n 5 file.txt` - Poslednjih 5 linija
-   `grep "keyword" file.txt` - Pronađi tekst
-   `find . -name "*.txt"` - Pronađi fajl

**Rezultat:** Čitam i pronalazim šta mi treba ✅

---

### ✅ FAZA 4: Pipes & Redirects (Advanced)

-   `cat file.txt | grep "word" | wc -l` - Kombinujem
-   `cat file.txt > output.txt` - Čuvam (overwrite)
-   `echo "text" >> output.txt` - Dodajem (append)
-   `command 2> error.log` - Čuvam greške

**Rezultat:** Pipes su prirodni dio mog workflow-a ✅

---

## Dan 2: Git + Environment (8 sati)

### ✅ FAZA 1: Git Setup (3h)

-   `git config --global user.name "Ime"`
-   `git config --global user.email "email@example.com"`
-   `git init` - Kreiraj repository
-   `git status` - Status
-   `git add file.txt` - Stage
-   `git commit -m "message"` - Commit

**Rezultat:** Git workflow je rutina ✅

---

### ✅ FAZA 2: .gitignore & Workflow (3h)

-   Kreiraj `.gitignore` sa Python patternima:
    -   `venv/`
    -   `*.pyc`
    -   `__pycache__/`
    -   `.env`
-   `git log --oneline` - Vidim istoriju
-   `git diff` - Vidim razlike

**Rezultat:** Znam što da ignorišem i što da commitujem ✅

---

### ✅ FAZA 3: Paths, Environment, Venv (2h)

-   `echo $PATH` - Sve izvršne lokacije
-   `echo $HOME` - Home folder
-   `python3 -m venv venv` - Kreiraj venv
-   `source venv/bin/activate` - Aktiviraj
-   `pip freeze > requirements.txt` - Čuvaj pakete

**Rezultat:** Venv je kreiram i aktiviram bez greške ✅

---

## 🏆 TOP 3 ZA STVARI ZA ZAŠTITU

### 1️⃣ Pipes (`|`) su Moćne za Automatizaciju

```bash
# Pre: Morao sam da čini 4 komande sa intermediate files
cat file.txt > temp1.txt
grep "keyword" temp1.txt > temp2.txt
sort temp2.txt > temp3.txt
uniq temp3.txt > result.txt

# Sada: Sve u jednoj liniji
cat file.txt | grep "keyword" | sort | uniq > result.txt

# Razlika: 3 sekunde vs 5 minuta (sa intermediate fajlovima)
```

---

### 2️⃣ .gitignore Sprečava Bloat (Neželjene Fajlove)

```bash
# Pre: Commitam sve
git add .
# Rezultat: venv/ je 500MB, __pycache__/ je 100MB, .log fajlovi...

# Sada: Sa .gitignore
git add .
# Rezultat: Samo moj kod! venv/ se ignoriše automatski
```

---

### 3️⃣ Venv je Izolacija

```bash
# Pre: pip install zaglavi global environment
pip install requests==1.0
# Ali drugi projekat trebá request==2.0

# Sada: Svaki projekat ima svoj venv
# projekt1/venv - request==1.0
# projekt2/venv - request==2.0
```

---

## 📊 ZNANJE KOJE IMAŠ SADA

| Tema                  | Nivo | Status             |
| --------------------- | ---- | ------------------ |
| **Navigation**        | 100% | ✅ Spreman         |
| **File Ops**          | 100% | ✅ Spreman         |
| **Searching**         | 90%  | ⏳ Treba malo više |
| **Pipes & Redirects** | 85%  | ⏳ Treba malo više |
| **Git Basics**        | 95%  | ✅ Spreman         |
| **.gitignore**        | 90%  | ✅ Spreman         |
| **Venv**              | 100% | ✅ Spreman         |
| **Paths & Env**       | 85%  | ⏳ Reference often |

---

## ✅ Checklist — Šta Možeš SADA

-   [x] Mogu da se krećem sa `cd`, `pwd`, `ls`
-   [x] Mogu da kreiram i brišem fajlove
-   [x] Mogu da čitam fajlove sa `cat`, `head`, `tail`
-   [x] Mogu da pronalazim sa `grep`, `find`
-   [x] Mogu da kombinujem sa pipes i redirects
-   [x] Mogu da inicijalizujem git repository
-   [x] Mogu da commitam sa dobrom porukom
-   [x] Kreiram .gitignore
-   [x] Kreiram Python venv bez problema
-   [x] Razumem `$PATH` i environment varijable

---

## 🚀 Što Radiš Sutra (Dan 3)

```
Dan 3: CSV Osnove (Dialect, Sniffer, csv.excel)
├─ Kreiraj test folder sa terminal (Den 1)
├─ Git init sa .gitignore (Day 2)
├─ Venv sa requirements.txt (Day 2)
└─ Pokreni csv_repl_exercises.md
```

---

## 💪 Motivacija

```
Day 1 Ujutro:    "Šta je `ls -la`?"
Day 1 Veče:      "Mogu da navigiram bez razmišljanja"
Day 2 Ujutro:    "Kako git radi?"
Day 2 Veče:      "Kreiram prvi git repo sa confidence"
Day 3 Ujutro:    "Terminal je kao svoj dom!"
Day 3+:          "Spreman za Python automatizaciju"
```

---

## 🎓 Što Je Ključno Zapamtiti

### Terminal

```bash
pwd              # Gde sam?
cd /path         # Idi tamo
ls -la           # Što je tu?
cat | grep | wc  # Kombinuj
```

---

### Git

```bash
git init         # Kreiraj repo
git add .        # Stage
git commit -m "" # Commit
git log          # Istorija
```

---

### Python

```bash
python -m venv venv      # Kreiraj
source venv/bin/activate # Aktiviraj
pip install -r req.txt   # Instaliraj
```

---

## 📈 Razvoj u toku 48 sati

```
12h-0h (Dan 1, 00:00)    | 🌅 Čitam START_GUIDE + kickoff
3h (Dan 1, 09:00)        | 🖥️ Terminal: Navigation (FAZA 1)
6h (Dan 1, 12:00)        | 📁 Terminal: Files (FAZA 2)
9h (Dan 1, 15:00)        | 🔍 Terminal: Pipes (FAZA 3)
12h (Dan 1, 18:00)       | 🔄 Ponavljanje + Self-test
                         |
24h (Dan 1, 18:00)       | ✅ DAN 1 GOTOV! Terminal je prirodan
24h (Dan 2, 09:00)       | 🐙 Git: Setup + .gitignore (FAZA 1-2)
30h (Dan 2, 15:00)       | 🔧 Environment: Paths + Venv (FAZA 3)
36h (Dan 2, 18:00)       | 🔄 Ponavljanje + Kompletan workflow
                         |
48h (Dan 2, 21:00)       | ✅ DAN 2 GOTOV! Git + Terminal su osnova
```

---

## 🎯 Finalna Poruka

**Šta si ostvario u 48 sati:**

1. **Terminal** - Kao svoj dom

    - Navigacija bez razmišljanja
    - Fajlove kreiram, brišem, čitam
    - Pipes kombinujem za kompleksne zadatke

2. **Git** - Verzija kontrola

    - Init, add, commit sa porukom
    - .gitignore sa Python patternima
    - Historija vidim sa git log

3. **Environment** - Setup
    - Venv kreiram i aktiviram
    - Requirements.txt za distributivnost
    - Paths razumem (absolute vs relative)

**Rezultat:** Fundamentalni alati su u rukama!

---

## ⏭️ Sledećih 12 Dana

```
Dan 3-4:  CSV Osnove (Dialect, Sniffer)
Dan 5-6:  CSV read/write + clean
Dan 7:    Pathlib + Logging
Dan 8-9:  Testing + Error handling
Dan 10-11: Requests + BeautifulSoup
Dan 12-13: Web scraper projekat
Dan 14:   Consolidation
```

**Osnova od Dan 1-2 će biti u svakom danu!**

---

**Spreman za Dan 3? 🚀**

P.S. Kroz 48 sati, terminal i git nisu više "strašni" - trebali su samo praksa i redosled. Isto će biti sa CSV, web scraping-om i svim drugim!

**Sretno na putu do Python Automatizacije! 💪**

---
