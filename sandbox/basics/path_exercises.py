import csv
import json
import logging
import shutil
import tempfile  # za privremene fajlove i direktorijume
import time
from datetime import datetime
from pathlib import Path

# Module-level application logger (do not import asyncio's internal logger)
logger = logging.getLogger(__name__)

def setup_logging(
    *,
    level: int = logging.INFO,
    to_file: bool = True,
    file_path: Path | str | None = None,
) -> logging.Logger:
    """Configure module logger with console and optional file handler.

    - level: logging level for this module's logger
    - to_file: when True, also logs to 'logs/latest.log' under this script folder
    - file_path: override log file path; by default uses sandbox/basics/logs/latest.log
    """
    logger.setLevel(level)

    # Avoid duplicating handlers if called multiple times
    if not logger.handlers:
        fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")

        # Console handler
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        logger.addHandler(sh)

        # Optional file handler (points to the symlink by default)
        if to_file:
            if file_path is None:
                # Default to the project's sandbox/basics/logs/latest.log
                base = Path(__file__).parent
                file_path = base / "logs" / "latest.log"
            fp = Path(file_path)
            fp.parent.mkdir(parents=True, exist_ok=True)
            fh = logging.FileHandler(fp, encoding="utf-8")
            fh.setFormatter(fmt)
            logger.addHandler(fh)

    return logger

# ================================================================================
# Kreiranje i navigacija sa Path
# ================================================================================

# Trenutni radni dir
cwd = Path.cwd()
print(f"Trenutni radni direktorijum: {cwd}")
print("✅ Done ...")
# Alternativno: Path(".").resolve()
# Trenutni radni dir je mesto odakle je pokrenut Python skript ili interaktivna sesija!

# Home dir korisnika
home = Path.home()
print(f"Home direktorijum korisnika: {home}")
print("✅ Done ...")

# Putanja do trenutnog fajla
current_file = Path(__file__)
print(f"Putanja do trenutnog fajla: {current_file}")
print("✅ Done ...")

# Parent direktorijum
parent = Path(__file__).parent
print(f"Roditeljski direktorijum trenutnog fajla: {parent}")
print("✅ Done ...")

# Svi roditelji (list)
parents = Path(__file__).parents  # [parent, grandparent, ...]
print(f"Svi roditelji trenutnog fajla: {parents}")
print("✅ Done ...")

# Join sa / operator
data_file = Path.cwd() / "data" / "products.csv"
log_file = Path(__file__).parent / "cli_logging_practice" / "logs" / "file_logger.log"
print(f"Putanja do CSV fajla: {data_file}")
print(f"Putanja do log fajla: {log_file}")
print("✅ Done ...")

# ================================================================================
# Normalizacija i resolving
# ================================================================================

# Resolve: konvertuje relativnu u apsolutnu putanju u odnosu na cwd
abs_path = Path("./data/products.csv").resolve()
print(f"Resolved putanja: {abs_path}")
print("Resolve: konvertuje relativnu u apsolutnu putanju u odnosu na cwd!")
print("✅ Done ...")
# NAPOMENA: resolve() takođe uklanja . i .. iz putanje
relative_path = Path("./home/user/../user/documents/./file.txt").resolve()
print(f"Normalized putanja: {relative_path}")
print("Resolve: uklanja . i .. iz putanje!")
print("✅ Done ...")
# NAPOMENA: resolve() može baciti grešku ako delovi putanje ne postoje na fajl sistemu
# `Path("/home/users/users/ ../user/documents/./file.txt").resolve()`
# Output -> 'Normalized putanja: /home/user/documents/file.txt
# `Path("./home/user/../user/documents/./file.txt").resolve()`
# Output -> '/current/working/dir/home/user/documents/file.txt'
# Gde je /current/working/dir trenutni radni direktorijum (cwd)! Ovo je bitno razumeti!
# Ako želite da normalizujete putanju bez obzira na cwd -> .absolute() umesto .resolve()
normalized_path = Path("./home/user/../user/documents/./file.txt").absolute()
print(f"Absolute putanja: {normalized_path}")
print("Absolute: konvertuje relativnu u apsolutnu putanju bez obzira na cwd!")
print("✅ Done ...")


# Expanduser: konvertuje ~ u home dir
docs = Path("~/documents/report.txt").expanduser()
print(f"Expanded user path: {docs}")
print("Expanduser: konvertuje ~ u home dir!")
print("✅ Done ...")


# Kombinovano (best practice za user input)
def normalize_path(raw: str) -> Path:
    return Path(raw).expanduser().resolve()


normalized = normalize_path("~/../some/relative/path.txt")
print(f"Normalized putanja: {normalized}")
print("✅ Done ...")

# Relative to: dobij relativnu putanju
home = Path.home()  # / "/home/user"
current = Path.cwd()  # / "/home/user/projects"
rel = current.relative_to(home)  # npr. "code/project"
print(f"Relativna putanja od home do cwd: {rel}")
print("Relative to: dobij relativnu putanju u odnosu na neki drugi direktorijum!")
print("✅ Done ...")

# ================================================================================
# Inspekcija fajlova
# ================================================================================
# path = log_file # ili bilo koja druga putanja do fajla
path = data_file
print(f"Putanja: {path}")

# Proveri da li putanja postoji
exists = path.exists()  # True ako postoji
print(f"Postoji: {exists}")

is_file = path.is_file()  # True ako je fajl
print(f"Fajl: {is_file}")

