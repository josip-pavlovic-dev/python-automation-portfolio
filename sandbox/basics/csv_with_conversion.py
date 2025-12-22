"""
CSV with Type Conversion Example | CSV sa konverzijom tipova
"""

import csv
from pathlib import Path
from typing import NotRequired, TypedDict


# TypedDict sa NotRequired poljima (neobavezna polja, python 3.11+)
class UserStrictRecord(TypedDict):
    """Stroga tipizacija jednog reda iz CSV fajla (svi stringovi)"""

    name: str
    age: str  # Čuvamo kao string iz CSV-a
    city: str
    email: NotRequired[str]  # Neobavezno polje


class UserConvertedRecord(TypedDict):
    """Konvertovana verzija UserRecord sa odgovarajućim tipovima (age je integer)"""

    name: str
    age: int  # Konvertovano u int
    city: str
    email: NotRequired[str]  # Neobavezno polje


def load_and_convert_users(file_path: Path) -> list[UserConvertedRecord]:
    """Učitaj korisnike iz CSV fajla i konvertuj tipove podataka."""

    converted_users: list[UserConvertedRecord] = []
    with file_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row and row.get("name"):
                try:
                    # Konvertuj age iz stringa u int
                    age_int = int(row["age"]) if row["age"].isdigit() else 0
                    user: UserConvertedRecord = {
                        "name": row["name"],
                        "age": age_int,
                        "city": row["city"],
                    }
                    # Dodaj email ako postoji
                    if "email" in row and row["email"]:
                        user["email"] = row["email"]
                    converted_users.append(user)
                except ValueError as e:
                    print(f"⚠️ Greška pri konverziji za red {row}: {e}")
                    print(f"⚠️ Greška pri konverziji: {row['age']} nije integer — {e}")
    return converted_users


def main() -> None:
    data_dir = Path(__file__).parent / "type_exercises_data"
    csv_file = data_dir / "users.csv"

    users = load_and_convert_users(csv_file)

    for user in users:
        ten_years: int = user["age"] + 10
        email_info = f", email: {user['email']}" if "email" in user else ""
        print(f"{user['name']} ({user['age']}) iz {user['city']}{email_info}. ")
        print(f"Za 10 godine će imati {ten_years} godine. ")

if __name__ == "__main__":
    main()
