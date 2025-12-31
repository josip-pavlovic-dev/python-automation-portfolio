---
type: mini_exercises
date: 2026-01-01
estimated_time: 1.5 hours
difficulty: beginner
---

# 🎯 MINI PROBLEMI — Dan 1: Praktična Vežba

**Cilj:** Rešiti 20+ malih zadataka koji kombinuju sve koncepte iz Dana 1.

**Kako koristiti:**

1. Čitaj zadatak
2. Pokušaj da rešiš U REPL-u ILI u fajlu `mini_problemi.py`
3. Pokreni i vidi rezultat
4. Ako ne radi - vrati se na teoriju

---

## GRUPA 1: If/Else (Osnovni Nivo)

### Zadatak 1.1

```
Napiši kod koji ispituje da li je broj 10 > 5.
Ako jeste, ispiši "Broj je veći".
Ako nije, ispiši "Broj je manji".
```

**Resenje:**

```python
x = 10
if x > 5:
    print("Broj je veći")
else:
    print("Broj je manji")
```

---

### Zadatak 1.2

```
Napisani kod koji proverava da li je promenljiva x
jednaka 10. Ako jeste, ispiši "X je 10",
ako je manje, ispiši "X je manje od 10",
ako je vise, ispiši "X je vise od 10".
```

**Resenje:**

```python
x = 7
if x == 10:
    print("X je 10")
elif x < 10:
    print("X je manje od 10")
else:
    print("X je vise od 10")
```

---

### Zadatak 1.3

```
Napisani kod koji proverava:
- Ako je x > 0, ispiši "Pozitivno"
- Ako je x < 0, ispiši "Negativno"
- Ako je x == 0, ispiši "Nula"

Testiraj sa x = 0, x = 5, x = -3
```

**Resenje:**

```python
x = 0
if x > 0:
    print("Pozitivno")
elif x < 0:
    print("Negativno")
else:
    print("Nula")
```

---

## GRUPA 2: For Petlja (Osnovni Nivo)

### Zadatak 2.1

```
Ispiši brojeve od 0 do 4 koristeći for petlju.
```

**Resenje:**

```python
for i in range(5):
    print(i)
```

---

### Zadatak 2.2

```
Ispiši brojeve od 1 do 10, ali SAMO parne.
```

**Resenje:**

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

---

### Zadatak 2.3

```
Kreiraj listu: ["Ana", "Bora", "Cica"]
Ispiši svako ime sa brojem (počevši od 1).

Očekivani output:
1: Ana
2: Bora
3: Cica
```

**Resenje:**

```python
names = ["Ana", "Bora", "Cica"]
for i, name in enumerate(names, start=1):
    print(f"{i}: {name}")
```

---

### Zadatak 2.4

```
Koristeći for petlju, saberi sve brojeve od 1 do 10.
(1+2+3+...+10 = 55)
```

**Resenje:**

```python
total = 0
for i in range(1, 11):
    total += i
print(total)  # 55
```

---

## GRUPA 3: While Petlja (Osnovni Nivo)

### Zadatak 3.1

```
Koristeći while petlju, ispiši brojeve od 5 do 1 unazad.
```

**Resenje:**

```python
x = 5
while x > 0:
    print(x)
    x -= 1
```

---

### Zadatak 3.2

```
Napiši while petlju koja se izvršava dok x nije 0.
Počni sa x = 10 i svaki put oduzmi 2.
```

**Resenje:**

```python
x = 10
while x > 0:
    print(x)
    x -= 2
```

---

## GRUPA 4: Funkcije sa If/For (Srednji Nivo)

### Zadatak 4.1

```
Napiši funkciju `is_even(n)` koja vraća True ako je broj
paran, False ako je neparan.
```

**Resenje:**

```python
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(5))   # False
```

---

### Zadatak 4.2

```
Napiši funkciju `count_greater_than(numbers, threshold)`
koja broji koliko brojeva je veće od threshold-a.

Primer: count_greater_than([1, 5, 3, 8, 2], 4)
Odgovor: 2 (jer 5 i 8 su > 4)
```

