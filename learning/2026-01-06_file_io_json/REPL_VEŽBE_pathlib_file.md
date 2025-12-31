---
type: repl_exercises
time: 90 minutes
topics: [pathlib, file io]
---

# 🧪 REPL Vežbe — Pathlib + File I/O

## FAZA 1 — Osnove (20 min)

1. Napravi fajl `demo.txt` sa `Path.write_text` i pročitaj ga.
2. Proveri `Path.cwd()`, `Path.home()`.

## FAZA 2 — Iteracija (20 min)

3. `for p in Path(".").iterdir(): print(p)`.
4. Pronađi sve `.md` fajlove: `Path(".").glob("**/*.md")`.

## FAZA 3 — Pisanje/čitanje (20 min)

5. `with open("notes.txt", "w", encoding="utf-8") as f: f.write("hej")`.
6. Dodaj još linija sa modom "a".
7. Pročitaj liniju po liniju `readline` vs `readlines`.

## FAZA 4 — Kopiranje (15 min)

8. Napravi kopiju fajla `notes.txt` u `backup/notes.txt` sa `shutil.copy` (napravi folder pre toga `mkdir`).

## FAZA 5 — Mini izazovi (15 min)

9. Ispiši veličine fajlova u trenutnom folderu (`p.stat().st_size`).
10. Napravi funkciju `save_text(path, text)` koja kreira parent direktorijum ako ne postoji i upiše tekst.

✅ Check: koristiš Path za putanje, `with open` za fajl, znaš glob iteraciju.
