"""
Generički tipovi za sopstvene klase
"""
from typing import Generic, TypeVar

# TypeVar — varijabla tipa (kao template)
T = TypeVar('T')

class Container(Generic[T]):
    """Generička klasa koja čuva bilo šta"""

    def __init__(self, value: T) -> None:
        self.value: T = value

    def get(self) -> T:
        return self.value

    def set(self, value: T) -> None:
        self.value = value

def test() -> None:
    # Container sa stringom
    str_container: Container[str] = Container("hello")
    text: str = str_container.get()
    print(f"Text: {text}")

    # Container sa brojem
    int_container: Container[int] = Container(42)
    number: int = int_container.get()
    print(f"Number: {number}")

    # Container sa listom
    list_container: Container[list[str]] = Container(["a", "b", "c"])
    items: list[str] = list_container.get()
    print(f"Items: {items}")

if __name__ == "__main__":
    test()
