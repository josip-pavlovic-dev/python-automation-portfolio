---
type: problems
time: 60 minutes
count: 14
---

# 🎯 MINI PROBLEMI — Dan 7 (Logging + Pytest)

## Logging

1. `setup_logger(name)` vrati logger sa INFO nivoom i formatom; testiraj da ne duplira handlere.
2. Dodaj FileHandler koji upisuje WARNING+ u `warnings.log`; generiši warning i proveri da je upisan.
3. Funkcija `calc(a,b)` loguje DEBUG ulaz/izlaz ako level dozvoljava.
4. `safe_div(a,b)` loguje ERROR i vraća None ako b==0.

## Pytest

5. Testiraj `safe_div` da vraća None za b==0 i broj za b!=0.
6. Parametrizuj `add(a,b)` test sa 3 para vrednosti.
7. Fixture `tmp_file` koji pravi fajl sa tekstom; test `read_file` funkcije.
8. Test koji očekuje `ValueError` iz `validate_email` (pytest.raises).
9. Test za `Inventory` klasu (dodavanje i greška kad nema zalihe).
10. Napravi marker `slow` (samo dekorator), obeleži jedan test; pokreni sve (`pytest -q`) i vidi marker u izlazu.

## Kombinacija

11. Funkcija koja parsira JSON string; testiraj dobar i loš input (loš treba da podigne JSONDecodeError).
12. Logger u modulu `service.py`; test da `caplog` hvata warning poruku.
13. Test parametrizovan za `is_even` sa granicama (0, -1, 2).
14. Bonus: test koji koristi `monkeypatch` da zameni funkciju u importovanom modulu (kratko, npr. zameni `time.time`).

Self-check: 10+/14 rešenih; logger format ispravan; pytest pokrenut i razumeš izlaz.
