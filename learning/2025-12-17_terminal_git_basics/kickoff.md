---
type: kickoff
date: 2025-12-17
linked_to: 2025-12-17_terminal_git_basics
language: bilingual
status: init
phase: onboarding
milestone: Terminal + Git Basics
environment: wsl2+vscode
---

# 🚀 Daily Kickoff — 2025-12-17

## ☀️ DAN 1: TERMINAL OSNOVE (8 sati)

### 🌅 FAZA 1: NAVIGATION (09:00-11:00) — 2h

**Cilj:** Mogu da se krećem kroz direktorijume bez razmišljanja

```bash
# KOMANDI KOJE ĆEŠ KORISTITI:
pwd           # Print working directory
cd            # Change directory
ls            # List files
cd ..         # Go to parent folder
cd ~          # Go to home
cd -          # Go to previous folder
ls -la        # List all (including hidden)
ls -l         # Detailed listing
```

**Dnevna Vežba:**

```bash
# 09:00-09:30: Osnove
pwd                           # Gde sam?
cd /tmp                       # Idi u /tmp
ls                           # Šta vidim?
cd ..                        # Idi gore
pwd                          # Gde sam sada?

# 09:30-10:00: Kompleksnija navigacija
cd ~                         # Home folder
cd /home/tvoje_korisnicko_ime
ls -la                       # Sa hidden fajlovima
cd -                         # Nazad

# 10:00-10:30: Test sam/provjera
mkdir ~/test_terminal        # Kreiraj test folder
cd ~/test_terminal           # Idi tamo
pwd                          # Proveri
cd /tmp && pwd               # Kombinuj komandi

# 10:30-11:00: Ponavljanje
# Ponovite sve bez gledanja u tutorial
```

**Očekivani Output:**

```
/tmp
/
/home/tvoje_korisnicko_ime
/tmp
```

---

### 🌤️ FAZA 2: FILE OPERATIONS + READING (11:00-14:00) — 3h

**Cilj:** Kreiram, brišem, čitam fajlove kao prirodno

```bash
# KREIRANJE
mkdir folder_name             # Kreiraj folder
touch file.txt               # Kreiraj prazan fajl
echo "sadržaj" > file.txt    # Kreiraj sa sadržajem

# BRISANJE
rm file.txt                  # Obriši fajl
rm -r folder_name            # Obriši folder (sa sadržajem)

# KOPIRANJE
cp file.txt copy.txt         # Kopiraj fajl
cp -r folder copy_folder     # Kopiraj folder

# PREBACIVANJE
mv file.txt new_name.txt     # Preimenuj
mv file.txt /tmp/            # Prebaci folder

# ČITANJE
cat file.txt                 # Ceo fajl
head -n 10 file.txt          # Prvih 10 linija
tail -n 5 file.txt           # Poslednjih 5 linija
less file.txt                # Paging (q za izlaz)
wc -l file.txt               # Broj linija
```

**Dnevna Vežba:**

```bash
# 11:00-11:45: Kreiranje i brisanje
cd ~/test_terminal
touch sample.txt
echo "Hello World" > sample.txt
cat sample.txt
cp sample.txt backup.txt
ls -la
rm backup.txt

# 11:45-12:15: RUČAK

# 12:15-13:00: Čitanje fajlova
# Kreiraj veći fajl
for i in {1..100}; do echo "Linija $i" >> big_file.txt; done

head -n 5 big_file.txt       # Prvih 5
tail -n 10 big_file.txt      # Poslednjih 10
wc -l big_file.txt           # Ukupno linija

# 13:00-14:00: Kombinovanje
cat big_file.txt | head -n 20
cat big_file.txt | tail -n 5
```

---

### 🌆 FAZA 3: SEARCHING + PIPES + REDIRECTS (14:00-17:00) — 3h

**Cilj:** Kombinujem komandi za napredne zadatke

