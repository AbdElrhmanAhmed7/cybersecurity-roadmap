# Day 20 - W05 (14/07) - Sorting Algorithms

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Bubble Sort, Selection Sort, Merge Sort, Divide and Conquer, Recursion, Two Pointers

---

## 1. Bubble Sort

### Idea
Compare every two adjacent elements. If left > right, swap them. After each pass, the largest element "bubbles" to the end.

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst
```

### Complexity

| Case | Time |
|------|------|
| Best | O(n) *(with optimization)* |
| Average | O(n²) |
| Worst | O(n²) |

**Space:** O(1)

### Pros & Cons
- ✅ Easy to understand
- ❌ Very slow for large datasets

---

## 2. Selection Sort

### Idea
Find the smallest element, swap it with the first unsorted position. Repeat until sorted.

```python
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
```

### Complexity

| Case | Time |
|------|------|
| Best | O(n²) |
| Average | O(n²) |
| Worst | O(n²) |

**Space:** O(1)

### Pros & Cons
- ✅ Fewer swaps than Bubble Sort
- ❌ Still O(n²), scans remaining list every iteration

---

## 3. Merge Sort — Divide and Conquer

### Main Idea
Instead of sorting a large list directly:
1. Divide into two halves
2. Keep dividing until every list has one element
3. Merge sorted lists back together

```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Complexity

| Case | Time |
|------|------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |

**Space:** O(n)

### Why O(n log n)?
- `log n` = number of times we divide the list
- `n` = during every merge level we visit every element once
- Total: `O(n log n)`

---

## 4. Recursion Essentials

Every recursive function needs:

### Base Case
```python
if len(lst) <= 1:
    return lst
```
Without it → infinite calls → `RecursionError`

### Recursive Case
```python
left = merge_sort(lst[:mid])
right = merge_sort(lst[mid:])
return merge(left, right)
```

---

## 5. Two Pointers Technique

Instead of `pop(0)` (slow, shifts elements):

```python
i = j = 0
while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
```

**Advantages:**
- Faster (no element shifting)
- Cleaner implementation
- O(1) extra space per merge step

---

## 6. Algorithm Comparison

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) |
| Selection | O(n²) | O(n²) | O(n²) | O(1) |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) |

---

## 7. Interview Notes

| Algorithm | Key Points |
|-----------|-----------|
| **Bubble** | Adjacent swaps; optimize with swap flag |
| **Selection** | Finds minimum each pass; fewer swaps |
| **Merge** | Divide and Conquer; recursion; extra memory; best for large datasets |

---

## 8. Errors I Made Today

| Mistake | Why It Was Wrong | Correct Way |
|---------|-----------------|-------------|
| Used `pop(0)` in merge | Shifts all elements → O(n) per pop | Use Two Pointers (`i`, `j`) |
| Forgot to return merged list | Function returns `None` | Always `return result` |
| Thought Two Pointers were complex | Actually simpler than `pop(0)` | Just increment indices |

---

## 9. Quick Cheat Sheet

```python
# Bubble Sort
for i in range(n):
    for j in range(n - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

# Selection Sort
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if lst[j] < lst[min_idx]:
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]

# Merge Sort
def merge_sort(lst):
    if len(lst) <= 1: return lst
    mid = len(lst) // 2
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result
```

---

✅ **Status:** Day 20 Complete — Bubble, Selection, Merge Sort, Recursion, Two Pointers  
