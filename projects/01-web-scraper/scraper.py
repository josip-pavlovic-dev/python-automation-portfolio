from __future__ import annotations

import argparse
import json
import logging
import os
import time
from collections.abc import Sequence
from logging.handlers import RotatingFileHandler
from typing import Any

import requests
from bs4 import BeautifulSoup

try:
    import config as cfg
except ImportError:  # Fallbacks when config is missing
    cfg = None


DEFAULT_URLS: Sequence[str] = (
    cfg.URLS if cfg and hasattr(cfg, "URLS") else ["https://quotes.toscrape.com/"]
)
DEFAULT_HEADERS: dict[str, str] = (
    cfg.HEADERS
    if cfg and hasattr(cfg, "HEADERS")
    else {"User-Agent": "python-automation-portfolio/1.0"}
)
DEFAULT_OUTPUT_PATH: str = (
    cfg.OUTPUT_PATH if cfg and hasattr(cfg, "OUTPUT_PATH") else "output.json"
)
DEFAULT_TIMEOUT: int = (
    cfg.REQUEST_TIMEOUT if cfg and hasattr(cfg, "REQUEST_TIMEOUT") else 15
)
DEFAULT_DELAY: float = (
    cfg.DELAY_BETWEEN_REQUESTS
    if cfg and hasattr(cfg, "DELAY_BETWEEN_REQUESTS")
    else 0.0
)


def setup_logger(
    level: int = logging.INFO, log_path: str = "logs/scraper.log"
) -> logging.Logger:
    logger = logging.getLogger("web_scraper")
    if logger.handlers:
        # Reuse existing handlers if already configured
        logger.setLevel(level)
        return logger

    logger.setLevel(level)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(logging.Formatter("%(levelname)s %(message)s"))

    # Rotating file handler
    fh = RotatingFileHandler(log_path, maxBytes=512_000, backupCount=3)
    fh.setLevel(level)
    fh.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s [%(name)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )

    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger


class Scraper:
    def __init__(
        self,
        urls: Sequence[str] | None = None,
        headers: dict[str, str] | None = None,
        output_path: str | None = None,
        timeout: int = DEFAULT_TIMEOUT,
        delay: float = DEFAULT_DELAY,
        logger: logging.Logger | None = None,
    ) -> None:
        self.urls = list(urls) if urls is not None else list(DEFAULT_URLS)
        self.headers = headers if headers is not None else dict(DEFAULT_HEADERS)
        self.output_path = output_path or DEFAULT_OUTPUT_PATH
        self.timeout = timeout
        self.delay = delay
        self.logger = logger or setup_logger()

    def fetch(self, url: str) -> str:
        self.logger.info(f"Fetching: {url}")
        resp = requests.get(url, headers=self.headers, timeout=self.timeout)
        resp.raise_for_status()
        self.logger.info(f"Fetched {len(resp.text)} chars")
        return resp.text

    def parse_quotes(self, html: str) -> list[dict[str, Any]]:
        soup = BeautifulSoup(html, "lxml")
        results: list[dict[str, Any]] = []

        # Typical structure on quotes.toscrape.com
        for block in soup.select("div.quote"):
            text_el = block.select_one("span.text")
            author_el = block.select_one("small.author")
            # Accept both structures: with or without a wrapping div.tags
            tag_els = block.select("a.tag")

            text = text_el.get_text(strip=True) if text_el else ""
            author = author_el.get_text(strip=True) if author_el else ""
            tags = [t.get_text(strip=True) for t in tag_els] if tag_els else []

            # Normalize smart quotes if present
            text = text.replace("“", '"').replace("”", '"')

            results.append(
                {
                    "text": text,
                    "author": author,
                    "tags": tags,
                }
            )

        return results

    def run(self) -> list[dict[str, Any]]:
        all_rows: list[dict[str, Any]] = []

        for i, url in enumerate(self.urls, 1):
            self.logger.info(f"[{i}/{len(self.urls)}] Processing {url}")
            html = self.fetch(url)
            rows = self.parse_quotes(html)
            self.logger.info(f"Parsed {len(rows)} quotes")
            all_rows.extend(rows)

            if self.delay and i < len(self.urls):
                time.sleep(self.delay)

        return all_rows


# Module-level function to satisfy tests importing `parse_quotes`
def parse_quotes(html: str) -> list[dict[str, Any]]:
    return Scraper().parse_quotes(html)


def _write_output(rows: list[dict[str, Any]], fmt: str, out_path: str | None) -> None:
    if fmt == "json":
        content = json.dumps(rows, ensure_ascii=False, indent=2)
    elif fmt == "csv":
        import csv
        from io import StringIO

        buf = StringIO()
        writer = csv.DictWriter(buf, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        for r in rows:
            writer.writerow(
                {
                    "text": r.get("text", ""),
                    "author": r.get("author", ""),
                    "tags": ",".join(r.get("tags", [])),
                }
            )
        content = buf.getvalue()
    else:
        raise ValueError("Unsupported format: " + fmt)

    if out_path:
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        print(content)


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Quotes scraper CLI")
    p.add_argument("--url", help="URL to scrape", default=None)
    p.add_argument(
        "--format", choices=["json", "csv"], default="json", help="Output format"
    )
    p.add_argument("--out", help="Write output to file (optional)")
    p.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logger level",
    )
    return p


def main() -> None:
    args = build_arg_parser().parse_args()
    level = getattr(logging, args.log_level.upper(), logging.INFO)
    logger = setup_logger(level=level)
    urls = [args.url] if args.url else list(DEFAULT_URLS)
    scraper = Scraper(urls=urls, logger=logger)

    rows = scraper.run()
    _write_output(rows, args.format, args.out or scraper.output_path)


if __name__ == "__main__":
    main()
