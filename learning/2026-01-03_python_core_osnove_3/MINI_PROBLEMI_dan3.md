---
type: problems
time: 60 minutes
count: 18
---

# 🎯 MINI PROBLEMI — Dan 3 (Kolekcije)

## Grupacija 1 — Liste

1. **Ukloni duplikate**: data lista brojeva; vrati novu listu bez duplikata, ali sačuvaj redosled prvog pojavljivanja.
2. **Rotacija liste**: pomeri sve elemente udesno za 1 (zadnji ide na početak).
3. **Spoji i sortiraj**: dve liste brojeva spoji, ukloni duplikate, sortiraj.

## Grupacija 2 — Tuple

4. **Parovi u tuple**: iz dve liste `imena` i `godine` napravi listu tuplova `(ime, godina)` (pretpostavi iste dužine).
5. **Koordinate filter**: data lista tuplova `(x, y)`; izdvoji samo one gde je `x > 0` i `y > 0`.
6. **Tuple kao ključ**: napravi dict gde je ključ `(ime, prezime)`, vrednost godine; pristupi jednom ključu.

## Grupacija 3 — Set

7. **Presek listi**: nađi elemente koji su zajednički za dve liste korišćenjem set preseka.
8. **Simetrična razlika**: nađi elemente koji su u jednoj ili drugoj listi, ali ne u obe.
9. **Provera podskupa**: da li je `{1,2}` podskup `{1,2,3}`? (koristi set metode).

## Grupacija 4 — Dict

10. **Invertuj dict**: obrni mapiranje `skracenica -> naziv` u `naziv -> skracenica` (pretpostavi unikatne vrednosti).
11. **Brojanje reči**: prebroj pojavljivanja svake reči u stringu (split po space), vrati dict.
12. **Merge sa preferencijom**: spoji dva dict-a; ako ključ postoji u oba, uzmi vrednost iz drugog.

## Grupacija 5 — Slicing i kopije

13. **Svaki drugi**: iz liste vrati novi `lst[::2]` i objasni zašto ne diže IndexError.
14. **Obrnuto**: vrati obrnutu kopiju liste bez `reverse()` (slicing).
15. **Duboka kopija**: dati ugnježdeni list `[[1,2],[3,4]]`; napravi duboku kopiju i promeni jedan unutrašnji element bez uticaja na original.

## Grupacija 6 — Comprehensions

16. **Filter + kvadrat**: list comprehension za kvadrate parnih brojeva 1..20.
17. **Dict comprehension filter**: iz dict-a ocena `{ime: poeni}` izvuci samo one >= 70.
18. **Set comprehension**: iz stringa izvuci sva slova osim samoglasnika (u set).

---

## Brzi hintovi

-   1. koristi pomoćni `seen = set()` za redosled.
-   2. `lst[-1:] + lst[:-1]`.
-   7. `set(a) & set(b)`; 8) `set(a) ^ set(b)`.
-   11. `for rec in tekst.split(): broj[rec] = broj.get(rec, 0) + 1`.
-   15. `copy.deepcopy`.
-   16. `[x*x for x in range(1,21) if x%2==0]`.
