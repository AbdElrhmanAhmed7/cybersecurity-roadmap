# Week 02 (27/06 - 29/06) - File I/O, Float Precision & Tuples

---

### Day 5 - Evening & Morning Session (W02 - 27/06): Practical File I/O & CLI Scripting

#### 1. Key Modules & Functions I Used Today

- **`sys.argv`**: 
  - A list that stores command-line arguments.
  - `argv[0]` = script name, `argv[1]` = first argument (the file path).
  - **Use case**: Makes the script flexible without hardcoding file names.

- **`os.path`**:
  - `os.path.exists(path)`: Returns `True` if the file/folder exists.
  - `os.path.isfile(path)`: Returns `True` if it's a file (not a folder). Prevents reading directories by mistake.
  - `os.path.basename(path)`: Extracts the file name from the full path. (e.g., `C:/docs/file.txt` -> `file.txt`).

- **`json.dump()`**:
  - Writes a Python dictionary directly into a `.json` file.
  - Better than `json.dumps()` + `f.write()` because it's more direct and memory-efficient.
  - **Key args**: `indent=4` (for readability), `ensure_ascii=False` (to preserve Arabic characters).

---

#### 2. Mistakes I Made & How I Fixed Them

| Mistake | What I did wrong | The Fix |
| :--- | :--- | :--- |
| **Modifying `sys.argv`** | I tried to append a user input directly to `argv` if the user forgot the argument. | Never modify `sys.argv`. Use a separate variable (e.g., `file_path`) to handle the logic. |
| **Reading the file twice** | Used `f.readlines()` then used `''.join(content)` twice to count words and characters. | Used `f.read()` once to get the full text as a single string. This saves memory and time (best practice). |
| **Filename in report** | Saved the full path (e.g., `/home/user/projects/data.txt`) as the filename. | Used `os.path.basename()` to save only `data.txt` for a cleaner JSON report. |

---

#### 3. Best Practices I Applied Today

1. **Separation of Concerns**:
   - I separated the analysis logic (`analyze_file`) from the saving logic (`save_to_json`). 
   - If I want to use this analyzer in a web app or another project later, I can just `import` it without running the CLI part automatically.

2. **The `if __name__ == "__main__":` Guard**:
   - Wrapped the script execution inside this block.
   - **Why?** If someone imports my script, it won't run automatically. It only runs when I execute the script directly from the terminal.

3. **Defensive Programming (Validations)**:
   - Check if the file exists.
   - Check if the path points to a file, not a folder.
   - Wrap the file reading in a `try/except` block to catch unexpected errors (e.g., permission denied).

---

#### 4. Test Cases Results (Validation)

| # | Scenario | Command | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Normal text file | `python file_analyzer.py test.txt` | JSON with correct counts | ✅ Passed (Counted 26 chars including newline) |
| 2 | Empty file | `python file_analyzer.py empty.txt` | `lines: 0, words: 0, chars: 0` | ✅ Passed |
| 3 | File with empty lines | `python file_analyzer.py blank.txt` | Correctly counted empty rows | ✅ Passed |
| 4 | File does NOT exist | `python file_analyzer.py missing.txt` | Prints error message, doesn't crash | ✅ Passed |
| 5 | Path is a folder | `python file_analyzer.py ./` | Prints error message, doesn't crash | ✅ Passed |

---

#### 5. Final Code Architecture (Mental Model)

1. **Input**: `sys.argv` OR `input()`.
2. **Validation**: `os.path.exists` + `os.path.isfile`.
3. **Processing**: 
   - `with open(...) as f: content = f.read()`
   - `splitlines()` for lines.
   - `split()` for words.
   - `len()` for characters.
4. **Output**: 
   - Build dictionary.
   - `json.dump()` to `analysis.json`.

---

#### 6. Summary (What I learned today)

- Writing a CLI tool is not scary. `sys.argv` is my friend.
- Always assume the user will make a mistake (Defensive Programming).
- Using `read()` is more efficient than `readlines()` when I need the whole text.
- Clean code = reusable code (Separation of functions).

