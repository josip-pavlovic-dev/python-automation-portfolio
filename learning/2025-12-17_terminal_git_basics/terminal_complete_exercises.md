---
type: exercises
topic: Terminal Praksa — Sve Komande iz Cheatsheet-a
date: 2025-12-17
linked_to: 2025-12-17_terminal_git_basics
language: bilingual
status: active
difficulty: beginner-intermediate
environment: terminal
estimated_time: 4-6 hours
---

# 🎯 Terminal REPL Vežbe — Kompletna Praksa

**Cilj:** Isprobaj SVE komande iz cheatsheet-a kroz praktične vežbe
**Format:** Copy-paste ready kod
**Trajanje:** 4-6 sati (radi u fazama)

---

## 🏁 SETUP — Priprema Test Okruženja (10 min)

### 1. Kreiraj Test Folder

```bash
# Kreiraj folder za vežbe
cd ~
mkdir -p terminal_practice
cd terminal_practice

# Proveri gde si
pwd
# Output: /home/jole-pavlovic-dev/terminal_practice
```

---

### 2. Kreiraj Test Fajlove

```bash
# Kreiraj različite tipove fajlova
touch sample.txt
touch data.csv
touch script.sh
touch notes.md

# Kreiraj sa sadržajem
# Napomena : koristi >> za dodavanje na kraj fajla a ne > koji prepisuje fajl
echo "Hello World" > greeting.txt
echo "Line 1" > multiline.txt # Prva linija u fajlu
echo "Line 2" >> multiline.txt # Dodavanje druge linije u fajl
echo "Line 3" >> multiline.txt # Dodavanje treće linije u fajl

# Proveri
ls -la
```

---

### 3. Kreiraj Folder Strukturu

```bash
# Kreiraj nested foldere
mkdir -p project/{src,tests,docs}
mkdir -p data/{raw,processed}
mkdir -p logs

# Proveri strukturu
tree .
# Ili ako nema tree:
find . -type d # find prikazuje sve foldere
```

---

## 📂 FAZA 1: NAVIGATION (30 min)

### 1.1 Osnovno Kretanje

```bash
# Gde sam?
pwd

# Lista fajlova
ls         # Basic listing
ls -l      # Detaljni listing
ls -la     # Uključi skrivene fajlove
ls -lh     # Human readable
ls -lt     # Sortirano po vremenu
ls -lS     # Sortirano po veličini

# Idi u folder
cd project
pwd

# Vrati se nazad
cd ..
pwd

# Idi u home
cd ~
pwd

# Vrati se na prethodni folder
cd -
pwd

# Idi u root
cd /
pwd
ls

# Vrati se u terminal_practice
cd ~/terminal_practice
```

---

### 1.2 Kreiranje i Brisanje

```bash
# Kreiraj novi folder
mkdir temp_folder
ls -la

# Kreiraj nested foldere odjednom
mkdir -p deep/nested/structure
tree deep  # Ili: find deep -type d, razlika izmedju tree i find je sto tree prikazuje hijerarhiju dok find samo listu

# Obriši prazan folder
rmdir temp_folder

# Kreiraj i obriši sa sadržajem
mkdir test_dir
touch test_dir/file1.txt
touch test_dir/file2.txt
rm -r test_dir # Rekurzivno briše folder sa sadržajem
ls -la
# Razlika između rm i rmdir je što rmdir briše samo prazne foldere, dok rm -r briše foldere sa sadržajem.
```

---

### 1.3 Copy & Move

```bash
# Kopiraj fajl
cp greeting.txt greeting_backup.txt
ls -l greeting* # Izlistava sve fajlove koji počinju sa "greeting"

# Kopiraj folder
cp -r project project_backup # Rekurzivno kopira folder u root folder u kojem se nalazi
ls -la

# Preimenuj fajl
mv greeting_backup.txt hello.txt
ls -l

# Prebaci fajl u folder
mv hello.txt project/
ls project/

# Prebaci nazad
mv project/hello.txt . # "." označava trenutni folder u kojem se nalazimo
ls -la
```

