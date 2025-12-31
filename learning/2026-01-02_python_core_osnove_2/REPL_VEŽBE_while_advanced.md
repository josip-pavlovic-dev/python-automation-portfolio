---
type: repl_exercises
time: 90 minutes
topics: [while, break, continue, input]
---

# 🧪 REPL Vežbe — `while`, `break`, `continue`

## Pravila

-   Uvek osiguraj da se uslov MENJA u petlji (inače beskonačna petlja).
-   Ako zaglaviš, `Ctrl+C` prekida REPL petlju.

---

## FAZA 1 — Osnovno `while` (15 min)

1. Brojanje do 5

```python
broj = 0
while broj < 5:
    print(broj)
    broj += 1
```

2. Odbrojavanje od 5 do 1

```python
broj = 5
while broj > 0:
    print(broj)
    broj -= 1
```

---

## FAZA 2 — Uslovni Unosi (20 min)

3. Traži "da" ili "ne"

```python
while True:
    odgovor = input("Da ili ne? ")
    if odgovor in ("da", "ne"):
        print("Hvala!")
        break
    print("Pokušaj ponovo")
```

4. Samo brojevi

```python
while True:
    unos = input("Unesi broj: ")
    if unos.isdigit():
        print(f"Validan broj: {unos}")
        break
    print("Nije broj!")
```

---

## FAZA 3 — `continue` i Filtriranje (20 min)

5. Preskači neparne

```python
n = 0
while n < 10:
    n += 1
    if n % 2 == 1:
        continue
    print(n)
```

6. Do prvog broja deljivog sa 7

```python
x = 1
while x <= 50:
    if x % 7 == 0:
        print(f"Prvi deljiv sa 7: {x}")
        break
    x += 1
```

---

## FAZA 4 — Kombinacije sa `for` (15 min)

7. Prebroj slova u stringu (while umesto for)

```python
tekst = "python"
idx = 0
while idx < len(tekst):
    print(idx, tekst[idx])
    idx += 1
```

8. Napravi obrnutu reč

```python
tekst = "program"
idx = len(tekst) - 1
obrnuto = ""
while idx >= 0:
    obrnuto += tekst[idx]
    idx -= 1
print(obrnuto)
```

---

## FAZA 5 — Mini Zadaci (20 min)

9. Suma do 100, samo parni

```python
total = 0
n = 0
while n <= 100:
    if n % 2 == 0:
        total += n
    n += 1
print(total)  # očekuj 2550
```

10. FizzBuzz sa while (1-15)

```python
n = 1
while n <= 15:
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    n += 1
```

11. Traži prvu cifru veću od 5 u listi

```python
brojevi = [1, 2, 3, 4, 6, 2, 9]
idx = 0
pronadjen = None
while idx < len(brojevi):
    if brojevi[idx] > 5:
        pronadjen = brojevi[idx]
        break
    idx += 1
print(pronadjen)  # očekuj 6
```

---

## ✅ Checklista

-   [ ] Možeš da napišeš `while` sa korektnom promenom uslova
-   [ ] Razlika `break` vs `continue` jasna
-   [ ] Koristio si `while` sa `input()` i validacijom
-   [ ] Znaš prebaciti `for` u `while` stil
