"""
CSV Reader sa Type Annotations — DictReader verzija
"""

import csv
from pathlib import Path
from typing import TypedDict


# 1. Definiši strukturu podataka sa TypedDict
class UserRecord(TypedDict):
    """Struktura jednog reda iz users.csv"""

    name: str
    age: str  # CSV čita sve kao stringove;
    # kasnije možemo konvertovati u int ako je potrebno
    city: str


# 2. Helperske funkcije za čitanje CSV-a
def load_users(file_path: Path) -> list[UserRecord]:
    """Učitaj korisnike iz CSV fajla kao listu UserRecord."""
    users: list[UserRecord] = []
    with file_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # ✅ Provera da li red ima sadržaj (nije prazan)
            if row and row.get("name"):  # Ako row postoji I ima 'name' polje
                user: UserRecord = {
                    "name": row["name"],
                    "age": row["age"],
                    "city": row["city"],
                }
                users.append(user)
    return users

# 3. Glavna (Main) funkcija za demonstraciju
def main() -> None:
    data_dir = Path(__file__).parent / "type_exercises_data"
    csv_file = data_dir / "users.csv"

    users = load_users(csv_file)

    for user in users:
        print(f"{user['name']} ({user['age']}) iz {user['city']}")

if __name__ == "__main__":
    main()

# Run mypy to check types:
# mypy sandbox/basics/csv_with_types.py
# mypy should report no errors if everything is correct
