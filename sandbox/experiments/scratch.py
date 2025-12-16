from __future__ import annotations

import csv
from pathlib import Path

"""
Scratch File - Free Experimentation
====================================

This is your playground! Test anything here.
No rules, no structure - just code and learn!
"""

# Your experiments here! 👇

print("Hello from scratch.py! 🚀")

# Example: Test a quick idea
def quick_test():
    """Test whatever you're curious about."""
    SCRIPT_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    DATA_DIR = SCRIPT_DIR.parent / "basics" / "data"
    CSV_FILE = DATA_DIR / "sample.csv"
    with open(CSV_FILE, newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
        print(rows)
        print(type(rows[0]))



if __name__ == "__main__":
    quick_test()
