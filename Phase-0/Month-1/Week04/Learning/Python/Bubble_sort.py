# Day 20 (Bubble sort)
from time import time
import random

def bubble_sort(lst):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(lst) - 1):
            if lst[i + 1] < lst[i]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = False

# start = time()
# bubble_sort([random.randint(1, 1000000) for _ in range(25000)])
# print("Bubble sort:")
# print(f"{time() - start:.7f}")
