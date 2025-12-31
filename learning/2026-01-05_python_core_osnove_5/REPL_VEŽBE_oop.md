---
type: repl_exercises
time: 90 minutes
topics: [class, init, property, inheritance]
---

# 🧪 REPL Vežbe — OOP Osnove

## FAZA 1 — Klasa i instanca (15 min)

1. Napravi klasu `Osoba` sa `ime`, `godine`; metoda `predstavi_se`.
2. Instanciraj i pozovi metod.

## FAZA 2 — @property (20 min)

3. Dodaj `_ime` i `@property ime` sa validacijom (ne prazno).
4. Pokušaj postaviti prazno ime → ValueError.

## FAZA 3 — **repr** (10 min)

5. Dodaj `__repr__` i proveri štampu liste objekata.

## FAZA 4 — Nasleđivanje (20 min)

6. Klasa `Zaposleni(Osoba)` sa poljem `plata` i metodom `povecaj(iznos)`.
7. Override `predstavi_se` da doda info o plati; pozovi `super()`.

## FAZA 5 — Mini integracija (25 min)

8. Klasa `Konto` sa `uplata`, `isplata` (ValueError ako isplata > stanje).
9. Dodaj `@property stanje` read-only.
10. Napravi listu konta i iteriraj, ispiši repr.

✅ Check: razumeš `self`, `__init__`, `@property`, `super()`.
