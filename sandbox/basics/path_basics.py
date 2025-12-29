"""
Path Basics - Refaktorisano za testove (Dan 6-7)

Cilj: Sve funkcije vraćaju vrednosti umesto print()
Fokus: cwd, home, __file__, parent, parents, resolve, relative_to, expanduser, `/`
Operator, metapodaci fajlova, direktorijumi
Struktura: 4 sekcije sa najmanje 8+ funkcija u prvoj sekciji, 3+ u ostalim
Komentari: Detaljni docstring-komentari sa primerima i napomenama

VAŽNO: Sve funkcije su testirane kroz testove u sandbox/basics/tests/test_path_basics.py
"""

from pathlib import Path

# ======================================================================================
# SEKCIJA 1: Osnovne Path operacije (8+ funkcija)
# ======================================================================================


def get_current_working_directory() -> Path:
    """
    Vrati trenutni radni direktorijum (cwd).

    Returns:
        Path: Absolutna putanja do trenutnog radnog direktorijuma.

    Napomena:
        - `cwd` može biti različit na različitim mestima gde se pokreće skripta
        - Koristi `Path.cwd()` da bi dobio ispravnu putanju bez obzira na OS
        - Selektuj testove: pytest -k "test_get_current_working"
    """
    return Path.cwd()


def get_user_home_directory() -> Path:
    """
    Vrati home direktorijum korisnika.

    Returns:
        Path: Putanja do home direktorijuma korisnika.

    Napomena:
        - Linux/Mac: `/home/username` ili `/Users/username`
        - Windows: `C:\\Users\\username`
        - `Path.home()` automatski detektuje OS
        - Koristi `Path.home()` umesto `~` za bolje kompatibilnost
    """
    return Path.home()


def get_current_file_path() -> Path:
    """
    Vrati apsolutnu putanju do trenutne Python skripte.

    Returns:
        Path: Apsolutna putanja do fajla (__file__).

    Napomena:
        - `__file__` može biti relativan u nekim slučajevima
        - `resolve()` pretvara relativnu putanju u apsolutnu
        - Uvek koristi `resolve()` sa `__file__` za sigurnost
    """
    return Path(__file__).resolve()


def get_parent_directory() -> Path:
    """
    Vrati roditeljski direktorijum trenutne Python skripte.

    Returns:
        Path: Putanja do parent direktorijuma.

    Napomena:
        - `.parent` daje jedan nivo iznad trenutnog fajla
        - Za više nivoa, koristi `.parents` iterator
        - `.parents[1]` za dva nivoa iznad fajla, `.parents[2]` za tri, itd.
        - Primena: pronalaženje putanje direktorijuma u kom se nalazi skripta
        - Selektuj testove: pytest -k "test_get_parent_directory"
    """
    return Path(__file__).resolve().parent


def get_all_parent_directories() -> list[Path]:
    """
    Vrati sve roditeljske direktorijume trenutne skripte kao listu.

    Returns:
        list[Path]: Lista svih parent direktorijuma (od bližeg ka daljem).

    Primer:
        Ako je skripta u /home/user/project/src/utils/helper.py:
        - Vraća: [
            /home/user/project/src/utils,
            /home/user/project/src,
            /home/user/project,
            /home/user,
            /home,
            /
        ]

    Napomena:
        - `.parents` je iterator, zato koristimo `list()` za konverziju
        - Redosled je od bližeg ka daljem roditeljskom direktorijumu
        - Može se koristiti za navigaciju kroz hijerarhiju direktorijuma
        - Selektuj testove: pytest -k "test_get_all_parent_directories"
    """
    return list(Path(__file__).resolve().parents)

def get_absolute_path(relative_path: str) -> Path:
    """
    Konvertuj relativnu putanju u apsolutnu na osnovu lokacije trenutne skripte.

    Args:
        relative_path: Relativna putanja (primer: "../data/file.txt").

    Returns:
        Path: Apsolutna putanja.

    Primer:
        >>> path = get_absolute_path("../data/sample.txt")
        >>> path.exists()
        True
    """
    base = Path(__file__).resolve().parent
    return (base / relative_path).resolve()


