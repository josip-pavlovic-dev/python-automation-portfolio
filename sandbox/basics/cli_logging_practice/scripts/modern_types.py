"""
Moderni Python types (3.10+)
"""
from __future__ import annotations  # Omogući lenjo evaluiranje anotacija!

from collections.abc import Iterable, Sequence
from typing import Literal, TypedDict


# 1. Union sa |
def process(data: str | int | list[str]) -> str:
    """Union sa | umesto Union[str, int, list[str]]"""
    return str(data)

# 2. Optional sa |
def get_config() -> dict[str, str] | None:
    """Vraća dict ili None — lakše od Optional[Dict[str, str]]"""
    return None

# 3. Specifične kolekcije sa collections.abc
def process_items(items: Iterable[str]) -> Sequence[str]:
    """Iterable input, Sequence output — fleksibilnije od list[str]"""
    return list(items)

# 4. TypedDict za recordove
class UserRecord(TypedDict):
    name: str
    age: int
    email: str | None

# 5. Literal za enum-like vrednosti
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def set_log_level(level: LogLevel) -> None:
    """Type checker će promeniti samo validne nivoe"""
    print(f"Log level: {level}")

def main() -> None:
    """Sve je type-safe"""
    user: UserRecord = {"name": "Jole", "age": 30, "email": "j@ex.com"}
    print(process(user["name"]))
    set_log_level("DEBUG")

if __name__ == "__main__":
    main()
