# Day 22 - W05 (18/07) - Regex Basics

> **Track:** Cybersecurity Python Fundamentals  
> **Source:** Automate the Boring Stuff — Chapter 9  
> **Topics:** `re` module, Patterns, Matching, Groups, Substitution

---

## 1. What is Regex?

**Regular Expressions (Regex)** = tool for finding and matching text patterns.

**Use cases:** searching, validating, extracting, replacing text.

```python
import re
```

---

## 2. Core Functions

### `re.compile()` — Create a Pattern Object

```python
pattern = re.compile(r"\d+")
```

**Why use it:** Reuse the same pattern multiple times. Cleaner and faster.

---

### `re.search()` — First Match Anywhere

```python
match = re.search(r"\d+", text)
```

- Searches the **entire** string
- Returns a **Match Object** or `None`

```python
match.group()      # matched text
match.start()      # start index
match.end()        # end index
```

---

### `re.match()` — Match at Beginning Only

```python
match = re.match(r"\d+", text)
```

- Checks **only index 0**
- Returns Match Object or `None`

---

### `re.findall()` — All Matches as List

```python
numbers = re.findall(r"\d+", text)
# ['123', '456']
```

---

### `re.finditer()` — All Matches as Iterator

```python
for match in re.finditer(r"\d+", text):
    print(match.group(), match.start(), match.end())
```

- Returns **Match Objects** one by one
- Better for large data (memory efficient)

---

### `re.sub()` — Replace Matches

```python
re.sub(r"Alice", "Bob", "My name is Alice")
# "My name is Bob"
```

---

### `re.IGNORECASE` — Case-Insensitive

```python
re.search(r"python", text, re.IGNORECASE)
# Matches: Python, python, PYTHON
```

---

## 3. Groups

Parentheses `()` create capture groups.

```python
pattern = re.compile(r"(\w+)@(\w+)")
match = pattern.search("user@gmail.com")

match.group()       # "user@gmail"  (full match)
match.group(1)      # "user"        (first group)
match.group(2)      # "gmail"       (second group)
match.groups()      # ('user', 'gmail')  (tuple of all groups)
```

> `groups()` returns a **tuple**, not a list.

---

## 4. Object Types

| Object | Created By | Purpose |
|--------|-----------|---------|
| **Pattern** | `re.compile()` | Reusable search pattern |
| **Match** | `search()`, `match()` | Result with `.group()`, `.start()`, `.end()` |

---

## 5. Quick Comparison

| Function | Scope | Returns | Use When |
|----------|-------|---------|----------|
| `search()` | Entire string | Match Object or `None` | Find first occurrence |
| `match()` | Beginning only | Match Object or `None` | Validate prefix |
| `findall()` | Entire string | List of strings | Get all matches |
| `finditer()` | Entire string | Iterator of Match Objects | Need positions |
| `sub()` | Entire string | New string | Replace text |

---

## 6. Quick Cheat Sheet

```python
import re

# Compile pattern
pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

# Search
match = pattern.search(text)
if match:
    print(match.group())

# Find all
matches = pattern.findall(text)

# Replace
clean = re.sub(r"\s+", " ", text)

# Case insensitive
re.search(r"failed", log, re.IGNORECASE)

# Groups
m = re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
if m:
    print(m.groups())   # ('192', '168', '1', '1')
```

---

✅ **Status:** Day 18 Complete — Regex basics (`re` module, patterns, groups)  
🚀 **Next:** Advanced Regex (lookahead, greedy vs lazy, character classes)
