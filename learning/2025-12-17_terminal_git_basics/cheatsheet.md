---
type: cheatsheet
topic: Terminal + Git Quick Reference
date: 2025-12-17
linked_to: 2025-12-17_terminal_git_basics
language: bilingual
status: draft
difficulty: beginner
audience: myself
recommended_by: codex
environment: terminal, git, python-venv
---

# 💡 CHEATSHEET — Terminal + Git Quick Reference

**Format:** Copy-paste spreman kod
**Korišćenje:** Drži otvoreno pored sebe

---

## 🖥️ TERMINAL CHEATSHEET

### Navigation

```bash
pwd                     # Print working directory (gde sam?)
cd /path/to/folder      # Change directory
cd ..                   # Go to parent folder
cd ~                    # Go to home folder ($HOME)
cd -                    # Go to previous folder
cd /                    # Go to root
ls                      # List files
ls -la                  # List all (sa hidden)
ls -l                   # Long format
ls -lt                  # Sortirano po vremenu
ls -lS                  # Sortirano po veličini
```

---

### File Operations

```bash
# Kreiranje
touch file.txt          # Kreiraj prazan fajl
echo "text" > file.txt  # Kreiraj sa sadržajem
mkdir folder            # Kreiraj folder
mkdir -p a/b/c          # Kreiraj sve foldere
cp file.txt copy.txt    # Kopiraj fajl
cp -r folder/ copy/     # Kopiraj folder

# Prebacivanje & Brisanje
mv file.txt newname.txt # Preimenuj
mv file.txt /tmp/       # Prebaci u folder
rm file.txt             # Obriši fajl
rm -r folder/           # Obriši folder
rm -f file.txt          # Force delete (bez upozorenja)

# Informacije
file file.txt           # Tip fajla
stat file.txt           # Detalji fajla
du -h folder/           # Veličina foldera
du -sh folder/          # Ukupna veličina
du -sh *                # Veličina svega u trenutnom
```

---

### Reading Files

```bash
cat file.txt            # Ceo sadržaj
head -n 10 file.txt     # Prvih 10 linija
tail -n 10 file.txt     # Poslednjih 10 linija
less file.txt           # Paging (q za exit, space za next)
more file.txt           # Stari paging
wc -l file.txt          # Broj linija
wc -w file.txt          # Broj reči
wc file.txt             # Linije, reči, karakteri
```

---

### Searching & Filtering

```bash
grep "keyword" file.txt      # Pronađi liniju
grep -n "keyword" file.txt   # Sa brojem linije
grep -i "keyword" file.txt   # Case insensitive
grep -c "keyword" file.txt   # Broji poklapanja
grep -v "keyword" file.txt   # Invert match (sve osim)
find . -name "*.txt"         # Pronađi po imenu
find . -type f               # Samo fajlovi
find . -type d               # Samo folderi
find . -size +10M            # Veća od 10MB
find . -mtime -7             # Promenjeno prethodnih 7 dana
```

---

### Pipes & Redirects

```bash
# Pipes - Kombinovanje
cat file.txt | grep "word"
cat file.txt | head -n 5 | tail -n 2
cat file.txt | sort | uniq
cat file.txt | sort | uniq -c | sort -rn

# Redirects
cat file.txt > output.txt           # Overwrite
cat file.txt >> output.txt          # Append
echo "text" > file.txt              # Write
echo "text" >> file.txt             # Append

# Combining stdout & stderr
command > output.txt 2>&1           # Svi output
command > out.txt 2> err.txt        # Odvojeni
command 2> /dev/null                # Ignoriši greške

# Input redirection
sort < unsorted.txt > sorted.txt    # Read from stdin
```

---

### Sorting & Counting

```bash
sort file.txt           # Sortiraj linije
sort -r file.txt        # Sortiraj obrnutu
sort -n file.txt        # Numerički
sort -u file.txt        # Sortiraj i ukloni duplikate
uniq file.txt           # Ukloni duplikate (treba presortiran)
uniq -c file.txt        # Broji duplikate
sort file.txt | uniq    # Sortiraj i ukloni
```

---

### Text Processing

```bash
sed 's/old/new/' file.txt           # Zameni prvi old sa new
sed 's/old/new/g' file.txt          # Zameni sve
sed 's/old/new/2' file.txt          # Zameni drugi
sed 'Nd' file.txt                   # Obriši red N
sed 'NMd' file.txt                  # Obriši redove N-M
awk '{print $1}' file.txt           # Print prvi field
awk -F: '{print $1}' file.txt       # Koristi : kao delimiter
```

---

### Permissions

```bash
ls -l file.txt                      # Vidi permissions
chmod 755 file.txt                  # rwx r-x r-x
chmod 644 file.txt                  # rw- r-- r--
chmod +x script.sh                  # Dodaj execute
chmod -x script.sh                  # Ukloni execute
chmod u+rw file.txt                 # User: add read+write
chown user:group file.txt           # Promeni owner
```

---

### System Info

```bash
whoami                  # Koji je korisnik?
hostname                # Ime računara
uname -a                # OS informacije
echo $PATH              # Sve izvršne lokacije
echo $HOME              # Home folder
pwd                     # Trenutni folder
env                     # Sve environment varijable
```

---