---

### Day 6 - Evening & Morning Session (W02 - 28/06): Binary & Float Precision

#### 1. The Shocking Fact

- In Python, `0.1 + 0.2 == 0.3` returns **`False`**.
- The result of `0.1 + 0.2` is actually `0.30000000000000004`.

#### 2. The Simple Reason (Why?)

- Computers only speak **Binary (0s and 1s)**.
- In binary, the decimal number `0.1` is a **repeating fraction** (just like `1/3 = 0.33333...` in our decimal system).
- Because computer memory is limited, it cuts off the repeating number and stores a **rounded approximation**.
- So, `0.1` stored in memory is actually `0.10000000000000000555` (a tiny bit more than 0.1).

#### 3. The Rule of Thumb (When does it end?)

- A decimal fraction has an **exact** binary representation **only if** the denominator (in its simplest form) is a power of `2`.
    - `0.5` (1/2) -> Exact (Power of 2).
    - `0.75` (3/4) -> Exact (Power of 2).
    - `0.1` (1/10) -> **NOT** exact (10 = 2 × 5). -> Repeating (Rounded).

#### 4. The Hidden Truth: `str()` vs `repr()`

- **`str()`** (String): Shows the **pretty/readable** version for humans. (Prints `0.1`).
- **`repr()`** (Representation): Shows the **exact/raw** version for programmers. (Prints `0.10000000000000000555`).
- *Lesson:* Use `repr()` whenever you want to see what the computer *actually* stored.

#### 5. The Safe Fix (How to code properly)

- **Don't** use `==` (equals) to compare two floats directly.
- **Do** check if the **difference** between them is very tiny.
- **The Solution Code:**

"```python
#### Safe comparison function
def is_close(a, b):
    return abs(a - b) < 1e-9"

#### Test it
print(is_close(0.1 + 0.2, 0.3))  # Output: True

---------------------------

### Day 7 - W02 (29/06) - Tuples: Theory & Practice

#### 1. What is a Tuple?

- A Tuple is a collection type in Python, similar to a List, but **Immutable** (cannot be changed after creation).
- **Syntax:** Defined using parentheses `()`.
- **Example:** `my_tuple = (10, 20, 30, 40, 50)`
- **Note:** They can hold mixed data types (e.g., `("hello", 1, [1, 2])`).

#### 2. Indexing & Slicing (Accessing Data)

- **Indexing:** Access specific items using `[index]` (starts at 0).
  - `my_tuple[2]` → `30` (Third element).
  - `my_tuple[-1]` → `50` (Last element, using negative indexing).
- **Slicing:** Access a range of items using `[start:end]` (end is exclusive).
  - `my_tuple[1:4]` → `(20, 30, 40)`.

#### 3. Unpacking (Assigning to variables)

- You can assign Tuple elements to multiple variables in one line.
- **Correct:** `x, y, z = (1, 2, 3)` → `x=1, y=2, z=3`.
- **Error (Discovered Practically):** `x, y, z = my_tuple` (where my_tuple has 5 elements).
  - Result: `ValueError: too many values to unpack (expected 3, got 5)`.
  - **Lesson:** The number of variables MUST match the number of elements.

#### 4. Tuple Operations (Allowed)

Since Tuples are immutable, we cannot modify them, but we can perform these actions:

- **Length:** `len(my_tuple)` → `5`.
- **Concatenation:** `my_tuple + (50,)` → `(10, 20, 30, 40, 50, 50)`. 
  - *(Note: Must add a trailing comma `,` to create a single-element tuple).*
- **Repetition:** `my_tuple * 3` → Repeats the tuple 3 times.
- **Membership:** `30 in my_tuple` → `True`.

#### 5. Reversing a Tuple (Slicing Trick)

- **Syntax:** `my_tuple[::-1]`.
- **Result:** `(50, 40, 30, 20, 10)`.
- **Function created:**

```python
def reverse_tuple(t):
    return t[::-1]