---
type: kickoff
schedule: 8h
---

# 🚀 Kickoff — Dan 7: Logging + Pytest

## Plan (8h)

| Vreme       | Aktivnost             |
| ----------- | --------------------- |
| 08:00-08:20 | START_HERE            |
| 08:20-10:00 | TEORIJA_logging       |
| 10:00-11:00 | REPL logging          |
| 11:00-11:20 | Pauza                 |
| 11:20-13:00 | TEORIJA_pytest_osnove |
| 13:00-14:00 | REPL pytest           |
| 14:00-15:00 | MINI_PROBLEMI_dan7    |
| 15:00-16:00 | summary               |

## Fokus

-   Logger hijerarhija, nivo, handleri, format
-   `basicConfig` vs ručna konfiguracija
-   `caplog`, `pytest.raises`, `parametrize`, fixture životni ciklus
-   Markeri (`-m slow`) i selekcija testova

## Česta spoticanja

-   Duplirani handleri (proveri `logger.handlers`)
-   Propagacija ka root loggeru kada ne želiš
-   Zaboravljeno `ensure_ascii=False` u JSON logovima
-   Testovi zavisni od reda (loše!
    )
-   `caplog` mora videti logger level <= message level da bi zabeležio poruku

## Pytest komande (primer)

-   `pytest -q` — tihi izlaz
-   `pytest -m "not slow"` — preskoči `@pytest.mark.slow`
-   `pytest -k add -q` — pokreni testove koji u imenu sadrže "add"

Srećno! 💪
