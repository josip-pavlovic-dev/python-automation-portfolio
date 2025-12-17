---
type: tasklist
linked_to: 2025-12-17_terminal_git_basics
status: in_progress
date: 2025-12-17
topic: TERMINAL + GIT BASICS
---

# ✅ TASKS — 48-HOURS CHECKLIST

**Status:** Pravim svoju rutinu
**Format:** Čekboxi za svaki zadatak
**Rezultat:** Mogu bez tutorial-a

---

## 📅 DAN 1: TERMINAL (8 SATI)

### 🌅 UJUTRO (09:00-12:00) — NAVIGATION

-   [ ] Otvorim terminal i vidim `$` ili `#` prompt
-   [ ] Tipkam `pwd` i vidim gde sam
-   [ ] Kreiram test folder: `mkdir ~/test_terminal`
-   [ ] Navigiram sa `cd ~/test_terminal`
-   [ ] Proverim sa `pwd` - trebalo bi `/home/korisnik/test_terminal`
-   [ ] Navigiram sa `cd ..` i `cd ~`
-   [ ] Koristim `ls`, `ls -l`, `ls -la`
-   [ ] Razumem razliku između them
-   [ ] Vežbam `cd -` (nazad)
-   [ ] ✅ REZULTAT: Mogu slobodno da se krećem

---

### 🌤️ PREDPODNE (12:00-15:00) — FILE OPERATIONS

-   [ ] Kreiram fajl: `touch sample.txt`
-   [ ] Kreiram sa sadržajem: `echo "Hello" > sample.txt`
-   [ ] Čitam sa `cat sample.txt`
-   [ ] Kreiram veliki fajl (100+ linija) sa `for` loop-om
-   [ ] Koristim `head -n 10` i `tail -n 5`
-   [ ] Prebrojavam linije sa `wc -l`
-   [ ] Kopiram fajl: `cp sample.txt backup.txt`
-   [ ] Preimenujem: `mv backup.txt renamed.txt`
-   [ ] Brišem: `rm renamed.txt`
-   [ ] ✅ REZULTAT: Mogu sa fajlovima bez greške

---

### 🌆 POSLE PODNE (15:00-18:00) — PIPES & REDIRECTS

-   [ ] Tražim sa `grep "Linija" big_file.txt`
-   [ ] Pronalazim fajlove sa `find . -name "*.txt"`
-   [ ] Kombinujem: `cat file.txt | head -n 5`
-   [ ] Kombinujem: `cat file.txt | grep "word" | wc -l`
-   [ ] Čuvam output: `cat file.txt > output.txt`
-   [ ] Dodajem na kraj: `echo "tekst" >> output.txt`
-   [ ] Sortiranje: `sort file.txt | uniq`
-   [ ] Pipes sa 3+ komandi: `cat file.txt | grep "x" | sort | uniq`
-   [ ] ✅ REZULTAT: Pipes i redirects su prirodni

---

### 🌙 VEČE (18:00-21:00) — PONAVLJANJE + TEST

-   [ ] Čitam `terminal_repl_exercises.md` FAZA 1-3
-   [ ] Ponavljam sve vežbe DRUKI PUT (bez gledanja)
-   [ ] Self-test (bez tutorial-a):
    -   [ ] Kreiram folder "my_work"
    -   [ ] Kreiram 3 fajla sa tekstom
    -   [ ] Pronalazim sve fajlove sa `.txt` ekstenzijom
    -   [ ] Kombinijem sadržaj u jedan fajl
    -   [ ] Sortiram i čuvam u `output.txt`
-   [ ] ✅ REZULTAT: Sve bez gledanja - GOTOV DAN 1

---

## 📅 DAN 2: GIT + ENVIRONMENT (8 SATI)

### 🌅 UJUTRO (09:00-12:00) — GIT BASICS

-   [ ] Postavljam `git config user.name` i `user.email`
-   [ ] Kreiram projekt folder: `mkdir my_project && cd my_project`
-   [ ] Inicijalizujem git: `git init`
-   [ ] Kreiram README: `echo "# My Project" > README.md`
-   [ ] Stageam: `git add README.md`
-   [ ] Commitam: `git commit -m "Initial commit"`
-   [ ] Vidim istoriju: `git log --oneline`
-   [ ] Kreiram više fajlova i commitam ih
-   [ ] Vidim razlike sa `git diff`
-   [ ] ✅ REZULTAT: Git workflow razumem

---

### 🌤️ PREDPODNE (12:00-15:00) — GITIGNORE + VENV

