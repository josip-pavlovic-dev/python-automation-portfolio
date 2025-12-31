---
type: repl_exercises
time: 60 minutes
topics: [logging]
---

# 🧪 REPL Vežbe — Logging

## FAZA 1 — BasicConfig (15 min)

1. Postavi `basicConfig` sa level INFO i format `'%(levelname)s:%(message)s'`; pošalji `logger.debug/info/warning` i vidi šta se prikazuje.

## FAZA 2 — File handler (20 min)

2. Dodaj `FileHandler("app.log")` sa WARNING nivoom; generiši warning/error i proveri sadržaj fajla.

## FAZA 3 — Modul logger (15 min)

3. Napravi `utils_log.py` sa loggerom `logging.getLogger(__name__)`; importuj ga i pozovi funkciju koja loguje.

## FAZA 4 — Mini integracija (10 min)

4. Napravi funkciju `div(a,b)` koja loguje INFO pre deljenja, a na ZeroDivisionError loguje ERROR i propagira grešku.

✅ Check: razlika nivoa, file handler radi, logger po modulu radi.