is_dir = path.is_dir()  # True ako je direktorijum
print(f"Direktorijum: {is_dir}")

is_symlink = path.is_symlink()  # True ako je simbolički link
print(f"Simbolički link: {is_symlink}")

size = path.stat().st_size  # Veličina fajla u bajtovima
print(f"Veličina: {size} bajtova")

modified_time = path.stat().st_mtime  # Vreme poslednje izmene
print(f"Vreme poslednje izmene: {modified_time}")
# Output: Vreme poslednje izmene: 1697041234.56789

created_time = path.stat().st_ctime  # Vreme kreiranja fajla
print(f"Vreme kreiranja: {created_time}")
# Output: Vreme kreiranja: 1697031234.56789

# Sažetak inspekcije
print(f"Postoji: {exists}, Fajl: {is_file}, Dir: {is_dir}, Symlink: {is_symlink}")
print(f"Veličina: {size} bajtova")
print(f"Modifikovano: {modified_time}, Kreirano: {created_time}")
print()
# NAPOMENA: Vremena su u sekundama od epoch (1970-01-01)
# Možete koristiti datetime.fromtimestamp() za čitljiv format

# Imena fajlova i ekstenzije
filename = path.name  # Ime fajla sa ekstenzijom
print(f"Ime fajla: {filename}")

stem = path.stem  # Ime fajla bez ekstenzije
print(f"Ime fajla bez ekstenzije: {stem}")

suffix = path.suffix  # Ekstenzija fajla (npr. .txt)
print(f"Ekstenzija fajla: {suffix}")

suffixes = path.suffixes  # Sve ekstenzije (npr. .tar.gz)
print(f"Sve ekstenzije fajla: {suffixes}")
print()

# Meta podaci o putanji
parent = path.parent  # Roditeljski direktorijum
print(f"Roditeljski direktorijum (direktorijum u kojem se fajl nalazi): {parent}")

parts = path.parts  # Svi delovi putanje kao tuple
print(f"Svi delovi putanje: {parts}")

absolute = path.resolve()  # Apsolutna putanja
print(f"Apsolutna putanja: {absolute}")

relative = path.relative_to(home)  # Relativna putanja od home

# Sažetak meta podataka o putanji
print(f"Relativna putanja od home: {relative}")
print(f"Path parts: {parts}")
print(f"Filename: {filename}, Stem: {stem}, Suffix: {suffix}, Suffixes: {suffixes}")
print(f"Parent direktorijum trenutnog fajla: {parent}")
print()

# Meta podaci o fajlu
stat = path.stat()  # Ukupna statistika fajla
print(f"Statistika fajla: {stat}")

mode = stat.st_mode  # Dozvole fajla
print(f"Mode (dozvole): {mode}")
# NAPOMENA: mode je u oktalnom formatu, može se koristiti za provere dozvola
# '33188' je decimalni prikaz oktalnog '0o100644'- regularni fajl sa rw-r--r-- dozvolama

inode = stat.st_ino  # Inode broj
print(f"Inode broj: {inode}")
# NAPOMENA: inode je jedinstveni identifikator fajla na fajl sistemu
# '202646' je primer inode broja za fajl i predstavlja lokaciju fajla na disku

device = stat.st_dev  # Uređaj na kojem je fajl
print(f"Uređaj (device) broj: {device}")
# NAPOMENA: device identifikuje fizički uređaj (disk) na kojem se fajl nalazi
# '2096' je primer device broja koji predstavlja određeni disk ili particiju

nlink = stat.st_nlink  # Broj hard linkova na fajl
print(f"Broj hard linkova: {nlink}")
# NAPOMENA: nlink pokazuje koliko imena (linkova) ukazuje na isti inode
# '1' znači da postoji samo jedan link za ovaj fajl u fajl sistemu.
# Veći od 1, fajl ima više linkova sto znači da više imena ukazuje na isti sadržaj fajla

uid = stat.st_uid  # User ID vlasnika fajla
print(f"UID vlasnika: {uid}")
# NAPOMENA: 'uid' identifikuje korisnika koji je vlasnik fajla
# '1000' je primer 'uid' broja koji predstavlja određenog korisnika na sistemu

gid = stat.st_gid  # Group ID vlasnika fajla
print(f"GID vlasnika: {gid}")
# NAPOMENA: 'gid' identifikuje grupu koja je vlasnik fajla
# '1000' je primer 'gid' broja koji predstavlja određenu grupu na sistemu

# Sažetak meta podataka o fajlu
print(f"Mode: {mode}, Inode: {inode}, Device: {device}")
print(f"Nlink: {nlink}, UID: {uid}, GID: {gid}")
print()

# Meta podeaci o veličini, vremenu i dozvolama (permissions)
stat = path.stat()
print(f"Statistika fajla: {stat}")

size = stat.st_size  # Veličina fajla u bajtovima
print(f"Veličina fajla: {size} bajtova")

atime = stat.st_atime  # Vreme poslednjeg pristupa
print(f"Vreme poslednjeg pristupa: {atime}")

mtime = stat.st_mtime  # Vreme poslednje izmene
print(f"Vreme poslednje izmene: {mtime}")

ctime = stat.st_ctime  # Vreme kreiranja fajla
print(f"Vreme kreiranja fajla: {ctime}")

permissions = stat.st_mode  # Dozvole fajla
print(f"Dozvole (mode): {permissions}")