---

## 📄 FAZA 2: FILE OPERATIONS (45 min)

### 2.1 Kreiranje Fajlova

```bash
# Touch - prazan fajl
touch empty.txt
ls -l empty.txt

# Echo - sa sadržajem
echo "Test content" > test.txt
cat test.txt

# Append
echo "More content" >> test.txt
cat test.txt

# Multi-line sa heredoc (heredoc je način da se unese više linija teksta u fajl)
cat > story.txt << EOF # "EOF" označava kraj unosa
Once upon a time
There was a programmer
Who loved the terminal
EOF

cat story.txt
```

---

### 2.2 Čitanje Fajlova

```bash
# Kreiraj test fajl sa više linija (svaka linija je broj od 1 do 100)
seq 1 100 > numbers.txt

# Cat - ceo fajl
cat numbers.txt

# Head - prvih 10
head numbers.txt
head -n 5 numbers.txt
head -n 20 numbers.txt

# Tail - poslednjih 10
tail numbers.txt
tail -n 5 numbers.txt
tail -n 20 numbers.txt

# Less - interaktivno
less numbers.txt
# Tipkaj: space (next page), b (prev), g (start), G (end), q (quit)

# More - stari način
more numbers.txt
# Tipkaj: space (next page), enter (next line), q (quit)

# Brojanje
wc numbers.txt          # Linije, reči, karakteri
# output: 100 100 292 ./numbers.txt -> 100 linija, 100 reči, 292 karaktera
wc -l numbers.txt       # Samo linije
wc -w numbers.txt       # Samo reči
wc -c numbers.txt       # Samo karakteri (karakteri uključuju whitespace)
```

---

### 2.3 CSV Test Fajl

```bash
# Kreiraj CSV
cat > employees.csv << EOF
id,name,age,department,salary
1,Ana,25,IT,50000
2,Marko,30,Sales,45000
3,Petar,28,IT,52000
4,Milica,26,HR,43000
5,Jovana,32,Sales,48000
6,Stefan,29,IT,51000
7,Maja,27,HR,44000
8,Nikola,31,Sales,47000
9,Ivana,24,IT,49000
10,Lazar,33,HR,46000
EOF

# Vidi header
head -n 1 employees.csv

# Vidi prvih 5 redova
head -n 6 employees.csv

# Vidi poslednji red
tail -n 1 employees.csv

# Broji redove
wc -l employees.csv
```

---

## 🔍 FAZA 3: SEARCHING & FILTERING (60 min)

### 3.1 Grep Osnove

```bash
# Pronađi tekst
grep "IT" employees.csv
grep "Sales" employees.csv

# Sa brojem linije
grep -n "IT" employees.csv

# Case insensitive
echo "Hello WORLD" > mixed.txt
grep "world" mixed.txt        # Neće naći
grep -i "world" mixed.txt     # Naći će

# Broji poklapanja (koliko puta se pojavljuje reč)
grep -c "IT" employees.csv

# Invert match (sve osim)
grep -v "IT" employees.csv
```

---

### 3.2 Grep Advanced

```bash
# Rekurzivno po folderima
mkdir -p test_search
echo "Important data" > test_search/file1.txt
echo "Important info" > test_search/file2.txt
echo "Random text" > test_search/file3.txt

grep -r "Important" test_search/

# Sa ekstenzijom
find . -name "*.txt" | xargs grep "Important"

# Multiple patterns
grep -E "IT|Sales" employees.csv
```

### 3.3 Find Komande

```bash
# Po imenu
find . -name "*.txt"
find . -name "*.csv"
find . -name "sample*"

# Po tipu
find . -type f          # Samo fajlovi
find . -type d          # Samo folderi

# Po veličini
find . -size +1k        # Veći od 1KB
find . -size -10k       # Manji od 10KB

# Po vremenu
touch old_file.txt
sleep 2
touch new_file.txt
find . -name "*.txt" -mtime -1   # Promenjeno u poslednjih 24h
find . -name "*.txt" -mmin -5    # Promenjeno u poslednjih 5 min

# Kombinovanje
find . -name "*.txt" -type f -size +0
```

