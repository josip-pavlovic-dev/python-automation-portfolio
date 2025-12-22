"""
CSV Write with Types Example | CSV pisanje sa tipovima
"""
import csv
from pathlib import Path
from typing import TypedDict


# 1. Definiši strukturu podataka sa TypedDict
class PersonalRecord(TypedDict):
    """Template podataka za osobu koju ćemo upisivati u CSV."""

    ime: str
    godine: str
    grad: str

# 2. Helper funkcija za snimanje podataka u CSV
def save_personal_records(output_path: Path, records: list[PersonalRecord]) -> None:
    """Sačuvaj listu PersonalRecord u CSV fajl."""
    fieldnames = ["ime", "godine", "grad"]
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)  # kraće od petlje
        # for record in records:
        #     writer.writerow(record)

# 3. Glavna funkcija za demonstraciju
def main() -> None:
    # Pripremi podatke za upis
    people: list[PersonalRecord] = [
        {"ime": "Jole", "godine": "40", "grad": "Novi Sad"},
        {"ime": "Jovana", "godine": "42", "grad": "Novi Sad"},
        {"ime": "Bojan", "godine": "11", "grad": "Sremska Mitrovica"},
        {"ime": "Danijel", "godine": "30", "grad": "Đurđevo"}
    ]

    # Sačuvaj podatke u CSV fajl
    output_dir = Path(__file__).parent / "type_exercises_data"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "output_people.csv"

    save_personal_records(output_file, people)
    print(f"✅ Podaci su sačuvani u {output_file}")

    # Proveri sadržaj fajla (opciono)
    with output_file.open(newline="", encoding="utf-8") as f:
        content = f.read()
        print("Sadržaj fajla:")
        print(content)

# Pokreni glavnu funkciju samo ako je ovaj fajl pokrenut direktno
if __name__ == "__main__":
    main()
