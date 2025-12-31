---
type: repl_exercises
time: 60 minutes
topics: [try, except, raise]
---

# 🧪 REPL Vežbe — Error Handling

## FAZA 1 — Osnove (15 min)

1. `int("12a")` u try/except `ValueError` → odštampaj poruku.
2. Deljenje: traži unos broja; hvataj `ZeroDivisionError` i `ValueError` odvojeno.

## FAZA 2 — else/finally (15 min)

3. Čitanje fajla u try; `except FileNotFoundError`; `else` štampa dužinu; `finally` zatvara fajl.
4. Napravi funkciju `procitaj(path)` koja vraća tekst ili diže grešku dalje.

## FAZA 3 — raise (15 min)

5. `def kvadrat(x)`: ako nije broj, `raise TypeError`.
6. `def podeli(x, y)`: ako `y==0`, `raise ZeroDivisionError("Deljenje nulom")`.

## FAZA 4 — Custom exception (15 min)

7. Definiši `class NegativeAmountError(ValueError): pass` i koristi u funkciji `uplata`.
8. Napiši `validate_age(age)` → ako <0 ili >120, `raise ValueError`.

✅ Check: koristiš specifične izuzetke, znaš else/finally, dižeš grešku kada je ulaz loš.