### 3.4 Find sa Akcijama

```bash
# Prikaži sa detaljima
find . -name "*.txt" -ls

# Exec na svaki fajl
find . -name "*.txt" -exec wc -l {} \;

# Delete (OPREZNO!)
touch delete_me.tmp
find . -name "*.tmp" -delete
ls *.tmp  # Neće naći
```

---

## 🔗 FAZA 4: PIPES & REDIRECTS (60 min)

### 4.1 Basic Pipes

```bash
# Pipe u grep
cat employees.csv | grep "IT"

# Multi-pipe
cat employees.csv | grep "IT" | head -n 2

# Sa sort
cat employees.csv | sort
cat employees.csv | sort -r  # Reverse

# Sa wc
cat employees.csv | wc -l
ls -la | wc -l
```

### 4.2 Redirects

```bash
# Output redirect (overwrite)
cat employees.csv > employees_backup.csv
ls -l employees*

# Output redirect (append)
echo "New line" >> employees_backup.csv
tail employees_backup.csv

# Input redirect
sort < employees.csv > employees_sorted.csv
head employees_sorted.csv

# Stderr redirect
ls nonexistent 2> errors.log
cat errors.log

# Kombinuj stdout i stderr
ls . nonexistent > output.log 2>&1
cat output.log

# Ignoriši greške
ls . nonexistent 2> /dev/null
```

### 4.3 Advanced Piping

```bash
# Sort i unique
cat > colors.txt << EOF
red
blue
red
green
blue
yellow
red
EOF

sort colors.txt
sort colors.txt | uniq
sort colors.txt | uniq -c        # Broji duplikate
sort colors.txt | uniq -c | sort -rn  # Top po brojnosti

# Extract kolone
cat employees.csv | cut -d',' -f2     # Samo imena
cat employees.csv | cut -d',' -f2,4   # Imena i departmani

# Head i tail kombinirani
cat employees.csv | head -n 5 | tail -n 3  # Redovi 3-5
```

### 4.4 Tee Command

```bash
# Piše u fajl I prikazuje na ekranu
cat employees.csv | grep "IT" | tee it_employees.txt
cat it_employees.txt

# Append mode
cat employees.csv | grep "Sales" | tee -a it_employees.txt
cat it_employees.txt
```

---

## 📊 FAZA 5: SORTING & COUNTING (45 min)

### 5.1 Sort Osnove

```bash
# Osnovno sortiranje
sort employees.csv

# Reverse
sort -r employees.csv

# Po numerical value
cat > ages.txt << EOF
30
5
100
22
8
EOF

sort ages.txt           # Leksikografski: 100, 22, 30, 5, 8
sort -n ages.txt        # Numerički: 5, 8, 22, 30, 100

# Unique dok sortiraš
sort -u colors.txt
```

### 5.2 Sort sa CSV

```bash
# Sortiraj po koloni (delimiter comma)
sort -t',' -k3 employees.csv        # Po age (3. kolona)
sort -t',' -k5 employees.csv        # Po salary (5. kolona)
sort -t',' -k5 -n employees.csv     # Po salary numerički
sort -t',' -k5 -nr employees.csv    # Po salary numerički reverse
```

### 5.3 Uniq i Counting

```bash
# Kreiraj test fajl sa duplikatima
cat > logs.txt << EOF
ERROR: Connection failed
INFO: Started server
ERROR: Connection failed
WARNING: Low memory
ERROR: Connection failed
INFO: Request processed
ERROR: Timeout
EOF

# Uniq zahteva sortirani fajl
sort logs.txt | uniq

# Broji duplikate
sort logs.txt | uniq -c

# Top greške
sort logs.txt | uniq -c | sort -rn

# Samo unique linije
sort logs.txt | uniq -u
```

### 5.4 Analiza CSV-a

