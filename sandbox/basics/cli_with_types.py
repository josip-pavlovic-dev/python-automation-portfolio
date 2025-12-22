"""
CLI sa Type Annotations - Protocol klase za args
"""
import argparse
from pathlib import Path
from typing import Protocol


# 1. Definiši šta očekuješ od args objekta
class ProcessArgs(Protocol):
    """Struktura argumenata za process komandu"""
    input_file: str
    output_file: str | None
    verbose: bool
    limit: int

# 2. Handler funkcija sa tipizacijom
def cmd_process(args: ProcessArgs) -> None:
    """Process komanda"""
    input_path = Path(args.input_file)

    if not input_path.exists():
        print(f"❌ Fajl ne postoji: {input_path}")
        return

    print(f"📖 Procesuiram: {args.input_file}")
    if args.verbose:
        print(f"   - Limit: {args.limit}")
        if args.output_file:
            print(f"   - Output: {args.output_file}")

# 3. Main sa argparse
def main() -> None:
    parser = argparse.ArgumentParser(
        prog="file_processor",
        description="Procesuira fajlove sa tipskom sigurnošću"
    )

    parser.add_argument("input_file", help="Ulazni fajl")
    parser.add_argument("-o", "--output", dest="output_file", help="Izlazni fajl")
    parser.add_argument("-v", "--verbose", action="store_true", help="Detaljni ispis")
    parser.add_argument("-l", "--limit", type=int, default=100, help="Limit redova")

    args = parser.parse_args()

    # Type cast ako treba (Python to radi automatski pri argparse)
    typed_args: ProcessArgs = args  # type: ignore  # Ili koristi cast()

    cmd_process(typed_args)

if __name__ == "__main__":
    main()
