# Day 21 - W06 (15/07) - Search Algorithms

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Linear Search, Binary Search (Iterative & Recursive), Best Practices

---

## 1. Linear Search

### Idea
Check every element one by one until target is found or list ends.

```python
def linear_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1
```

### Complexity
- **Best:** O(1) — target is first element
- **Worst:** O(n) — target is last or missing

### Pros & Cons
- ✅ Works on sorted and unsorted lists
- ✅ Very simple
- ❌ Slow for large datasets

---

## 2. Binary Search

### Idea
Only works on **sorted** lists. Remove half the search space every iteration.

```
[1, 3, 5, 7, 9, 11, 13]
         ^
        mid
```
- target < mid → search left
- target > mid → search right

### Why Must the List Be Sorted?
Binary Search decides "go left" or "go right" based on comparison. If unsorted, this decision is meaningless.

```
[9, 2, 15, 7, 1]   # unsorted — Binary Search fails
```

---

## 3. Iterative Binary Search

```python
def binary_search(lst, target):
    low, high = 0, len(lst) - 1

    while low <= high:          # while search space exists
        mid = (low + high) // 2

        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid + 1       # search right half
        else:
            high = mid - 1      # search left half

    return False                # search space disappeared
```

### Key Insight
> **Stop when the search space disappears (`low > high`), not when you decide a number of iterations.**

---

## 4. Recursive Binary Search

Same logic, different implementation.

```python
def binary_search_recursive(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1

    if low > high:              # base case: empty search space
        return False

    mid = (low + high) // 2

    if lst[mid] == target:
        return True
    elif lst[mid] < target:
        return binary_search_recursive(lst, target, mid + 1, high)
    else:
        return binary_search_recursive(lst, target, low, mid - 1)
```

---

## 5. Best Practices

### ✅ Pass indices, not slices
```python
# BAD: creates new list every call
binary_search(lst[:mid], target)

# GOOD: pass low/high indices
binary_search(lst, target, low, mid - 1)
```

### ✅ Use `is None` for defaults
```python
if high is None:      # correct
if high == None:      # avoid (works but not Pythonic)
```

### ✅ Flatten after return
```python
# BAD
if condition:
    return True
else:
    do_something()

# GOOD
if condition:
    return True

do_something()        # no else needed after return
```

### ✅ Don't use `while True`
```python
# BAD — hides the real stopping condition
while True:
    if low > high:
        break

# GOOD — condition is explicit
while low <= high:
    ...
```

---

## 6. Common Mistakes

| Mistake | Why It's Wrong |
|---------|---------------|
| `while True` | Hides real stopping condition |
| `for range(len(lst))` | Binary Search doesn't know iteration count |
| `log2()` for iterations | Algorithm decides when to stop, not you |
| Slicing `lst[:mid]` | O(n) memory per call — kills performance |
| Special conditions like `high == 0` | Trust the algorithm: `low > high` is enough |

---

## 7. Comparison

| Algorithm | Requires Sorted | Best | Worst | Use Case |
|-----------|----------------|------|-------|----------|
| Linear | No | O(1) | O(n) | Small/unsorted data |
| Binary | Yes | O(1) | O(log n) | Large sorted data |

---

## 8. Quick Cheat Sheet

```python
# Linear Search
for i, item in enumerate(lst):
    if item == target:
        return i
return -1

# Binary Search (Iterative)
low, high = 0, len(lst) - 1
while low <= high:
    mid = (low + high) // 2
    if lst[mid] == target: return True
    elif lst[mid] < target: low = mid + 1
    else: high = mid - 1
return False

# Binary Search (Recursive)
if low > high: return False
mid = (low + high) // 2
if lst[mid] == target: return True
elif lst[mid] < target:
    return binary_search(lst, target, mid + 1, high)
else:
    return binary_search(lst, target, low, mid - 1)
```

---

## 9. Key Takeaway

> **The algorithm stops because the search space disappeared (`low > high`), not because we decided on a number of iterations.**

---

✅ **Status:** Day 21 Complete — Linear Search, Binary Search (Iterative & Recursive)  
