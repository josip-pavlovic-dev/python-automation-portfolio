import argparse


def main():
    parser = argparse.ArgumentParser(description="Cli alat sa višestrukim argumentima.")

    # Dodaj argument koji prihvata više vrednosti

    # nargs="+" znači jedan ili više argumenata
    parser.add_argument(
        "files",
        nargs="+",
        help="Lista fajlova za obradu (jedan ili više)."
    )

    # nargs="*" znači nula ili više argumenata
    parser.add_argument(
        "--ignore",
        nargs="*",
        default=[],
        help="Lista fajlova (paterni) koje treba ignorisati (nula ili više)."
    )

    # nargs=2 znači tačno dva argumenta
    parser.add_argument(
        "--range",
        nargs=2,
        type=int,
        help="Početak i kraj opsega za obradu (npr: --range 1 10)."
    )

    # Parsuj argumente
    args = parser.parse_args()

    # Koristi argumente
    print(f"Fajlovi za obradu: {args.files}")
    print(f"Fajlovi koje treba ignorisati: {args.ignore}")
    if args.range:
        print(f"Opseg za obradu: od {args.range[0]} do {args.range[1]}")
    else:
        print("Nije definisan opseg za obradu.")

# Zaštitni blok za pokretanje glavne funkcije
if __name__ == "__main__":
    main()
