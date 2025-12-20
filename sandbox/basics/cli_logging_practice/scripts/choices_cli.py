import argparse


def main():
    parser = argparse.ArgumentParser(description="Cli alat sa ogrančenim izborima.")

    # Dodaj argument sa ograničenim izborima
    parser.add_argument(
        "format",
        choices=["json", "xml", "csv"],
        help="Izaberite format za izlazne podatke (json, xml, csv)."
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Izaberite nivo logovanja."
    )

    # Parsuj argumente
    args = parser.parse_args()

    # Koristi argumente
    print(f"Izabrani format: {args.format}")
    print(f"Izabrani nivo logovanja: {args.log_level}")

# Zaštitni blok za pokretanje glavne funkcije
if __name__ == "__main__":
    main()