# Sažetak meta podataka o veličini, vremenu i dozvolama
print(f"Veličina: {size} bajtova")
print(f"Pristup: {atime}, Modifikacija: {mtime}, Kreiranje: {ctime}")
print(f"Dozvole (mode): {permissions}")
print()

# Timestamps u čitljivom formatu (datetime)
mtime_readable = datetime.fromtimestamp(mtime)
print(f"Vreme poslednje izmene (čitljivo): {mtime_readable}")
print()

# ================================================================================
# Čitanje fajlova
# ================================================================================

# 1. Textualno čitanje celog fajla
content = path.read_text(encoding="utf-8")
print(f"Sadržaj fajla:\n{content}")
# NAPOMENA: Ova metoda čita ceo tekstualni fajl u memoriju kao string.
# Pogodna je za male do srednje velike fajlove gde je potrebno brzo čitanje.
print("✅ Done ...")


# 2. Text fajl sa error handling-om (provera postojanja)
def read_text_safely(file_path: Path) -> str:
    """Čitanje tekstualnog fajla sa proverom postojanja"""
    if not file_path.exists():
        raise FileNotFoundError(f"Fajl ne postoji: {file_path}")
    return file_path.read_text(encoding="utf-8")


read_text_safely(path)
# NAPOMENA: Ova metoda čita fajl samo ako postoji, inače baca grešku.
# Korisno za izbegavanje grešaka prilikom čitanja nepostojećih fajlova.
print("✅ Done ...")


# 3. Čitanje fajla liniju po liniju (generator, memory efficient)
def read_file_lines(file_path: Path) -> None:
    """Čitanje fajla liniju po liniju"""
    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())  # strip() uklanja whitespace i nove linije


read_file_lines(path)
# NAPOMENA: Ova metoda je memory efficient jer ne učitava ceo fajl u memoriju odjednom.
# Umesto toga, čita fajl liniju po liniju, što je korisno za velike fajlove.
# Možete prilagoditi obradu svake linije unutar petlje prema potrebama.
print("✅ Done ...")


