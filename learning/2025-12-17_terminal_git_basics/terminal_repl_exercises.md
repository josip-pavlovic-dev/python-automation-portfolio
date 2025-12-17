# 📝 TERMINAL EXERCISES — REPL Ready (3 Faze)

**Format:** Kopiraj & Pokreni u terminal
**Rezultat:** Kroz 8 sati, terminal je kao svoj dom

---

## 🎯 FAZA 1: NAVIGATION & FILE OPERATIONS (2h)

### Setup

```bash
# 1. Kreiraj test folder
mkdir -p ~/terminal_practice
cd ~/terminal_practice
pwd
```

---

### 1.1 Navigation — Understanding Paths

```bash
# Vidim gde sam
pwd
# Očekivani output: /home/korisnik/terminal_practice

# Vidim šta je tu
ls
ls -la

# Ideš u /tmp
cd /tmp
pwd
# Očekivani output: /tmp

# Nazad
cd -
pwd
# Trebalo bi: /home/korisnik/terminal_practice

# Home folder
cd ~
pwd

# Nazad u test folder
cd ~/terminal_practice
pwd
```

---

### 1.2 Creating Files & Folders

```bash
# Kreiraj folder
mkdir project_files
cd project_files

# Kreiraj fajlove
touch file1.txt file2.txt file3.txt
ls -la # Provera sadržaja

# Kreiraj sa sadržajem
echo "Hello World" > greeting.txt
cat greeting.txt

# Kreiraj sa više linija
cat > poem.txt << EOF
Prva linija
Druga linija
Treća linija
EOF

cat poem.txt
```

---

### 1.3 Reading Files

```bash
# Kreiraj test fajl sa 20 linija
for i in {1..20}; do echo "Linija broj $i"; done > numbers.txt

# Čitaj celo
cat numbers.txt

# Prvih 5
head -n 5 numbers.txt

# Poslednjih 5
tail -n 5 numbers.txt

# Paging
less numbers.txt
# Pritisni: space (sledeća strana), q (izlaz)

# Broji linije
wc -l numbers.txt
# Očekivani output: 20 numbers.txt

# Broji reči
wc -w numbers.txt

# Broji karaktere
wc -c numbers.txt
```

---

### 1.4 Copying & Moving

```bash
# Kopiraj fajl
cp numbers.txt backup.txt
ls -la

# Kopiraj folder
cp -r project_files project_backup
ls -la

# Preimenuj (move)
mv backup.txt numbers_backup.txt
ls -la

# Prebaci u drugi folder
mv numbers_backup.txt project_files/
ls -la
ls project_files/
```

---

### 1.5 Deleting

```bash
# Obriši fajl
rm poem.txt
ls -la

# Obriši folder
cd ~/terminal_practice
rm -r project_backup
ls -la

# OPASNO - Nemoj!
# rm -rf /    # NIKAD!
# rm -rf ~/*  # NIKAD!
```

---

### 1.6 Permissions

```bash
# Vidim permissions
ls -la

# Promenim na rwx r-x r-x (755)
chmod 755 file1.txt
ls -la file1.txt

# Promenim na rw- r-- r-- (644)
chmod 644 file2.txt
ls -la file2.txt

# Dodaj execute
chmod +x script.sh

# Ukloni read za ostale
chmod o-r file3.txt
```

---

## 🎯 FAZA 2: SEARCHING, PIPES & REDIRECTS (3h)

### 2.1 Searching Files

```bash
# Kreiraj test data
cat > data.txt << EOF
apple
banana
apple juice
orange
application
EOF

# Pronađi linije sa "apple"
grep "apple" data.txt
# Očekivani output: 3 linije

# Case insensitive
grep -i "APPLE" data.txt

# Sa brojem linije
grep -n "apple" data.txt

# Samo broji
grep -c "apple" data.txt

# Invert - sve osim
grep -v "apple" data.txt
```

---

## 2.2 Finding Files

```bash
# Kreiraj struktur
mkdir -p project/src
mkdir -p project/tests
mkdir -p project/docs
touch project/README.md
touch project/src/main.py
touch project/src/utils.py
touch project/tests/test_main.py
touch project/docs/guide.txt

# Pronađi sve Python fajlove
find project -name "*.py"

# Pronađi sve fajlove sa "test" u imenu
find project -name "*test*"

# Samo direktorijumi
find project -type d

# Samo fajlovi
find project -type f

# Veće od 1MB
find project -size +1M

# Promenjeno u poslednjih 7 dana
find project -mtime -7
```

---

### 2.3 Pipes — Kombinovanje

```bash
# Kreiraj test data
cat > names.txt << EOF
Alice
Bob
Charlie
Alice
David
Bob
Eve
EOF

# Pronađi i broji
grep "Alice" names.txt | wc -l
# Očekivani output: 2

# Sortiraj
cat names.txt | sort

# Sortiraj i ukloni duplikate
cat names.txt | sort | uniq

# Broji duplikate
cat names.txt | sort | uniq -c

# Sortiraj po broju (silazno)
cat names.txt | sort | uniq -c | sort -rn

# Kompleksan pipeline
cat names.txt | grep -i "a" | sort | uniq -c | sort -rn
```

---

### 2.4 Redirects — Čuvanje