## 🐙 GIT CHEATSHEET

### Setup

```bash
git config --global user.name "Tvoje Ime"
git config --global user.email "tvoj@email.com"
git config --list                           # Proveri config
git config --global core.editor "nano"      # Promeni editor
```

---

### Basic Workflow

```bash
git init                    # Kreiraj novi repo
git clone <url>             # Kloniraj repo
git status                  # Što se promenilo?
git add file.txt            # Stage fajl
git add .                   # Stage sve
git commit -m "message"     # Sačuvaj sa porukom
git push                    # Pošalji na remote
git pull                    # Preuzmi sa remote
```

---

### Viewing History

```bash
git log                     # Svi commitovi
git log --oneline           # Kraće
git log --oneline -5        # Poslednjih 5
git log --author="name"     # Po authoru
git log --since="2 weeks ago"  # Noviji od
git log --until="2 weeks ago"  # Stariji od
git log -p                  # Sa razlika (diff)
git log --graph --all --decorate --oneline  # Vizuelno
git show <commit_id>        # Detalji commita
git diff                    # Unstaged promene
git diff --staged           # Staged promene
git diff <commit1> <commit2>  # Između dva commita
```

---

### Staging & Committing

```bash
git add file.txt            # Stage jedan fajl
git add .                   # Stage sve
git add *.txt               # Stage svi .txt
git reset file.txt          # Unstage fajl
git reset                   # Unstage sve
git commit -m "msg"         # Commit sa porukom
git commit -a -m "msg"      # Stage & commit
git commit --amend          # Promeni prethodni commit
git commit --amend --no-edit # Dodaj fajl bez promene poruke
```

---

### Branching

```bash
git branch                  # Vidim grane
git branch -a               # Sve grane (lokalne + remote)
git branch feature          # Kreiraj granu
git checkout feature        # Idi na granu
git checkout -b feature     # Kreiraj i idi
git merge feature           # Spoji granu
git branch -d feature       # Obriši granu
git branch -D feature       # Silno obriši
```

---

### Undoing Changes

```bash
git restore file.txt        # Vrati prethodnu verziju
git restore --staged file.txt  # Unstage
git revert <commit_id>      # Napravi novi commit koji poništava
git reset --soft HEAD~1     # Undo commit, čuva promene
git reset --hard HEAD~1     # Undo commit, briše promene
```

---

### Remote

```bash
git remote                  # Vidi sve remotove
git remote -v               # Sa URL-ovima
git remote add origin <url> # Dodaj remote
git remote remove origin    # Ukloni remote
git push origin main        # Pošalji granu
git pull origin main        # Preuzmi granu
git fetch                   # Preuzmi bez merge-a
```

---

### .gitignore Pattern

```
*.pyc                       # Sve .pyc fajlove
__pycache__/                # Ceo folder
*.log                       # Sve .log fajlove
.env                        # .env fajl
venv/                       # Virtual environment
*.swp                       # Vim swap files
.DS_Store                   # Mac files
build/                      # Build folder
dist/                       # Distribution folder
*.egg-info/                 # Python egg info
.pytest_cache/              # Pytest cache
.coverage                   # Coverage report
```

---

## 🐍 PYTHON VENV CHEATSHEET

```bash
# Kreiranje
python3 -m venv venv        # Kreiraj virtual env
python -m venv venv         # (Na nekim sistemima)

# Aktivacija
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows (CMD)
. venv/bin/activate         # Linux/Mac (alternativa)

# Verifikacija
which python                # Trebalo bi venv/bin/python
pip --version               # Trebalo bi venv verzija

# Paketi
pip install requests        # Instaliraj paket
pip install -r requirements.txt  # Instaliraj iz fajla
pip list                    # Vidim instalacije
pip freeze > requirements.txt   # Sačuvaj u fajl
pip uninstall requests      # Deinstaliraj

# Deaktivacija
deactivate                  # Deaktiviraj venv
```

---

## 📌 ČESTA KOMBINOVANJA

```bash
# Pronađi sve Python fajlove sa "test" u kodu
find . -name "*.py" | xargs grep "test"

# Broji linije Python koda
find . -name "*.py" | xargs wc -l | tail -1

# Pronađi sve .log fajlove i obriši
find . -name "*.log" -delete

# Pronađi modifikovane fajlove poslednje 24h
find . -type f -mtime -1

# Sortiraj fajlove po veličini (najveći prvi)
ls -lS

# Pronađi top 10 najvećih fajlova
find . -type f -exec ls -lh {} + | sort -k5 -hr | head -10

# Pronađi tekst u svim fajlovima
grep -r "search_text" .

# Pronađi sa određenim ekstenzija
find . -name "*.py" -o -name "*.txt"
```

---

## 🚀 Prvo što Radiš sa Novim Projektom

```bash
# 1. Setup Git
git init
git config user.name "Ime"
git config user.email "email@example.com"

# 2. Kreiraj .gitignore
echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".env" >> .gitignore

# 3. Kreiraj venv
python3 -m venv venv
source venv/bin/activate

# 4. Prvi commit
git add .gitignore
git commit -m "Initial commit"

# 5. Spreman za rad
pip install requests
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add requirements"
```

---

**Čuvaj ovaj cheatsheet! 📌**

---
