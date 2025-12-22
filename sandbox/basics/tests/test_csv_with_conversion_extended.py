import csv
import subprocess
import sys
from pathlib import Path


def test_update_email_persists(tmp_path: str) -> None:
    # Arrange: create a temporary CSV without email column
    csv_path = Path(tmp_path) / "users.csv"
    csv_path.write_text(
        "name,age,city\nJole,40,Novi Sad\nAna,28,Novi Sad\n",
        encoding="utf-8",
    )

    # Path to the script under test
    script_path = Path(__file__).parents[1] / "csv_with_conversion_extended.py"

    # Act: run the script to update Jole's email
    subprocess.run(
        [
            sys.executable,
            str(script_path),
            "--csv",
            str(csv_path),
            "--name",
            "Jole",
            "--email",
            "jole@example.com",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    # Assert: CSV now has an email column and the row updated
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert reader.fieldnames is not None
        assert "email" in reader.fieldnames

        # Check updated user
        jole_row = next(r for r in rows if r["name"] == "Jole")
        assert jole_row["email"] == "jole@example.com"

        # Check other users have empty email
        ana_row = next(r for r in rows if r["name"] == "Ana")
        assert ana_row["email"] == ""

    # Optional: verify CLI output contains success message (skip locale quirks)
    # assert "Ažuriran email" in result.stdout
