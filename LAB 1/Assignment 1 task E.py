def function():
    N = int(input())
    array = list(map(int, input().split()))

    sorted_array = sorted(array[:])
    if array == sorted_array:
        print("YES")
        return
    possible = True
    for i in range(0, N, 2):
        if array[i] != sorted_array[i]:
            possible = False
            break
    if possible:
        for i in range(1, N, 2):
            if array[i] != sorted_array[i]:
                possible = False
                break
    if possible:
        print("YES")
        return
    original_even = []
    original_odd = []
    sorted_even = []
    sorted_odd = []
    for i in range(N):
        if i % 2 == 0:
            original_even.append(array[i])
        else:
            original_odd.append(array[i])

    for i in range(N):
        if i % 2 == 0:
            sorted_even.append(sorted_array[i])
        else:
            sorted_odd.append(sorted_array[i])

    if sorted(original_even) != sorted_even or sorted(original_odd) != sorted_odd:
        print("NO")
    else:
        print("YES")
function()
