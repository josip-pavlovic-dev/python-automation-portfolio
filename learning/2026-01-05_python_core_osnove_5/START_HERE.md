---
type: quick_start
time: "30 min"
---

# ⚡ 30-Min Start — Dan 5: Greške + OOP

## Brzi okviri

-   `try/except/else/finally`: hvatam očekivane greške, u `else` stavljam kod koji se izvršava ako nije bilo greške, `finally` se uvek izvršava.
-   Podigni grešku kada ulaz nije validan (`raise ValueError`), ne sakrivaj je.
-   Klasa = šablon, instanca = konkretan objekat. `self` pokazuje na instancu.
-   `__init__` postavlja stanje; `@property` za čitljiv getter/setter.

## Mikro primer (REPL)

```python
# Try/except
try:
    val = int("12a")
except ValueError:
    print("Nije broj")
else:
    print("Broj je", val)
finally:
    print("Gotovo")
```

```python
# Klasa
class Konto:
    def __init__(self, vlasnik: str, stanje: float = 0.0):
        self.vlasnik = vlasnik
        self.stanje = stanje

    def uplata(self, iznos: float) -> None:
        if iznos <= 0:
            raise ValueError("Iznos mora biti pozitivan")
        self.stanje += iznos

k = Konto("Ana")
k.uplata(100)
print(k.stanje)
```

✅ Spreman; idi na kickoff.

## Hintovi za rad (tvoj nivo)

-   Try/except/else/finally: napiši `read_int` sa logovanjem; u `else` stavi deo koji se izvršava bez greške.
-   Podigni custom grešku (`ConfigError`) kad validacija pada; nemoj hvatati šire od potrebnog (`Exception`).
-   OOP: `Account` sa `deposit/withdraw` i greškom kad nema dovoljno; dodaj `@property is_empty`.
-   Nasleđivanje: `SavingsAccount` dodaje kamatu; koristi `super().__init__` da ne dupliraš kod.
