---
type: lecture
time: 100 minutes
topics: [logging, levels, format]
---

# 📖 Teorija: Logging

## 1. Zašto logging umesto print

-   Nivoi (DEBUG, INFO, WARNING, ERROR, CRITICAL)
-   Format i timestamp
-   Jednostavno isključivanje/uključivanje

## 2. BasicConfig

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)
logger.info("Start")
```

## 3. Nivoi

-   DEBUG: detalji za debug
-   INFO: normalan tok
-   WARNING: neočekivano, ali radi
-   ERROR: došlo do problema, neka funkcija nije završila
-   CRITICAL: ozbiljan kvar

## 4. Logger po modulu

```python
logger = logging.getLogger(__name__)
```

## 5. Handleri (kratko)

-   Console (default via basicConfig)
-   FileHandler: zapis u fajl

```python
fh = logging.FileHandler("app.log", encoding="utf-8")
fh.setLevel(logging.WARNING)
formatter = logging.Formatter("%(levelname)s:%(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
```

## 6. Česte greške

-   Višestruki `basicConfig` pozivi (ignorisano posle prvog)
-   Logovanje pre `basicConfig`
-   Neodgovarajući nivo (DEBUG poruke ne vide se ako je level INFO)

## 7. Mini kontrola

-   Kako postaviti format?
-   Kada koristiti WARNING vs ERROR?
-   Zašto `__name__` u getLogger?

Spreman za REPL logging vežbe.
