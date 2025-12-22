"""
Faza 1: Path Basics - Exercises
"""
from pathlib import Path

# FAZA 1 (2h) — Osnove Path

# Napravi `path_basics.py` sa 12+ primera:
# cwd, home, __file__, parent, parents, resolve,relative_to, expanduser, `/` operator.

# ================================================================================
# Primeri rešenja:
# ================================================================================

# ========== Osnovne operacije sa Path ===========================================

# ================================================================================
# 1. Prikaži trenutni radni dir.
# ================================================================================
def current_working_directory():
    """Prikaži trenutni radni direktorijum"""
    cwd = Path.cwd()
    print(f"Trenutni radni direktorijum: {cwd}")

# ================================================================================
# 2. Prikaži home dir korisnika.
# ================================================================================
def user_home_directory():
    """Prikaži home direktorijum korisnika"""
    home = Path.home()
    print(f"Home direktorijum korisnika: {home}")

# Napomena:
# `home` može biti različit na različitim OS-ovima.
# Linux/Mac -> `/home/username` ili `/Users/username`, na Windows-u `C:\Users\username`
# Koristi `Path.home()` da bi dobio ispravnu putanju bez obzira na OS.

# ================================================================================
# 3. Prikaži putanju do trenutnog fajla.
# ================================================================================
def current_file_path():
    """Prikaži putanju do trenutnog fajla"""
    current_file = Path(__file__).resolve() # resolve da dobiješ apsolutnu putanju
    print(f"Putanja do trenutnog fajla: {current_file}")

# ================================================================================
# 4. Prikaži parent dir trenutnog fajla.
# ================================================================================
def parent_directory():
    """Prikaži roditeljski direktorijum trenutnog fajla"""
    parent = Path(__file__).resolve().parent
    print(f"Parent direktorijum trenutnog fajla: {parent}")

# ================================================================================
#  5. Prikaži sve roditeljske dir-ove trenutnog fajla.
# ================================================================================
def all_parent_directories():
    """Prikaži sve roditeljske direktorijume trenutnog fajla"""
    parents = Path(__file__).resolve().parents
    print("Svi roditeljski direktorijumi trenutnog fajla:")
    for p in parents:
        print(p)

# ================================================================================
# 6. Prikaži apsolutnu putanju do fajla `../data/sample.txt` u odnosu na trenutni fajl.
# ================================================================================
def absolute_path_to_sample():
    """Apsolutna putanja do ../data/sample.txt u odnosu na trenutni fajl"""
    sample_path = (Path(__file__).resolve().parent / "../data/sample.txt").resolve()
    print(f"Apsolutna putanja do sample.txt: {sample_path}")

# ================================================================================
# 7. Prikaži relativnu putanju od home do trenutnog fajla.
# ================================================================================
def relative_path_from_home():
    """Relativna putanja od home do trenutnog fajla"""
    home = Path.home()
    current_file = Path(__file__).resolve()
    relative_path = current_file.relative_to(home)
    print(f"Relativna putanja od home do trenutnog fajla: {relative_path}")

# ================================================================================
# 8. Prikaži putanju do fajla `~/documents/report.txt` sa proširenim home.
# ================================================================================
def expanded_home_path():
    """Putanja do ~/documents/report.txt sa proširenim home"""
    report_path = Path("~/documents/report.txt").expanduser()
    print(f"Putanja do report.txt sa proširenim home: {report_path}")

# ================================================================================
# 9. Spoji putanju `data` i `output` koristeći `/` operator.
# ================================================================================
def join_paths():
    """Spoji putanju data i output koristeći / operator"""
    combined_path = Path("data") / "output"
    print(f"Spojena putanja: {combined_path}")

# ================================================================================
# Zadaci:
# ================================================================================

# 1. Spoji putanje za `data/users.csv` i `logs/app.log` bez `os.path`.
data_path = Path("data") / "users.csv"
log_path = Path("logs") / "app.log"
print(f"Data path: {data_path.resolve()}")
print(f"Log path: {log_path.resolve()}")

# 2. Prikaži `stem`, `suffix`, `suffixes`, `name` za primer fajl.
example_file = Path("/home/user/docs/report.tar.gz")
print(f"Stem: {example_file.stem}")
print(f"Suffix: {example_file.suffix}")
print(f"Suffixes: {example_file.suffixes}")
print(f"Name: {example_file.name}")

# 3. Napravi funkciju
# `def ensure_dir(path: Path) -> Path` koja kreira dir ako ne postoji i vrati ga.
# Test hint: koristi `tmp_path / "a" / "b"` za kreiranje strukture.
# Output hint: `print(path.resolve())` da vidiš realnu putanju.

def ensure_dir(path: Path) -> Path:
    """Kreiraj direktorijum ako ne postoji i vrati putanju"""
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return path

# 4. Napravi helper
# type: ignore # def normalize(raw: str) -> Path` koji radi `expanduser().resolve()` i baca `ValueError` ako nema suffix.
def normalize(raw: str) -> Path:
    """Normalizuj putanju i baci ValueError ako nema suffix"""
    path = Path(raw).expanduser().resolve()
    if not path.suffix:
        raise ValueError("Path must have a suffix")
    return path

# Primeri korišćenja:
if __name__ == "__main__":
    current_working_directory()
    user_home_directory()
    current_file_path()
    parent_directory()
    all_parent_directories()
    absolute_path_to_sample()
    relative_path_from_home()
    expanded_home_path()
    join_paths()
    data_path = Path("data") / "users.csv"
    log_path = Path("logs") / "app.log"
    print(f"Data path: {data_path.resolve()}")
    print(f"Log path: {log_path.resolve()}")

    example_file = Path("/home/user/docs/report.tar.gz")
    print(f"Stem: {example_file.stem}")
    print(f"Suffix: {example_file.suffix}")
    print(f"Suffixes: {example_file.suffixes}")
    print(f"Name: {example_file.name}")

    dir_path = ensure_dir(Path("output/data"))
    print(f"Ensured directory: {dir_path.resolve()}")

    try:
        normalized_path = normalize("~/documents/file.txt")
        print(f"Normalized path: {normalized_path}")
    except ValueError as e:
        print(e)

# Napomena:
# 1. `__file__` može biti relativan, zato koristimo `resolve()`.
# 2. `Path.cwd()` vraća trenutni radni direktorijum.
# 3. `Path.home()` vraća home direktorijum korisnika.
# 4. `resolve()` vraća apsolutnu putanju.
# 5. `parent` vraća roditeljski direktorijum.
# 6. `parents` vraća sve roditeljske direktorijume kao listu.
# 7. `expanduser()` proširuje `~` na home direktorijum korisnika.
# 8. `/` operator se koristi za spajanje putanja.
# 9. `relative_to()` vraća relativnu putanju u odnosu na dati direktorijum.
# 10. `suffix`, `suffixes`, `stem`, `name` daju informacije o fajlu.
# 11. `mkdir()` kreira direktorijum.
# 12. `exists()` proverava da li putanja postoji.
# 13. Baci `ValueError` ako putanja nema suffix.
# 14. Uvek koristi `Path` umesto stringova za putanje.
# 15. Testiraj funkcije koristeći `pytest` i `tmp_path` fixture.

# Kraj faze 1
