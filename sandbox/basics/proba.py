from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

# ============================================================================
# TEORIJA 1: TIPOVI PODATAKA U PYTHONU
# ============================================================================
# Python ima nekoliko osnovnih tipova koje ćeš koristiti sa CSV modulom:
#
# 1. STRING (str) - Tekst u navodnicima: "Jole", 'Novi Sad'
#    - Sve vrednosti u CSV fajlu su UVEK stringovi!
#    - Čak i brojevi: "25", "3.14" su stringovi dok ih ne konvertuješ
#
# 2. LIST (lista) - Uredjeni niz elemenata: [1, 2, 3] ili ["Ana", "Marko"]
#    - csv.reader vraća svaki red kao listu: ['ime', 'prezime', 'godine']
#    - Može se menjati: dodavanje, brisanje, sortiranje
#    - Može imati duplikate: [1, 1, 2, 2]
#
# 3. DICT (rečnik) - Parovi ključ:vrednost: {"ime": "Jole", "godine": "25"}
#    - csv.DictReader vraća svaki red kao rečnik
#    - Ključevi MORAJU biti jedinstveni
#    - Vrednosti mogu biti bilo šta
#
# 4. TUPLE (torka) - Nepromenjiva lista: (1, 2, 3)
#    - Kao lista, ali se NE MOŽE MENJATI nakon kreiranja
#    - Često se koristi za return više vrednosti iz funkcije
#
# 5. SET (skup) - Neuređeni niz JEDINSTVENIH elemenata: {1, 2, 3}
#    - Automatski odbacuje duplikate
#    - Ne može se indeksirati: set[0] → ERROR!
#
# ANOTACIJE (Type Hints):
# list[str] = lista stringova
# dict[str, str] = rečnik sa string ključevima i vrednostima
# list[dict[str, str]] = lista rečnika
# tuple[list[str], list[str]] = tuple sa 2 liste stringova

# ============================================================================
# TEORIJA 2: CSV MODUL - OSNOVNI KONCEPTI
# ============================================================================
# CSV = Comma Separated Values (vrednosti odvojene zarezima)
#
# ČITANJE:
# - csv.reader(f) → ITERATOR koji vraća list[str] za svaki red
# - csv.DictReader(f) → ITERATOR koji vraća dict[str, str | Any] za svaki red
#
# PISANJE:
# - csv.writer(f) → piše list[str] kao jedan red
# - csv.DictWriter(f, fieldnames) → piše dict[str, str] kao jedan red
#
# VAŽNI PARAMETRI:
# - newline='' → OBAVEZNO kod open() da CSV ne doda dodatne prazne redove
# - encoding='utf-8' → Za naše karaktere (č, š, ž, đ, ć)
# - delimiter=',' → Separator kolona (može biti ;, \t, |)
# - restval='' → Šta upisati kad fali vrednost
# - restkey=None → Gde staviti višak vrednosti
# - extrasaction='ignore' → Šta raditi sa viškom ključeva u DictWriter

# Putanje su stabilne bez obzira odakle pokrećeš skriptu
DATA_DIR = Path(__file__).parent / "data"
CSV_FILE = DATA_DIR / "sample.csv"

# Starter podaci da REPL primeri uvek rade
SAMPLE_ROWS: list[list[str]] = [
    ["ime", "prezime", "godine", "grad"],
    ["Jovana", "Zelenković", "41", "Novi Sad"],
    ["Jole", "Pavlović", "40", "Novi Sad"],
    ["Bojan", "Stambolija", "11", "Sremska Mitrovica"],
]


def ensure_sample_data() -> None:
    """Kreiraj data/ i sample.csv ako ne postoje (idempotentno)."""
    DATA_DIR.mkdir(exist_ok=True)
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(SAMPLE_ROWS)


