def isarraysorted(arr, n):
    if n == 1:
        return 1
    if arr[n - 1] < arr[n - 2]:
        return 0
    return isarraysorted(arr, n - 1)

arr = [1, 2, 3, 4, 5]
n = len(arr)
k = isarraysorted(arr, n)
print(k)
