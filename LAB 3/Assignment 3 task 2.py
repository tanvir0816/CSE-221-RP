def merge(a, b):
    temp = []
    i = j = 0
    count = 0
    b_squared = [x * x for x in b]
    b_squared.sort()
    for val in a:
        lo, hi = 0, len(b_squared)
        while lo < hi:
            mid = (lo + hi) // 2
            if val > b_squared[mid]:
                lo = mid + 1
            else:
                hi = mid
        count += lo
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(b[j])
            j += 1
    while i < len(a):
        temp.append(a[i])
        i += 1
    while j < len(b):
        temp.append(b[j])
        j += 1
    return temp, count
def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        left, inv_left = mergeSort(arr[:mid])
        right, inv_right = mergeSort(arr[mid:])
        merged, cross_count = merge(left, right)
        total = inv_left + inv_right + cross_count
        return merged, total
N = int(input())
arr = list(map(int, input().split()))

sorted_arr, result = mergeSort(arr)

print(result)
