import csv
from pathlib import Path


def detect_dialect(csv_path: Path) -> csv.Dialect:
    """Try to sniff delimiter/quote settings; fall back to default comma."""
    sample = csv_path.read_text(encoding="utf-8", errors="ignore")[:2048]
    try:
        return csv.Sniffer().sniff(sample)
    except Exception:
        return csv.excel


def read_rows(csv_path: Path) -> list[list[str]]:
    dialect = detect_dialect(csv_path)
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f, dialect)
        return list(reader)


def clean_rows(rows: list[list[str]]) -> tuple[list[list[str]], dict[str, int]]:
    cleaned: list[list[str]] = []
    stats = {"input_rows": len(rows), "output_rows": 0, "skipped_empty": 0}

    if not rows:
        return cleaned, stats

    for row in rows:
        trimmed = [cell.strip() for cell in row]
        if all(cell == "" for cell in trimmed):
            stats["skipped_empty"] += 1
            continue
        cleaned.append(trimmed)

    stats["output_rows"] = len(cleaned)
    return cleaned, stats


def write_rows(csv_path: Path, rows: list[list[str]]) -> None:
    if not rows:
        csv_path.write_text("", encoding="utf-8")
        return
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, dialect=csv.excel)
        writer.writerows(rows)


def main() -> None:
    src = Path("dirty_sample.csv")
    dst = Path("clean.csv")

    rows = read_rows(src)
    cleaned, stats = clean_rows(rows)
    write_rows(dst, cleaned)

    print(f"Input rows: {stats['input_rows']}")
    print(f"Output rows: {stats['output_rows']}")
    print(f"Skipped empty: {stats['skipped_empty']}")
    print(f"Saved to: {dst}")


if __name__ == "__main__":
    main()
