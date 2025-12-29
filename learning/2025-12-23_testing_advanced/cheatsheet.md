---
type: cheatsheet
linked_to: 2025-12-23_testing_advanced
date: 2025-12-23
status: published
title: Pytest Cheatsheet
summary: Kratki pytest primeri: layout, parametrizacija, fixtures, monkeypatch, caplog, markers, coverage
tags: pytest, cheatsheet, testing
language: bilingual
---

# 🧾 Pytest Cheatsheet

## Basic layout

```python
# file: tests/test_example.py
def test_add():
    assert 1 + 1 == 2
```

Run:

```bash
pytest -q
```

Napomene:

-   Ime fajla mora počinjati sa `test_` ili završavati sa `_test.py`
-   Ime funkcije mora počinjati sa `test_`, inače pytest neće prepoznati
-   Koristi `assert` za provere, ne `print`
-   Organizuj testove u klase ako ima smisla, ali bez `__init__` metode
-   Fixtures idu u `conftest.py` ili u isti fajl, ako su specifične za testove u tom fajlu
-   optional: koristi `if __name__ == "__main__": pytest.main()` za pokretanje iz IDE-a

---

## Parametrize

```python
import pytest
@pytest.mark.parametrize("raw,expected", [("1", 1), ("2", 2)])
def test_to_int(raw, expected):
    assert int(raw) == expected
```

Napomene:

-   Možeš koristiti listu tuple-ova ili listu dict-ova, npr. `[{"raw": "1", "expected": 1}, ...]`
-   Možeš kombinovati sa fixtures, npr. `@pytest.mark.parametrize("input", [1,2])` i `def test_func(input, fixture1): ...`
-   Koristi `ids` parametar za prilagođene nazive test slučajeva ako je potrebno, npr. `ids=["case1", "case2"]`.
-   Možeš koristiti `indirect=True` za parametrize koji koristi fixture imena.
-   Više parametara je moguće, npr. `@pytest.mark.parametrize("a,b,expected", [(1,2,3), (4,5,9)])`
-   Parametrize može biti složen, koristi ga za table-driven testove.
-   Kombinuj sa `pytest.lazy_fixture` za korišćenje fixture vrednosti u parametrize.
-   Koristi `pytest.param` za dodatne opcije po test slučaju, npr. `marks=pytest.mark.skip`.
-   Možeš koristiti `pytest.mark.parametrize` unutar test klase.
-   Parametrize može biti ugnježden, koristi `@pytest.mark.parametrize` više puta na istoj funkciji.
-   Koristi `pytest.mark.parametrize` za generisanje velikog broja test slučajeva iz malog skupa podataka.

---

## Fixtures

```python
@pytest.fixture
def sample_path(tmp_path: Path) -> Path:
    file = tmp_path / "data.txt"
    file.write_text("hi", encoding="utf-8")
    return file

def test_read(sample_path: Path):
    assert sample_path.read_text(encoding="utf-8") == "hi"
```

Napomene:

-   Fixtures se definišu sa `@pytest.fixture` dekoratorom
-   Fixtures mogu imati scope: `function` (default), `module`, `class`, `session`
-   Fixtures mogu zavisiti jedni od drugih (fixture može koristiti drugi fixture kao argument)
-   Koristi `tmp_path` ili `tmpdir` za privremene fajlove i foldere
-   Možeš koristiti `yield` u fixture za setup/teardown logiku
-   Fixtures mogu biti automatski primenjene sa `autouse=True`
-   Možeš koristiti `request` fixture za pristup informacijama o testu
-   Fixtures mogu vraćati bilo koji objekat, ne samo fajl puteve
-   Možeš koristiti `params` argument u fixture za parametrizaciju fixture-a
-   Fixtures mogu biti definisane u `conftest.py` za deljenje među više test fajlova ili unutar modula
-   Koristi `finalizer` za čišćenje resursa nakon testa
-   Fixtures mogu biti asinhrone koristeći `async def` i `pytest-asyncio` plugin, ako je potrebno.
-   Možeš koristiti `factory as fixture` pattern za kreiranje objekata sa različitim konfiguracijama.

