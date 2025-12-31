---
type: lecture
time: 100 minutes
topics: [file io, with, pathlib]
---

# 📖 Teorija: File I/O + Pathlib

## 1. `with open`

```python
with open("data.txt", "r", encoding="utf-8") as f:
    sadržaj = f.read()
```

-   `with` zatvara fajl automatski (čak i na grešku).
-   Modovi: `"r"`, `"w"` (overwrite), `"a"` (append), `"b"` (binary), kombinuj (`"rb"`).

## 2. Čitanje/ pisanje

```python
text = f.read()      # ceo fajl
line = f.readline()  # jedna linija
lines = f.readlines()# list linija
```

Pisanje:

```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")
```

## 3. Pathlib

```python
from pathlib import Path
p = Path("data/demo.txt")
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("hi", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
```

-   `Path.cwd()`, `Path.home()`
-   `Path.iterdir()`, `Path.glob("*.csv")`

## 4. Kopija i pomeranje

```python
import shutil
shutil.copy(src, dst)
shutil.move(src, dst)
```

## 5. CSV newline podsetnik

-   Ako pišeš CSV ručno: `open(..., newline="", encoding="utf-8")`.

## 6. Tipične greške

-   Zaboravljen `encoding` → problemi sa č/ć/ž.
-   Nezatvoren fajl (bez `with`).
-   Ručno spajanje putanja stringovima umesto `Path` (`Path("data")/"file.txt"`).

## 7. Mini kontrola

-   Kada koristiš `"a"` mod?
-   Zašto `with`?
-   Kako pronaći sve `.txt` u folderu? (`Path(".").glob("**/*.txt")`)

Spreman za REPL vežbe sa Pathlib.
