import argparse


def main():
    parser = argparse.ArgumentParser(description="Cli alat sa boolean zastavicama.")

    # Dodaj pozicioni argument
    parser.add_argument("path", help="Putanja do fajla za obradu.")

    # Dodaj boolean zastavicu
    # Boolean Flag -> defaultno je False, ako se navede postaje True
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Omogući detaljno ispisivanje informacija.",
    )

    # Dodaj još jednu boolean zastavicu
    parser.add_argument(
        "--dry-run",
        "-d",
        action="store_true",
        help="Simuliraj probni rad bez stvarnih izmena.",
    )

    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Ne prikazuj nikakve informacije osim grešaka."
    )
    # Parsuj argumente
    args = parser.parse_args()

    # Koristi argumente
    print(f"Putanja do fajla: {args.path}")
    if args.verbose:
        print("Detaljno ispisivanje je omogućeno.")
    if args.dry_run:
        print("Probni rad je omogućen. Nema stvarnih izmena.")
    if args.quiet:
        print("Tihi režim je omogućen. Prikazivaće se samo greške.")

# Zaštitni blok za pokretanje glavne funkcije
if __name__ == "__main__":
    main()