---

## Monkeypatch

```python
def test_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "test")
```

```python
def test_time(monkeypatch):
    class FakeDateTime:
        @classmethod
        def now(cls):
            return datetime(2020, 1, 1)
    monkeypatch.setattr("datetime.datetime", FakeDateTime)
```

Napomene:

-   `monkeypatch.setattr(target, value)` menja atribut na ciljanom objektu ili modulu
-   `monkeypatch.setenv(key, value)` postavlja promenljivu okruženja
-   `monkeypatch.delenv(key, raising=False)` briše promenljivu okruženja
-   `monkeypatch.setitem(mapping, key, value)` menja vrednost u mapiranom objektu (npr. dict)
-   `monkeypatch.delitem(mapping, key, raising=False)` briše ključ iz mapiranog objekta
-   Koristi za izbegavanje stvarnog IO, mrežnih poziva, ili vremenskih zavisnosti u testovima
-   Možeš koristiti unutar fixture-a za setup/teardown efekat
-   Vraća sve promene nakon testa automatski
-   Možeš koristiti za zamenu funkcija ili metoda sa lažnim verzijama tokom testa, npr. za mocking.
-   Možeš koristiti `monkeypatch.context()` za grupisanje više promena koje će biti vraćene zajedno.
-   Možeš koristiti `monkeypatch` za testiranje koda koji zavisi od spoljnog stanja ili konfiguracije.
-   Koristi `monkeypatch` pažljivo, jer može otežati razumevanje koda ako se previše koristi.

---

## caplog / capsys

```python
def test_logs(caplog):
    logger.info("hello")
    assert "hello" in caplog.text
```

```python
def test_output(capsys):
    print("output")
    captured = capsys.readouterr()
    assert "output" in captured.out
```

Napomene:

-   `caplog` hvata logove generisane tokom testa
-   `caplog.text` sadrži sve logove kao string
-   `caplog.records` sadrži listu log zapisa (objekata)
-   Možeš podesiti nivo logovanja sa `caplog.set_level(logging.INFO)`
-   `capsys` hvata standardni izlaz i greške (`stdout`, `stderr`)
-   `capsys.readouterr()` vraća objekat sa `out` i `err` atributima
-   Koristi `caplog` za provere da li su određene poruke logovane
-   Koristi `capsys` za provere ispisa na konzolu
-   Možeš koristiti oba zajedno u istom testu ako je potrebno
-   `caplog` i `capsys` su automatski dostupni kao fixture
-   Možeš koristiti `with capsys.disabled():` da isključiš hvatanje unutar bloka koda
-   Možeš koristiti `caplog.at_level(level)` kao kontekst menadžer za privremeno podešavanje nivoa logovanja.
-   Možeš koristiti `caplog.clear()` da očistiš prethodno uhvaćene logove tokom testa.
-   Možeš koristiti `capsys` za testiranje koda koji piše na standardni izlaz ili greške, kao što su funkcije koje koriste `print()` ili `sys.stderr.write()`.
-   Možeš koristiti `caplog` za testiranje koda koji koristi Python-ov `logging` modul za generisanje logova.
-   Možeš koristiti `caplog` i `capsys` zajedno sa parametrizacijom za testiranje različitih scenarija logovanja i ispisa.

---

## Markers

```python
import pytest
@pytest.mark.slow
def test_big():
    ...
```

Napomene:

-   Definiši marker u `pytest.ini` ako je custom:
    ```ini
    [pytest]
    markers =
        slow: marks tests as slow (deselect with '-m "not slow"')
    ```