# 4. Čitanje fajla u blokovima (chunking)
def read_file_in_chunks(file_path: Path, chunk_size: int = 1024) -> None:
    """Čitanje fajla u blokovima od chunk_size bajtova"""
    with file_path.open("r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            print(chunk)


read_file_in_chunks(path, chunk_size=50)
# NAPOMENA: Ova metoda je korisna za veoma velike fajlove gde je potrebno
# čitanje u manjim delovima (chunkovima) kako bi se smanjila potrošnja memorije.
# Možete prilagoditi chunk_size prema potrebama.
# chunk_size je broj bajtova koji se čitaju u jednom potezu.
# Funkcionise za tekstualne fajlove, ali može se prilagoditi i za binarne fajlove.
print("✅ Done ...")


# 5. Čitanje binarnog fajla sa error handling-om
def read_binary_safely(file_path: Path) -> bytes:
    """Čitanje binarnog fajla sa proverom postojanja"""
    if not file_path.exists():
        raise FileNotFoundError(f"Fajl ne postoji: {file_path}")
    return file_path.read_bytes()


read_binary_safely(path)
# NAPOMENA: Ova metoda čita fajl u binarnom modu i vraća sadržaj kao bytes objekat.
# Korisno za čitanje slika, PDF-ova i drugih binarnih fajlova. (ne tekstualni fajlovi)
print("✅ Done ...")


# 6. CSV čitanje fajla sa Pathlib i DictReader-om
def read_csv_file(file_path: Path) -> None:
    """Čitanje CSV fajla koristeći pathlib i csv.DictReader"""
    with file_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


read_csv_file(path)
# NAPOMENA: Ova metoda koristi csv modul za čitanje CSV fajlova.
# csv.DictReader vraća svaku liniju kao rečnik gde su ključevi nazivi kolona.
# Ovo olakšava pristup podacima po imenu kolone umesto po indeksu.
print("✅ Done ...")


# 7. Čitanje fajla sa specificiranim encoding-om
def read_file_with_encoding(file_path: Path, encoding: str = "utf-8") -> str:
    """Čitanje fajla sa specificiranim encoding-om"""
    return file_path.read_text(encoding=encoding)


read_file_with_encoding(path, encoding="utf-8")
# NAPOMENA: Ova metoda omogućava čitanje fajlova sa različitim encoding-ima.
# Podrazumevani encoding je "utf-8", ali možete navesti i druge kao "latin-1", "utf-16".
# Ovo je korisno kada radite sa fajlovima koji nisu u UTF-8 formatu.
print("✅ Done ...")

# ================================================================================
# Zapisivanje u fajlove
# ================================================================================
new_file = Path(__file__).parent / "data" / "new_file.txt"
print(f"Putanja do novog fajla za zapisivanje: {new_file}")
# 1. Textualno zapisivanje celog fajla
new_content = "Ovo je novi sadržaj fajla.\nDruga linija teksta."
new_file.write_text(new_content, encoding="utf-8")
print(f"Sadržaj je zapisan u fajl: {new_file}")
# NAPOMENA: Ova metoda prepisuje ceo fajl novim sadržajem.
# Pogodna je za brzo zapisivanje malih do srednje velikih tekstualnih fajlova.
print("✅ Done ...")

# 2. Binary zapisivanje celog fajla
binary_file = Path(__file__).parent / "data" / "image.png"
print(f"Putanja do binarnog fajla za zapisivanje: {binary_file}")
new_binary_content = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00"
binary_file.write_bytes(new_binary_content)
print(f"Binarni sadržaj je zapisan u fajl: {binary_file}")
# NAPOMENA: Ova metoda prepisuje ceo fajl novim binarnim sadržajem.
# Korisno za zapisivanje slika, PDF-ova i drugih binarnih fajlova.
# Nikako ne koristite za tekstualne fajlove!
print("✅ Done ...")

# 3. Dodavanje teksta na kraj fajla (append)
with new_file.open("a", encoding="utf-8") as f:
    f.write("\nOvo je dodatna linija na kraj fajla.")
print(f"Dodat tekst na kraj fajla: {new_file}")
# NAPOMENA: Ova metoda otvara fajl dodaje novi sadržaj na kraj fajla.(append mode)
# Korisno za log fajlove ili kada želite sačuvati postojeći sadržaj i dodati novi.
# Obavezno koristite "a" mod za dodavanje, a ne "w" koji prepisuje fajl.
print("✅ Done ...")


# 4. Safe overwrite sa backup-om
def safe_overwrite(file_path: Path, content: str) -> None:
    """Sigurno prepisivanje fajla sa backup-om"""
    if file_path.exists():
        backup_path = file_path.with_suffix(file_path.suffix + ".bak")
        file_path.rename(backup_path)
        print(f"Napravljen backup fajla: {backup_path}")
    file_path.write_text(content, encoding="utf-8")


safe_overwrite(new_file, "Tekst koji se prepisuje preko postojećeg fajla.")
print(f"Sigurno kreiran novi fajl: {new_file}")
# NAPOMENA: Ova metoda pravi backup postojećeg fajla pre prepisivanja.
# Backup fajl dobija ekstenziju ".bak".
# Ovo je korisno kada želite sačuvati prethodnu verziju fajla pre izmene.
print("✅ Done ...")


# 5. Safe append sa kreiranjem backup-a starih podataka
def safe_append(file_path: Path, content: str) -> None:
    """Sigurno dodavanje teksta uz backup originala."""
    if file_path.exists():
        backup_path = file_path.with_suffix(file_path.suffix + ".bak")
        backup_path.write_bytes(file_path.read_bytes())  # Pravi tačnu kopiju fajla
        print(f"Napravljen backup fajla pre dodavanja: {backup_path}")
    with file_path.open("a", encoding="utf-8") as f:
        f.write(content)


safe_append(new_file, "\nJoš jedna linija dodata sa backup-om.")
print(f"Sigurno dodat tekst na kraj fajla: {new_file}")
# NAPOMENA: Ova metoda pravi backup postojećeg fajla pre dodavanja novog sadržaja.
# Backup fajl dobija ekstenziju ".bak".
# Korisno kada želite sačuvati prethodnu verziju fajla pre dodavanja novih podataka.
# Koristimo write_bytes i read_bytes da bismo napravili tačnu kopiju fajla!
# Za tekstualne fajlove možemo koristiti i read_text i write_text umesto bytes metoda!
# Fajl ima i tekstualni i binarni sadržaj -> bytes metode su sigurnije za tačnu kopiju!
print("✅ Done ...")


# 6. CSV zapisivanje fajla sa Pathlib-om i csv.writer-om
def write_csv_file(file_path: Path, rows: list[list[str]]) -> None:
    """Zapisivanje CSV fajla koristeći pathlib i csv.writer"""
    with file_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


csv_file = Path(__file__).parent / "data" / "output.csv"
rows = [["name", "age"], ["Ana", "28"], ["Marko", "35"], ["Jelena", "22"]]
write_csv_file(csv_file, rows)
print(f"CSV fajl je zapisan: {csv_file}")
# NAPOMENA: Ova metoda koristi csv modul za zapisivanje CSV fajlova.
# csv.writer omogućava lako zapisivanje redova podataka u CSV format.
print("✅ Done ...")


# ================================================================================
# Kreiranje Direktorijuma
# ================================================================================

# 1. Kreiranje direktorijuma i svih roditeljskih direktorijuma
new_dir = Path(__file__).parent / "data" / "output" / "logs"
new_dir.mkdir(parents=True, exist_ok=True)
print(f"Kreiran direktorijum: {new_dir}")
# NAPOMENA:
# Ova metoda kreira dir zajedno sa svim nepostojećim roditeljskim direktorijumima.
# Korisno kada želite kreirati duboku hijerarhiju direktorijuma odjednom.
# exist_ok=True znači da neće biti greške ako direktorijum već postoji.
# exist_ok=False, baca FileExistsError ako direktorijum postoji.
# parents=True znači da će se kreirati svi roditeljski direktorijumi ako ne postoje.
print("✅ Done ...")


# 2. Helper funkcija za kreiranje direktorijuma
def ensure_dir(path: Path) -> Path:
    """Kreiraj dir ako ne postoji, vrati Path."""
    path.mkdir(parents=True, exist_ok=True)
    return path


ensured_dir = ensure_dir(Path(__file__).parent / "data" / "temp")
print(f"Kreiran ili osiguran direktorijum: {ensured_dir}")
# NAPOMENA:
# Ova funkcija pojednostavljuje kreiranje direktorijuma sa roditeljima.
# Vraća Path objekat za dalje korišćenje.
print("✅ Done ...")

# Proveri pre kreiranja
dir_to_create = Path(__file__).parent / "data" / "reports"
if not dir_to_create.exists():
    dir_to_create.mkdir(parents=True)
    print(f"Kreiran direktorijum: {dir_to_create}")
else:
    print(f"Direktorijum već postoji: {dir_to_create}")
# NAPOMENA:
# Ova metoda proverava postojanje pre kreiranja direktorijuma.
# Korisno kada želite izbeći greške ili nepotrebne operacije kreiranja.
print("✅ Done ...")

# 3. Kreiranje privremenog direktorijuma unutar sistema uz pomoć tempfile modula

with tempfile.TemporaryDirectory() as temp_dir:
    temp_path = Path(temp_dir)
    print(f"Kreiran privremeni direktorijum: {temp_path}")
    # Rad sa privremenim fajlovima unutar temp_path
    temp_file = temp_path / "temp_file.txt"
    temp_file.write_text("Ovo je privremeni fajl.", encoding="utf-8")
    print(f"Privremeni fajl kreiran: {temp_file}")
# NAPOMENA:
# Ova metoda koristi tempfile modul za kreiranje privremenog direktorijuma.
# Direktorijum i svi njegovi fajlovi se brišu automatski kada se izađe iz with bloka.
# Korisno za testiranje ili privremene operacije bez ostavljanja tragova na disku.
# tempfile se ne koristi ako imate pytest tmp_path fixture.
print("✅ Done ...")

# ================================================================================
# Globovanje fajlova(pretraga fajlova po šablonu
# Traversal direktorijuma(prolaz/walk kroz direktorijume)
# ================================================================================

# 1. Iteracija kroz dir (nerekurzivno)
data_dir = Path(__file__).parent / "data"
for item in data_dir.iterdir():
    if item.is_file():
        print(f"Fajl u direktorijumu [{data_dir}]: {item.name}")
    elif item.is_dir():
        print(f"Direktorijum u direktorijumu [{data_dir}]: {item.name}")
# NAPOMENA:
# Ova metoda iterira kroz sve stavke (fajlove i direktorijume) u datom direktorijumu.
# Ne prolazi rekurzivno kroz poddirektorijume.
print("✅ Done ...")

# 2. Globovanje fajlova po šablonu ("*.csv") nerekurzivno
for csv_file in data_dir.glob("*.csv"):
    print(f"CSV fajl pronađen: {csv_file.name}")
# NAPOMENA:
# Ova metoda pronalazi sve fajlove koji se poklapaju sa šablonom u datom direktorijumu.
# Ne prolazi rekurzivno kroz poddirektorijume.
print("✅ Done ...")

# Drugi način globovanja (lokup uz obrazac)
csv_files = list(Path("data").glob("*.csv"))
print(f"Pronađeni CSV fajlovi: {csv_files}")
# Output: [PosixPath('data/products.csv'), PosixPath('data/output.csv')]
# Ova metoda vraća listu svih CSV fajlova u "data" direktorijumu.
# Možete koristiti različite šablone kao "*.txt", "data_*.csv", itd.
# Ne prolazi rekurzivno kroz poddirektorijume.
# Korisno za brzo pronalaženje fajlova po tipu ili obrascu imena
print("✅ Done ...")

# 3. Rekurzivno globovanje fajlova po šablonu ("**/*.json")
json_files = list(Path("data").rglob("**/*.json"))
for json_file in json_files:
    if json_file.is_file():
        print(f"JSON fajl pronađen rekurzivno: {json_file}")
    else:
        print(f"Nije pronađen JSON fajl: {json_file}")

# NAPOMENA:
# Ova metoda pronalazi sve fajlove koji se poklapaju sa šablonom rekurzivno!
# Pretražuje sve poddirektorijume unutar datog direktorijuma.
# Korisno za pretragu fajlova u dubokim hijerarhijama direktorijuma.
# '*.json' i '**/*.json' su primeri šablona koji se mogu koristiti.
# '**' označava rekurzivno pretraživanje kroz sve poddirektorijume.
print("✅ Done ...")

# 4. Filtriranje po veličini fajla (mali fajlovi < 1KB)
small_files = [
    f for f in Path("data").rglob("*") if f.is_file() and f.stat().st_size < 1024
]
# # rglob("*") za rekurzivno pretraživanje svih fajlova!
# Konverzija comprehension u standardni for loop za bolju čitljivost
# Napomena : Ovo je samo primer za čitljivost!
# Kod iznad je ekvivalentan sledećem kodu:
# small_files = []
# for f in Path("data").rglob("*"): # Prolazak kroz sve fajlove rekurzivno
#     if f.is_file() and f.stat().st_size < 1024:
#         small_files.append(f)
# Za svaki mali fajl, ispiši ime i veličinu
# for f in small_files:
#     print(f"Fajlovi (<1KB): {f} - Veličina: {f.stat().st_size} bajtova")

for small_file in small_files:
    print(
        f"Fajlovi (<1KB): {small_file} - Veličina: {small_file.stat().st_size} bajtova"
    )
# NAPOMENA:
# Ova metoda koristi rglob("*") za rekurzivno pretraživanje svih fajlova.
# Filtrira fajlove koji su manji od 1KB koristeći stat().
# Korisno za pronalaženje malih fajlova u direktorijumu i poddirektorijumima.
print("✅ Done ...")

# 5. Filtriranje fajlova po veličini (> 1KB)
large_files = [
    f for f in data_dir.rglob("*") if f.is_file() and f.stat().st_size > 1024
]
# Konverzija comprehension u standardni for loop za bolju čitljivost
# Napomena : Ovo je samo primer za čitljivost!
# Kod iznad je ekvivalentan sledećem kodu:
# large_files = []
# for f in data_dir.rglob("*"): # Prolazak kroz sve fajlove rekurzivno
#     if f.is_file() and f.stat().st_size > 1024:
#         large_files.append(f)
# Za svaki veliki fajl, ispiši ime i veličinu
# for f in large_files:
#     print(f"Fajlovi (>1KB): {f} - Veličina: {f.stat().st_size} bajtova")

for large_file in large_files:
    print(
        f"Fajl (>1KB): {large_file} - Veličina: {large_file.stat().st_size} bajtova"
    )
# NAPOMENA:
# Ova metoda koristi rglob za rekurzivno pretraživanje svih fajlova.
# Filtrira fajlove koji su veći od 1KB koristeći stat().
# Korisno za pronalaženje velikih fajlova u direktorijumu i poddirektorijumima.
print("✅ Done ...")

# 6. Filtriranje po mtime (novije od X sekundi)
# cutoff = time.time() - 60  # poslednji minut
cutoff = time.time() - 7 * 24 * 60 * 60   # poslednjih 7 dana
recent = [f for f in Path("logs").glob("*.log") if f.stat().st_mtime > cutoff]
for recent_file in recent:
    print(f"Nedavno izmenjeni log fajl: {recent_file}")
# NAPOMENA:
# Ova metoda koristi glob za pronalaženje svih .log fajlova u "logs" direktorijumu.
# Filtrira fajlove koji su izmenjeni u poslednjih 60 sekundi koristeći stat().st_mtime.
# Možete prilagoditi cutoff vreme prema potrebama.
# Računanje je u sekundama od epoch vremena.
# 7 dana = 7 * 24 * 60 * 60 sekundi.
# Poslednjih 2 sata = 2 * 60 * 60 sekundi.
# Nedavno izmenjeni fajlovi, oni čije je vreme poslednje izmene veće od cutoff vremena.
# Ovo je korisno za praćenje nedavnih izmena u log fajlovima.
print("✅ Done ...")

# 7. Sortiranje putanja po imenu fajla
sorted_files = sorted(Path("data").glob("*.csv"), key=lambda p: p.name)
for sorted_file in sorted_files:
    print(f"Sortirani fajl: {sorted_file}")
# NAPOMENA:
# Ova metoda koristi glob za pronalaženje svih .csv fajlova u "data" direktorijumu.
# Sortira fajlove po imenu koristeći sorted() funkciju sa lambda funkcijom kao ključem.
# Možete prilagoditi ključ sortiranja prema potrebama (npr. po veličini, vremenu, itd.).
# Ovo je korisno za organizaciju fajlova pre daljih operacija.
#
print("✅ Done ...")

# ================================================================================
# Copy, Move, Delete fajlova
# ================================================================================

# 1. Copy (read_bytes + write_bytes)
src = Path("data/sample.csv")
dst = Path("backup/in.csv")
dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_bytes(src.read_bytes())
print(f"Kopiran fajl: {src} → {dst}")
# NAPOMENA:
# Koristimo read_bytes() za čitanje binarnog sadržaja iz izvornog fajla
# i write_bytes() za pisanje tog sadržaja u odredišni fajl.
# Ova metoda kopira fajl čitajući ceo sadržaj iz izvornog fajla.
# A zatim piše sadržaj u odredišni fajl.
# Koristi se za kopiranje bilo kog tipa fajla (tekstualni, binarni, slike, itd.).
# Može biti neefikasno za velike fajlove jer učitava ceo fajl u memoriju.
# Alternativno, možete koristiti shutil.copy2(src, dst) za efikasniju kopiju.
# shutil.copy2 čuva i meta podatke fajla (vremena, dozvole).
# Primer:
# import shutil
# src = Path("data/sample.csv")
# dst = Path("backup/in.csv")
# dst.parent.mkdir(parents=True, exist_ok=True)
# shutil.copy2(src, dst)
# print(f"Kopiran fajl koristeći shutil: {src} → {dst}")
print("✅ Done ...")

# 2. Copy sa error handling-om i logging-om
# Definirajte logger (pretpostavimo da je već definisan negde u kodu)
def safe_copy(src: Path, dst: Path) -> None:
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
    except Exception as e:
        logger.exception(f"Copy failed: {src} → {dst}, error: {e}")
        raise
src = Path("data/products.csv")
dst = Path("backup/safe_in.csv")
safe_copy(src, dst)
# NAPOMENA:
# Ova funkcija pokušava da kopira fajl sa izvora na odredište.
# Ako dođe do greške tokom kopiranja, hvata izuzetak i loguje grešku.
# Logger mora biti prethodno definisan.
# Zatim ponovo baca izuzetak kako bi ga pozivajući kod mogao obraditi.
# Ovo je korisno za robustno kopiranje fajlova sa obradom grešaka.
print("✅ Done ...")

# 3. Rename/Move fajl
old = Path("data/products.csv")
new = Path("data/new.csv")
old.rename(new)
print(f"Preimenovan/Moved fajl: {old} → {new}")
# NAPOMENA:
# Ova metoda preimenuje ili premesti fajl sa stare putanje na novu.
# Ako su stara i nova putanja na različitim fajl sistemima, može doći do greške.
# Za premještanje između različitih fajl sistema, koristite shutil.move(old, new).
# Primer:
# import shutil
# old = Path("data/products.csv")
# new = Path("data/moved/products.csv")
# new.parent.mkdir(parents=True, exist_ok=True)
# shutil.move(old, new)
# print(f"Moved fajl koristeći shutil: {old} → {new}")
print("✅ Done ...")

# 4. Delete fajl
path = Path("data/old_file.txt") # primer fajla za brisanje
path.unlink() # baca gresku ako ne postoji
path.unlink(missing_ok=True)  # tiho ignoriše
print(f"Obrisan fajl: {path}")
# NAPOMENA:
# 'unlink()' briše fajl na datoj putanji.
# Ako fajl ne postoji, baca FileNotFoundError.
# Koristeći missing_ok=True, greška se ignoriše ako fajl ne postoji.
print("✅ Done ...")

# 5. Delete prazan direktorijum
path = Path("data/empty_dir") # primer praznog dir za brisanje
# Kreiraj prazan dir za primer
path.mkdir(parents=True, exist_ok=True)
# Sada obriši prazan dir
path.rmdir()
print(f"Obrisan prazan direktorijum: {path}")
# NAPOMENA:
# Ova metoda briše prazan direktorijum na datoj putanji.
# Ako direktorijum nije prazan, baca OSError.
print("✅ Done ...")

# 6. Delete dir sa sadržajem (koristi shutil)
shutil.rmtree(path)
print(f"Obrisan direktorijum sa sadržajem: {path}")
# NAPOMENA:
# Ova metoda briše direktorijum i sav njegov sadržaj rekurzivno.
# Koristi se za brisanje direktorijuma koji nisu prazni.
# Budite oprezni jer ova operacija ne može biti poništena!
print("✅ Done ...")

# ================================================================================
# Symbolički linkovi (Symlinks)
# ================================================================================

link = Path("logs/latest.log")

# 1. Proveri da li je symlink
print(f"Da li je symlink? {link.is_symlink()}")

# 2. Vidi TARGET putanju (resolve prateći link)
target = link.resolve()
print(f"Target putanja: {target}")

# 3. Čitaj readlink (raw symlink target bez resolving-a)
print(f"Raw symlink pokazuje na: {link.readlink()}")

# 1. Kreiranje simboličkog linka(radi samo na Unix sistemima i Windows sa admin pravima)
link = Path("logs/latest.log") # putanja do linka
# ciljna putanja, ne mora da postoji ali ce logs/latest.log baciti gresku ako ne postoji
# Greška se javlja samo kada se pokusa pristupiti fajlu logs/latest.log!
# Fajl logs/latest.log je obrisan ili ne postoji!
target = Path("cli_logging_practice/logs/app_2025-12-23.log")
if link.exists() or link.is_symlink():
    link.unlink()  # ukloni postojeći link ili fajl
link.symlink_to(target)
print(f"Kreiran simbolički link: {link} → {target}")
# NAPOMENA:
# Ova metoda kreira simbolički link na datu putanju.
# Link pokazuje na ciljnu putanju.
# Koristi se za kreiranje prečica ili referenci na fajlove/direktorijume.
print("✅ Done ...")
real_path=link.resolve()
print(f"Stvarna putanja na koju link pokazuje: {real_path}")
print("Resolve: dobij stvarnu putanju iz simboličkog linka!")
print("✅ Done ...")

# 2. Symlink Helper (safe update + check)
def update_symlink(link: Path, target: Path, *, relative: bool = True) -> None:
    """
    Create/update symlink at `link` pointing to `target`.
    - Removes ONLY existing symlinks, not regular files.
    - Uses relative target by default (more robust when moving the project).
    """
    # VAŽNO: Obriši SAMO symlink, ne regularni fajl!
    if link.is_symlink():
        link.unlink()
    elif link.exists():
        raise FileExistsError(
            f"Cannot overwrite regular file: {link}. "
            f"If you want to replace it, delete it manually first."
        )

    if relative:
        # Snimi relativnu putanju kada je moguće
        # (npr., logs/latest.log -> app_2025-12-26.log)
        try:
            target_rel = target.relative_to(link.parent)
        except ValueError:
            # Ako cilj nije unutar link.parent, koristi apsolutnu putanju
            target_rel = target
        link.symlink_to(target_rel)
    else:
        link.symlink_to(target)

update_symlink(link, target, relative=True)
print(f"Ažuriran simbolički link: {link} → {target} (relative=True)")
# NAPOMENA:
# Ova funkcija kreira ili ažurira simbolički link ako
# Uklanja postojeći link ili fajl pre kreiranja novog linka.
# Podrazumevano koristi relativnu putanju za cilj.
# Ako je relativna putanja nemoguća, koristi apsolutnu putanju.
# Ovo je korisno za održavanje simboličkih linkova u projektu.
print("✅ Done ...")

# 3. Symlink proverava da li link pokazuje na cilj
def symlink_points_to(link: Path, target: Path) -> bool:
    """Return True if `link` resolves to `target` (strict check)."""
    try:
        return link.resolve(strict=True) == target.resolve(strict=True)
    except FileNotFoundError:
        return False
points = symlink_points_to(link, target)
print(f"Link {link} pokazuje na cilj {target}: {points}")
# NAPOMENA:
# Ova funkcija proverava da li simbolički link pokazuje na dati cilj.
# Koristi `resolve(strict=True)` za dobijanje stvarne putanje.
# Vraća True ako link pokazuje na cilj, inače False.
print("✅ Done ...")


# 4. Kombinacija: Kreiranje i provera symlinka
link = Path("logs/latest.log")
target = Path("cli_logging_practice/logs/app_2025-12-26.log")

# Update symlink; koristi relativni target unutar logs/
update_symlink(link, target)

# Preskoči ako već ukazuje na isti target
if not symlink_points_to(link, target):
    update_symlink(link, target)

# Resolve i uzmi stvarnu putanju
real_path = link.resolve()  # strict=False
update_symlink(link, target, relative=True)
print(f"Kreiran i potvrđen simbolički link: {link} → {target}")
# NAPOMENA:
# Ovaj kod kombinuje kreiranje i proveru simboličkog linka.
# Prvo ažurira link koristeći relativni cilj.
# Zatim proverava da li link već pokazuje na isti cilj.
# Ako ne pokazuje, ponovo ažurira link.
# Na kraju, koristi `resolve()` za dobijanje stvarne putanje.
print("✅ Done ...")


# 5. Pytest primer

def test_update_symlink(tmp_path: Path):
    logs = tmp_path / "logs"
    logs.mkdir()
    target = logs / "app_2025-12-23.log"
    target.write_text("data", encoding="utf-8")
    link = logs / "latest.log"

    # First create
    update_symlink(link, target)
    assert link.is_symlink()
    assert link.resolve(strict=True) == target

    # Update to a new target
    new_target = logs / "app_2025-12-24.log"
    new_target.write_text("new", encoding="utf-8")
    update_symlink(link, new_target)
    assert link.resolve(strict=True) == new_target


def test_symlink_points_to(tmp_path: Path):
    base = tmp_path
    t1 = base / "file1.txt"
    t1.write_text("one", encoding="utf-8")
    t2 = base / "file2.txt"
    t2.write_text("two", encoding="utf-8")
    link = base / "latest.txt"
    update_symlink(link, t1)

    assert symlink_points_to(link, t1) is True
    assert symlink_points_to(link, t2) is False
# NAPOMENA:
# Ovi testovi koriste pytest tmp_path fixture za kreiranje privremenih direktorijuma
# Testiraju funkcije za kreiranje i proveru simboličkih linkova.
# Osiguravaju da funkcije rade ispravno u izolovanom okruženju.
print("✅ Done ...")

# 6. # Testing sa tmp_path fixture
def test_write_read_roundtrip(tmp_path: Path):
    """Test pisanje i čitanje fajla."""
    file = tmp_path / "test.txt"
    file.write_text("Hello", encoding="utf-8")
    assert file.read_text(encoding="utf-8") == "Hello"

def test_mkdir_creates_parents(tmp_path: Path):
    """Test da mkdir kreira sve roditelje."""
    nested = tmp_path / "a" / "b" / "c"
    nested.mkdir(parents=True, exist_ok=True)
    assert nested.exists()
    assert nested.is_dir()

def test_glob_filters_by_extension(tmp_path: Path):
    """Test glob pattern filtriranje."""
    (tmp_path / "file1.csv").touch()
    (tmp_path / "file2.txt").touch()
    (tmp_path / "file3.csv").touch()

    csv_files = list(tmp_path.glob("*.csv"))
    assert len(csv_files) == 2
    assert all(f.suffix == ".csv" for f in csv_files)
# NAPOMENA:
# Ovi testovi koriste pytest tmp_path fixture za kreiranje privremenih direktorijuma
# Testiraju osnovne operacije sa fajlovima i direktorijumima koristeći pathlib metode.
# Osiguravaju da funkcije rade ispravno u izolovanom okruženju.
print("✅ Done ...")

# ================================================================================
# Logging sa Path
# ================================================================================
logger = logging.getLogger(__name__)

def process_file(path: Path) -> None:
    """Process fajl sa logovanjem."""
    logger.info(f"Processing file: {path.resolve()}")

    if not path.exists():
        logger.error(f"File not found: {path}")
        raise FileNotFoundError(path)

    try:
        content = path.read_text(encoding="utf-8")
        logger.debug(f"Read {len(content)} chars from {path.name}")
    except Exception:
        logger.exception(f"Failed to read {path}")
        raise
    # Dalja obrada fajla...
    logger.info(f"Successfully processed file: {path.name}")
test_path = Path("data/sample.csv")
process_file(test_path)
# NAPOMENA:
# Ova funkcija demonstrira korišćenje logging modula sa pathlib.
# Loguje različite nivoe informacija tokom obrade fajla.
# Koristi resolve() za dobijanje apsolutne putanje fajla u logovima.
# Logovanje pomaže u praćenju toka izvršavanja i grešaka.
print("✅ Done ...")

# ================================================================================
# Error Handling patterns
# ================================================================================

def read_config(path: Path) -> dict[str, str]:
    """Čitaj config sa jasnim error porukama."""
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path.resolve()}")

    if not path.is_file():
        raise ValueError(f"Expected file, got directory: {path}")

    if path.suffix != ".json":
        raise ValueError(f"Expected .json file, got: {path.suffix}")

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {path}: {e}") from e

def get_latest_backup(backup_dir: Path) -> Path | None:
    """Najnoviji backup fajl ili None."""
    if not backup_dir.exists():
        return None

    backups = list(backup_dir.glob("backup_*.csv"))
    if not backups:
        return None

    return max(backups, key=lambda p: p.stat().st_mtime)

