"""
Pisanje JSON sa Type Annotations
"""

import json
from pathlib import Path
from typing import TypedDict


# Definiši tipove podataka za JSON strukturu
class Person(TypedDict):
    """TypedDict za osobu"""
    name: str
    age: int
    email: str | None

class Database(TypedDict):
    """TypedDict za bazu podataka osoba"""
    version: str
    people: list[Person]

def save_database(output_path: Path, data: Database) -> None:
    """Sačuvaj bazu podataka osoba u JSON fajl sa tipovima."""
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main() -> None:
    # Pripremi podatke za upis
    data: Database = {
        "version": "1.0",
        "people": [
            {"name": "Ana", "age": 28, "email": "ana@example.com"},
            {"name": "Marko", "age": 35, "email": None},
            {"name": "Jelena", "age": 22, "email": "jelena@example.com"},
        ],
    }

    output_path = Path(__file__).parent / "type_exercises_data" / "people_database.json"
    save_database(output_path, data)
    print(f"📁 Baza podataka sačuvana u: {output_path.resolve()}")

if __name__ == "__main__":
    main()

# Kako pokrenuti:
# python sandbox/basics/json_write_with_types.py
