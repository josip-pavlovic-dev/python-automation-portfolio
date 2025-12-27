"""
Testovi za path_basics.py - Dan 6 (FAZA 1)

Cilj: Testirati sve funkcije koje vraćaju putanje sa `pytest` i `tmp_path` fixture.

Test pokretanje:
  - Svi testovi: pytest sandbox/basics/tests/test_path_basics.py -v
  - Specifičan test:pytest sandbox/basics/tests/test_path_basics.py::test_get_current_working_directory -v
  - Sa print output: pytest sandbox/basics/tests/test_path_basics.py -v -s
"""  # noqa: E501

from pathlib import Path

import pytest
from sandbox.basics.path_basics import (
    # Sekcija 3: Operacije sa direktorijumima
    ensure_directory_exists,
    expand_home_path,
    get_absolute_path,
    get_all_parent_directories,
    get_current_file_path,
    # Sekcija 1: Osnovne Path operacije
    get_current_working_directory,
    get_file_info,
    # Sekcija 2: File metapodaci
    get_file_metadata,
    get_parent_directory,
    get_relative_path_from_home,
    get_user_home_directory,
    join_paths,
    list_directory_contents,
    normalize_path,
)

# ======================================================================================
# SEKCIJA 1: Osnovne Path operacije - TESTOVI (8+ testova)
# ======================================================================================


class TestBasicPathOperations:
    """Testovi za osnovne Path operacije."""

    def test_get_current_working_directory(self):
        """Test da get_current_working_directory vraća Path objekat."""
        result = get_current_working_directory()

        assert isinstance(result, Path)
        assert result.is_absolute()
        assert result.exists()
        assert result.is_dir()

    def test_get_user_home_directory(self):
        """Test da get_user_home_directory vraća home direktorijum."""
        result = get_user_home_directory()

        assert isinstance(result, Path)
        assert result.exists()
        assert result.is_dir()
        assert result.is_absolute()
        # Home direktorijum zawsze završava sa imenom korisnika
        assert result.name

    def test_get_current_file_path(self):
        """Test da get_current_file_path vraća apsolutnu putanju do path_basics.py."""
        result = get_current_file_path()

        assert isinstance(result, Path)
        assert result.exists()
        assert result.is_file()
        assert result.is_absolute()
        assert result.name == "path_basics.py"
        assert result.suffix == ".py"

    def test_get_parent_directory(self):
        """Test da get_parent_directory vraća parent direktorijum."""
        result = get_parent_directory()

        assert isinstance(result, Path)
        assert result.exists()
        assert result.is_dir()
        assert result.is_absolute()
        assert result.name == "basics"

    def test_get_all_parent_directories(self):
        """Test da get_all_parent_directories vraća listu svih parent direktorijuma."""
        result = get_all_parent_directories()

        assert isinstance(result, list)
        assert len(result) > 0
        # Svi elementi su Path objekti
        for parent in result:
            assert isinstance(parent, Path)
            assert parent.is_absolute()
            assert parent.exists()
        # Poslednji element je root direktorijum
        assert str(result[-1]) == "/"

    def test_get_absolute_path(self):
        """Test da get_absolute_path konvertuje relativnu putanju u apsolutnu."""
        relative = "../data/sample.txt"
        result = get_absolute_path(relative)

        assert isinstance(result, Path)
        assert result.is_absolute()

    def test_get_relative_path_from_home(self):
        """Test da get_relative_path_from_home vraća relativnu putanju."""
        result = get_relative_path_from_home()

        # Rezultat može biti None ako skripta nije u home direktorijumu
        if result is not None:
            assert isinstance(result, Path)
            # Relativna putanja ne sme biti apsolutna
            assert not result.is_absolute()

    def test_expand_home_path(self):
        """Test da expand_home_path proširiava ~ na home direktorijum."""
        home = get_user_home_directory()

        result = expand_home_path("~/documents/file.txt")

        assert isinstance(result, Path)
        assert result.is_absolute()
        assert str(result).startswith(str(home))
        assert "documents" in str(result)
        assert "file.txt" in str(result)

    def test_join_paths(self):
        """Test da join_paths spaja putanja sa / operatorom."""
        result = join_paths("data", "input", "2025-12", "users.csv")

        assert isinstance(result, Path)
        assert str(result) == "data/input/2025-12/users.csv"


