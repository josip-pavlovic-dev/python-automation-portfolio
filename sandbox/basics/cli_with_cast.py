"""
Bolje: Koristi cast() umesto type: ignore
"""
import argparse
from pathlib import Path
from typing import Protocol, cast


class ProcessArgs(Protocol):
    input_file: str
    output_file: str | None
    verbose: bool
    limit: int

def cmd_process(args: ProcessArgs) -> None:
    input_path = Path(args.input_file)
    print(f"📖 Procesuiram: {input_path}")
    if args.verbose:
        print(f"   - Limit: {args.limit}")
        if args.output_file:
            print(f"   - Output: {args.output_file}")

def main() -> None:
    parser = argparse.ArgumentParser(prog="file_processor")
    parser.add_argument("input_file")
    parser.add_argument("-o", "--output", dest="output_file")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-l", "--limit", type=int, default=100)

    args = parser.parse_args()

    # BOLJE: Koristi cast() - jasno je da konvertuješ
    typed_args: ProcessArgs = cast(ProcessArgs, args)

    cmd_process(typed_args)

if __name__ == "__main__":
    main()
