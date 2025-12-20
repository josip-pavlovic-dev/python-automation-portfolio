import argparse


def main():
    parser = argparse.ArgumentParser(description="Cli alat sa opcionim argumentima.")
    # Dodaj opcione argumente
    # Pozicioni argumenti su obavezni, dok su opcioni argumenti oni koji nisu obavezni.
    parser.add_argument("input_file", help="Ulazni fajl za obradu.")

    # Opcioni argument sa podrazumevanom vrednošću (pocinje sa -- ili -)
    parser.add_argument(
        "--output_file",
        "-o",
        help="Izlazni fajl za čuvanje rezultata.",
        default="output.txt"
    )

    # Opcioni argument sa tipom podataka i podrazumevanom vrednošću
    parser.add_argument(
        "--limit",
        "-l",
        type=int,
        default=10,
        help="Ograniči broj obrađenih redova (podrazumevano: 10)."
    )

    # Parsuj argumente
    args = parser.parse_args()

    # Koristi argumente
    print(f"Ulazni fajl: {args.input_file}")
    print(f"Izlazni fajl: {args.output_file}")
    print(f"Ograničenje broja redova: {args.limit}")

# Zaštitni blok za pokretanje glavne funkcije
if __name__ == "__main__":
    main()
