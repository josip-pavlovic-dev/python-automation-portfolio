# Cheatsheet – CLI + Logging (Day 02)

## Argparse brzinski

```python
parser = argparse.ArgumentParser(description="Web Scraper")
parser.add_argument("--urls", nargs="*", default=None)
parser.add_argument("--output", type=Path, default=Path("output/quotes.csv"))
parser.add_argument("--delay", type=float, default=1.0)
parser.add_argument("--timeout", type=int, default=10)
parser.add_argument("--log", type=Path, default=Path("logs/scraper.log"))
parser.add_argument("--level", default="INFO", choices=["DEBUG","INFO","WARNING","ERROR"])
args = parser.parse_args()
```

## Logging setup (console + rotating)

```python
from logging.handlers import RotatingFileHandler

def setup_logger(log_file: Path, level: str) -> logging.Logger:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("scraper")
    logger.setLevel(getattr(logging, level))
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    ch = logging.StreamHandler()
    ch.setLevel(getattr(logging, level))
    ch.setFormatter(fmt)

    fh = RotatingFileHandler(log_file, maxBytes=500_000, backupCount=3)
    fh.setLevel(getattr(logging, level))
    fh.setFormatter(fmt)

    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)
    return logger
```

## Korišćenje

```bash
python scraper.py --urls https://quotes.toscrape.com/page/1/ --output output/quotes.csv --delay 0.5 --timeout 10 --log logs/scraper.log --level INFO
```

## Test stub (pytest)

```python
class DummyLogger:
    def info(self, *_, **__):
        pass
    def error(self, *_, **__):
        pass


def test_parse_quotes():
    html = "<div class='quote'><span class='text'>Q1</span><small class='author'>A1</small></div>"
    data = scraper.parse_quotes(html)
    assert data[0]["author"] == "A1"
```
