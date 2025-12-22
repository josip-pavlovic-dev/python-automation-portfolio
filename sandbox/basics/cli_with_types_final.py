"""
CLI sa Type Annotations - Protocol klase za args (moderni stil)
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Protocol, cast


class ProcessArgs(Protocol):
    """Struktura očekivanih argumenata iz CLI-a za process komandu."""

    input_file: Path
    output_file: Path | None
    verbose: bool
    limit: int


def cmd_process(args: ProcessArgs) -> None:
    """Obradi fajl sa zadatim argumentima."""

    if not args.input_file.exists():
        print(f"⚠️ Ulazni fajl '{args.input_file}' ne postoji.")
        return

    print(f"📂 Processing file: {args.input_file}")
    if args.verbose:
        print(f"   - Limit: {args.limit}")
        if args.output_file:
            print(f"   - Output: {args.output_file}")

    # Ovde bi išla prava obrada fajla (čitanje, transformacija, zapis...)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="file_processor",
        description="Process input files with specified options",
    )
    # Pozicioni argument (obavezna vrednost bez zastavice)
    parser.add_argument(
        "input_file",
        type=Path,
        help="Putanja do ulaznog fajla za obradu",
    )
    # Opcionalne zastavice
    parser.add_argument(
        "-o",
        "--output-file",
        type=Path,
        default=None,
        help="Putanja za čuvanje obrađenog izlaza (opciono)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Uključi detaljni ispis tokom obrade",
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        default=100,
        help="Maksimalan broj redova za obradu (standardno: 100)",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    """Glavna funkcija za pokretanje CLI-a."""

    parser = build_parser()
    args = parser.parse_args(argv)

    typed_args = cast(ProcessArgs, args)
    cmd_process(typed_args)


if __name__ == "__main__":
    main()
