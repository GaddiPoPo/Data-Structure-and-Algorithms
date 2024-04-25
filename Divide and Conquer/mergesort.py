# merge sort
def merge(arr, s, mid, e):
    len1 = mid - s + 1
    len2 = e - mid

    left = [0] * len1
    right = [0] * len2

    for i in range(len1):
        left[i] = arr[s + i]
    for j in range(len2):
        right[j] = arr[mid + j + 1]

    i = j = 0
    k = s
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1


def mergesort(arr, s, e):
    if s < e:
        mid = (s + e) // 2
        mergesort(arr, s, mid)
        mergesort(arr, mid + 1, e)
        merge(arr, s, mid, e)


arr = [2, 1, 3, 5, 7, 8, 4, 9, 6]
n = len(arr)
mergesort(arr, 0, n - 1)
print(arr)