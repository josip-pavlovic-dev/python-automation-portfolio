# CSV operacije (biće ti jako potrebno!)
import csv

data = [
    ["Name", "Price", "Brand"],
    ["Laptop", "1200", "Dell"],
    ["Mouse", "25", "Logitech"]
]

with open("test_products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV fajl kreiran!")

# =========================
# 1. VARIABLES & TYPES (10min)
# =========================
name = "Jole"
age = 40
is_motivated = True
skills = ["Python", "automation", "problem-solving"]

print(f"Ime: {name}, Godina: {age}")
print(f"Skills: {', '.join(skills)}")

# ====================
# 2. FUNCTIONS (15min)
# ====================
def greet(name):
    """Pozdravlja korisnika."""
    return f"Hello, {name}! Ready to scrape! 🕷️"

def calculate_discount(price, discount_percent):
    """Računa cenu sa popustom."""
    discount = price * (discount_percent / 100)
    return price - discount

# Testiranje
print(greet("Jole"))
print(f"Cena sa popustom: {calculate_discount(100, 20)} EUR")

# =========================
# 3. LISTS & LOOPS (20min)
# =========================
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

# For petlja
for url in urls:
    print(f"Scraping: {url}")

# List comprehension (Python način!)
urls_upper = [url.upper() for url in urls]
print(urls_upper)

# =======================
# 4. DICTIONARIES (20min)
# =======================
product = {
    "name": "Laptop",
    "price": 1200,
    "brand": "Dell",
    "in_stock": True
}

# Pristup vrednostima
print(f"Proizvod: {product['name']}, Cena: {product['price']} EUR")

# Iteracija kroz dictionary
for key, value in product.items():
    print(f"{key}: {value}")

# Lista dictionaries (tipičan scraping output!)
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75}
]

for product in products:
    print(f"{product['name']}: €{product['price']}")

# ===========================
# 5. FILE OPERATIONS (15min)
# ===========================
# Pisanje u fajl
with open("test_output.txt", "w") as f:
    f.write("Hello from Python!\n")
    f.write("Web scraping is awesome!\n")

# Čitanje iz fajla
with open("test_output.txt") as f:
    content = f.read()
    print(content)

# ===========================
# 6. EXCEPTION HANDLING (10min)
# ===========================
def divide(a, b):
    """Deli dva broja sa rukovanjem greškama."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed!"
    except TypeError:
        return "Error: Please provide numbers only!"
    else:
        return result

# Testiranje
print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "a"))

# ===========================
# END OF PYTHON REFRESHER
# ===========================