```bash
# Koji departmani postoje?
cat employees.csv | cut -d',' -f4 | sort | uniq

# Broji po departmanima
cat employees.csv | cut -d',' -f4 | sort | uniq -c

# Prosečna plata (treba awk za ovo)
cat employees.csv | awk -F',' 'NR>1 {sum+=$5; count++} END {print sum/count}'

# Najviša plata
cat employees.csv | tail -n +2 | cut -d',' -f5 | sort -n | tail -n 1

# Najniža plata
cat employees.csv | tail -n +2 | cut -d',' -f5 | sort -n | head -n 1
```

---

## 🛠️ FAZA 6: TEXT PROCESSING (60 min)

### 6.1 Sed Basics

```bash
# Replace prva instanca
echo "hello world hello" | sed 's/hello/hi/'
# Output: hi world hello

# Replace sve instance (global)
echo "hello world hello" | sed 's/hello/hi/g'
# Output: hi world hi

# Replace u fajlu (prikaži output)
sed 's/IT/Technology/g' employees.csv

# Replace u fajlu (sačuvaj u novi)
sed 's/IT/Technology/g' employees.csv > employees_modified.csv
head employees_modified.csv

# In-place editing (OPREZNO!)
cp employees.csv employees_backup2.csv
sed -i 's/IT/Tech/g' employees_backup2.csv
grep Tech employees_backup2.csv
```

### 6.2 Sed za Delete

```bash
# Obriši red 2
sed '2d' employees.csv

# Obriši redove 2-4
sed '2,4d' employees.csv

# Obriši poslednji red
sed '$d' employees.csv

# Obriši prazan redove
cat > text_with_blanks.txt << EOF
Line 1

Line 3

Line 5
EOF

sed '/^$/d' text_with_blanks.txt
```

### 6.3 Awk Basics

```bash
# Printaj prvu kolonu
awk '{print $1}' employees.csv

# Printaj više kolona
awk '{print $1, $3}' employees.csv

# Sa custom delimiter
awk -F',' '{print $2}' employees.csv        # Imena
awk -F',' '{print $2, $4}' employees.csv    # Imena i departmani

# Skip header
awk -F',' 'NR>1 {print $2, $5}' employees.csv
```

### 6.4 Awk Filtering

```bash
# Conditional printing
awk -F',' '$5 > 48000 {print $2, $5}' employees.csv    # Plata > 48000

# String match
awk -F',' '$4 == "IT" {print $2}' employees.csv        # IT employees

# Kombinuj
awk -F',' '$4 == "IT" && $5 > 50000 {print $2, $5}' employees.csv

# Računanje
awk -F',' 'NR>1 {sum+=$5} END {print "Total:", sum}' employees.csv
awk -F',' 'NR>1 {sum+=$5; count++} END {print "Average:", sum/count}' employees.csv
```

### 6.5 Cut Command

```bash
# Extract kolone (space delimiter)
echo "one two three four" | cut -d' ' -f1
echo "one two three four" | cut -d' ' -f2,4

# CSV columns
cut -d',' -f1,2 employees.csv              # ID i ime
cut -d',' -f2,4,5 employees.csv            # Ime, dept, salary

# Range
cut -d',' -f1-3 employees.csv              # Kolone 1-3
cut -d',' -f3- employees.csv               # Kolone 3 do kraja
```

---

## 🔐 FAZA 7: PERMISSIONS (30 min)

### 7.1 Čitanje Permisija

```bash
# Detaljni listing
ls -l greeting.txt

# Šta znači: -rw-r--r--
# - = regular file
# rw- = owner (read, write, no execute)
# r-- = group (read only)
# r-- = others (read only)

# Direktorijum
ls -ld project/
# drwxr-xr-x
# d = directory
# rwx = owner (read, write, execute/traverse)
# r-x = group (read, execute)
# r-x = others (read, execute)
```

### 7.2 Chmod Numerical