```bash
# PRETRAGA
grep "keyword" file.txt              # Pronađi liniju
grep -n "keyword" file.txt           # Sa brojem linije
grep -i "keyword" file.txt           # Case insensitive
find . -name "*.txt"                 # Pronađi sve .txt fajlove
find . -type f -name "sample*"       # Fajl sa imenom početi sa sample

# PIPES - Kombinovanje
cat file.txt | grep "word" | wc -l   # Pronađi "word" i broji linije
ls -la | grep ".txt"                 # Listaj samo .txt fajlove
cat big_file.txt | sort | uniq       # Sortiraj i ukloni duplikate

# REDIRECTS - Čuvanje
cat file.txt > output.txt            # Sačuvaj u novi fajl (overwrite)
cat file.txt >> output.txt           # Dodaj na kraj
cat file1.txt file2.txt > combined.txt  # Kombinuj dva fajla
grep "error" logfile.txt > errors.txt   # Sačuvaj samo greške

# STDERR
cat nonexistent.txt 2> error.log     # Sačuvaj greške
cat file.txt 2>&1 | grep "error"     # Kombiniraj stdout i stderr
```

**Dnevna Vežba:**

```bash
# 14:00-14:45: Pretraga
grep "Linija 5" big_file.txt
grep -n "Linija" big_file.txt | head -n 3
find ~/test_terminal -name "*.txt"

# 14:45-15:30: Pipes
cat big_file.txt | grep "Linija" | wc -l
cat big_file.txt | grep "Linija" | head -n 5
cat sample.txt big_file.txt | sort | uniq

# 15:30-16:00: Redirects
grep "Linija" big_file.txt > results.txt
cat results.txt
cat sample.txt >> results.txt

# 16:00-17:00: Kombinovanje (Advanced)
# Pronađi koliko puta se "Linija" pojavljuje
grep "Linija" big_file.txt | wc -l

# Pronađi i sortiraj
cat big_file.txt | grep "Linija" | sort -r | head -n 10

# Čuvaj pipeline rezultate
cat big_file.txt | grep "Linija" | sort | uniq > unique_lines.txt
```

---

### 🌙 VEČE (17:00-21:00) — 4h

**17:00-18:00:** Ponavljanje i vežbe iz `terminal_repl_exercises.md` FAZA 1-3

**18:00-19:00:** Testiranje samog sebe

```bash
# Bez gledanja u tutorial, uradi ovo:
1. Kreiraj folder "my_project"
2. Kreiraj 3 fajla sa teksom
3. Pronađi sve .txt fajlove
4. Kombiniraj sadržaj u jedan fajl
5. Sortiraj i sačuvaj u output.txt
```

**19:00-20:00:** Dodaj poznate komandi u `cheatsheet.md`

**20:00-21:00:** Zapisi svoj progress u `summary.md`

---

## ☀️ DAN 2: GIT + ENVIRONMENT (8 sati)

### 🌅 FAZA 1: GIT BASICS (09:00-12:00) — 3h

**Cilj:** `git init` je kao novi početak projekta

```bash
# KONFIGURACIJA
git config --global user.name "Tvoje Ime"
git config --global user.email "tvoj@email.com"
git config --list                    # Proveri konfiguraciju

# INICIJALIZACIJA
git init                             # Kreiraj novi repository
git status                           # Vidim šta je promenjeno
git add file.txt                     # Spremi promenu (staging)
git add .                            # Spremi sve
git commit -m "Poruka"               # Sačuvaj sa porukom

# ISTORIJA
git log                              # Sve commitove
git log --oneline                    # Kraće
git diff                             # Šta je promenjeno
git show <commit_id>                 # Vidim specifičan commit
```

**Dnevna Vežba:**

```bash
# 09:00-10:00: Setup
cd ~/test_project  # ili gde god da imaš projekat
git init
git config --global user.name "Tvoje Ime"
git config --global user.email "email@example.com"
git status

# 10:00-11:00: Prvi commit
echo "# My Project" > README.md
git add README.md
git commit -m "Initial commit"
git log --oneline

# 11:00-12:00: Više commitova
echo "## Opis" >> README.md
git add README.md
git commit -m "Add description"
git log --oneline
git diff HEAD~1
```

---

### 🌤️ FAZA 2: GITIGNORE + WORKFLOW (12:00-15:00) — 3h

**Cilj:** `.gitignore` sprečava da gajim `__pycache__` u git-u

```bash
# .gitignore primer
# Kreiraj fajl sa sadržajem:
*.pyc
__pycache__/
*.log
.env
venv/
.DS_Store
```

**Dnevna Vežba:**

