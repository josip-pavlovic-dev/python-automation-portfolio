"""
Kompleksna tipizacija u Pythonu
"""
from collections.abc import Callable
from typing import Literal

# 1. UNION TIPOVI (više mogućih tipova)

def process_input(data: str | int | list[str]) -> str:
    """Obrada ulaza koji može biti str, int ili lista str."""
    if isinstance(data, str):
        return f"String dužine {len(data)}"
    elif isinstance(data, int):
        return f"Ceo broj: {data}"
    else:  # lista str
        return f"Lista sa {len(data)} elementa"

# 2. LITERALI - ograničavanje vrednosti na fiksne konstante
def set_log_level(level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]) -> None:
    """Postavljanje nivoa logovanja (samo level iz Literal je dozvoljen)."""
    print(f"Nivo logovanja postavljen na: {level}")

# 3. Callable - funkcija kao tip
def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    """Prihvatanje funkcije kao argumenta i njena primena na dva cela broja."""
    return operation(x, y)

def test_operations() -> None:
    """Testiranje funkcija sa kompleksnim tipovima."""
    print(process_input("Hello, World!"))
    print(process_input(42))
    print(process_input(["apple", "banana", "cherry"]))

    set_log_level("DEBUG")
    # set_log_level("VERBOSE")  # Ovo bi izazvalo grešku pri tipizaciji

    # Callable test
    suma = apply_operation(5, 7, lambda a, b: a + b)
    proizvod = apply_operation(5, 7, lambda a, b: a * b)
    print(f"Suma: {suma}, Proizvod: {proizvod}")

if __name__ == "__main__":
    test_operations()
