"""
Refaktorisan basic_cli.py koristeći Type Annotations
"""

from __future__ import annotations

import argparse
import logging

# Konfiguriši logger
logger = logging.getLogger("basic_cli")

def positive_int(value: str) -> int:
    """Validator: Provera da li je vrednost pozitivan ceo broj."""
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} nije pozitivan ceo broj")
    return ivalue

def configure_logging(verbose: int) -> None:
    """Konfiguracija logovanja prema verbosity levelu"""
    level = logging.WARNING
    if verbose == 1:
        level = logging.INFO
    elif verbose >= 2:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger.debug("Logger configured")

def main(argv: list[str] | None = None) -> int:
    """Glavna funkcija sa tipskom sigurnošću"""
    parser = argparse.ArgumentParser(
        prog="basic_cli",
        description="CLI alat sa tipskim anotacijama"
    )

    parser.add_argument("-v", "--verbose", action="count", default=0,
    help="Verbosity (-v, -vv)")
    parser.add_argument("name", help="Your name")
    parser.add_argument("age", type=positive_int, help="Your age (>= 0)")

    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    logger.info("Starting application")
    print(f"Zdravo, {args.name}! Imaš {args.age} godina.")
    logger.debug(f"Processed: name={args.name}, age={args.age}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())

# Pokreni iz komandne linije:

# python3 sandbox/basics/cli_logging_practice/scripts/basic_cli_typed.py Jole 30

# python3 sandbox/basics/cli_logging_practice/scripts/basic_cli_typed.py Jole 30 -v

# python3 sandbox/basics/cli_logging_practice/scripts/basic_cli_typed.py Jole 30 -vv

# python3 sandbox/basics/cli_logging_practice/scripts/basic_cli_typed.py Jole -5 -vv