# ============================================================================
# TEORIJA 3: PETLJE I ITERATORI
# ============================================================================
# FOR PETLJA - prolazi kroz svaki element u nizu
# for element in lista:
#     print(element)
#
# ENUMERATE - daje i indeks i element
# for i, element in enumerate(lista):
#     print(f"Indeks {i}: {element}")
#
# ZIP - kombinuje dve liste
# for ime, godine in zip(imena, godine_lista):
#     print(f"{ime} ima {godine} godina")
#
# WHILE PETLJA - ponavlja dok je uslov True
# while uslov:
#     # radi nešto
#
# ITERATORI:
# csv.reader je ITERATOR - možeš ga potrošiti samo JEDNOM!
# prvi = list(reader)  # radi
# drugi = list(reader)  # PRAZAN [] jer je iterator već potrošen!

# ---------- READ PRIMERI ----------

def read_as_lists() -> list[list[str]]:
    """
    Čita ceo CSV u listu listi (najlakše za debug).

    Vraća: [['ime', 'prezime', 'godine', 'grad'],
            ['Jovana', 'Jovic', '41', 'Novi Sad'], ...]

    Svaki red je LISTA STRINGOVA!
    """
    with CSV_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)


def read_as_dicts(fill_missing: str = "") -> list[dict[str, str]]:
    """
    Čita CSV kao listu rečnika; None vrednosti se pune fill_missing.

    Vraća: [{'ime': 'Jovana', 'prezime': 'Jovic',
             'godine': '41', 'grad': 'Novi Sad'}, ...]

    KLJUČNA RAZLIKA:
    - csv.reader → list[list[str]]
    - csv.DictReader → list[dict[str, str | Any]]

    DictReader automatski koristi prvi red kao HEADER (ključeve za rečnik)!
    """
    with CSV_FILE.open(newline="", encoding="utf-8") as f:
        reader: csv.DictReader[str] = csv.DictReader(f)
        reader.restval = fill_missing  # Šta staviti kad fali vrednost
        rows: list[dict[str, str]] = []
        for row in reader:
            # Comprehension: {key: value for key, value in dict.items()}
            # Ovde čistimo None vrednosti i menjamo ih sa fill_missing
            clean: dict[str, str] = {
                k: (v if v is not None else fill_missing)
                for k, v in row.items()
            }
            rows.append(clean)
        return rows


def read_with_enumerate() -> None:
    """
    PETLJA SA ENUMERATE - pokazuje indeks + element.

    enumerate(lista) vraća: (0, element0), (1, element1), ...
    Korisno kad ti treba BROJ REDA!
    """
    with CSV_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            print(f"Red {i}: {row}")
            # Red 0: ['ime', 'prezime', 'godine', 'grad']
            # Red 1: ['Jovana', 'Jovic', '41', 'Novi Sad']


def read_first_n_rows(n: int = 3) -> list[list[str]]:
    """
    SLICING DEMO - uzima prvih N redova.

    rows[:3] = prva 3 reda
    rows[1:] = svi osim prvog (bez headera)
    rows[-2:] = poslednja 2 reda
    """
    rows = read_as_lists()
    return rows[:n]


# ============================================================================
# TEORIJA 4: COMPREHENSIONS (KOMPREHENCIJE)
# ============================================================================
# LIST COMPREHENSION - pravi novu listu iz postojeće
# nova = [x * 2 for x in stara]  # udvostruči sve
# nova = [x for x in stara if x > 10]  # samo one > 10
#
# DICT COMPREHENSION - pravi novi rečnik
# nova = {k: v * 2 for k, v in stara.items()}
# nova = {k: v for k, v in stara.items() if v > 10}
#
# SET COMPREHENSION - pravi novi skup
# nova = {x * 2 for x in stara}
#
# KORISTI SE ZA: filter, map, transform u JEDNOJ LINIJI!

def filter_by_age(min_age: int = 30) -> list[dict[str, str]]:
    """
    FILTER + COMPREHENSION - uzima samo ljude starije od min_age.

    Ovo je EKVIVALENTNO:

    rows = []
    for person in read_as_dicts():
        if int(person["godine"]) >= min_age:
            rows.append(person)
    return rows

    Ali MNOGO KRAĆE sa comprehension!
    """
    return [row for row in read_as_dicts() if int(row["godine"]) >= min_age]


