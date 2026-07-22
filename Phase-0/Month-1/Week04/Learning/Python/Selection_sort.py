# Day 20 (Selection sort)
from time import time
import random

def selection_sort(lst):
    lst_len = len(lst)
    for k in range(lst_len):
        flag = True
        smallest = k
        for i in range(k, len(lst) - 1):
            if lst[smallest] > lst[i + 1]:
                smallest = i + 1
                flag = False
        if flag:
            break
        lst[k] , lst[smallest] = lst[smallest], lst[k]


# start = time()
# selection_sort([random.randint(1, 1000000) for _ in range(25000)])
# print("Selection Sort: ")
# print(f"{time() - start:.2f}")
