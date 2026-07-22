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