# ======================================================================================
# SEKCIJA 2: File metapodaci - TESTOVI (3+ testova)
# ======================================================================================


class TestFileMetadata:
    """Testovi za ekstraktovanje metapodataka o fajlima."""

    def test_get_file_metadata_single_extension(self):
        """Test metapodataka za fajl sa jednom ekstenzijom."""
        metadata = get_file_metadata("/home/user/docs/report.txt")

        assert metadata["name"] == "report.txt"
        assert metadata["stem"] == "report"
        assert metadata["suffix"] == ".txt"
        assert metadata["suffixes"] == [".txt"]

    def test_get_file_metadata_multiple_extensions(self):
        """Test metapodataka za fajl sa više ekstenzija."""
        metadata = get_file_metadata("/home/user/docs/report.tar.gz")

        assert metadata["name"] == "report.tar.gz"
        assert metadata["stem"] == "report.tar"
        assert metadata["suffix"] == ".gz"
        assert metadata["suffixes"] == [".tar", ".gz"]

    def test_get_file_info_nonexistent_file(self, tmp_path: Path):
        """Test info o nepostojećem fajlu."""
        nonexistent = tmp_path / "nonexistent.txt"

        info = get_file_info(str(nonexistent))

        assert info["exists"] is False
        assert info["is_file"] is False
        assert info["size_bytes"] == 0


# ======================================================================================
# SEKCIJA 3: Operacije sa direktorijumima - TESTOVI (3+ testova)
# ======================================================================================


class TestDirectoryOperations:
    """Testovi za operacije sa direktorijumima."""

    def test_ensure_directory_exists_creates_nested_dirs(self, tmp_path: Path):
        """Test da ensure_directory_exists kreira nested direktorijume."""
        nested_path = tmp_path / "a" / "b" / "c"

        result = ensure_directory_exists(nested_path)

        assert isinstance(result, Path)
        assert result.exists()
        assert result.is_dir()
        # Proverite da su svi parent direktorijumi kreirani
        assert (tmp_path / "a").exists()
        assert (tmp_path / "a" / "b").exists()

    def test_ensure_directory_exists_idempotent(self, tmp_path: Path):
        """Test da ensure_directory_exists ne javlja grešku ako direktorijum već postoji."""  # noqa: E501
        existing_dir = tmp_path / "existing"
        existing_dir.mkdir()

        # Trebalo bi da radi bez greške
        result = ensure_directory_exists(existing_dir)

        assert result.exists()

    def test_normalize_path_valid_file(self):
        """Test normalizovanja validne file putanje."""
        result = normalize_path("~/documents/file.txt")

        assert isinstance(result, Path)
        assert result.is_absolute()
        assert result.suffix == ".txt"

    def test_normalize_path_raises_on_no_suffix(self, tmp_path: Path):
        """Test da normalize_path baca ValueError ako nema suffixa."""
        # Direktorijum umesto fajla
        with pytest.raises(ValueError, match="must be a file"):
            normalize_path(str(tmp_path))

    def test_list_directory_contents(self, tmp_path: Path):
        """Test da list_directory_contents vraća fajlove sa pattern-om."""
        # Kreiraj test fajlove
        (tmp_path / "file1.py").write_text("content")
        (tmp_path / "file2.py").write_text("content")
        (tmp_path / "file3.txt").write_text("content")

        result = list_directory_contents(tmp_path, "*.py")

        assert isinstance(result, list)
        assert len(result) == 2
        assert all(f.suffix == ".py" for f in result)

    def test_list_directory_contents_nonexistent_dir(self, tmp_path: Path):
        """Test da list_directory_contents vraća praznu listu za nepostojeći direktorijum."""  # noqa: E501
        nonexistent = tmp_path / "nonexistent"

        result = list_directory_contents(nonexistent)

        assert result == []


