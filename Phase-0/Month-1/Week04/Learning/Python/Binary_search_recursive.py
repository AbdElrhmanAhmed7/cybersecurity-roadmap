# Day 21 (Binary Search recursive)

def binary_search_recursive(target, lst, high = None, low = 0):

    if high is None:
        high = len(lst) - 1
    if low > high:
        return False
    
    mid = (low + high) // 2

    if lst[mid] == target:
        return True
    
    if lst[mid] > target:
        return binary_search_recursive(target, lst, low = low , high = mid - 1)
    elif lst[mid] < target:
        return binary_search_recursive(target, lst, low = mid + 1, high = high)
        

