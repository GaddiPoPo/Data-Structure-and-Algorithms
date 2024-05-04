#quicksort
def partition(arr, s, e):
    pivot = arr[e]
    i = s - 1
    for j in range(s, e):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[e] = arr[e], arr[i + 1]
    return i

def quicksort(arr, s, e):
    if s >= e:
        return
    p = partition(arr, s, e)
    quicksort(arr, s, p - 1)
    quicksort(arr, p + 1, e)

arr = [8, 1, 3, 4, 20, 50, 30]
n = len(arr)
quicksort(arr, 0, n - 1)
print(arr)