def get_all_names() -> list[str]:
    """
    MAP + COMPREHENSION - izvlači samo jednu kolonu (imena).

    Rezultat: ['Jovana', 'Jole', 'Boki']
    """
    return [row["ime"] for row in read_as_dicts()]


def update_ages_plus_one() -> list[dict[str, str]]:
    """
    TRANSFORM + COMPREHENSION - dodaje +1 svim godinama.

    PAZI: godine su STRING! Mora int() → +1 → str()
    """
    rows = read_as_dicts()
    return [
        {**row, "godine": str(int(row["godine"]) + 1)}
        for row in rows
    ]


# ---------- EDGE CASE PRIMERI ----------

def iterator_exhaustion_demo() -> tuple[list[list[str]], list[list[str]]]:
    """
    EDGE CASE 1: Iterator se troši!

    csv.reader je ITERATOR - možeš ga potrošiti samo JEDNOM!
    Posle prvog list(reader), pokazivač je na kraju fajla.
    Drugi list(reader) vraća PRAZNU LISTU []!

    FIX: Koristi list() odmah ili resetuj fajl sa f.seek(0).
    """
    with CSV_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        first = list(reader)
        second = list(reader)  # prazan jer je iterator potrošen
    return first, second


def wrong_delimiter_demo() -> list[list[str]]:
    """
    EDGE CASE 2: Pogrešan delimiter!

    Ako CSV koristi "," a ti tražiš ";" → SVE IDE U JEDNU KOLONU!
    Rezultat: [['ime,prezime,godine,grad'], ['Jovana,Jovic,41,Novi Sad'], ...]

    FIX: Proveri delimiter u fajlu (otvori u text editor-u).
    """
    with CSV_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        return list(reader)


def missing_values_demo() -> None:
    """
    EDGE CASE 3: Manjkajuće vrednosti!

    CSV može imati redove sa manje kolona:
    ime,prezime,godine,grad
    Ana,,25,  ← fali prezime i grad je prazan

    csv.reader → ['Ana', '', '25', '']  (prazni stringovi)
    csv.DictReader → {'ime': 'Ana', 'prezime': '', 'godine': '25', 'grad': ''}

    Ako CSV ima MANJE kolona od headera:
    csv.DictReader → {'ime': 'Ana', 'prezime': None, 'godine': None, 'grad': None}
    restval parametar kontroliše ovu vrednost!
    """
    # Kreiraj broken CSV
    broken_csv = DATA_DIR / "broken.csv"
    with broken_csv.open("w", newline="", encoding="utf-8") as f:
        f.write("ime,prezime,godine,grad\n")
        f.write("Ana\n")  # Fali 3 kolone!
        f.write("Marko,,,\n")  # Prazni stringovi

    # Čitaj sa DictReader
    with broken_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        reader.restval = "N/A"  # Umesto None stavlja "N/A"
        for row in reader:
            print(row)

    # Cleanup
    broken_csv.unlink()


def extra_columns_demo() -> None:
    """
    EDGE CASE 4: Višak kolona!

    Ako CSV ima VIŠE kolona od headera:
    csv.DictReader stavlja višak u ključ None!

    Header: ime,prezime
    Red: Ana,Jovic,25,Novi Sad  ← 2 viška!

    Rezultat: {'ime': 'Ana', 'prezime': 'Jovic', None: ['25', 'Novi Sad']}
    """
    extra_csv = DATA_DIR / "extra.csv"
    with extra_csv.open("w", newline="", encoding="utf-8") as f:
        f.write("ime,prezime\n")
        f.write("Ana,Jovic,25,Novi Sad\n")  # 2 viška kolone!

    with extra_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)  # {'ime': 'Ana', 'prezime': 'Jovic', None: ['25', 'Novi Sad']}

    extra_csv.unlink()