```bash
# Kreiraj test fajl
echo "#!/bin/bash" > test_script.sh
echo "echo 'Hello'" >> test_script.sh

# Proveri permisije
ls -l test_script.sh
# -rw-r--r-- (644)

# Chmod numerical
chmod 755 test_script.sh
ls -l test_script.sh
# -rwxr-xr-x (755)

# Common modes
chmod 644 test.txt      # rw-r--r-- (text file)
chmod 755 script.sh     # rwxr-xr-x (executable)
chmod 600 secret.txt    # rw------- (private)
chmod 777 public.sh     # rwxrwxrwx (everyone full access)
```

### 7.3 Chmod Symbolic

```bash
# Dodaj execute vlasniku
chmod u+x test_script.sh
ls -l test_script.sh

# Ukloni write od grupe
chmod g-w test_script.sh

# Dodaj read za sve
chmod a+r test.txt

# Kombinuj
chmod u+rw,g+r,o-r test.txt

# Exec samo za owner
chmod u=rwx,g=rx,o=rx script.sh
```

### 7.4 Practical Permissions

```bash
# Make script executable i pokreni
echo "#!/bin/bash" > hello.sh
echo "echo 'Hello from script!'" >> hello.sh
chmod +x hello.sh
./hello.sh

# Recursive chmod
mkdir -p secure_data
touch secure_data/file1.txt
touch secure_data/file2.txt
chmod -R 700 secure_data
ls -la secure_data/

# Test permission denied
chmod 000 test.txt
cat test.txt    # Permission denied
chmod 644 test.txt
cat test.txt    # Radi
```

---

## 🖥️ FAZA 8: SYSTEM INFO (20 min)

### 8.1 Basic Info

```bash
# Ko sam ja?
whoami

# Hostname
hostname

# OS info
uname -a
uname -s    # Kernel name
uname -r    # Kernel release
uname -m    # Machine hardware

# Date i time
date
date "+%Y-%m-%d"
date "+%H:%M:%S"
date "+%Y-%m-%d %H:%M:%S"
```

### 8.2 Environment Variables

```bash
# Prikaži sve
env

# Specific variables
echo $HOME
echo $USER
echo $PATH
echo $SHELL
echo $PWD

# Set custom variable
export MY_VAR="test_value"
echo $MY_VAR

# Add to PATH (temporary)
export PATH=$PATH:/new/path
echo $PATH
```

### 8.3 Disk Usage

```bash
# Disk space
df -h           # Human readable
df -h .         # Current filesystem

# Folder sizes
du -sh *                        # Sve u trenutnom
du -sh project/                 # Jedan folder
du -h project/ | sort -h        # Sortirano

# Find large files
find . -type f -size +1M -ls

# Top 5 largest
du -sh * | sort -hr | head -5
```

---

## 🔄 FAZA 9: ADVANCED COMBINATIONS (60 min)

### 9.1 Real-World Scenarios

```bash
# Scenario 1: Log analiza
cat > app.log << EOF
2025-12-17 10:00:00 INFO Server started
2025-12-17 10:01:23 ERROR Connection failed
2025-12-17 10:02:45 INFO Request processed
2025-12-17 10:03:12 ERROR Timeout
2025-12-17 10:04:56 WARNING Low memory
2025-12-17 10:05:23 ERROR Connection failed
2025-12-17 10:06:01 INFO Request processed
2025-12-17 10:07:45 ERROR Database error
EOF

# Koliko ERROR-a?
grep -c "ERROR" app.log

# Koje greške i koliko puta?
grep "ERROR" app.log | cut -d' ' -f4- | sort | uniq -c | sort -rn

# Poslednje 3 greške
grep "ERROR" app.log | tail -n 3

# Sve osim INFO
grep -v "INFO" app.log
```

---

### 9.2 CSV Manipulation

```bash
# Scenario 2: Analiza employees CSV

# Najviše plaćen po departmanu
for dept in IT Sales HR; do
    echo "=== $dept ==="
    grep "$dept" employees.csv | sort -t',' -k5 -nr | head -n 1
done

# Prosek po departmanu
for dept in IT Sales HR; do
    avg=$(grep "$dept" employees.csv | awk -F',' '{sum+=$5; count++} END {print sum/count}')
    echo "$dept: $avg"
done

# Export samo IT department
grep "IT" employees.csv > it_only.csv
echo "id,name,age,department,salary" > it_with_header.csv
grep "IT" employees.csv >> it_with_header.csv
cat it_with_header.csv
```

