---
type: repl_exercises
time: 90 minutes
topics: [pytest]
---

# 🧪 REPL Vežbe — Pytest

## FAZA 1 — Osnovni test (15 min)

1. Napravi `calc.py` i `test_calc.py` sa funkcijom `add` i testom `test_add`.
2. Pokreni `pytest -q`.

## FAZA 2 — Više assercija (20 min)

3. Dodaj `sub(a,b)` i testiraj negativan rezultat.
4. Testiraj da `div(a,b)` baca `ZeroDivisionError` (`pytest.raises`).

## FAZA 3 — Fixture (20 min)

5. Kreiraj fixture `sample_list` i koristi ga u dva testa.

## FAZA 4 — Parametrizacija (20 min)

6. `@pytest.mark.parametrize("a,b,res", [(1,2,3), (2,5,7)])` za `add`.

## FAZA 5 — Mini integracija (15 min)

7. Funkcija koja čita fajl; napiši test koji koristi `tmp_path` da kreira privremeni fajl i proveri rezultat.

✅ Check: znaš `pytest -q`, fixtures, parametrizaciju, `raises`.
