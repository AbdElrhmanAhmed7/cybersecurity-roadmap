# Day 17 - W04 (13/07) - Big O Notation & Complexity Analysis

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Time Complexity, Space Complexity, Big O Hierarchy, Laws of Big O

---

## 1. What is Big O?

Mathematical way to describe **how fast an algorithm runs** (time) or **how much memory it uses** (space) as input size `n` grows.

**Core idea:** Ignore constants, focus on the **dominant term** (fastest-growing part).

**Why it matters in Cybersecurity:**
- O(n²) IDS scanning 10K logs = seconds
- O(n²) IDS scanning 100K logs = minutes/hours
- Choosing O(n log n) over O(n²) = tool works vs tool crashes

---

## 2. The Hierarchy (Fastest → Slowest)

| Complexity | Name | Speed | Example |
|------------|------|-------|---------|
| **O(1)** | Constant | 🚀 Fastest | `my_list[0]` |
| **O(log n)** | Logarithmic | ⚡ Very fast | Binary search |
| **O(n)** | Linear | ✅ Good | Single loop |
| **O(n log n)** | Linearithmic | 👍 Decent | Merge sort |
| **O(n²)** | Quadratic | 🐢 Slow | Nested loops |
| **O(2ⁿ)** | Exponential | 💀 Deadly | Naive Fibonacci |

---

## 3. Deep Dive with Examples

### O(1) — Constant
```python
def get_first(lst):
    return lst[0]   # 1 step, always
```

### O(n) — Linear
```python
def find_max(lst):
    max_val = lst[0]
    for num in lst:     # n times
        if num > max_val:
            max_val = num
    return max_val
```

### O(n²) — Quadratic (Nested Loops)
```python
def has_duplicates(lst):
    for i in lst:           # n
        for j in lst:       # n
            if i == j:
                return True
    return False
```

### O(log n) — Logarithmic (Divide by 2)
```python
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
```

### O(n log n) — Merge Sort
```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])    # log n divisions
    right = merge_sort(lst[mid:])
    return merge(left, right)       # n merges per level
```

### O(2ⁿ) — Exponential
```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)      # 2 branches per call
```

---

## 4. Laws of Big O

### Addition Rule (Sequential Steps)
```python
# O(n) + O(n²) = O(n²)
# Dominant term wins
```

### Multiplication Rule (Nested Loops)
```python
# O(n) * O(n) = O(n²)
for i in lst:       # n
    for j in lst:   # n
        print(i, j)
```

---

## 5. My Functions Analyzed

| Function | Complexity | Why |
|----------|-----------|-----|
| `factorial(n)` | O(n) | Loop 1 to n |
| `linear_search(lst, target)` | O(n) | Scan each element |
| `binary_search(lst, target)` | O(log n) | Halve each iteration |
| `remove_duplicates` (no set) | O(n²) | `.count()` inside loop |
| `bubble_sort(lst)` | O(n²) | Nested loops |
| `merge_sort(lst)` | O(n log n) | Divide + merge |

---

## 6. Measuring Time

```python
import time

def measure(func, data):
    start = time.time()
    func(data)
    return time.time() - start

# O(n²) vs O(n log n) — gap grows fast as n increases
```

---

## 7. Quick Cheat Sheet

| Operation | Big O |
|-----------|-------|
| Index access `lst[i]` | O(1) |
| List search `x in lst` | O(n) |
| Dict access `d[key]` | O(1) |
| List sort `.sort()` | O(n log n) |
| Nested loops | O(n²) |
| Binary search | O(log n) |

---

## 8. Key Takeaway

> **Recognize when you're writing O(n²) and ask: can I optimize to O(n log n) or O(n)?**

---

✅ **Status:** Day 17 Complete — Big O mastered  
🚀 **Next:** Sorting Algorithms (Bubble, Selection, Merge)
