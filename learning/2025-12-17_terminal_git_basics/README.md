# 🖥️ Terminal + Git Osnove — Dan 1-2

**Tema:** Linux Terminal i Git — Fundamentalni Alati za Python Automatizaciju
**Datum:** 2025-12-17 (Dan 1) - 2025-12-18 (Dan 2)
**Trajanje:** ~16 sati (8h/dan)
**Status:** ✅ Kompletno + Spreman za Učenje

---

## 🎬 BRZI START

**Sutra ujutro:**

1. Otvori: [`START_GUIDE.md`](./START_GUIDE.md) (10 min)
2. Pročitaj: [`kickoff.md`](./kickoff.md) (20 min)
3. Pokreni: [`terminal_repl_exercises.md`](./terminal_repl_exercises.md) (FAZA 1-3)

**Rezultat:** Kroz 48 sati, terminal je kao svoj dom! 🏠

---

## 📚 Šta Pokriva

### Dan 1: Terminal Osnove (8h)

| Tema                  | Vreme | Rezultat                           |
| --------------------- | ----- | ---------------------------------- |
| **Navigation**        | 1h    | `pwd`, `cd`, `ls` bez razmišljanja |
| **File Operations**   | 1.5h  | `mkdir`, `touch`, `rm`, `cp`, `mv` |
| **Reading Files**     | 1h    | `cat`, `head`, `tail`, `less`      |
| **Searching**         | 1h    | `grep`, `find` sa opcijama         |
| **Pipes & Redirects** | 1.5h  | `\|`, `>`, `>>`, `2>` kombinovano  |
| **Scripts**           | 1h    | Pokrenjivanje `.sh` fajlova        |

---

### Dan 2: Git + Paths (8h)

| Tema                    | Vreme | Rezultat                               |
| ----------------------- | ----- | -------------------------------------- |
| **Git Init & Basics**   | 1.5h  | `git init`, `git config`, `.gitignore` |
| **Git Workflow**        | 2h    | `git add`, `git commit`, `git status`  |
| **Git History**         | 1.5h  | `git log`, `git diff`, branching       |
| **Paths & Permissions** | 1h    | absolute/relative, `chmod`, `PATH`     |
| **Env Variables**       | 0.5h  | `echo $PATH`, `.bashrc`                |
| **Virtual Env**         | 1.5h  | `python -m venv` setup                 |

---

## 📁 Struktura Foldera

```
2025-12-17_terminal_git_basics/
├── 📌 README.md                      ← Ti si ovde
├── 🚀 START_GUIDE.md                 ← Početna tačka
├── 📖 kickoff.md                     ← Dnevni plan
├── ✅ tasks.md                       ← Checklist
├── 💡 cheatsheet.md                  ← Quick reference
├── 📝 terminal_repl_exercises.md     ← Detaljne vežbe (3 faze)
├── 🧠 chatlog.md                     ← Q&A + Razgovor
└── 📊 summary.md                     ← Što si naučio
```

---

## 🎯 Redosled Čitanja

```
1. START_GUIDE.md       (10 min) ← POČETNA TAČKA
2. kickoff.md           (20 min) ← Dnevni plan
3. tasks.md             (5 min)  ← Što trebaš uraditi
4. cheatsheet.md        (10 min) ← Reference
5. terminal_repl_exercises.md (8h) ← PRAKSA
6. chatlog.md           (15 min) ← Q&A Ponavljanje
7. summary.md           (10 min) ← Što si naučio
```

---

## 🔥 Top 3 Stvari za Pamćenje

```bash
# 1. Navigation je osnova
pwd                    # Where am I?
cd /path/to/folder     # Go there
ls -la                 # What's inside?

# 2. Pipes = Kombinovanje komandi
cat file.txt | grep "search" | wc -l

# 3. Git = Verzije + Istorija
git add .
git commit -m "message"
git log --oneline
```

---

## 📊 14-dnevni Kontekst

```
NEDELJA 1:
├─ 🔴 Dan 1-2: Terminal + Git (TI STE OVDE)
│           ├─ Terminal osnove
│           └─ Git workflow + .gitignore
├─ Dan 3-4: CSV Osnove (Dialect, Sniffer)
├─ Dan 5-6: CSV praktika (read/write/clean)
└─ Dan 7:   Pathlib + Logging

NEDELJA 2:
├─ Dan 8-9: Testing + Error handling
├─ Dan 10-11: Requests + BeautifulSoup
├─ Dan 12-13: Web scraper projekat
└─ Dan 14: Consolidation

REZULTAT: Spreman za Python Automatizaciju! 🚀
```

---

## 💪 Motivacija

```
Dan 1 Ujutro:   "Šta je ls -la?"
Dan 1 Veče:     "Mogu da navigiram bez razmišljanja"
Dan 2 Ujutro:   "Kako git radi?"
Dan 2 Veče:     "Kreiram prvi git repository"
Dan 3 Ujutro:   "Spreman sam za CSV!"
```

---

## ✅ Checklist — Šta Ćeš Uraditi

**Dan 1 (Terminal):**

-   [ ] Otvorim terminal i `pwd`
-   [ ] Navigiram sa `cd` između foldera
-   [ ] Kreiram fajlove i foldere sa `mkdir`, `touch`
-   [ ] Čitam fajlove sa `cat`, `head`, `tail`
-   [ ] Tražim sa `grep` i `find`
-   [ ] Kombinujem komandi sa pipes (`|`) i redirects (`>`)

---

**Dan 2 (Git):**

-   [ ] `git init` prvi repository
-   [ ] Konfigurišem `user.name` i `user.email`
-   [ ] Kreiram `.gitignore` sa popularnim patternima
-   [ ] `git add` i `git commit` sa porukom
-   [ ] Vidim istoriju sa `git log`
-   [ ] Kreiram prvi Python venv

---

## 🚀 KRENI SADA

**Sledeći 10 Minuta:**

-   [ ] Otvori: [`START_GUIDE.md`](./START_GUIDE.md)

**Narednih 20 Minuta:**

-   [ ] Čitaj: [`kickoff.md`](./kickoff.md)

**Narednih 8 Sati:**

-   [ ] Vežbaj: [`terminal_repl_exercises.md`](./terminal_repl_exercises.md)

---

## 📞 Ako se Zaglaviš

1. **Otvori cheatsheet.md** - Sve komande su tu
2. **Pogledaj chatlog.md** - Česta pitanja sa odgovorima
3. **Ponovi vežbu** - Kodiranje > Čitanje
4. **Eksperimentiši** - Napraviti greške je OK!

---

**Počni sa [`START_GUIDE.md`](./START_GUIDE.md)! 🖥️**

---