def custom_delimiter_demo() -> None:
    """
    EDGE CASE 5: Custom delimiter (;, |, tab).

    CSV ne mora biti "Comma" Separated - može biti bilo šta!
    - Evropski Excel često koristi ; umesto ,
    - TSV (Tab Separated Values) koristi \t
    - Custom formati mogu koristiti | ili drugi karakter
    """
    # Kreiraj CSV sa ; delimiterom
    semicolon_csv = DATA_DIR / "semicolon.csv"
    with semicolon_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["ime", "prezime", "godine"])
        writer.writerow(["Ana", "Jovic", "25"])

    # Čitaj sa ispravnim delimiterom
    with semicolon_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        print(list(reader))

    semicolon_csv.unlink()


# ============================================================================
# TEORIJA 5: FILE MODES (REŽIMI OTVARANJA FAJLA)
# ============================================================================
# "r" - READ (čitanje) - default, fajl mora postojati
# "w" - WRITE (pisanje) - BRIŠE postojeći fajl i piše novi!
# "a" - APPEND (dodavanje) - dodaje na kraj fajla
# "r+" - READ+WRITE - čita i piše, fajl mora postojati
# "x" - EXCLUSIVE CREATE - kreira fajl, ERROR ako već postoji
#
# PAZI: "w" BRIŠE fajl! Ako slučajno pozivaš dva puta, prvi upis se gubi!

# ---------- WRITE PRIMERI ----------

def overwrite_all(rows: list[list[str]]) -> None:
    """
    Prepiše ceo fajl novim redovima (pazi: briše postojeće)!

    MODE "w" = WRITE:
    - Ako fajl postoji → BRIŠE ga i pravi novi
    - Ako fajl ne postoji → pravi novi

    KORISTI OVO kad hoćeš da ZAMENIŠ ceo fajl!
    """
    with CSV_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def append_row(row: list[str]) -> None:
    """
    Doda jedan red na kraj fajla (append).

    MODE "a" = APPEND:
    - NE BRIŠE postojeći fajl!
    - Dodaje novi sadržaj NA KRAJ
    - Ako fajl ne postoji → pravi novi

    KORISTI OVO kad hoćeš da DODAŠ podatke bez brisanja starih!
    """
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)


def insert_header_if_missing(header: list[str]) -> None:
    """
    Dodaje header ako ga nema; čuva postojeće podatke (r+ + seek + truncate).

    MODE "r+" = READ + WRITE:
    - Fajl mora postojati!
    - Možeš čitati i pisati u istom fajlu

    KORACI:
    1. f.read() → učitaj sve u memoriju
    2. f.seek(0) → vrati pokazivač na početak
    3. writer.writerow() → upiši header
    4. f.write() → upiši stare podatke nazad
    5. f.truncate() → obriši sve posle pokazivača (ako ima viška)

    PAZI: Ovo radi samo za MALE fajlove (ceo fajl ide u RAM)!
    """
    with CSV_FILE.open("r+", newline="", encoding="utf-8") as f:
        existing = f.read()
        f.seek(0)
        writer = csv.writer(f)
        writer.writerow(header)
        f.write(existing)
        f.truncate()