def get_relative_path_from_home() -> Path | None:
    """
    Vrati relativnu putanju od home direktorijuma do trenutne skripte.

    Returns:
        Optional[Path]: Relativna putanja ili None ako skripta nije u home direktorijumu

    Primer:
        Ako je home /home/user i skripta je u /home/user/projects/script.py:
        >>> get_relative_path_from_home()
        Path('projects/script.py')

    Napomena:
        - Koristi `relative_to()` za dobijanje relativne putanje
        - Baca ValueError ako skripta nije unutar home direktorijuma
        - U tom slučaju vraća None umesto greške
        - Selektuj testove: pytest -k "test_get_relative_path_from_home"
    """
    try:
        home = Path.home()
        current_file = Path(__file__).resolve()
        return current_file.relative_to(home)
    except ValueError:
        # Skripta nije u home direktorijumu
        return None


def expand_home_path(path_with_tilde: str) -> Path:
    """
    Proširi `~` na home direktorijum i vrati apsolutnu putanju.

    Args:
        path_with_tilde: Putanja sa `~` (primer: "~/documents/report.txt").

    Returns:
        Path: Apsolutna putanja.

    Primer:
        >>> expand_home_path("~/documents/file.txt")
        Path('/home/user/documents/file.txt')

    Napomena:
        - `expanduser()` automatski detektuje home direktorijum
        - Radi na svim operativnim sistemima
        - Koristi se za korisnički unete putanje koje počinju sa `~`
        - Selektuj testove: pytest -k "test_expand_home_path"
    """
    return Path(path_with_tilde).expanduser()

def join_paths(base: str, *parts: str) -> Path:
    """
    Spoji više putanja koristeći `/` operator (cross-platform safe).

    Args:
        base: Bazna putanja kao string.
        *parts: Dodatne (string) putanje za spajanje sa baznom putanjom.
        *parts: Varijabilan broj string argumenata koji predstavljaju delove putanje.
        *parts: Svaki deo može biti direktorijum ili fajl.

    Returns:
        Path: Spojena putanja kao Path objekat.

    Primer:
        >>> join_paths("data", "input", "2025-12", "users.csv")
        Path('data/input/2025-12/users.csv')

    Napomena:
        - `/` operator automatski prilagođava separatore za svaki OS
        - Bolji je nego `os.path.join()` jer radi sa Path objektima
        - Selektuj testove: pytest -k "test_join_paths"
    """
    result = Path(base)
    for part in parts:
        result = result / part
    return result


# ======================================================================================
# SEKCIJA 2: File metapodaci (3+ funkcije)
# ======================================================================================


def get_file_metadata(file_path: str) -> dict[str, str | list[str]]:
    """
    Vrati metapodatke o fajlu (stem, suffix, suffixes, name).

    Args:
        file_path: Putanja do fajla.

    Returns:
        dict: Rečnik sa 'stem', 'suffix', 'suffixes', 'name'.

    Primer:
        >>> meta = get_file_metadata("/home/user/docs/report.tar.gz")
        >>> meta['stem']
        'report.tar'
        >>> meta['suffix']
        '.gz'
        >>> meta['suffixes']
        ['.tar', '.gz']

    Napomena:
        - Koristi `Path` objekte za rad sa putanjama
        - Radi za fajlove sa višestrukim suffix-ima (npr. .tar.gz)
        - Selektuj testove: pytest -k "test_get_file_metadata"
    """
    path = Path(file_path)
    return {
        "stem": path.stem,          # Fajl bez suffixa (za .tar.gz → report.tar)
        "suffix": path.suffix,      # Poslednji sufiks (.gz)
        "suffixes": path.suffixes,  # Svi suffiksi (['.tar', '.gz'])
        "name": path.name,          # Ime fajla (report.tar.gz)
    }



