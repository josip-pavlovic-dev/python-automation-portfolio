"""
Refaktorisani subcommands_cli.py sa type annotations
"""

from __future__ import annotations

import argparse
import logging
from typing import Protocol

logger = logging.getLogger("datatools")


# 1. Definiši strukture za svaku komandu
class ListArgs(Protocol):
    path: str # Putanja do direktorijuma za listanje
    recursive: bool # Da li je rekurzivno listanje uključeno
    verbose: bool # verbose flag je zajednički za sve komande i koristi se za logovanje


class SearchArgs(Protocol):
    pattern: str # Šta tražiš
    file: str # Gde tražiš
    verbose: bool # verbose znači da li je logovanje detaljno


class ExportArgs(Protocol):
    format: str # Format za izvoz
    output: str | None # Putanja do izlaznog fajla ili None
    verbose: bool # verbose znači da li je logovanje detaljno


# 2. Handler funkcije sa tipama
def cmd_list(args: ListArgs) -> None:
    """List command"""
    logger.info(f"Listing: {args.path}")
    print(f"📝 Listanje fajlova u: {args.path}")
    if args.recursive:
        logger.debug("Recursive mode enabled")
        print("🔄 Rekurzivno listanje uključeno.")


def cmd_search(args: SearchArgs) -> None:
    """Search command"""
    logger.info(f"Searching for: {args.pattern} in {args.file}")
    print(f"🔍 Pretraga fajlova za: {args.pattern}")
    print(f" 💾 U fajlu: {args.file}")


def cmd_export(args: ExportArgs) -> None:
    """Export command"""
    logger.info(f"Exporting as: {args.format}")
    print(f"📤 Izvoz fajlova u format: {args.format}")
    if args.output:
        logger.info(f"Output file: {args.output}")
        print(f" 💾 Izlazni fajl: {args.output}")


# 3. Main sa potpunom tipizacijom
def main() -> int:
    """Main function"""
    # Common options available both before and after subcommands
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Omogući detaljno ispisivanje informacija.",
    )

    parser = argparse.ArgumentParser(
        prog="datatools",
        description="Alat za rad sa podacima - listanje, pretraga i izvoz fajlova.",
        parents=[common],
    )

    subparsers = parser.add_subparsers(
        title="Komande",
        description="Dostupne komande za rad sa podacima.",
        dest="command",
        required=True,
    )

    # List subcommand
    parser_list = subparsers.add_parser(
        "list", help="Listanje fajlova u direktorijumu.", parents=[common]
    )
    parser_list.add_argument("path", help="Putanja do direktorijuma za listanje.")
    parser_list.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="Rekurzivno listanje poddirektorijuma.",
    )
    parser_list.set_defaults(func=cmd_list)

    # Search subcommand
    parser_search = subparsers.add_parser(
        "search", help="Pretraga fajlova.", parents=[common]
    )
    parser_search.add_argument("pattern", help="Šta tražiš?")
    parser_search.add_argument("file", help="Gde tražiš?")
    parser_search.set_defaults(func=cmd_search)

    # Export subcommand
    parser_export = subparsers.add_parser(
        "export", help="Izvoz fajlova.", parents=[common]
    )
    parser_export.add_argument(
        "--format", choices=["csv", "json"], default="csv", help="Format za export"
    )
    parser_export.add_argument("--output", "-o", help="Putanja do izlaznog fajla.")
    parser_export.set_defaults(func=cmd_export)

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s",
    )

    if args.verbose:
        print("🔊 Verbose mode enabled.")

    # Pozovi handler
    args.func(args)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Pokreni iz komandne linije:
# type:ignore # python3 sandbox/basics/cli_logging_practice/scripts/subcommands_cli_typed.py list /tmp -v
# type:ignore # python3 sandbox/basics/cli_logging_practice/scripts/subcommands_cli_typed.py search "test" file.txt
# mypy sandbox/basics/cli_logging_practice/scripts/subcommands_cli_typed.py
