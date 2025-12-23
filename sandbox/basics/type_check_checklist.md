# ✅ Type Annotations Checklist

Pre nego što commitaš kod, proveri:

## Imports

-   [ ] `from __future__ import annotations` na početku (3.10+ kompatibilnost)
-   [ ] Sortirani importi (stdlib, third-party, local)
-   [ ] Nema `typing.List`, `typing.Dict` — koristi `list[T]`, `dict[K, V]`
-   [ ] `collections.abc` za `Iterable`, `Sequence`, `Mapping`

---

## Funkcije

-   [ ] Sve funkcije imaju `-> NoneType` ili `-> <tip>`
-   [ ] Svi parametri imaju tipske anotacije
-   [ ] Optional vrednosti: `X | None` umesto `Optional[X]`

---

## Klase i TypedDict

-   [ ] Sve klase imaju `__init__` sa tipama
-   [ ] TypedDict umesto plain dict-a za recordove
-   [ ] Protokoli za dinamičke objekte (npr. argparse.Namespace)

---

## CSV/JSON

-   [ ] TypedDict za JSON strukture
-   [ ] list[TypedDict] za CSV redove
-   [ ] Konverzija stringova (CSV) u prave tipove

---

## Type Checking

-   [ ] `mypy --strict sandbox/basics/` — bez greške
-   [ ] Pylance u VSCode je tiho
-   [ ] Nema `type: ignore` comentara (ili su opravdani)

---

## Documentation

-   [ ] Docstring za sve javne funkcije
-   [ ] Primer tipske upotrebe u docstring-u
-   [ ] README ili comments za kompleksne tipove (npr. nested dicts)
-   [ ] Objašnjenje za custom protokole ili TypedDicts
-   [ ] Changelog ili summary fajl sa zabeleškom o dodavanju tipova
-   [ ] Commit poruke jasno navode dodavanje tipova (npr. "Add type annotations to ...")

---
