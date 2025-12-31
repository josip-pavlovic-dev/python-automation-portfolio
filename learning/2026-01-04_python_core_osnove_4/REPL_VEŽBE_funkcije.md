---
type: repl_exercises
time: 90 minutes
topics: [functions, args, kwargs, defaults]
---

# 🧪 REPL Vežbe — Funkcije

## FAZA 1 — Osnove (15 min)

1. Definiši `povecaj(x)` → vrati `x+1`.
2. `pozdrav(ime, jezik="sr")` → vrati poruku za sr/en.

## FAZA 2 — Default i keyword (15 min)

3. `podeli(x, y=2)` → `x/y` zaokruženo na 2 decimale.
4. Pozovi `podeli` positional i keyword, vidi razlike.

## FAZA 3 — \*args / \*\*kwargs (20 min)

5. `zbir(*brojevi)` → sumiraj.
6. `info(**podatak)` → štampaj dict.
7. Kombinuj: `def calc(a, b=1, *args, **kwargs): print(a, b, args, kwargs)`.

## FAZA 4 — Mutabilni default test (15 min)

8. Napiši namerno pogrešnu verziju sa `lst=[]`, vidi bug.
9. Ispravi sa `lst=None`.

## FAZA 5 — Keyword-only (15 min)

10. `def format_ime(ime, prezime, *, veliko=False)` → ako `veliko` True, vrati uppercase.
11. Pozovi sa/bez keyword-only da vidiš TypeError.

## FAZA 6 — Mini izazovi (10 min)

12. `def filtriraj_pozitivne(*nums)` → vrati novu listu pozitivnih.
13. `def spoji_sep(*delovi, sep="-")` → spoji stringove sa `sep`.

✅ Check: razumeš razliku positional/keyword, \*args/\*\*kwargs, mutabilni default.
