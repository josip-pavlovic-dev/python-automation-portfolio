import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="basic_cli",
        description="Primer osnovnog CLI alata sa argumentima.",
        epilog="Hvala što koristite naš CLI alat!"
    )
    # 2. Dodaj argumente
    parser.add_argument("name", help="Vaše ime.")
    parser.add_argument("godine", type=int, help="Vaše godine.")

    # 3. Parsuj
    args = parser.parse_args()

    # 4. Koristi argumente
    print(f"Zdravo, {args.name}! Imaš {args.godine} godina.")

# Zaštitni blok za pokretanje glavne funkcije
if __name__ == "__main__":
    main()