def drop_column(index: int) -> None:
    """
    Uklanja kolonu po indeksu iz headera i svih redova.

    SLICING I DEL:
    - rows[0] → prvi red (header)
    - rows[1:] → svi redovi osim prvog (podaci)
    - del header[1] → obriši drugi element (indeks 1)

    PROVERA INDEKSA:
    - if 0 <= index < len(header) → da ne brisamo indeks koji ne postoji!
    """
    with CSV_FILE.open("r+", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
        if not rows:
            return
        f.seek(0)
        writer = csv.writer(f)
        header = rows[0]
        if 0 <= index < len(header):
            del header[index]
        writer.writerow(header)
        for row in rows[1:]:
            if 0 <= index < len(row):
                del row[index]
            writer.writerow(row)
        f.truncate()


# ============================================================================
# TEORIJA 6: DictWriter PARAMETRI
# ============================================================================
# DictWriter(f, fieldnames, restval='', extrasaction='raise')
#
# fieldnames - LISTA KLJUČEVA koji će biti kolone (obavezno!)
# restval - Šta staviti ako ključ fali u rečniku (default: '')
# extrasaction - Šta raditi ako rečnik ima VIŠAK ključeva:
#   - 'raise' (default) -> ValueError
#   - 'ignore' -> preskače višak ključeve
#
# PRIMER:
# fieldnames = ['ime', 'godine']
# row = {'ime': 'Ana', 'godine': '25', 'grad': 'Beograd'}  <- 'grad' je višak!
# extrasaction='ignore' -> 'grad' se preskače, upis radi
# extrasaction='raise' -> ValueError!

# ---------- DICT WRITER PRIMERI ----------

def dict_writer_append(row: dict[str, str]) -> None:
    """
    Dodaje red rečnikom; extrasaction='ignore' preskače višak ključeva.

    SCENARIO:
    row = {'ime': 'Ana', 'prezime': 'Jovic', 'godine': '25',
           'grad': 'Beograd', 'email': 'ana@gmail.com'} <- VIŠAK!

    Sa extrasaction='ignore' -> 'email' se preskače.
    Sa extrasaction='raise' -> ValueError!
    """
    fieldnames = ["ime", "prezime", "godine", "grad"]
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
            extrasaction="ignore",
            restval=""
        )
        writer.writerow(row)


def dict_writer_overwrite(rows: list[dict[str, str | int]]) -> None:
    """
    Piše novu tabelu iz rečnika; int će biti konvertovan u string.

    CSV UVEK RADI SA STRINGOVIMA!
    Ako imaš int, float, bool mora se konvertovati u str()!

    COMPREHENSION UNUTAR COMPREHENSION:
    {k: str(v) for k, v in row.items()}
    Novi rečnik sa istim ključevima, ali vrednosti su stringovi.

    writer.writeheader() piše prvi red sa nazivima kolona (fieldnames).
    """
    fieldnames = list(rows[0].keys())
    with CSV_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            # Konvertuj sve vrednosti u string
            str_row = {k: str(v) for k, v in row.items()}
            writer.writerow(str_row)


# ============================================================================
# TEORIJA 7: QUOTING (NAVODNICI U CSV)
# ============================================================================
# Šta ako CSV sadrži zarez ili novi red UNUTAR vrednosti?
#
# Primer: "Jole, Python Developer" ← ima zarez unutra!
# CSV mora da ga "zatvori" u navodnike: "Jole, Python Developer",25,Beograd
#
# QUOTING NIVOI:
# QUOTE_MINIMAL (default) - samo kada je neophodno (ako ima zarez, novi red, ...)
# QUOTE_ALL - sve vrednosti u navodnicima
# QUOTE_NONNUMERIC - sve osim brojeva
# QUOTE_NONE - nikad (ako ima zarez → ERROR!)

def quoting_demo() -> None:
    """
    EDGE CASE 6: Quoting (navodnici).

    CSV vrednost može sadržati:
    - Zarez: "Jole, Python Dev"
    - Novi red: "Opis:\nDve linije"
    - Navodnike: 'Kaže: "Cao!"'

    csv.writer automatski stavlja navodnike kad treba!
    """
    quote_csv = DATA_DIR / "quotes.csv"

    with quote_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["ime", "opis"])
        writer.writerow(["Jole, Python Dev", "Kaže: \"Cao!\""])

    with quote_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        print(list(reader))

    quote_csv.unlink()


