# Day 21 (Linear Search)

def linear_search(target, lst):
    for item in lst:
        if item == target:
            print(f"The item '{target}' is in the list.")
            return True
    print(f"The item '{target}' isn't in the list.")
    return False


# linear_search(0, [9, 2, 15, 7, 1, 0])