**Resenje:**

```python
def count_greater_than(numbers, threshold):
    count = 0
    for num in numbers:
        if num > threshold:
            count += 1
    return count

print(count_greater_than([1, 5, 3, 8, 2], 4))  # 2
```

---

### Zadatak 4.3

```
Napiši funkciju `reverse_string(s)` koja
vraća string unazad.

Primer: reverse_string("python")
Odgovor: "nohtyp"

(Hint: koristite slicing sa [::-1])
```

**Resenje:**

```python
def reverse_string(s):
    return s[::-1]

print(reverse_string("python"))  # nohtyp
```

---

## GRUPA 5: Kombinovani Problemi (Srednji Nivo)

### Zadatak 5.1

```
Napiši funkciju `filter_evens(numbers)`
koja vraća samo parne brojeve iz liste.

Primer: filter_evens([1, 2, 3, 4, 5, 6])
Odgovor: [2, 4, 6]
```

**Resenje:**

```python
def filter_evens(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

print(filter_evens([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
```

---

### Zadatak 5.2

```
Napiši funkciju `multiply_list(numbers, factor)`
koja multiply-uje svaki broj u listi sa factor-om.

Primer: multiply_list([1, 2, 3], 2)
Odgovor: [2, 4, 6]
```

**Resenje:**

```python
def multiply_list(numbers, factor):
    result = []
    for num in numbers:
        result.append(num * factor)
    return result

print(multiply_list([1, 2, 3], 2))  # [2, 4, 6]
```

---

### Zadatak 5.3

```
Napiši funkciju `validate_password(password)`
koja proverava:
- Dužina > 8 karaktera
- Sadrži bar jedan broj
- Sadrži bar jednu veliku slova

Vraća True ako sve uslov su ispunjeni, False inače.
```

**Resenje:**

```python
def validate_password(password):
    if len(password) <= 8:
        return False

    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False

    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        return False

    return True

print(validate_password("Qwerty123"))   # True
print(validate_password("short"))        # False
print(validate_password("nouppercase1"))  # False
```

---

## GRUPA 6: Napredni Problemi (Teži Nivo)

### Zadatak 6.1

```
Napiši funkciju `fibonacci(n)` koja vraća
prvi n Fibonacci brojeva.

Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...

Primer: fibonacci(6)
Odgovor: [0, 1, 1, 2, 3, 5]
```

**Resenje:**

```python
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(6))  # [0, 1, 1, 2, 3, 5]
```

---

### Zadatak 6.2

```
Napiši funkciju `group_by_length(words)`
koja grupiše reči po dužini.

Primer: group_by_length(["a", "bb", "c", "dd", "eee"])
Odgovor: {1: ["a", "c"], 2: ["bb", "dd"], 3: ["eee"]}
```

**Resenje:**

```python
def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result

print(group_by_length(["a", "bb", "c", "dd", "eee"]))
# {1: ['a', 'c'], 2: ['bb', 'dd'], 3: ['eee']}
```

---

## ✅ CHECKLIST — Sami Testovi

Ako ste uspešno rešili:

-   [ ] Sve iz GRUPE 1 (If/Else)
-   [ ] Sve iz GRUPE 2 (For)
-   [ ] Sve iz GRUPE 3 (While)
-   [ ] Sve iz GRUPE 4 (Funkcije)
-   [ ] Sve iz GRUPE 5 (Kombinovani)
-   [ ] **Barem 2** iz GRUPE 6 (Napredni)

...Tada razumeš Python Core osnove Dana 1! 🎉

---

## 💡 Saveti ako se Zaglavim

1. **Prochitaj zadatak 3 puta polako**
2. **Napraviš skic-plan pre nego što kodiraš**
3. **Pokušaj sa manjim primerom prvo**
4. **Koristi `print()` da vidim međurezultate**

---

## 🔗 Dalje

-   Ako si gotov sa svim → Napiši summary.md
-   Ako nemaš vremena → Barem završi GRUPE 1-4

Sretno! 🚀
