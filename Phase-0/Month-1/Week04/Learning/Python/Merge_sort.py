# Day 20 (Merge sort)

from time import time
import random

def merge_sort(lst):
    if len(lst) <= 1:
        return lst[:]
    else:
        return merging(merge_sort(lst[:len(lst) // 2]), merge_sort(lst[len(lst) // 2:]))
           
def merging(lst1, lst2):
    result = []
    j = 0
    i = 0
    while i < len(lst1) and j < len(lst2):
            if lst1[i] > lst2[j]:
                result.append(lst2[j])
                j += 1
            else:
                result.append(lst1[i])
                i += 1
    result.extend(lst1[i:] + lst2[j:])
    return result


# start = time()
# merge_sort([random.randint(1, 1000000) for _ in range(25000)])
# print("Merge Sort:")
# print(f"{time() - start:.2f}")
