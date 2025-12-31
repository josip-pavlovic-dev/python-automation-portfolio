---
type: problems
time: 60 minutes
count: 18
---

# 🎯 MINI PROBLEMI — Dan 2 (Kontrola Toka)

## Grupacija 1 — Toplo-Hladno (if/elif/else)

1. **Pozdrav po satu**: `hour` (0-23) → ispiši "jutro" (<12), "dan" (<18), inače "noć".
2. **Ocena u slovo**: broj 0-100 → A(90+), B(80+), C(70+), D(60+), F(ostalo).
3. **Popust**: kupovina > 10.000 dobija 10%, između 5k-10k dobija 5%, manje nema popust.

## Grupacija 2 — `for` + `range`

4. **Saberi parne do N**: dato `n`, saberi sve parne od 0 do n.
5. **Prebroj samoglasnike** u stringu (a,e,i,o,u) — koristi `for`.
6. **Nađi min i max** u listi brojeva ručno (bez `min`/`max`).

## Grupacija 3 — `enumerate`

7. **Indeks + element**: za listu `['a','b','c']` štampaj `0:a`, `1:b`, `2:c`.
8. **Pronađi indeks cilja**: data lista i vrednost `target`; nađi PRVI indeks gde se pojavi; ako nema → `-1`.
9. **Zameni element na indeksu**: ako `index` validan, zameni element novim; ako nije validan, poruka greške.

## Grupacija 4 — `break` i `continue`

10. **Prvi broj deljiv sa 7** u rasponu 1..100 (koristi `break`).
11. **Preskoči neparne**: odštampaj samo parne 1..20 (koristi `continue`).
12. **Prekini na negativan**: data lista brojeva; štampaj dok ne naiđeš na negativan (tu stani).

## Grupacija 5 — `while` Praksa

13. **Pogodi broj**: tajni broj 13; traži unos dok korisnik ne pogodi; javi "veće" / "manje".
14. **Validacija lozinke**: traži unos dok string nije dužine ≥ 8.
15. **Sumiraj do stop**: unos brojeva dok korisnik ne kuca "stop"; ispiši sumu.

## Grupacija 6 — Kombinacije

16. **FizzBuzz 1..30**: `for` ili `while` (po želji).
17. **Brojanje reči**: dati string; prebroj koliko reči (razdvojene space).
18. **Naslovna slova**: dati string; napravi novi gde svaka reč počinje velikim slovom (bez `title()`).

---

## Predloženi Redosled

1 → 3 (zagrevanje), 4 → 6 (range + petlja), 7 → 9 (enumerate), 10 → 12 (break/continue), 13 → 15 (while), 16 → 18 (kombinacije).

## Brza Rešenja (self-check)

1. if/elif/else sa brojem sata.
2. if/elif sa granicama 90/80/70/60.
3. if > 10000, elif >= 5000, else.
4. `for i in range(n+1): if i%2==0: total+=i`.
5. `for slovo in tekst: if slovo in "aeiou": count+=1`.
6. set `min=first`, `max=first`, prolazi for.
7. `for idx, val in enumerate(lista): print(idx, val)`.
8. `for idx, val in enumerate(lista): if val==target: print(idx); break; else -1`.
9. provera granica `0 <= idx < len(lista)`.
10. `for i in range(1,101): if i%7==0: print(i); break`.
11. `for i in range(1,21): if i%2: continue; print(i)`.
12. `for n in lista: if n<0: break; print(n)`.
13. while True sa unosom, poredi sa 13.
14. while True, `len(pwd) >= 8` break.
15. while unos != "stop": suma += int(unos).
16. klasičan FizzBuzz.
17. `len(text.split())`.
18. split → join sa `word[0].upper() + word[1:]` ako dužina>0.
