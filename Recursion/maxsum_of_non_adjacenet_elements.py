def maxsumadj(arr, i, sum, maxi):
    if i >= len(arr):
        return max(sum, maxi)

    # include the current element
    incl_sum = maxsumadj(arr, i + 2, sum + arr[i], maxi)

    # exclude the current element
    excl_sum = maxsumadj(arr, i + 1, sum, maxi)

    return max(incl_sum, excl_sum)


sum = 0
i = 0
maxi = 0
arr = [2, 1, 4, 9]
max_sum = maxsumadj(arr, i, sum, maxi)
print(max_sum)