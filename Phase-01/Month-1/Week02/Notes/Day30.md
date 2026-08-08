# Day 30 — PasswordEntry: Bugs & Notes

## 1. Mutable/compute-once default argument
```python
def __init__(self, created_at=datetime.now()):  # ❌
```
- Default args are evaluated **once**, at class definition time — not per call.
- Result: every instance created without an explicit `created_at` gets the **same timestamp**.
- Breaks `is_expired()` and `__lt__` silently (no error, just wrong data).

**Fix:**
```python
self.created_at = datetime.now() if created_at is None else created_at
```

## 2. Incomplete if-branch → missing attribute
```python
if created_at is None:
    self.created_at = datetime.now()
# no else → self.created_at never set when a value IS passed
```
- Broke `from_dict()` specifically, since it always passes `created_at`.
- Raised `AttributeError: 'PasswordEntry' object has no attribute 'created_at'`.
- **Lesson:** ternary/either-branch assignments are safer than one-sided `if` blocks for required attributes.

## 3. Calling a method without `()`
```python
count = self.validate["score"]  # ❌ method object isn't subscriptable
```
**Fix:** `self.validate()["score"]`

## 4. `to_dict()` returning wrong type
- First version wrapped the dict in a list: `return [instance_dict]` → violated spec (`-> dict`).
- Also initially forgot `datetime` isn't JSON-serializable → needed `.isoformat()` in `to_dict()` and `datetime.fromisoformat()` in `from_dict()`.

## 5. Minor issues (naming/typing)
- `"symbols"` vs spec's `"symbol"` key — small mismatches like this break tests that check exact keys.
- `strength_label()` type hint said `-> dict`, actually returns `str`.
- Typo: `"Week"` instead of `"Weak"`.
- `to_dict()` leaking internal `_password` key (from `self.__dict__.copy()`) — fixed by building the dict explicitly.

## General takeaway
Most bugs were **silent** (no crash, wrong data) rather than loud (exceptions). Habit to build: after writing a class, test round-trips (`from_dict(to_dict())`) and edge cases (multiple instances close in time, empty password, no-symbol password) before calling it done — not just the happy path.