```bash
# 12:00-12:30: Kreiraj .gitignore
cat > .gitignore << EOF
*.pyc
__pycache__/
*.log
.env
venv/
EOF

# 12:30-13:00: RUČAK

# 13:00-14:00: Kompletan workflow
mkdir logs
echo "Error: 123" > logs/app.log
python3 -c "import sys"  # Kreiraj __pycache__
git status               # Vidiš samo .gitignore
git add .gitignore
git commit -m "Add .gitignore"

# 14:00-15:00: Ponavljanje
# Unesi novu datoteku
echo "# New Feature" > feature.md
git status
git add feature.md
git commit -m "Add feature documentation"
git log --oneline
```

---

### 🌆 FAZA 3: PATHS, ENV, VENV (15:00-18:00) — 3h

**Cilj:** Python venv je spreman za rad

```bash
# ABSOLUTE vs RELATIVE
pwd                                  # /home/korisnik/test_project
ls /home/korisnik/test_project       # Absolute path
ls .                                 # Relative path (trenutno)
ls ..                                # Parent folder
ls ~/test_project                    # ~ = home folder

# ENVIRONMENT VARIABLES
echo $PATH                           # Sve izvršne lokacije
echo $HOME                           # Home folder
echo $USER                           # Tvoje korisničko ime
export MY_VAR="vrednost"             # Kreiraj promenljivu

# PYTHON VENV
python3 -m venv venv                 # Kreiraj virtual environment
source venv/bin/activate             # Aktiviraj (Linux/Mac)
# venv\Scripts\activate              # Aktiviraj (Windows)
pip install -r requirements.txt      # Instaliraj pakete
deactivate                           # Deaktiviraj venv
```

**Dnevna Vežba:**

```bash
# 15:00-15:45: Paths
pwd
cd ..
pwd
cd -
cd ~/test_project
pwd
ls /tmp
ls .
ls ..

# 15:45-16:30: Environment variables
echo $HOME
echo $PATH
echo $USER
echo $PWD

# 16:30-17:30: Venv
python3 -m venv venv
source venv/bin/activate             # AKTIVIRAJ
pip install requests                 # Instaliraj pakete
pip list                             # Vidim instalacije
deactivate                           # Deaktiviraj
python3 -c "import requests"         # Treba greška (venv nije aktivan)

# 17:30-18:00: Git venv
# Venv je već u .gitignore? Proveri
cat .gitignore | grep venv
# Ako nije, dodaj:
echo "venv/" >> .gitignore
git add .gitignore
git commit -m "Ensure venv in gitignore"
```

---

### 🌙 VEČE (18:00-21:00) — 3h

**18:00-19:00:** Kombinovanje (Terminal + Git + Venv)

```bash
# Kompletan workflow:
1. Kreiraj projekat sa git
2. Kreiraj .gitignore
3. Kreiraj venv
4. Aktiviraj venv
5. Instaliraj pakete
6. Git commit svega
```

**19:00-20:30:** Self-test — Možeš li bez tutorial-a?

-   [ ] Kreiraj folder "python_project"
-   [ ] `git init` sa tom porukom
-   [ ] Kreiraj .gitignore (sa `venv/`, `*.pyc`, `__pycache__/`)
-   [ ] Kreiraj venv
-   [ ] Aktiviraj venv
-   [ ] `pip install requests numpy pandas`
-   [ ] Kreiraj `requirements.txt` sa `pip freeze`
-   [ ] Git commit svega

**20:30-21:00:** Zapisi finale resultado u `summary.md`

---

## ✅ Checklist

**Dan 1:**

-   [ ] Mogu da se krećem sa `cd`, `pwd`, `ls`
-   [ ] Mogu da kreiram/brišem fajlove
-   [ ] Mogu da čitam fajlove sa `cat`, `head`, `tail`
-   [ ] Mogu da tražim sa `grep`, `find`
-   [ ] Mogu da kombinujem sa pipes (`|`)
-   [ ] Mogu da čuvam sa redirects (`>`, `>>`)

**Dan 2:**

-   [ ] `git init` i `git config`
-   [ ] `git add`, `git commit`, `git status`
-   [ ] `.gitignore` sa Python patternima
-   [ ] Razumejem `$PATH`, `$HOME`
-   [ ] Venv je kreiram i aktiviram
-   [ ] Mogu sveoliko bez tutorial-a

---

## 🚀 Sutra Ujutru

1. Otvori terminal
2. `pwd` — Proveri gde si
3. Otvori `terminal_repl_exercises.md`
4. FAZA 1 — Kreni!

---

**Spreman? Kreni sutra! 🚀**

---
