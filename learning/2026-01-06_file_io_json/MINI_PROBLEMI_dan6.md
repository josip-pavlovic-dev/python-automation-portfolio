---
type: problems
time: 60 minutes
count: 15
---

# 🎯 MINI PROBLEMI — Dan 6 (File I/O + JSON)

1. **Read safe**: funkcija `read_text_safe(path)` → vrati tekst ili `None` ako fajl ne postoji.
2. **Write lines**: upiši listu stringova u fajl, svaki u novi red.
3. **Count lines**: prebroj linije u fajlu bez `len(readlines())` (itera liniju po liniju).
4. **Find by glob**: vrati listu svih `.txt` u folderu `data/` (rekurzivno).
5. **Backup**: kopiraj `data.txt` u `backup/data.txt` (kreiraj folder ako ne postoji).
6. **JSON save**: `save_json(path, obj)` koristi `ensure_ascii=False`, `indent=2`.
7. **JSON load safe**: `load_json(path)` hvata `JSONDecodeError` i `FileNotFoundError`.
8. **CSV → JSON**: pročitaj CSV sa `csv.DictReader` i snimi u JSON.
9. **Filter JSON**: učitaj listu dict-ova, filtriraj gde `age > 18`, snimi novi fajl.
10. **Merge JSON files**: učitaj dva JSON fajla listi, spoji u jedan i snimi.
11. **Normalize path**: funkcija koja prima string path, vraća `Path` i kreira parent direktorijum.
12. **Replace in file**: učitaj fajl, zameni reč, snimi nazad.
13. **File size report**: ispiši veličinu svakog fajla u folderu (u bajtima).
14. **UTF-8 check**: upiši string sa š/ć/ž, pročitaj i potvrdi da nema zamenskih karaktera.
15. **JSON pretty print**: napravi helper koji prima dict/list i vraća lep string (`json.dumps(..., indent=2, ensure_ascii=False)`).

Self-check: 12+/15 rešenih; svi fajlovi koriste `with` i `encoding="utf-8"`.