-   [ ] Kreiram `.gitignore` sa:
    -   [ ] `*.pyc`
    -   [ ] `__pycache__/`
    -   [ ] `venv/`
    -   [ ] `*.log`
-   [ ] Stagiram `.gitignore`: `git add .gitignore`
-   [ ] Commitam: `git commit -m "Add .gitignore"`
-   [ ] Kreiram Python venv: `python3 -m venv venv`
-   [ ] Aktiviram venv: `source venv/bin/activate`
-   [ ] Vidim prompt promenu (trebalo bi `(venv)`)
-   [ ] Instaliram paket: `pip install requests`
-   [ ] Kreiram `requirements.txt`: `pip freeze > requirements.txt`
-   [ ] Commitam: `git add requirements.txt && git commit -m "Add requirements"`
-   [ ] ✅ REZULTAT: Venv i .gitignore su rutina

---

### 🌆 POSLE PODNE (15:00-18:00) — PATHS & ENV VARS

-   [ ] Pokazujem absolute path: `/home/korisnik/my_project`
-   [ ] Pokazujem relative path: `.` (trenutno) i `..` (parent)
-   [ ] Vidim `$PATH`: `echo $PATH`
-   [ ] Vidim `$HOME`: `echo $HOME`
-   [ ] Kreiram custom varijablu: `export MY_VAR="vrednost"`
-   [ ] Vidim je: `echo $MY_VAR`
-   [ ] Vidim sve varijable: `env`
-   [ ] Razumem zašto venv menja `$PATH`
-   [ ] Vidim `python` u venv vs außerhalb
-   [ ] ✅ REZULTAT: Paths i env varijable jasne

---

### 🌙 VEČE (18:00-21:00) — KOMBINOVANJE + TEST

-   [ ] Čitam `terminal_repl_exercises.md` DEO 2 (Git)
-   [ ] Self-test - Kompletan workflow bez help-a:
    -   [ ] Kreiram novi folder "python_project"
    -   [ ] `git init` sa config
    -   [ ] Kreiram `.gitignore` sa Python patternima
    -   [ ] Kreiram `venv`
    -   [ ] Aktiviram `venv`
    -   [ ] `pip install requests numpy pandas`
    -   [ ] `pip freeze > requirements.txt`
    -   [ ] Commitam sve
    -   [ ] Vidim `git log --oneline` (trebalo bi 2-3 commita)
-   [ ] Deaktiviram venv: `deactivate`
-   [ ] ✅ REZULTAT: Kompletan workflow radi - GOTOV DAN 2

---

## 🏁 FINALNI TEST (Kraj Dana 2)

Sve bez gledanja u materijale:

```bash
# Test 1: Terminal
1. Kreiraj folder sa 5 .txt fajlova
2. Pronađi fajl sa određenim tekstom
3. Kombiniuj sadržaj i sortiraj
4. Čuvaj u output.txt
5. ✅ Ako radiš - PASS

# Test 2: Git
1. git init projekat
2. Kreiraj .gitignore
3. 3x commit sa raznim porukar
4. git log --oneline (trebalo bi 3)
5. ✅ Ako radiš - PASS

# Test 3: Venv
1. python -m venv venv
2. source venv/bin/activate
3. pip install 3 paketa
4. pip freeze > requirements.txt
5. ✅ Ako radiš - PASS
```

**Ako sve 3 testa PASS → Spreman za Dan 3 (CSV)! 🚀**

---

## 📊 DAILY TRACKING

### DAN 1

```
Vreme: ____:____
Energija: ☐☐☐☐☐ (1-5)
Šta je teško? ___________
Šta je lako? ____________
Napredak: ___%
```

---

### DAN 2

```
Vreme: ____:____
Energija: ☐☐☐☐☐ (1-5)
Šta je teško? ___________
Šta je lako? ____________
Napredak: ___%
```

---

## 🎯 Očekivano Stanje Kraju Dana 2

```
✅ Mogu da se krećem sa cd, ls, pwd
✅ Mogu da kreiram, brišem, čitam fajlove
✅ Mogu da pronalazim sa grep, find
✅ Mogu da kombinujem sa pipes i redirects
✅ Mogu da inicijalizujem git
✅ Mogu da commitam sa dobrom porukom
✅ Kreiram .gitignore
✅ Kreiram venv bez problema
✅ Razumem $PATH, $HOME, env varijable
✅ Skoro sve bez tutorial-a!
```

---

**Popuni checklist-e! 📌**