---

### 9.3 Batch File Operations

```bash
# Scenario 3: Rename multiple files

# Kreiraj test fajlove
mkdir batch_test
cd batch_test
touch file1.txt file2.txt file3.txt

# Rename sa loop
for f in *.txt; do
    mv "$f" "${f%.txt}_backup.txt"
done
ls

# Vrati nazad
for f in *_backup.txt; do
    mv "$f" "${f%_backup.txt}.txt"
done
ls

cd ..
```

---

### 9.4 Find & Replace u Multiple Files

```bash
# Scenario 4: Update koda

# Kreiraj Python fajlove
mkdir code_update
cat > code_update/file1.py << EOF
import old_module
result = old_function()
EOF

cat > code_update/file2.py << EOF
from old_module import old_function
x = old_function()
EOF

# Find all Python files sa "old_module"
grep -r "old_module" code_update/

# Replace u svim fajlovima
find code_update/ -name "*.py" -exec sed -i 's/old_module/new_module/g' {} \;
grep -r "new_module" code_update/
```

---

### 9.5 Monitoring u Real-Time

```bash
# Scenario 5: Live log monitoring

# Terminal 1: Generiši log
while true; do
    echo "$(date '+%Y-%m-%d %H:%M:%S') Event $(($RANDOM % 100))" >> live.log
    sleep 1
done &

# Uzmi PID za kasnije
LOGGER_PID=$!
echo "Logger PID: $LOGGER_PID"

# Terminal (isti): Prati log
tail -f live.log
# Ctrl+C za stop

# Prati samo ERROR (simulacija)
tail -f live.log | grep --line-buffered "5"

# Cleanup
kill $LOGGER_PID
rm live.log
```

---

## 📈 FAZA 10: PERFORMANCE & OPTIMIZATION (30 min)

### 10.1 Fast Searching

```bash
# Kreiraj veliki fajl
seq 1 100000 > huge.txt

# Time commands
time cat huge.txt > /dev/null
time head -n 1000 huge.txt > /dev/null
time tail -n 1000 huge.txt > /dev/null

# Grep performance
time grep "12345" huge.txt
time grep -F "12345" huge.txt    # Fixed string (brže)
```

---

### 10.2 Parallel Processing

```bash
# Sequential
time for i in {1..5}; do
    sleep 1
    echo "Task $i done"
done

# Parallel (sa background jobs)
for i in {1..5}; do
    (sleep 1; echo "Task $i done") &
done
wait
echo "All done"
```

---

### 10.3 Efficient Pipelines

```bash
# Loše - multiple passes
cat employees.csv | grep "IT" > temp1.txt
cat temp1.txt | sort > temp2.txt
cat temp2.txt | head -n 3
rm temp1.txt temp2.txt

# Dobro - jedan pipeline
cat employees.csv | grep "IT" | sort | head -n 3

# Best - manje komandi
grep "IT" employees.csv | sort | head -n 3
```

---

## ✅ FINALNI TEST (30 min)

### Challenge 1: CSV Analiza

```bash
# Kreiraj kompleksan CSV
cat > sales.csv << EOF
date,product,quantity,price
2025-01-01,Laptop,2,1000
2025-01-01,Mouse,5,50
2025-01-02,Laptop,1,1000
2025-01-02,Keyboard,3,100
2025-01-03,Mouse,10,50
2025-01-03,Laptop,3,1000
EOF

# ZADACI (reši samostalno):
# 1. Koliko ukupno laptopa je prodato?
# 2. Koji proizvod ima najveću ukupnu vrednost?
# 3. Kolika je prosečna cena po produktu?
# 4. Sortiraj po datumu i proizvodu
```

### Challenge 2: Log Processing

