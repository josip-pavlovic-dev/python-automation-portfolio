---
type: quick_start
time: "30 min"
---

# ⚡ 30-Min Start — Dan 7: Logging + Pytest

## Logging brzi start

```python
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
logger = logging.getLogger(__name__)
logger.info("Pokrenuto")
```

## Pytest brzi start

Napravi `calc.py`:

```python
def add(a, b):
    return a + b
```

Napravi `test_calc.py`:

```python
from calc import add

def test_add():
    assert add(2, 3) == 5
```

Pokreni: `pytest -q`

✅ Spreman; idi na kickoff.

## Hintovi za rad (tvoj nivo)

-   Logger: setuj `level=logging.DEBUG` i dodaj `StreamHandler` sa formatom; pre poziva proveri `len(logger.handlers)` da nema duplikata.
-   Propagacija: napravi podlogger `logging.getLogger("app.service")` i postavi `propagate=False` ako ne želiš dupli izlaz.
-   Pytest: napiši `pytest.raises(ValueError)` test, jedan `@pytest.mark.parametrize`, i fixture sa `yield` (setup/teardown osećaj).
-   Caplog: u testu `caplog.set_level(logging.WARNING, logger="app")`, pozovi funkciju i proveri `caplog.records` da vidiš poruku.
-   Markeri: dodaj `@pytest.mark.slow` i probaj `pytest -m "not slow"` da filtriraš.
