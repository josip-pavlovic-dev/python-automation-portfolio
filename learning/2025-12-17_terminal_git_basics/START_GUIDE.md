---
type: guide
title: "🚀 START_GUIDE — Terminal + Git u 48 Sati"
date: 2025-12-17
linked_to: 2025-12-17_terminal_git_basics
status: active
phase: onboarding
milestone: Terminal + Git Basics
environment: wsl2+vscode
---

# 🚀 START_GUIDE — Terminal + Git u 48 Sati

**Cilj:** Naučiti osnove terminala i git-a kroz intenzivan 2-dnevni kurs.

---

## 📋 Šta Ćeš Naučiti

### Dan 1: Terminal Osnove (8 sati)

```
├─ Navigation (pwd, cd, ls)
├─ Files (mkdir, touch, rm, cp, mv)
├─ Reading (cat, head, tail, less)
├─ Searching (grep, find)
├─ Pipes & Redirects (|, >, >>)
└─ Rezultat: Komandna linija je prirodna
```

---

### Dan 2: Git + Setup (8 sati)

```
├─ Git Basics (init, config, status)
├─ Git Workflow (add, commit, log)
├─ .gitignore patterns
├─ Paths & Permissions (chmod, PATH)
└─ Rezultat: Python venv je gotov
```

---

## 📅 Dnevni Raspored (48 SATI)

### ☀️ DAN 1: TERMINAL (8 sati)

#### 🌅 UJUTRO (09:00-12:00) — 3h

```
09:00-09:20  Otvori terminal, `pwd`, `cd`
09:20-09:40  Kreiraj test folder sa `mkdir`
09:40-10:00  Kreiraj fajlove sa `touch`
10:00-10:20  Pročitaj fajlove sa `cat`
10:20-10:40  Koristi `head` i `tail`
10:40-11:00  Koristi `less` za paging
11:00-11:30  PAUZA ☕
11:30-12:00  Prvo vežbe: FAZA 1 (Navigation)
```

---

#### 🌤️ PREDPODNE (12:00-15:00) — 3h

```
12:00-12:30  `grep` osnove
12:30-13:00  `find` sa opcijama
13:00-13:30  RUČAK 🍽️
13:30-14:00  Pipes (|) — kombinovanje komandi
14:00-14:30  Redirects (>, >>) — čuvanje outputa
14:30-15:00  Vežbe: FAZA 2 (Combining commands)
```

---

#### 🌆 POSLE PODNE (15:00-18:00) — 3h

```
15:00-15:30  Scripts - `.sh` fajlovi
15:30-16:00  Permissions - `chmod`
16:00-16:30  Vežbe: FAZA 3 (Advanced exercises)
16:30-17:30  REPETITION - Ponavljaš sve komandi
17:30-18:00  Self-test - Можeš li sve bez guglovanja?
```

---

#### 🌙 VEČE (18:00-21:00) — 3h

```
18:00-18:30  Relaksacija + Čitanje cheatsheet-a
18:30-19:30  Dodatne vežbe iz terminal_repl_exercises.md
19:30-20:30  Eksperimentisanje sa vlastitim komandi
20:30-21:00  Zapisi što si naučio u summary.md
```

---

### ☀️ DAN 2: GIT + ENVIRONMENT (8 sati)

#### 🌅 UJUTRO (09:00-12:00) — 3h

```
09:00-09:30  Git osnove - `git init`
09:30-10:00  Git config - `user.name`, `user.email`
10:00-10:30  .gitignore patterns
10:30-11:00  Kreiraj prvi repository
11:00-11:30  PAUZA ☕
11:30-12:00  Vežbe: Git init + commit
```

---

#### 🌤️ PREDPODNE (12:00-15:00) — 3h

```
12:00-12:30  `git add` - staging
12:30-13:00  `git commit` - sa dobrim porukom
13:00-13:30  RUČAK 🍽️
13:30-14:00  `git status` i `git log`
14:00-14:30  `git diff` - vidi šta je promenjeno
14:30-15:00  Vežbe: Git workflow
```

---

#### 🌆 POSLE PODNE (15:00-18:00) — 3h

```
15:00-15:30  Paths - absolute vs relative
15:30-16:00  Environment variables ($PATH, $HOME)
16:00-16:30  Virtual environment - `python -m venv`
16:30-17:00  Aktivacija venv-a
17:00-17:30  Vežbe: Venv setup
17:30-18:00  Testiranje - pip install & aktivacija
```

---

#### 🌙 VEČE (18:00-21:00) — 3h

```
18:00-18:30  Review - Sve što si naučio
18:30-19:30  Kombinovanje: Terminal + Git + Venv
19:30-20:30  Self-test - Možeš li sve bez guglovanja?
20:30-21:00  Finalni summary - Zapisi u summary.md
```

---

## 🎯 Očekivani Rezultati

### Na Kraju Dana 1