```bash
# Kreiraj log fajl
cat > access.log << EOF
192.168.1.1 - - [17/Dec/2025:10:00:00] "GET /index.html" 200
192.168.1.2 - - [17/Dec/2025:10:01:00] "GET /about.html" 200
192.168.1.1 - - [17/Dec/2025:10:02:00] "GET /contact.html" 404
192.168.1.3 - - [17/Dec/2025:10:03:00] "POST /api/data" 500
192.168.1.2 - - [17/Dec/2025:10:04:00] "GET /index.html" 200
192.168.1.1 - - [17/Dec/2025:10:05:00] "GET /index.html" 200
EOF

# ZADACI:
# 1. Koliko 404 greški?
# 2. Koji IP ima najviše requesta?
# 3. Prikaži samo uspešne requesta (200)
# 4. Koliko jedinstvenih IP adresa?
```

### Challenge 3: File Management

```bash
# ZADACI:
# 1. Kreiraj folder "archive"
# 2. Pronađi sve .txt fajlove veće od 1KB
# 3. Kopiraj ih u archive/ sa datumom u imenu
# 4. Kreiraj .tar.gz arhivu
# 5. Proveri veličinu arhive
```

---

## 🎓 REŠENJA (Ne gledaj pre nego što probaš!)

```bash
# 1. Ukupno laptopa
grep "Laptop" sales.csv | awk -F',' '{sum+=$3} END {print sum}'

# 2. Najveća ukupna vrednost
awk -F',' 'NR>1 {total[$2]+=$3*$4} END {for(p in total) print p, total[p]}' sales.csv | sort -k2 -nr | head -1

# 3. Prosečna cena po produktu
awk -F',' 'NR>1 {sum[$2]+=$4; count[$2]++} END {for(p in sum) print p, sum[p]/count[p]}' sales.csv

# 4. Sort po datumu i proizvodu
(head -n 1 sales.csv; tail -n +2 sales.csv | sort -t',' -k1,1 -k2,2) > sales_sorted.csv
```

---

```bash
# 1. 404 greške
grep -c "404" access.log

# 2. IP sa najviše requesta
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -1

# 3. Samo 200 responses
grep "200" access.log

# 4. Jedinstveni IP-ovi
awk '{print $1}' access.log | sort -u | wc -l
```

---

```bash
# 1-3. Kreiraj archive i kopiraj
mkdir -p archive
find . -name "*.txt" -size +1k -exec cp {} archive/{}_$(date +%Y%m%d) \;

# 4. Tar arhiva
tar -czf archive_backup.tar.gz archive/

# 5. Veličina
ls -lh archive_backup.tar.gz
```

---

## 🎯 ZAVRŠNI CHECKLIST

Po završetku svih vežbi, trebao bi moći:

```bash
✅ Navigacija:
   - cd, pwd, ls u različitim varijacijama
   - mkdir, rmdir, tree

✅ Fajlovi:
   - touch, echo, cat, head, tail, less
   - cp, mv, rm sa opcijama
   - wc, file, stat

✅ Pretraga:
   - grep sa svim opcijama
   - find po imenu, tipu, veličini, vremenu
   - Kombinovanje sa xargs

✅ Pipes & Redirects:
   - | za pipeing -> povezivanje komandi
   - >, >> za output preusmeravanje -> stdout
   - 2>, 2>&1 za stderr
   - < za input

✅ Processing:
   - sort sa opcijama
   - uniq, uniq -c
   - cut, awk, sed
   - Kombinovani pipelines

✅ Permissions:
   - ls -l čitanje
   - chmod numerical i symbolic
   - chown (ako imaš prava)

✅ System:
   - whoami, hostname, uname
   - env, echo $VAR
   - du, df

✅ Advanced:
   - Complex pipelines
   - Log analiza
   - CSV manipulation
   - Batch operations
```

---

## 📚 Sledeći Koraci

```bash
# 1. Ponavljaj vežbe dok ne ide bez gledanja
# 2. Primeni na svoje projekte
# 3. Kreiraj vlastite skripte
# 4. Pređi na Git vežbe (2025-12-17_terminal_git_basics)
```

**Bravo! 🎉 Prošao si kompletni terminal trening!**

---

```

```
