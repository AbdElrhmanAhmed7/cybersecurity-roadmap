# Day 21 (Binary Search iterative)

from math import log2

def binary_search_iter(target, lst):
    low = 0
    high = len(lst) - 1
    for _ in range(len(lst)):
        if low > high:
            return False
        
        mid = (low + high) // 2

        if lst[mid] == target:
            return True
        elif lst[mid] > target:
            high = mid - 1
        elif lst[mid] < target:
            low = mid + 1
    return False


