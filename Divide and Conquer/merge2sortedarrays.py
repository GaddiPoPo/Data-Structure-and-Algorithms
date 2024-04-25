def merge(arr1, arr2, len1, len2):
    merged = []
    i = 0
    j = 0
    while i < len1 and j < len2:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len1:
        merged.append(arr1[i])
        i += 1
    while j < len2:
        merged.append(arr2[j])
        j += 1
    return merged

arr1 = [2, 2, 3, 5, 7]
arr2 = [4, 6, 7, 9, 13]
len1 = len(arr1)
len2 = len(arr2)
k = merge(arr1, arr2, len1, len2)
print(k)