from __future__ import annotations

import argparse
import json
import logging
from collections.abc import Iterable, Sequence
from logging.handlers import RotatingFileHandler
from pathlib import Path
from time import sleep

# =============================================================================
# DAY 02 MINI-LAB: CLI + LOGGING + TESTABILNOST
# -----------------------------------------------------------------------------
# Ovaj fajl je "mini-skriper" za vežbu argparser + logging + strukture podataka.
# Fokus: čitljiv CLI, predvidljiv logging, jasni tipovi za Pylance/Mypy.
# Sve funkcije su male i testabilne.
# =============================================================================

DEFAULT_URLS: list[str] = [
    "https://quotes.toscrape.com/page/1/",
    "https://quotes.toscrape.com/page/2/",
]
DEFAULT_HEADERS: dict[str, str] = {"User-Agent": "python-automation-lab/0.1"}
DEFAULT_OUTPUT = Path("output/cli_logging_demo.json")
DEFAULT_LOG = Path("logs/cli_logging_demo.log")


# -----------------------------------------------------------------------------
# ARGPARSE
# -----------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Mini scraper demo (CLI + logging)")
    parser.add_argument(
        "--urls",
        nargs="*",
        default=None,
        help="Lista URL-ova za scraping; ako nije zadato koristi DEFAULT_URLS",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Putanja za izlazni JSON (default: output/cli_logging_demo.json)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Pauza između URL-ova u sekundama",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Timeout za jednu stranicu (sekunde) – simuliran u ovom demo-u",
    )
    parser.add_argument(
        "--log",
        type=Path,
        default=DEFAULT_LOG,
        help="Putanja za log fajl (rotating)",
    )
    parser.add_argument(
        "--level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Log nivo",
    )
    return parser


# -----------------------------------------------------------------------------
# LOGGING
# -----------------------------------------------------------------------------

def setup_logger(log_file: Path, level: str) -> logging.Logger:
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("cli_demo")
    logger.setLevel(getattr(logging, level))

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    console = logging.StreamHandler()
    console.setLevel(getattr(logging, level))
    console.setFormatter(formatter)

    rotating = RotatingFileHandler(log_file, maxBytes=500_000, backupCount=3)
    rotating.setLevel(getattr(logging, level))
    rotating.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console)
        logger.addHandler(rotating)

    return logger


# -----------------------------------------------------------------------------
# SCRAPER CORE (DEMO) - čisto za vežbu, bez realnog mrežnog poziva
# -----------------------------------------------------------------------------

def choose_urls(user_urls: Sequence[str] | None) -> list[str]:
    return list(user_urls) if user_urls else DEFAULT_URLS


def fake_fetch(url: str, timeout: int, delay: float, logger: logging.Logger) -> str:
    logger.debug("Fetching %s (timeout=%s, delay=%s)", url, timeout, delay)
    sleep(delay)
    # Simuliramo HTML koji bi došao sa quotes.toscrape.com
    return f"<html><body><div class='quote'>Quote from {url}</div></body></html>"


def parse_quotes_from_html(html: str) -> list[dict[str, str]]:
    # Minimalna pars logika (string based) da izbegnemo dodatne zavisnosti.
    # Tražimo substring "Quote from <URL>".
    markers: list[str] = []
    start_token = "Quote from "
    remaining = html
    while start_token in remaining:
        start_idx = remaining.index(start_token) + len(start_token)
        end_idx = remaining.find("</", start_idx)
        if end_idx == -1:
            break
        markers.append(remaining[start_idx:end_idx])
        remaining = remaining[end_idx:]
    return [{"quote": f"Quote {i+1}", "source": src} for i, src in enumerate(markers)]


def persist_results(output_path: Path, rows: Iterable[dict[str, str]]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    data = list(rows)
    output_path.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                            encoding="utf-8")


# -----------------------------------------------------------------------------
# ORCHESTRATION
# -----------------------------------------------------------------------------


def run_cli_demo(urls: Sequence[str] | None, output: Path, delay: float, timeout: int,
                 logger: logging.Logger) -> list[dict[str, str]]:
    chosen = choose_urls(urls)
    logger.info("Start scraping %d URL(s)", len(chosen))

    results: list[dict[str, str]] = []
    for url in chosen:
        html = fake_fetch(url, timeout, delay, logger)
        parsed = parse_quotes_from_html(html)
        logger.debug("Parsed %d quotes from %s", len(parsed), url)
        results.extend(parsed)

    persist_results(output, results)
    logger.info("Saved %d rows to %s", len(results), output)
    return results


# -----------------------------------------------------------------------------
# TEST HELPERS (za pytest / REPL)
# -----------------------------------------------------------------------------

def build_defaults() -> dict[str, object]:
    return {
        "urls": DEFAULT_URLS,
        "output": DEFAULT_OUTPUT,
        "delay": 0.1,
        "timeout": 5,
        "log": DEFAULT_LOG,
        "level": "INFO",
    }


def main() -> None:
    args = build_parser().parse_args()
    logger = setup_logger(args.log, args.level)
    run_cli_demo(args.urls, args.output, args.delay, args.timeout, logger)


if __name__ == "__main__":
    main()
