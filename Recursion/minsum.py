def minsum(arr, target):
    if target == 0:
        return 0
    if target < 0:
        return float('inf')  # Return infinity as this is not a valid solution
    mini = float('inf')  # Initialize with infinity
    for i in range(len(arr)):
        sub_min = minsum(arr, target - arr[i])  # Recursively find the minimum for the current target
        if sub_min != float('inf'):
            mini = min(mini, sub_min + 1)  # Update mini with the minimum count found so far
    return mini  # Return the minimum count


arr = [1, 2]
target = 5
k = minsum(arr, target)
print(k)  # Output should be 2, as 2 elements (2 and 3) can sum up to 5
