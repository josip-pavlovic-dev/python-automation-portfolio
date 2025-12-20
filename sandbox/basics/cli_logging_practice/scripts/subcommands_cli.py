import argparse
from typing import Protocol


class ListArgs(Protocol):
    path: str
    recursive: bool
    verbose: bool


class SearchArgs(Protocol):
    pattern: str
    file: str
    verbose: bool


class ExportArgs(Protocol):
    format: str
    output: str | None
    verbose: bool


def cmd_list(args: ListArgs) -> None:
    print(f"📝 Listanje fajlova u: {args.path}")
    if args.recursive:
        print("🔄 Rekurzivno listanje uključeno.")


def cmd_search(args: SearchArgs) -> None:
    print(f"🔍 Pretraga fajlova za: {args.pattern}")
    print(f" 💾 U fajlu: {args.file}")


def cmd_export(args: ExportArgs) -> None:
    print(f"📤 Izvoz fajlova u format: {args.format}")
    if args.output:
        print(f" 💾 Izlazni fajl: {args.output}")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="datatools",
        description="Alat za rad sa podacima - listanje, pretraga i izvoz fajlova."
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Omogući detaljno ispisivanje informacija."
    )

    subparsers = parser.add_subparsers(
        title="Komande",
        description="Dostupne komande za rad sa podacima.",
        dest="command",
        required=True
    )

    # Komanda: list
    parser_list = subparsers.add_parser(
        "list",
        help="Listanje fajlova u direktorijumu."
    )
    parser_list.add_argument("path", help="Putanja do direktorijuma za listanje.")
    parser_list.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="Rekurzivno listanje poddirektorijuma."
    )
    parser_list.set_defaults(func=cmd_list)

    # Komanda: search
    parser_search = subparsers.add_parser(
        "search",
        help="Pretraga fajlova za određenim obrascem."
    )
    parser_search.add_argument("pattern", help="Šta tražiš? (Obrazac za pretragu)")
    parser_search.add_argument(
        "file",
        help="Gde tražiš? (Fajl u kojem se vrši pretraga)"
    )
    parser_search.set_defaults(func=cmd_search)

    # Komanda: export
    parser_export = subparsers.add_parser(
        "export",
        help="Izvoz / Eksportovanje fajlova u određenom formatu."
    )
    parser_export.add_argument(
        "--format",
        choices=["csv", "json"],
        default="csv",
        help="Format u koji se fajlovi izvoze (npr. csv, json)."
    )
    parser_export.add_argument(
        "--output",
        "-o",
        help="Putanja do izlaznog fajla."
    )
    parser_export.set_defaults(func=cmd_export)

    args = parser.parse_args()

    if args.verbose:
        print("🔊 Verbose mode enabled.")

    args.func(args)


if __name__ == "__main__":
    main()