```bash
# Kreiraj test fajl
echo "First line" > output.txt

# Overwrite
echo "New content" > output.txt
cat output.txt

# Append
echo "Second line" >> output.txt
cat output.txt

# Kombinuj fajlove
cat data.txt names.txt > combined.txt
cat combined.txt

# Sačuvaj samo poklapanja
grep "apple" data.txt > apples.txt
cat apples.txt

# Sačuvaj greške
ls project nonexistent 2> errors.txt
cat errors.txt

# Sve output (stdout + stderr)
ls project nonexistent 2>&1 > all.txt
```

---

### 2.5 Advanced Searching

```bash
# Kreiraj program file
cat > program.log << EOF
ERROR: Connection failed
INFO: Starting process
ERROR: Timeout
INFO: Process completed
WARNING: Low memory
ERROR: Critical error
EOF

# Pronađi ERROR
grep "ERROR" program.log | wc -l

# Pronađi ERROR i sačuvaj
grep "ERROR" program.log > errors_only.txt

# Pronađi ERROR, sortiraj, broji
grep "ERROR" program.log | sort | uniq -c

# Pronađi sve osim INFO
grep -v "INFO" program.log | wc -l

# Pronađi multiple patterns
grep -E "ERROR|WARNING" program.log
```

---

### 2.6 Text Manipulation

```bash
# Kreiraj CSV data
cat > data.csv << EOF
name,age,city
Alice,25,NYC
Bob,30,LA
Charlie,35,Chicago
EOF

# Sort
sort data.csv

# Sort numerički po drugi koloni
sort -t',' -k2 -n data.csv

# Pronađi i zameni
sed 's/Alice/Anna/g' data.csv

# Obriši red
sed '2d' data.csv

# Print samo prvi field (delimiter :)
awk -F',' '{print $1}' data.csv
```

---

## 🎯 FAZA 3: ADVANCED COMBINATIONS (3h)

### 3.1 Complex Pipelines

```bash
# Kreiraj большой test file
for i in {1..100}; do
  echo "User$((RANDOM % 10)): Action $((RANDOM % 5))"
done > activity.log

# Top 5 most active users
cat activity.log | cut -d':' -f1 | sort | uniq -c | sort -rn | head -5

# Count actions per user
cat activity.log | grep "User1:" | wc -l

# Find all errors and log them
grep "ERROR" *.txt 2>/dev/null > all_errors.log || echo "No errors found"
```

---

### 3.2 Real-World Scenarios

```bash
# Scenario 1: Analyze Python file sizes
find project -name "*.py" -exec ls -lh {} + | awk '{print $9, $5}' | sort -k2 -hr

# Scenario 2: Find and count specific patterns
grep -r "TODO" . 2>/dev/null | wc -l

# Scenario 3: Backup files from last day
find . -name "*.py" -mtime -1 -exec cp {} ./backup/ \;

# Scenario 4: Generate file list
ls -lh | grep "^-" | awk '{print $9, $5}' > file_list.txt

# Scenario 5: Find large files
find . -type f -size +10M -exec ls -lh {} \;
```

---

### 3.3 Script-Like Usage

```bash
# Čuvaj kao commands.sh
cat > commands.sh << 'EOF'
#!/bin/bash
# Count all .py files
echo "Python files:"
find . -name "*.py" | wc -l

# Find TODO comments
echo "TODOs to fix:"
grep -r "TODO" . 2>/dev/null | wc -l

# Show largest files
echo "Largest files:"
find . -type f -exec ls -lh {} \; | sort -k5 -hr | head -5
EOF

# Dodaj execute permission
chmod +x commands.sh

# Pokreni
./commands.sh
```

---

### 3.4 Self-Test — Bez Tutorial-a

```bash
# Kreiraj folder "test_exercise"
mkdir test_exercise
cd test_exercise

# Kreiraj 5 fajlova sa random tekstom
for i in {1..5}; do
  echo "File $i content" > file_$i.txt
done

# ZADACI (bez gledanja gore):

# 1. Pronađi sve .txt fajlove
find . -name "*.txt"

# 2. Broji koliko ima .txt fajlova
find . -name "*.txt" | wc -l

# 3. Pronađi fajlove sa "File" u sadržaju
grep -r "File" .

# 4. Kombinuj sve u jedan fajl
cat *.txt > combined.txt

# 5. Sortiraj combined.txt i čuvaj
sort combined.txt > sorted.txt

# REZULTAT: Ako sve radi - FAZA 3 PASS ✅
```

---

## 📊 OČEKIVANI REZULTATI

### Posle FAZE 1

```
✅ Navigiram sa cd, ls, pwd
✅ Kreiram/brišem fajlove i foldere
✅ Čitam fajlove sa cat, head, tail
✅ Razumem permissions
```

---

### Posle FAZE 2

```
✅ Pronalazim sa grep, find
✅ Kombinujem sa pipes (|)
✅ Čuvam sa redirects (>, >>)
✅ Manipuliram tekst (sort, uniq)
```

---

### Posle FAZE 3

```
✅ Rad sa complex pipelines
✅ Real-world scenarios
✅ Automizacija sa scripts
✅ Sve bez tutorial-a!
```

---

**Kreni sada! 🚀**

---