-   Pokreni samo određene markere: `pytest -m slow`
-   Isključi određene markere: `pytest -m "not slow"`
-   Možeš koristiti više markera na istom testu: `@pytest.mark.slow @pytest.mark.integration`
-   Koristi markere za kategorizaciju testova (npr. `unit`, `integration`, `e2e`, `slow`, `fast`)
-   Možeš koristiti markere za uslovno preskakanje testova sa `@pytest.mark.skipif(condition, reason="...")`
-   Možeš koristiti `@pytest.mark.xfail(condition, reason="...")` za označavanje testova koji se očekuju da padnu, ali ne izazivaju grešku ako to učine
-   Možeš koristiti markere za dodavanje metapodataka testovima, npr. `@pytest.mark.priority(1)`
-   Možeš koristiti markere za grupisanje testova i pokretanje određenih grupa zajedno, npr. `pytest -m "unit or integration"`.
-   Možeš koristiti markere za podešavanje specifičnih konfiguracija ili setup-a za određene testove.
-   Možeš koristiti markere za filtriranje testova prilikom pokretanja, što je korisno za velike test suite-ove.

---

## Failure patterns

-   Arrange/Act/Assert pattern
-   Test jednu ideju po test funkciji
-   Jedan assert po ideji (ako je moguće)
-   Koristi descriptive test imena
-   Izbegavaj zavisnosti između testova
-   Koristi fixtures za setup/teardown
-   Mock eksterne zavisnosti
-   Isoluj testove koristeći `tmp_path` za fajl sistem
-   Koristi parametrizaciju za slične test slučajeve
-   Proveri logove sa `caplog` umesto print
-   Pokrij edge case-ove i greške
-   Redovno pokreći testove tokom razvoja
-   Održavaj testove čitljivim i jednostavnim
-   Refaktoriši testove kada se kod menja
-   Koristi `pytest` plugins za dodatne funkcionalnosti (npr. `pytest-cov` za coverage)
-   Piši testove pre koda (TDD) kada je moguće, kako bi se osigurala testabilnost
-   Redovno proveravaj pokrivenost koda testovima i ciljaj na visoku pokrivenost
-   Koristi CI/CD alate za automatsko pokretanje testova na svaku promenu koda.
-   Dokumentuj složene testove kako bi drugi (ili ti sam kasnije) mogli lako razumeti njihovu svrhu.
-   Redovno pregledaj i ažuriraj testove kako bi osigurao da ostanu relevantni i efikasni.

---

## Coverage quick

```bash
pytest --maxfail=1 -q --cov=sandbox --cov=projects/01-web-scraper
```

Napomene:

-   Instaliraj `pytest-cov` plugin: `pip install pytest-cov`
-   Pokreni pytest sa `--cov=<module>` za svaki modul koji želiš da pokriješ
-   Dodaj `--cov-report=term-missing` za izveštaj o nedostajućoj pokrivenosti
-   Možeš koristiti `--cov-fail-under=<percentage>` da testovi padnu ako pokrivenost padne ispod određenog procenta
-   Možeš koristiti `.coveragerc` fajl za konfiguraciju coverage opcija
-   Coverage meri linije koda koje su izvršene tokom testova
-   Fokusiraj se na pokrivenost kritičnog koda i edge case-ova
-   Redovno proveravaj coverage izveštaje kako bi identifikovao nedostajuće testove
-   Koristi coverage zajedno sa CI/CD za automatsko praćenje pokrivenosti tokom razvoja, osiguravajući da se ne smanjuje tokom vremena.
-   Možeš koristiti `coverage html` za generisanje HTML izveštaja koji je lakši za čitanje i analizu.
-   Možeš koristiti `coverage xml` za generisanje XML izveštaja koji može biti koristan za integraciju sa drugim alatima ili CI sistemima.
-   Možeš koristiti `coverage annotate` za generisanje anotiranih izvora koji pokazuju koje linije koda su pokrivene, a koje nisu.
-   Možeš koristiti `coverage combine` za kombinovanje rezultata iz više pokretanja testova, što je korisno za paralelno izvršavanje testova.

---

## 📝 Notes

-   Testovi nemaju `print`; koriste `assert` i eventualno `caplog`/`capsys`
-   Fajl sistem testovi uvek idu kroz `tmp_path`
-   Markiraj spore testove `@pytest.mark.slow`
-   Za izolaciju testova koristi `-k <pattern>` i `-m <marker>`
-   Coverage pokrećeš sa `coverage run -m pytest` i `coverage report -m`

---