# ======================================================================================
# SEKCIJA 4: Integrativni testovi (kombinovane operacije)
# ======================================================================================


class TestIntegration:
    """Integrativni testovi koji kombinuju više funkcija."""

    def test_workflow_create_and_normalize_path(self, tmp_path: Path):
        """Test workflow: kreiraj direktorijum → kreiraj fajl → normalizuj putanju."""
        # Korak 1: Kreiraj direktorijum
        data_dir = tmp_path / "data" / "output"
        ensure_directory_exists(data_dir)
        assert data_dir.exists()

        # Korak 2: Kreiraj fajl
        file_path = data_dir / "results.csv"
        file_path.write_text("name,age\nAlice,30")

        # Korak 3: Normalizuj putanju
        result = normalize_path(str(file_path))
        assert result.exists()
        assert result.is_file()

    def test_workflow_list_and_get_metadata(self, tmp_path: Path):
        """Test workflow: lista direktorijum → ekstraktuj metadata."""
        # Kreiraj test fajlove
        files = [
            "report.txt",
            "data.csv",
            "archive.tar.gz",
        ]
        for f in files:
            (tmp_path / f).write_text("content")

        # Lista fajlove
        file_list = list_directory_contents(tmp_path, "*")
        assert len(file_list) == len(files)

        # Ekstraktuj metadata
        for file_path in file_list:
            metadata = get_file_metadata(str(file_path))
            assert "stem" in metadata
            assert "suffix" in metadata

    def test_parent_directory_chain(self):
        """Test da je get_parent_directory deo parents liste."""
        parent = get_parent_directory()
        all_parents = get_all_parent_directories()

        # parent treba biti prvi element u all_parents
        assert parent == all_parents[0]


# ======================================================================================
# PARAMETRIZIRANI TESTOVI (testiranje više slučajeva sa jedan test)
# ======================================================================================


@pytest.mark.parametrize(
    "path_with_tilde,contains",
    [
        ("~/documents", "documents"),
        ("~/projects/python", "projects"),
        ("~/desktop/file.txt", "desktop"),
    ],
)
def test_expand_home_path_parametrized(path_with_tilde: str, contains: str):
    """Parametrizirani test za expand_home_path sa različitim ulazima."""
    result = expand_home_path(path_with_tilde)

    assert isinstance(result, Path)
    assert result.is_absolute()
    assert contains in str(result)


@pytest.mark.parametrize(
    "file_name,expected_suffix",
    [
        ("document.txt", ".txt"),
        ("archive.tar.gz", ".gz"),
        ("image.png", ".png"),
        ("data.csv", ".csv"),
    ],
)
def test_get_file_metadata_parametrized(file_name: str, expected_suffix: str):
    """Parametrizirani test za get_file_metadata sa različitim fajlovima."""
    metadata = get_file_metadata(f"/home/user/{file_name}")

    assert metadata["name"] == file_name
    assert metadata["suffix"] == expected_suffix


# ======================================================================================
# NAPOMENE ZA POKRETANJE TESTOVA
# ======================================================================================

"""
Pokretanje testova:

1. Svi testovi:
   pytest sandbox/basics/tests/test_path_basics.py -v

2. Samo testovi klase:
   pytest sandbox/basics/tests/test_path_basics.py::TestBasicPathOperations -v

3. Specifičan test:
   pytest sandbox/basics/tests/test_path_basics.py::test_get_current_working_directory -v

4. Sa print output (debug):
   pytest sandbox/basics/tests/test_path_basics.py -v -s

5. Sa coverage:
   pytest sandbox/basics/tests/test_path_basics.py --cov=sandbox.basics --cov-report=term-missing

6. Samo brzi testovi (bez file I/O):
   pytest sandbox/basics/tests/test_path_basics.py -m "not slow" -v

7. Parametrizirani testovi:
   pytest sandbox/basics/tests/test_path_basics.py::test_expand_home_path_parametrized -v
"""  # noqa: E501
