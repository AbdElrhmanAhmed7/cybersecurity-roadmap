# PasswordVault & Serialization Day 31

> Design notes for building a secure password manager in Python.

---

## 1. Architecture Overview

`PasswordVault` is the main class responsible for managing a collection of `PasswordEntry` objects.

Each `PasswordEntry` represents a single account, while `PasswordVault` acts as the database containing all accounts.

```
PasswordVault
│
├── PasswordEntry
├── PasswordEntry
├── PasswordEntry
└── ...
```

---

## 2. Method Responsibilities

### `__init__(vault_path)`

Stores:
- The path to the JSON file
- The list of entries

```python
self.vault_path = vault_path
self.entries = []
```

---

### `__len__()`

Enables:

```python
len(vault)
```

Returns the number of entries in the vault.

---

### `__iter__()`

Enables direct iteration:

```python
for entry in vault:
    ...
```

Instead of:

```python
for entry in vault.entries:
    ...
```

Must return:

```python
return iter(self.entries)
```

> Returns an iterator, not the list itself.

---

### `add(entry)`

Adds a new `PasswordEntry` to the vault.

---

### `get(website)`

Returns the **first** `PasswordEntry` matching the given website.

Returns `None` if no match is found.

---

### `delete(entry)`

Removes the entry from the internal list.

⚠️ **Do NOT use:**

```python
del entry
```

That only deletes the variable reference. You must remove the item from the list itself:

```python
self.entries.remove(entry)
```

---

### `list_all()`

Returns all entries.

Prefer:

```python
return self.entries.copy()
# or
return self.entries[:]
```

Instead of:

```python
return self.entries
```

**Why?** Because of **aliasing**. If you return the original list:

```python
lst = vault.list_all()
lst.clear()  # This also empties the vault!
```

---

### `search(query)`

Searches inside:
- `website`
- `username`

Returns:

```python
list[PasswordEntry]
```

> Returns **all** matches, not just the first result.

Prefer **case-insensitive** search using `.lower()`:

```python
query = query.lower()
return [e for e in self.entries
        if query in e.website.lower()
        or query in e.username.lower()]
```

---

### `get_expired()`

Returns **all expired entries**, not a list of booleans.

```python
return [entry for entry in self.entries if entry.is_expired()]
```

---

## 3. Serialization

JSON cannot save Python objects directly. It only supports:

- `dict`
- `list`
- `str`
- `int`
- `float`
- `bool`
- `None`

So the flow is:

```
PasswordEntry
    ↓
to_dict()
    ↓
dict
    ↓
json.dump()
```

---

## 4. `save()`

Converts all entries to dictionaries, then writes to JSON:

```
PasswordEntry Objects
    ↓
list[dict]
    ↓
json.dump()
    ↓
passwords.json
```

```python
def save(self):
    data = self.to_dict()
    with open(self.vault_path, "w") as f:
        json.dump(data, f, indent=4)
```

---

## 5. `load()`

The reverse process:

```
passwords.json
    ↓
json.load()
    ↓
list[dict]
    ↓
PasswordEntry.from_dict()
    ↓
PasswordEntry Objects
```

```python
def load(self):
    self.entries.clear()  # Prevent duplicates on repeated loads
    with open(self.vault_path, "r") as f:
        data = json.load(f)
    self.entries = [PasswordEntry.from_dict(d) for d in data]
```

> **Always call `self.entries.clear()` before loading** to avoid data duplication when `load()` is called multiple times.

---

## 6. `to_dict()`

Converts all entries to a list of dictionaries using list comprehension:

```python
def to_dict(self):
    return [entry.to_dict() for entry in self.entries]
```

---

## 7. Aliasing, Shallow Copy & Deep Copy

### Aliasing

```python
a = self.entries
b = self.entries
```

Both variables point to the **same list**. Any modification to one affects the other.

---

### Shallow Copy

```python
self.entries.copy()
# or
self.entries[:]
```

Creates a **new list**, but the objects inside are still shared.

```
New List → Same Objects
```

---

### Deep Copy

```python
import copy
copy.deepcopy(self.entries)
```

Creates a **new list** AND **new objects**.

```
New List → New Objects
```

---

## 8. `@classmethod`

Use when you need to create an object from inside the class itself.

Examples:

```python
PasswordEntry.from_dict(...)
PasswordVault.from_json(...)
```

### Why `cls` instead of the class name?

Using `cls(...)` instead of `PasswordVault(...)` makes it work with **inheritance**.

```
PasswordVault
    ↓
EncryptedVault
```

If you call:

```python
EncryptedVault.from_json(...)
```

Then `cls` refers to `EncryptedVault`, not `PasswordVault`.

---

### Why not `@staticmethod`?

`@staticmethod` knows neither `cls` nor `self`.

If you hardcode `PasswordVault(...)` inside it, subclasses cannot create their own type of objects.

---

### Handling Constructor Changes

If a subclass changes its constructor:

```python
class EncryptedVault(PasswordVault):
    def __init__(self, path, key):
        ...
```

Then `cls(path)` won't work because it now needs `path` **and** `key`.

**Solutions:**
- Pass the required parameters explicitly
- Or use `**kwargs` for flexibility

---

## 9. Design Principles

### Single Responsibility

| Class | Responsibility |
|-------|---------------|
| `PasswordEntry` | Represents a single account |
| `PasswordVault` | Manages a collection of accounts |

---

### Code Reusability

`save()` reuses `to_dict()`, which reuses `entry.to_dict()`:

```
save()
    ↓
to_dict()
    ↓
entry.to_dict()
```

Avoid duplicating the same logic.

---

### Best Practices

| Practice | Where Applied |
|----------|---------------|
| List comprehension | Data transformation (`to_dict()`, `load()`) |
| Magic methods | `__len__`, `__iter__` for intuitive API |
| `@classmethod` | Factory methods (`from_dict`, `from_json`) |
| Defensive copying | `list_all()` returns a copy, not the original |
| Case-insensitive search | `search()` uses `.lower()` |

---

## 10. Key Concepts Summary

| Concept | Description |
|---------|-------------|
| **Aliasing** | Multiple variables referencing the same object |
| **Shallow Copy** | New container, same inner objects |
| **Deep Copy** | New container, new objects |
| **Serialization** | Converting objects to a storable format (JSON) |
| **Deserialization** | Reconstructing objects from stored data |
| **JSON** | Text-based data format for persistence |
| **File Persistence** | Saving data to disk so it survives program restarts |
| **Composition** | `PasswordVault` contains `PasswordEntry` objects |
| **Magic Methods** | `__len__`, `__iter__` for Pythonic behavior |
| **`@classmethod`** | Factory methods that work with subclasses |
| **`cls` vs `self`** | `cls` = class, `self` = instance |
| **Separation of Concerns** | Each class has one clear job |
