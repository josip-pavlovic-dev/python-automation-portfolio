"""
DEMO: Type Annotations Intro | Osnove Type Annotations
This script demonstrates the use of type annotations in Python. |
Ova skripta demonstrira upotrebu type annotations u Python-u.
"""
# ================================================================================
# 1. Primitive Types | Primitivni Tipovi
# ================================================================================
age: int = 40
name: str = "Josip"
height: float = 1.85
is_student: bool = False
is_employed: bool = True

# ================================================================================
# 2. Complex Types | Kompleksni Tipovi
# ================================================================================

# Optional Types | Opcioni Tipovi (može biti određeni tip ili None)
# from typing import Optional # Za Python verzije < 3.10
# maybe_number: Optional[int] = None  # Može biti int ili None

# Za Python 3.10+ umesto Optional koristi se sintaksa sa |
maybe_number: int | None = None
maybe_email: str | None = None  # Može biti str ili None
maybe_active: bool | None = None  # Može biti bool ili None

# ================================================================================
# 3. Functions with Type Annotations | Funkcije sa Type Annotations
# ================================================================================
def greet(user_name: str, user_age: int) -> str:
    return f"Hello, my name is {user_name} and I am {user_age} years old."

greeting: str = greet(name, age)
print(greeting)


def add(x: int, y: int) -> int:
    """Returns the sum of two integers. | Vraća zbir dva cela broja."""
    return x + y


sum_result: int = add(5, 10)
print(f"Sum: {sum_result}")

# ================================================================================
# 4. Functions with optional parameters | Funkcije sa opcionim parametrima
# ================================================================================
def introduce(user_name: str, user_age: int = 30) -> str:
    """Introduces a person with their name and age. (default age is 30) |
    Predstavlja osobu sa njenim imenom i godinama. (podrazumevana starost je 30)"""
    return f"My name is {user_name} and I am {user_age} years old."


introduction: str = introduce("Ana")  # Koristi podrazumevanu vrednost za starost
print(introduction)

introduction_with_age: str = introduce("Marko", 25)
print(introduction_with_age)


def greet_serbian(user_name: str, greeting: str = "Zdravo") -> str:
    """Greets a person in Serbian or with a custom greeting. |
    Pozdravlja osobu na srpskom ili sa lično izabranim pozdravom."""
    return f"{greeting}, {user_name}!"

serbian_greeting: str = greet_serbian("Ivana")
print(serbian_greeting)

custom_greeting: str = greet_serbian("Petar", "Dobro jutro")
print(custom_greeting)

# ================================================================================
# 5. Lists | Liste
# ================================================================================
numbers: list[int] = [1, 2, 3, 4, 5]
squared_numbers: list[int] = [n ** 2 for n in numbers]
print(f"Squared Numbers: {squared_numbers}")

names: list[str] = ["Ana", "Marko", "Ivana"]
uppercase_names: list[str] = [n.upper() for n in names]
print(f"Uppercase Names: {uppercase_names}")

# ================================================================================
# 6. Dictionaries | Rečnici
# ================================================================================
user: dict[str, str | int] = {"name": "Luka", "age": 28}
print(f"User: {user}")

user["city"] = "Belgrade"
print(f"Updated User: {user}")

def get_user_info(info: dict[str, str | int], key: str) -> str | int | None:
    """Returns the value for the given key from the user info dictionary. |
    Vraća vrednost za dati ključ iz rečnika sa informacijama o korisniku."""
    return info.get(key)

age_info: str | int | None = get_user_info(user, "age")
print(f"Age Info: {age_info}")

city_info: str | int | None = get_user_info(user, "city")
print(f"City Info: {city_info}")

unknown_info: str | int | None = get_user_info(user, "country")
print(f"Unknown Info: {unknown_info}")

# 6. Dictionaries | Rečnici
product_prices: dict[str, float] = {
    "apple": 0.99,
    "banana": 0.59,
    "orange": 0.79
}

print(f"Product Prices: {product_prices}")

product_prices["grape"] = 1.29
print(f"Updated Product Prices: {product_prices}")

def get_price(prices: dict[str, float], product: str) -> float | None:
    """Returns the price of the given product or None if not found. |
    Vraća cenu datog proizvoda ili None ako nije pronađen."""
    return prices.get(product)

apple_price: float | None = get_price(product_prices, "apple")
print(f"Apple Price: {apple_price}")

mango_price: float | None = get_price(product_prices, "mango")
print(f"Mango Price: {mango_price}")

# ================================================================================
# 7. Tuples | Torke (fiksna dužina, različiti tipovi)
# ================================================================================
cordinates: tuple[float, float] = (45.2671, 19.8335)  # Latitude, Longitude
print(f"Cordinates: {cordinates}")
user_data: tuple[str, int, bool] = ("Maja", 22, True)
print(f"User Data: {user_data}")
def format_user_data(data: tuple[str, int, bool]) -> str:
    """Formats user data from a tuple. | Formatira korisničke podatke iz torke."""
    name, age, is_active = data
    status = "active" if is_active else "inactive"
    return f"Name: {name}, Age: {age}, Status: {status}"

formatted_data: str = format_user_data(user_data)
print(f"Formatted User Data: {formatted_data}")

# ================================================================================
# 8. Sets | Skupovi (jedinstveni elementi)
# ================================================================================
unique_cities: set[str] = {"Belgrade", "Novi Sad", "Niš"}
print(f"Unique Cities: {unique_cities}")
unique_cities.add("Subotica")
print(f"After Adding Subotica: {unique_cities}")
unique_cities.add("Belgrade")  # Dodavanje duplikata neće promeniti skup
print(f"After Adding Duplicate Belgrade: {unique_cities}")
def has_city(s: set[str], city: str) -> bool:
    """Checks if the set contains the given city. |
    Proverava da li skup sadrži dati grad."""
    return city in s

contains_nis: bool = has_city(unique_cities, "Niš")
print(f"Contains Niš: {contains_nis}")

contains_zagreb: bool = has_city(unique_cities, "Zagreb")
print(f"Contains Zagreb: {contains_zagreb}")

unique_numbers: set[int] = {1, 2, 3, 4, 5}
print(f"Unique Numbers: {unique_numbers}")

unique_numbers.add(3)  # Dodavanje duplikata neće promeniti skup
print(f"After Adding Duplicate: {unique_numbers}")

unique_numbers.add(6)
print(f"After Adding New Number: {unique_numbers}")

def has_number(s: set[int], number: int) -> bool:
    """Checks if the set contains the given number. |
    Proverava da li skup sadrži dati broj."""
    return number in s

contains_four: bool = has_number(unique_numbers, 4)
print(f"Contains 4: {contains_four}")

contains_ten: bool = has_number(unique_numbers, 10)
print(f"Contains 10: {contains_ten}")

# ================================================================================
# End of Demo
# ================================================================================
