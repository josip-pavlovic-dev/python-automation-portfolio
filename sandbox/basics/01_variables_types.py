"""
Python Basics: Variables & Types
=================================

Practice fundamental Python data types and operations.
Time: 15-20 minutes
"""

# ============================================================================
# 1. VARIABLES & BASIC TYPES
# ============================================================================

print("=" * 60)
print("1. VARIABLES & BASIC TYPES")
print("=" * 60)

# Strings
name = "Jole"
profession = "Python Developer"
motto = "All or nothing!"

print(f"Name: {name}")
print(f"Profession: {profession}")
print(f"Motto: {motto}")

# Numbers
age = 30  # Integer
hourly_rate = 25.50  # Float
hours_per_day = 8

daily_income = hourly_rate * hours_per_day
print(f"\nDaily income: €{daily_income}")

# Booleans
is_learning = True
is_employed = False
ready_to_work = True

print(f"\nLearning: {is_learning}")
print(f"Ready: {ready_to_work}")

# ============================================================================
# 2. STRING OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("2. STRING OPERATIONS")
print("=" * 60)

text = "Web Scraping"

# String methods
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)}")

# String concatenation
first_name = "Jole"
last_name = "Pavlović"
full_name = first_name + " " + last_name
print(f"\nFull name: {full_name}")

# f-strings (modern way!)
greeting = f"Hello, {full_name}! Welcome to Python!"
print(greeting)

# String slicing
url = "https://example.com/page"
domain = url[8:19]  # Extract 'example.com'
print(f"\nDomain: {domain}")

# ============================================================================
# 3. TYPE CONVERSION
# ============================================================================

print("\n" + "=" * 60)
print("3. TYPE CONVERSION")
print("=" * 60)

# String to integer
price_str = "100"
price_int = int(price_str)
print(f"String '{price_str}' → Integer {price_int}")

# Integer to string
count = 42
count_str = str(count)
print(f"Integer {count} → String '{count_str}'")

# String to float
rate_str = "25.50"
rate_float = float(rate_str)
print(f"String '{rate_str}' → Float {rate_float}")

# ============================================================================
# 4. MULTIPLE ASSIGNMENT
# ============================================================================

print("\n" + "=" * 60)
print("4. MULTIPLE ASSIGNMENT")
print("=" * 60)

# Assign multiple variables at once
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# Swap variables (Python magic!)
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Swap!
print(f"After swap: a={a}, b={b}")

# ============================================================================
# 5. CONSTANTS (Convention: UPPERCASE)
# ============================================================================

print("\n" + "=" * 60)
print("5. CONSTANTS")
print("=" * 60)

PI = 3.14159
MAX_RETRIES = 3
API_KEY = "secret_key_here"

print(f"Pi: {PI}")
print(f"Max retries: {MAX_RETRIES}")

# ============================================================================
# 6. EXERCISES
# ============================================================================

print("\n" + "=" * 60)
print("6. EXERCISES - TRY YOURSELF!")
print("=" * 60)

# Exercise 1: Create variables for your info
# TODO: Fill in your information
my_name = "Your Name"
my_city = "Your City"
daily_hours = 0  # How many hours you study per day

print("\nMy info:")
print(f"  Name: {my_name}")
print(f"  City: {my_city}")
print(f"  Daily hours: {daily_hours}")

# Exercise 2: Calculate monthly income goal
# TODO: Calculate based on hourly rate
hourly_rate = 20  # €20/hour
hours_per_week = 40
weeks_per_month = 4

monthly_income = 0  # Calculate this!
print(f"\nMonthly income goal: €{monthly_income}")

# Exercise 3: String manipulation
# TODO: Extract filename from path
file_path = "/home/user/projects/scraper.py"
filename = ""  # Extract 'scraper.py' using slicing
print(f"\nFilename: {filename}")

# Exercise 4: Type conversion
# TODO: Convert and calculate
num1_str = "50"
num2_str = "30"
result = 0  # Convert to int and sum them
print(f"\nResult: {result}")

# ============================================================================
# 7. COMMON MISTAKES TO AVOID
# ============================================================================

print("\n" + "=" * 60)
print("7. COMMON MISTAKES")
print("=" * 60)

# ❌ Don't do this:
# name = "Jole"
# Name = "Different"  # Different variable! Python is case-sensitive

# ✅ Do this:
first_name = "Jole"
last_name = "Pavlović"

# ❌ Don't use reserved keywords:
# class = "Python"  # SyntaxError!
# for = 5  # SyntaxError!

# ✅ Do this:
class_name = "Python"
iteration_count = 5

print("\n✅ All basics covered! Try the exercises above!")
print("Next: 02_functions.py")
