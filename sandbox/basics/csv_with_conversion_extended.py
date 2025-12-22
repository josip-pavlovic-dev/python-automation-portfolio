"""
CSV with Type Conversion (Extended)
- Adds optional email to users and persists to CSV
- Demonstrates idiomatic `with` usage and Path API you can reuse
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import NotRequired, TypedDict


# 1) Typed records used across read/update/write
class UserStrictRecord(TypedDict):
    """Strict CSV row as read — all values are strings."""

    name: str
    age: str
    city: str
    email: NotRequired[str]  # Optional field: may be missing in CSV


class UserConvertedRecord(TypedDict):
    """Converted record for processing — `age` becomes an int."""

    name: str
    age: int
    city: str
    email: NotRequired[str]


# 2) CSV helpers — consistent, reusable style
def load_users(csv_path: Path) -> list[UserStrictRecord]:
    """Load CSV into a list of dict rows (all strings).

    Style notes:
    - Define constants (like `fieldnames`) outside `with` when possible.
    - Use `Path.open()` for consistency with `pathlib.Path` across projects.
    - `with` ensures file is closed automatically, even on exceptions.
    """
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        users: list[UserStrictRecord] = []
        for row in reader:
            if not row:
                continue
            # Normalize: keep only known keys; ignore extras if present
            user: UserStrictRecord = {
                "name": row.get("name", ""),
                "age": row.get("age", ""),
                "city": row.get("city", ""),
            }
            if "email" in row and row["email"]:
                user["email"] = row["email"]
            users.append(user)
    return users


def convert_users(users: list[UserStrictRecord]) -> list[UserConvertedRecord]:
    """Convert `age` to int, keep optional `email` if present."""
    converted: list[UserConvertedRecord] = []
    for u in users:
        age_str = u.get("age", "")
        age_int = int(age_str) if age_str.isdigit() else 0
        cu: UserConvertedRecord = {
            "name": u.get("name", ""),
            "age": age_int,
            "city": u.get("city", ""),
        }
        if "email" in u:
            cu["email"] = u["email"]
        converted.append(cu)
    return converted


def update_email(users: list[UserStrictRecord], name: str, email: str) -> bool:
    """Update a user's email by `name`. Returns True if user found and updated.

    - If CSV lacks `email`, this function adds it for the matching user and
      leaves other users without `email` field. `save_users()` will normalize
      and write the email column header for persistence.
    """
    found = False
    for u in users:
        if u.get("name") == name:
            u["email"] = email
            found = True
    return found


def save_users(csv_path: Path, users: list[UserStrictRecord]) -> None:
    """Write users back to CSV, ensuring `email` column exists in header.

    Style notes:
    - Put `fieldnames` before the `with` block: clearer intent, reusable, and
      avoids re-allocating on each iteration.
    - Use `writer.writeheader()` then `writer.writerows(users)` for brevity.
    - Ensure each row has all header keys; fill missing `email` with empty string.
    """
    fieldnames = ["name", "age", "city", "email"]

    # Normalize rows to include all fieldnames
    normalized: list[dict[str, str]] = []
    for u in users:
        normalized.append(
            {
                "name": u.get("name", ""),
                "age": u.get("age", ""),
                "city": u.get("city", ""),
                "email": u.get("email", ""),
            }
        )

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(normalized)


# 3) CLI / interactive entry — provide a consistent pattern
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="csv_email_updater",
        description="Update a user's email and persist to users.csv",
    )
    parser.add_argument(
        "--name",
        help="User name to update (exact match)",
    )
    parser.add_argument(
        "--email",
        help="Email to set for the user",
    )
    parser.add_argument(
        "--csv",
        type=str,
        default=str(Path(__file__).parent / "type_exercises_data" / "users.csv"),
        help="Path to users.csv",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    csv_file = Path(args.csv)

    users = load_users(csv_file)

    # Get inputs either from CLI args or interactively
    name = args.name or input("Unesi ime korisnika za ažuriranje email-a: ").strip()
    email = args.email or input("Unesi email: ").strip()

    if not name:
        print("⚠️ Ime je obavezno.")
        return
    if not email:
        print("⚠️ Email je obavezan.")
        return

    updated = update_email(users, name, email)
    if not updated:
        print(f"ℹ️ Korisnik '{name}' nije pronađen — nijedan red nije izmenjen.")
    else:
        save_users(csv_file, users)
        print(f"✅ Ažuriran email za '{name}' i sačuvan u {csv_file}.")

    # Optional: show converted view for downstream processing
    converted = convert_users(users)
    for u in converted:
        next_year = u["age"] + 1
        email_info = f", email: {u['email']}" if "email" in u else ""
        print(
            f"{u['name']} ({u['age']}) iz {u['city']}{
                email_info} — sledeće godine {next_year}."
        )


if __name__ == "__main__":
    main()
