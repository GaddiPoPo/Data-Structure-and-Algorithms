def findSum(arr, n):
    # code here
    mini = arr[0]
    maxi = arr[0]
    for i in range(n):
        if maxi < arr[i]:
            maxi = arr[i]
        if mini > arr[i]:
            mini = arr[i]
    return (mini + maxi)
arr = [3, 9, 2, 5, 8]
n = len(arr)

result = findSum(arr, n)
print("Sum of minimum and maximum elements:", result)
