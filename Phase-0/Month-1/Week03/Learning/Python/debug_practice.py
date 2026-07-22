# Day 11

# -*- coding: utf-8 -*-
"""
Practice script with several intentional subtle bugs.
Find them without running... then run to check yourself.
"""
from random import choice

# Done
def remove_duplicates(lst):
    result = lst[:]
    for item in lst:
        if result.count(item) > 1:
            result.remove(item)
    return result


# Done
def get_average(numbers):
    return sum(numbers) / len(numbers)

# Done
def find_max_index(lst):
    max_value = lst[0]
    max_idx = 0
    for i in range(len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_idx = i
    return max_idx

# Done
def merge_dicts(d1, d2):
    result = d1.copy()
    for key in d2:
        result[key] = d2[key]
    return result

# Done
def count_words(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

# Done
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True

def main():
    nums = [1, 1, 1]
    print("Original:", nums)
    print("No duplicates:", remove_duplicates(nums))
    print("Still original after removing dups?:", nums)

    print("Average:", get_average([1, 2, 3]))
    print("Average again (same call):", get_average([1, 2, 3]))

    print(find_max_index([-5, -2, -9, -1]))

    d1 = {'a': 1}
    d2 = {'b': 2}
    merged = merge_dicts(d1, d2)
    print("d1 after merge:", d1)

    print(count_words("the cat sat on the mat the cat ran"))

    print(is_sorted([1, 2, 3, 4, 5]))

main()