def get_file_info(file_path: str) -> dict[str, bool | int | str]:
    """
    Vrati detaljne informacije o fajlu (exists, is_file, is_dir, size).

    Args:
        file_path: Putanja do fajla.

    Returns:
        dict: Informacije o fajlu.

    Primer:
        >>> info = get_file_info("~/documents/file.txt")
        >>> info['exists']
        True
        >>> info['size_bytes']
        1024

    Napomena:
        - Vraća veličinu fajla u bajtovima ako fajl postoji, inače 0
        - Koristi `expanduser()` i `resolve()` za sigurnost putanje
        - Selektuj testove: pytest -k "test_get_file_info"
    """
    path = Path(file_path).expanduser().resolve()
    return {
        "path": str(path),
        "exists": path.exists(),
        "is_file": path.is_file(),
        "is_dir": path.is_dir(),
        "size_bytes": path.stat().st_size if path.exists() else 0,
    }


# ======================================================================================
# SEKCIJA 3: Operacije sa direktorijumima (3+ funkcije)
# ======================================================================================


def ensure_directory_exists(dir_path: Path) -> Path:
    """
    Proverari te da li postoji zadata putanja za direktorijum.
    Kreiraj direktorijum ako zadata putanja ne postoji.
    Vrati putanju do kreiranog direktorijuma.

    Args:
        dir_path: Putanja do direktorijuma.

    Returns:
        Path: Putanja do kreiranog direktorijuma (sada garantovano postoji).

    Primer:
        >>> path = ensure_directory_exists(Path("output/data"))
        >>> path.exists()
        True
        >>> path.is_dir()
        True

    Napomena:
        - `parents=True` pravi sve parent direktorijume
        - `exist_ok=True` ne baca grešku ako direktorijum već postoji
        - Selektuj testove: pytest -k "test_ensure_directory_exists"
    """
    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def normalize_path(path_string: str) -> Path:
    """
    Normalizuj putanju: proširi home, reši relativne, proveri sufiks.

    Args:
        path_string: Putanja kao string.

    Returns:
        Path: Normalizovana (apsolutna) putanja.

    Raises:
        ValueError: Ako putanja nema sufiks (nije fajl).

    Primer:
        >>> path = normalize_path("~/documents/file.txt")
        >>> path.is_absolute()
        True

    Napomena:
        - Koristi se za validaciju putanja sa filenames
        - Baca ValueError ako je direktorijum umesto fajla
        - Selektuj testove: pytest -k "test_normalize_path"
    """
    path = Path(path_string).expanduser().resolve()
    if not path.suffix:
        raise ValueError(f"Path must be a file with suffix, got: {path}")
    return path


def list_directory_contents(dir_path: Path, pattern: str = "*") -> list[Path]:
    """
    Lista sve fajlove i direktorijume u direktorijumu.

    Args:
        dir_path: Putanja do direktorijuma.
        pattern: Glob pattern (primer: "*.csv", "*.py").

    Returns:
        list[Path]: Lista fajlova koji odgovaraju pattern-u.

    Primer:
        >>> files = list_directory_contents(Path("sandbox/basics"), "*.py")
        >>> len(files) > 0
        True

    Napomena:
        - Koristi `.glob()` umesto `.iterdir()` za filtriranje
        - Za rekurzivno pretraživanje, koristi `rglob()`: dir_path.rglob("*.py")
        - Selektuj testove: pytest -k "test_list_directory_contents"
    """
    if not dir_path.exists():
        return []
    return sorted(dir_path.glob(pattern))


# ======================================================================================
# SEKCIJA 4: Formatirana prikaza (za demonstracije u main-u)
# ======================================================================================


def get_all_parent_directories_formatted() -> list[dict[str, int | str | bool]]:
    """
    Vrati sve parent direktorijume sa formatiranom strukturom (za prikaz).

    Returns:
        list[dict]: Lista sa 'level', 'path', 'name', 'exists' ključevima.

    Napomena:
        - Ova funkcija je za demonstraciju u main-u
        - Za teste, koristi `get_all_parent_directories()` (jednostavnija)
    """
    parents = Path(__file__).resolve().parents
    return [
        {
            "level": i,
            "path": str(parent),
            "name": parent.name or "/",
            "exists": parent.exists(),
        }
        for i, parent in enumerate(parents)
    ]


