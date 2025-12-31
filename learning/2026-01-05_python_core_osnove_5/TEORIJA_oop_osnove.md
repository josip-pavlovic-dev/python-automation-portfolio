---
type: lecture
time: 100 minutes
topics: [class, init, methods, property, inheritance]
---

# 📖 Teorija: OOP Osnove

## 1. Klasa i instanca

```python
class Konto:
    def __init__(self, vlasnik, stanje=0.0):
        self.vlasnik = vlasnik
        self.stanje = stanje
```

-   `self` = instanca (prvi parametar metoda)
-   `__init__` inicijalizuje stanje

## 2. Metode instance

```python
    def uplata(self, iznos):
        if iznos <= 0:
            raise ValueError("Iznos mora biti pozitivan")
        self.stanje += iznos
```

-   Poziv: `k.uplata(100)` → Python prosledi `self` automatski

## 3. `@property`

```python
class Osoba:
    def __init__(self, ime):
        self._ime = ime

    @property
    def ime(self):
        return self._ime

    @ime.setter
    def ime(self, novo):
        if not novo:
            raise ValueError("Ime ne može biti prazno")
        self._ime = novo
```

-   Čitaš kao atribut, dobijaš kontrolu validacije.

## 4. `__repr__`

```python
    def __repr__(self):
        return f"Konto(vlasnik={self.vlasnik!r}, stanje={self.stanje})"
```

-   Čini debug lakšim.

## 5. Nasleđivanje (jednostavno)

```python
class PremiumKonto(Konto):
    def __init__(self, vlasnik, stanje=0.0, limit=1000):
        super().__init__(vlasnik, stanje)
        self.limit = limit
```

-   `super()` poziva roditelja.
-   Override metoda po potrebi.

## 6. Česte greške

-   Zaboravljen `self` u metodi → TypeError.
-   Mutabilni default u `__init__` (`def __init__(..., stavke=[])`).
-   `@property` bez setter-a kada pokušavaš menjati vrednost.

## 7. Mini kontrola

-   Zašto `self` mora prvi u metodama instance?
-   Kada koristiti `@property` umesto get/set funkcija?
-   Kako pozvati metod roditelja? (`super()`)

Spreman za REPL OOP vežbe.