```
✅ Mogu da navigiram sa cd, ls, pwd
✅ Mogu da kreiram/brišem fajlove i foldere
✅ Mogu da čitam fajlove na 4 različita načina
✅ Mogu da tražim sa grep i find
✅ Mogu da kombinujem komandi sa pipes
✅ Razumem stdout, stderr, stdin
```

---

### Na Kraju Dana 2

```
✅ Inicijalizujem prvi git repository
✅ Razumem staging, commits, log
✅ Kreiram dobar .gitignore
✅ Razumem absolute i relative paths
✅ Mogu da kreiram i aktiviram venv
✅ Spreman sam za Python + CSV
```

---

## 📖 Redosled Materijala

```
1. 📌 README.md
2. 🚀 START_GUIDE.md (Ti si ovde -> Ovaj fajl)
3. 📖 kickoff.md - Dnevni plan sa detaljima
4. ✅ tasks.md - Checklist
5. 💡 cheatsheet.md - Quick reference
6. 📝 terminal_repl_exercises.md - DETALJNE VEŽBE (FAZA 1-3)
7. 🧠 chatlog.md - Q&A format
8. 📊 summary.md - Finalni pregled
```

**Preporuka:** Čitaj redom, nemoj da skačeš!

---

## 🔥 Top 5 Komandi Koje Moraš Znati

```bash
# 1. NAVIGATION
pwd                    # Koji folder sam ja?
cd /path               # Idi tamo
cd ..                  # Idi gore

# 2. FILES
ls -la                 # Šta je tu?
mkdir folder           # Napravi folder
touch file.txt         # Kreiraj fajl
rm file.txt            # Obriši
cp file.txt copy.txt   # Kopiraj

# 3. READING
cat file.txt           # Ceo fajl
head -n 10 file.txt    # Prvih 10 linija
tail -n 10 file.txt    # Poslednjih 10
grep "search" file.txt # Pronađi tekst

# 4. PIPES & REDIRECTS
cat file.txt | grep "word" | wc -l  # Combine
cat file.txt > output.txt            # Sačuvaj
echo "text" >> file.txt              # Dodaj

# 5. GIT
git init                             # Kreiraj repo
git add file.txt                     # Spremi promenu
git commit -m "message"              # Sačuvaj sa porukom
git log --oneline                    # Istorija
```

---

## 💡 Saveti Pre Nego Što Počneš

### ✅ DOBRO

-   ✅ Otvori **jedan** terminal
-   ✅ Kreiraj test folder `/tmp/terminal_practice`
-   ✅ Eksperimentiši sa komandi bez straha
-   ✅ Ponavljaj vežbe 2-3 puta
-   ✅ Piši svoje kombinacije komandi

---

### ❌ LOŠE

-   ❌ Ne otvaraj 10 terminala
-   ❌ Ne radiš `rm -rf /` (opasno!)
-   ❌ Ne skačeš između vežbi
-   ❌ Ne čitaš samo teoretski
-   ❌ Ne očekuješ da zapamtiš sve prvi put

---

## 🎬 POČNI SADA

### Sledeći 20 Minuta

```
[ ] Otvori terminal
[ ] Tipkaj: pwd
[ ] Vidi gde si
[ ] Spreman!
```

---

### Narednih 20 Minuta

```
[ ] Čitaj kickoff.md
[ ] Razumej dnevni red
[ ] Spreman za vežbe
```

---

### Narednih 8 Sati

```
[ ] Pokreni terminal_repl_exercises.md FAZA 1
[ ] Vežbaj sve komande
[ ] Ponavljaj dok ne ide bez gledanja
[ ] Eksperimentiši
```

---

## 🚀 RED ČITANJA (VAŽNO!)

```
1. PRVO:   Ovaj START_GUIDE.md (završio si)
2. DRUGO:  kickoff.md (Dnevni plan sa detaljima)
3. TREĆE:  cheatsheet.md (Reference)
4. ČETVRTO: terminal_repl_exercises.md (PRAKSA - 8h)
```

**Nemoj da skačeš redosled!**

---

## 📝 Šta da Zapamtiš

```bash
# 1. NAVIGATION
pwd                    # Koji folder sam ja?
cd /path               # Idi tamo
cd ..                  # Idi gornjeg foldera
ls -la                 # Šta je tu?
mkdir folder           # Napravi folder
touch file.txt         # Kreiraj fajl
rm file.txt            # Obriši
cp file.txt copy.txt   # Kopiraj
cat file.txt           # Ceo fajl
head -n 10 file.txt    # Prvih 10 linija
tail -n 10 file.txt    # Poslednjih 10
grep "search" file.txt # Pronađi tekst
cat file.txt | grep "word" | wc -l  # Combine
cat file.txt > output.txt            # Sačuvaj
echo "text" >> file.txt              # Dodaj
git init                             # Kreiraj repo
git add file.txt                     # Spremi promenu
git commit -m "message"              # Sačuvaj sa porukom
git log --oneline                    # Istorija
```

**Otvori terminal. Tipkaj `pwd`. Kreni! 🖥️**

P.S. Kroz 48 sati, terminal će biti kao tvoj drugi dom. 🏠

---