def encoding_demo() -> None:
    """
    EDGE CASE 7: Encoding (č, ć, ž, š, đ).

    encoding='utf-8' je OBAVEZAN za naše karaktere!
    Bez njega → Mojibake (čudni simboli umesto č, ć, ...).
    """
    encoding_csv = DATA_DIR / "encoding.csv"

    with encoding_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ime", "grad"])
        writer.writerow(["Žarko", "Čačak"])
        writer.writerow(["Đorđe", "Šabac"])

    with encoding_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        print(list(reader))

    encoding_csv.unlink()


def dialect_demo() -> None:
    """
    EDGE CASE 8: Custom Dialect (CSV format variations).

    Dialect = skup pravila za CSV format:
    - delimiter (,)
    - quotechar (")
    - doublequote (True/False)
    - skipinitialspace (True/False)
    - lineterminator (\r\n)

    KORISTI OVO za čudne CSV formate (Excel, staré sisteme, itd.).
    """
    # Registruj custom dialect
    csv.register_dialect(
        'custom',
        delimiter='|',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )

    dialect_csv = DATA_DIR / "dialect.csv"

    with dialect_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, dialect='custom')
        writer.writerow(["ime", "prezime", "godine"])
        writer.writerow(["Ana", "Jovic", "25"])

    with dialect_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f, dialect='custom')
        print(list(reader))

    csv.unregister_dialect('custom')
    dialect_csv.unlink()


# ---------- QUICK EDGE CASES (za REPL) ----------

def edge_cases() -> dict[str, Any]:
    """Skupi male primere za brzi pregled u REPL-u."""
    first, second = iterator_exhaustion_demo()
    return {
        "read_lists": read_as_lists(),
        "read_dicts": read_as_dicts(),
        "iterator_first": first,
        "iterator_second": second,  # biće [] jer je iterator potrošen
        "wrong_delimiter": wrong_delimiter_demo(),
        "filter_age_30+": filter_by_age(30),
        "only_names": get_all_names(),
        "ages_plus_one": update_ages_plus_one(),
    }


# ============================================================================
# TEORIJA 8: DEBUGGING TEHNIKE
# ============================================================================
# 1. print() - najbrži način da vidiš šta se dešava
#    print(type(variable)) -> vidi tip
#    print(len(lista)) -> vidi dužinu
#
# 2. breakpoint() - zaustavlja kod i otvara debugger (Python 3.7+)
#    Možeš ispitati sve promenljive u tom trenutku!
#
# 3. assert - provera da li nešto ima vrednost koju očekuješ
#    assert len(rows) > 0, "CSV je prazan!"
#    Ako nije True -> AssertionError
#
# 4. try/except - hvatanje grešaka
#    try:
#        # code koji može da pukne
#    except ValueError as e:
#        print(f"Greška: {e}")


if __name__ == "__main__":
    ensure_sample_data()

    print("\n--- READ AS LISTS ---")
    print(read_as_lists())

    print("\n--- READ AS DICTS ---")
    print(read_as_dicts())

    print("\n--- ITERATOR EXHAUSTION ---")
    first, second = iterator_exhaustion_demo()
    print("first", first)
    print("second", second)

    print("\n--- WRONG DELIMITER (;) ---")
    print(wrong_delimiter_demo())

    print("\n--- APPEND + DICT WRITER DEMO ---")
    append_row(["Danica", "67", "Sremska Mitrovica", "RS"])
    dict_writer_append({
        "ime": "Petar",
        "prezime": "Petrovic",
        "godine": "35",
        "grad": "Beograd",
        "extra": "ignored"
    })
    print(read_as_lists())

    print("\n--- DROP COLUMN 1 (prezime) ---")
    drop_column(1)
    print(read_as_lists())

    print("\n--- OVERWRITE WITH NEW TABLE ---")
    dict_writer_overwrite(
        [
            {"ime": "Ana", "godine": 25, "grad": "Beograd"},
            {"ime": "Milan", "godine": 31, "grad": "Novi Sad"},
        ]
    )
    print(read_as_dicts())

    print("\n--- EDGE CASE SUMMARY ---")
    for k, v in edge_cases().items():
        print(f"{k}: {v}")