# ======================================================================================
# MAIN: Demonstracije svih funkcija
# ======================================================================================


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("PATH BASICS - DEMONSTRACIJE")
    print("=" * 80)

    # 1. Osnovne putanje
    print("\n[1] OSNOVNE PUTANJE")
    print(f"  Current Working Directory: {get_current_working_directory()}")
    print(f"  Home Directory: {get_user_home_directory()}")
    print(f"  Current File: {get_current_file_path()}")
    print(f"  Parent Directory: {get_parent_directory()}")

    # 2. Roditeljski direktorijumi - verzija 1 (jednostavna)
    print("\n[2] RODITELJSKI DIREKTORIJUMI (Jednostavna verzija)")
    for i, parent in enumerate(get_all_parent_directories(), 1):
        print(f"  {i}. {parent}")

    # 3. Roditeljski direktorijumi - verzija 2 (sa indentacijom)
    print("\n[3] RODITELJSKI DIREKTORIJUMI (Sa indentacijom)")
    for i, parent in enumerate(get_all_parent_directories()):
        indent = "  " * i
        print(f"{indent}└─ {parent.name or '/'}")

    # 4. Roditeljski direktorijumi - verzija 3 (sa informacijama)
    print("\n[4] RODITELJSKI DIREKTORIJUMI (Sa detaljima)")
    for info in get_all_parent_directories_formatted():
        exists_icon = "✓" if info["exists"] else "✗"
        print(f"  Level {
        info['level']}: {info['name']:<20} [{exists_icon}] | {info['path']}")

    # 5. Relativne putanje
    print("\n[5] RELATIVNE PUTANJE")
    rel_path = get_relative_path_from_home()
    if rel_path:
        print(f"  Relative from home: {rel_path}")
    else:
        print("  [Skripta nije u home direktorijumu]")

    # 6. Proširene putanje
    print("\n[6] PROŠIRENE PUTANJE (~)")
    example_paths = [
        "~/documents/file.txt",
        "~/projects/python",
        "~/desktop",
    ]
    for example in example_paths:
        expanded = expand_home_path(example)
        print(f"  {example:<30} → {expanded}")

    # 7. Metapodaci o fajlu
    print("\n[7] METAPODACI O FAJLU")
    example_file = "/home/user/docs/report.tar.gz"
    meta = get_file_metadata(example_file)
    print(f"  Fajl: {example_file}")
    print(f"    stem: {meta['stem']}")
    print(f"    suffix: {meta['suffix']}")
    print(f"    suffixes: {meta['suffixes']}")
    print(f"    name: {meta['name']}")

    # 8. Direktorijumi
    print("\n[8] OPERACIJE SA DIREKTORIJUMIMA")
    test_dir = Path("output/demo/nested")
    if ensure_directory_exists(test_dir):
        print(f"  ✓ Kreiram/proveravamo: {test_dir}")
        print(f"    Postoji: {test_dir.exists()}")

    # 9. Spajanje putanja
    print("\n[9] SPAJANJE PUTANJA")
    combined = join_paths("data", "input", "2025-12", "users.csv")
    print("  join_paths('data', 'input', '2025-12', 'users.csv')")
    print(f"  Result: {combined}")

    # 10. Normalizovanje putanja
    print("\n[10] NORMALIZOVANJE PUTANJA")
    try:
        normalized = normalize_path("~/documents/file.txt")
        print(f"  ✓ Normalizovana putanja: {normalized}")
        print(f"    Apsolutna: {normalized.is_absolute()}")
    except ValueError as e:
        print(f"  ✗ Greška: {e}")

    # 11. Listing direktorijuma
    print("\n[11] LISTING DIREKTORIJUMA (sandbox/basics/*.py)")
    py_files = list_directory_contents(Path("sandbox/basics"), "*.py")
    if py_files:
        print(f"  Pronađeni fajlovi ({len(py_files)}):")
        for py_file in py_files[:5]:  # Prikaži samo prvih 5
            print(f"    - {py_file.name}")
        if len(py_files) > 5:
            print(f"    ... i još {len(py_files) - 5} fajlova")
    else:
        print("  [Nema Python fajlova u direktorijumu]")

    print("\n" + "=" * 80)
    print("Za pokretanje testova: pytest sandbox/basics/tests/test_path_basics.py -v")
    print("=" * 80 + "\n")
