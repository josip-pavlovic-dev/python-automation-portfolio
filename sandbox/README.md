# 🧪 Python Automation Sandbox

**Ovo je tvoj prostor za vežbanje, eksperimentisanje, i testiranje ideja!**

---

## 📁 Struktura

```
sandbox/
├── README.md                  # This file
├── basics/                    # Python fundamentals refresh
│   ├── 01_variables_types.py
│   ├── 02_functions.py
│   ├── 03_lists_loops.py
│   ├── 04_dictionaries.py
│   ├── 05_file_operations.py
│   └── exercises/
├── web-scraping/              # Web scraping practice
│   ├── 01_requests_basics.py
│   ├── 02_beautifulsoup.py
│   ├── 03_css_selectors.py
│   ├── 04_pagination.py
│   ├── 05_error_handling.py
│   └── practice-sites.md
├── data-processing/           # Pandas & data manipulation
│   ├── 01_pandas_basics.py
│   ├── 02_csv_operations.py
│   ├── 03_data_cleaning.py
│   ├── 04_merging_data.py
│   └── sample-data/
├── excel-automation/          # Excel file processing
│   ├── 01_read_excel.py
│   ├── 02_write_excel.py
│   ├── 03_formulas.py
│   └── sample-files/
├── pdf-processing/            # PDF extraction
│   ├── 01_pypdf2_basics.py
│   ├── 02_tabula_tables.py
│   └── sample-pdfs/
├── api-integration/           # APIs & automation
│   ├── 01_rest_client.py
│   ├── 02_gmail_api.py
│   ├── 03_google_sheets.py
│   └── credentials/
├── testing/                   # Unit testing practice
│   ├── 01_pytest_basics.py
│   ├── 02_test_scraper.py
│   └── 03_mocking.py
├── mini-projects/             # Small projects for practice
│   ├── calculator/
│   ├── todo-cli/
│   ├── weather-fetcher/
│   └── file-organizer/
├── algorithms/                # Problem-solving practice
│   ├── sorting.py
│   ├── searching.py
│   └── string-manipulation.py
└── experiments/               # Free-form testing
    └── scratch.py
```

---

## 🎯 Kako Koristiti Sandbox

### **1. Daily Warm-Up (15-30 min)**

Pre nego što kreneš na glavni projekat:

```bash
cd sandbox/basics
python 01_variables_types.py
```

-   Pokreni jednu od vežbi
-   Izmeni kod, eksperimentuj
-   Lomi kod da razbiješ led

### **2. Practice Specific Skill**

Ako učiš BeautifulSoup:

```bash
cd sandbox/web-scraping
python 02_beautifulsoup.py
```

-   Radi kroz primere
-   Dodaj svoje varijacije
-   Beleži šta si naučio u comments

### **3. Test Ideas Before Main Project**

Pre nego što dodaš feature u `projects/01-web-scraper`:

```bash
cd sandbox/experiments
python scratch.py
```

-   Testiraj novu biblioteku
-   Proba architecture pattern
-   Break things without fear!

### **4. Mini-Projects (1-2h vežbe)**

```bash
cd sandbox/mini-projects/calculator
python calculator.py
```

-   Kompletan mali projekat
-   Practice full workflow (plan → code → test → refactor)
-   Add to portfolio ako je dobar!

---

## 📚 Learning Path

### **Week 1: Foundations**

**Folder:** `sandbox/basics/`

**Goals:**

-   [ ] Python syntax refresh (variables, functions, loops)
-   [ ] File I/O operations
-   [ ] Error handling basics

**Time:** 2-3h total (30min/day)

---

### **Week 1-2: Web Scraping**

**Folder:** `sandbox/web-scraping/`

**Goals:**

-   [ ] Requests library mastery
-   [ ] BeautifulSoup selectors
-   [ ] Pagination handling
-   [ ] Error handling & retries

**Time:** 5-6h total (1h/day)

---

### **Week 2-3: Data Processing**

**Folder:** `sandbox/data-processing/`

**Goals:**

-   [ ] Pandas DataFrame operations
-   [ ] CSV read/write/merge
-   [ ] Data cleaning techniques
-   [ ] GroupBy & aggregations

**Time:** 4-5h total

---

### **Week 3-4: Excel & PDF**

