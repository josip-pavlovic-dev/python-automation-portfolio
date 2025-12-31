---
type: problems
time: 60 minutes
count: 16
---

# 🎯 MINI PROBLEMI — Dan 4 (Funkcije + Import)

1. **Suma lista**: `sum_list(lst)` vrati zbir; default `lst=None` → vrati 0.
2. **Filter parnih**: `even_only(*nums)` vrati listu parnih.
3. **Range produkt**: `product_range(start, end)` vrati proizvod svih brojeva.
4. **Keyword-only format**: `format_name(ime, prezime, *, uppercase=False)`.
5. **Merge dict**: `merge_dicts(*dicts)` vraća jedan dict (kasniji prepisuje).
6. **Safe get**: `safe_get(d, key, default=None)` bez KeyError.
7. **Args i kwargs echo**: vrati tuple `(args, kwargs)` za test.
8. **Mutabilni default fix**: napiši lošu verziju, pa ispravi.
9. **Type hints**: dodaj hintove na `calc_area(width, height)`.
10. **Scope test**: `counter()` funkcija koja interno koristi `nonlocal` da broji pozive.
11. **Import math**: napravi `circle_area(r)` koristeći `math.pi`.
12. **Helper modul**: u `helpers.py` definiši `is_positive(x)`; importuj i koristi u drugoj funkciji.
13. **Docstring**: dodaj jasan docstring `def slugify(text: str) -> str` (može jednostavno replace space sa '-')
14. **Union hint**: `parse_int(x: str | int) -> int | None` (pokušaj kastovanja).
15. **Kw-only validation**: `def connect(host, *, timeout=5)` vrati string "connecting".
16. **Return None**: napravi funkciju koja vraća `None` kad nema uslova, objasni zašto.

Brzi self-check:

-   imaš barem 12/16 rešenih
-   svi mutabilni defaulti izbegnuti
-   helper modul import radi u REPL-u
