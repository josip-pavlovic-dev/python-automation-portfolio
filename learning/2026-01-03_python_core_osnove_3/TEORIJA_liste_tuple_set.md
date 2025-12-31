---
type: lecture
time: 100 minutes
topics: [list, tuple, set, mutability, membership]
---

# 📖 Teorija: Liste, Tuple, Set

## 1. Liste (mutabilne, čuvaju red)

```python
fruits = ["apple", "banana", "cherry"]
```

-   **Mutabilne**: možeš menjati elemente (`fruits[1] = "orange"`).
-   **Čuvaju red**: redosled ostaje kako si dodao.
-   **Dozvoljavaju duplikate**.

### Glavne operacije

| Operacija | Primer               | Rezultat                  |
| --------- | -------------------- | ------------------------- |
| `append`  | `nums.append(10)`    | dodaje na kraj            |
| `extend`  | `nums.extend([7,8])` | dodaje više               |
| `insert`  | `nums.insert(1, 99)` | ubaci na indeks           |
| `pop`     | `nums.pop()`         | vrati + ukloni poslednji  |
| `remove`  | `nums.remove(3)`     | ukloni prvo pojavljivanje |
| `len`     | `len(nums)`          | dužina                    |
| `in`      | `3 in nums`          | membership                |

### Indexing i slicing

```python
nums = [10, 20, 30, 40, 50]
nums[0]      # 10
nums[-1]     # 50
nums[1:4]    # [20, 30, 40]
nums[:3]     # [10, 20, 30]
nums[::2]    # [10, 30, 50]
```

### Kopije i reference

```python
orig = [1, 2, 3]
copy1 = orig        # reference (iste lokacije!)
copy2 = orig[:]     # plitka kopija
copy3 = list(orig)  # plitka kopija
```

-   Ako menjaš `copy1`, menjaš i `orig`.
-   Ako menjaš `copy2`, `orig` ostaje.

### `IndexError`

```python
nums = [1, 2, 3]
# nums[10]  # IndexError
```

Uvek proveri `len(nums)` pre pristupa.

---

## 2. Tuple (imutabilni, hashable)

```python
koordinate = (44.8, 20.5)
```

-   **Imutabilni**: ne možeš menjati posle kreiranja.
-   **Hashable**: može biti ključ u dict-u ili element seta (za razliku od liste).
-   **Koristi**: koordinatni parovi, povrat više vrednosti iz funkcije.

### Kreiranje

```python
prazan = ()
jedan = (5,)        # zarez je bitan!
multi = (1, "a", True)
```

### Čitanje

```python
x, y = koordinate   # unpacking
print(x, y)
```

### Tuple vs list

-   Ako ti treba struktura koja se NE menja → tuple.
-   Ako ti treba ključ u dict/set → tuple (jer je hashable).

---

## 3. Set (unikatne vrednosti, bez reda)

```python
brojevi = {1, 2, 2, 3}
print(brojevi)  # {1, 2, 3}
```

-   **Bez duplikata**: automatski uklanja duplikate.
-   **Bez garantovanog reda**: ne oslanjaj se na pozicije.
-   **Hashable only**: elementi moraju biti hashable (npr. tuple da, lista ne).

### Glavne operacije

| Operacija | Primer            | Rezultat                |
| --------- | ----------------- | ----------------------- |
| `add`     | `s.add(5)`        | dodaje element          |
| `update`  | `s.update([7,8])` | dodaje više             |
| `remove`  | `s.remove(3)`     | KeyError ako ne postoji |
| `discard` | `s.discard(3)`    | ne baca grešku          |
| `pop`     | `s.pop()`         | uklanja neki element    |
| `len`     | `len(s)`          | veličina                |
| `in`      | `3 in s`          | membership              |

### Set operacije (matematičke)

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # union {1,2,3,4,5}
print(a & b)   # intersection {3}
print(a - b)   # difference {1,2}
print(a ^ b)   # symmetric diff {1,2,4,5}
```

### Tipične greške

-   `TypeError: unhashable type: 'list'` → ne možeš listu u set.
-   `KeyError` kod `remove` ako element ne postoji; koristi `discard` ako nisi siguran.

---

## 4. Poređenje list vs tuple vs set

| Osobina              | list          | tuple            | set              |
| -------------------- | ------------- | ---------------- | ---------------- |
| Redosled             | Da            | Da               | Ne               |
| Mutabilnost          | Da            | Ne               | Da               |
| Duplikati            | Da            | Da               | Ne               |
| Hashable kao element | Ne            | Da               | N/A              |
| Tipičan use-case     | sekvenca, red | fiksna struktura | unikatni članovi |

---

## 5. Kada koristiti šta

-   **list**: kad redosled bitan, treba ti dodavanje/brisanje, duplikati su ok.
-   **tuple**: kad podaci ne treba da se menjaju; kao ključ u dict/set; povrat više vrednosti.
-   **set**: kada ti trebaju unikatne vrednosti, brzo membership pretraživanje, skup operacije.

---

## 6. Brza praksa (mentalni test)

-   Da li će `set([1, 1, 2])` zadržati oba `1`? → Ne.
-   Može li `(1, [2, 3])` biti element seta? → Ne, lista nije hashable.
-   Kako kopiraš listu bez reference? → `lst[:]` ili `list(lst)`.

Spreman za REPL? Pređi na vežbe. 💪