**Folders:** `sandbox/excel-automation/` + `sandbox/pdf-processing/`

**Goals:**

-   [ ] OpenPyXL basics
-   [ ] Excel formulas & formatting
-   [ ] PDF table extraction (Tabula)
-   [ ] Batch processing

**Time:** 4-5h total

---

### **Ongoing: Problem Solving**

**Folder:** `sandbox/algorithms/`

**Goals:**

-   [ ] 1 algorithm challenge/day (15-30min)
-   [ ] String manipulation practice
-   [ ] List comprehensions
-   [ ] Dictionary operations

**Time:** 15-30min daily

---

## 🔥 Sandbox Rules

### **DO:**

✅ **Break things!** - Sandbox je za greške
✅ **Experiment wildly** - Proba različite pristupe
✅ **Leave comments** - Objasni sebi šta si naučio
✅ **Copy-paste from Stack Overflow** - Učenje je cilj!
✅ **Commit progress** - `git commit -m "sandbox: learned pandas merge"`

### **DON'T:**

❌ **Don't worry about perfection** - Ovo nije production kod
❌ **Don't spend 2h debugging** - Ako ne ide, pređi na sledeće
❌ **Don't skip basics** - Fundamentals su ključni!

---

## 📝 Daily Sandbox Workflow

### **Morning (15 min):**

```bash
cd sandbox/basics
python [danas-vežba].py
```

### **During Main Work (ako zaglaviš):**

```bash
cd sandbox/experiments
# Testiraj problem izolovano
python scratch.py
```

### **Evening (optional, 30 min):**

```bash
cd sandbox/mini-projects/[projekat]
# Radi na malom projektu za relaksaciju
```

---

## 🎓 Learning Resources

### **Practice Websites (Web Scraping):**

Sačuvano u: `sandbox/web-scraping/practice-sites.md`

-   <https://quotes.toscrape.com/> (beginner-friendly)
-   <https://books.toscrape.com/> (pagination practice)
-   <https://httpbin.org/> (HTTP testing)

### **Sample Data:**

-   `sandbox/data-processing/sample-data/` - CSV fajlovi za vežbu
-   `sandbox/excel-automation/sample-files/` - Excel fajlovi
-   `sandbox/pdf-processing/sample-pdfs/` - PDF fajlovi

---

## 🏆 Milestones

### **Beginner → Intermediate:**

-   [ ] Can write scraper without looking at docs
-   [ ] Pandas operations feel natural
-   [ ] Error handling is automatic
-   [ ] Can debug in < 15 min

### **Intermediate → Advanced:**

-   [ ] Can refactor code for readability
-   [ ] Write tests without thinking
-   [ ] Optimize performance
-   [ ] Handle edge cases elegantly

---

## 📊 Track Your Progress

Kreiraj `sandbox/PROGRESS.md`:

```markdown
# Sandbox Progress Log

## Week 1 (Dec 13-20)

-   [x] basics/01-05 completed
-   [x] web-scraping/01-03 done
-   [ ] web-scraping/04-05 in progress

## Week 2 (Dec 21-27)

-   [ ] data-processing started
-   [ ] mini-project: calculator
```

---

## 🚀 Quick Commands

### **Create New Experiment:**

```bash
cd sandbox/experiments
touch test_feature.py
code test_feature.py
```

### **Run All Tests:**

```bash
cd sandbox
python -m pytest testing/ -v
```

### **Clean Scratch Files:**

```bash
cd sandbox/experiments
rm scratch_*.py
```

---

## 💡 Pro Tips

**1. Name Files Descriptively:**

```
❌ test.py
✅ test_beautifulsoup_selectors.py
```

**2. Add TODO Comments:**

```python
# TODO: Try different selector strategy
# FIXME: This breaks with special characters
# LEARN: Why does .select() work better than .find_all()?
```

**3. Commit Often:**

```bash
git add sandbox/
git commit -m "sandbox: practiced pandas merge + groupby"
```

**4. Share Learnings:**
Kopiraj najbolje primere u `learning/` folder za reference!

---

**Sandbox je tvoj!** Eksperimentuj, ломи, učи! 🧪🔥

**Remember:** Svaki profesionalac ima sandbox. Ovo je gde se prave greške bez posledica! 💪
