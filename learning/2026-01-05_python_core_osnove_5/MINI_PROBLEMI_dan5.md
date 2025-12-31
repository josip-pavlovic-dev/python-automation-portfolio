---
type: problems
time: 60 minutes
count: 18
---

# 🎯 MINI PROBLEMI — Dan 5 (Greške + OOP)

## Error handling

1. `safe_int(x)` → vrati int ili `None` ako nije konvertibilno (bez bacanja).
2. `read_first_line(path)` → hvata `FileNotFoundError`; vraća string ili poruku.
3. `divide_or_log(a, b)` → ako deljenje nulom, vrati `None` i štampaj upozorenje.
4. `validate_email(email)` → ako nema `@`, `raise ValueError`.

## OOP

5. Klasa `TodoItem` sa `naziv`, `done=False`; metod `oznaci()` postavlja done True; `__repr__` lep.
6. `@property progress` za procenat urađenog na klasi `TaskList` (drži listu TodoItem); read-only.
7. Nasledi `VipTodoItem` koji ima prioritet (int) i prikazuje ga u repr.
8. Klasa `Temperature` sa `celsius`; `@property fahrenheit` sa setterom koji konvertuje.
9. Klasa `Inventory` koja drži dict stavki→količina; metode `dodaj`, `uzmi` (raise ako nema dovoljno).
10. `BankAccount` sa `uplata` (raise ako <=0), `isplata` (raise ako > stanje), `__repr__`.

## Kombinacija

11. `load_numbers(path)` → čita fajl, svaku liniju pretvori u int; hvata ValueError po liniji; preskače loše; vraća listu dobrih.
12. `ParserError` custom; `parse_line(line)` podiže ako linija prazna.
13. `User` klasa sa `username`; `@property username` validira dužinu ≥3.
14. `Cart` klasa koristi `Inventory`; greška ako proizvod ne postoji; koristi try/except u metodu `kupi`.
15. `Rectangle` sa `width/height`; `area` metod; setter validacija pozitivno; `ValueError` ako nije.
16. `Logger` klasa sa metodom `log(level, message)`; prihvati samo "info", "warn", "error" ili podigni `ValueError`.
17. `Counter` sa `increment()` i `value`; koristi `__repr__` za debug.
18. `EmailService` stub: metod `send(to, subject)` koji podiže `NotImplementedError` (pokazuje apstrakciju).

Self-check: barem 12/18 rešenih, specifični izuzeci, validacija u klasama, nema mutabilnih default-ova.
