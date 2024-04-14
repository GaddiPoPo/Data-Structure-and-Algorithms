def findMinDiff(A, N, M):
    A.sort()
    min_diff = float('inf')
    for i in range(N - M + 1):
        diff = A[M - 1 + i] - A[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

A = [3, 4, 1, 9, 56, 7, 9, 12]
N = len(A)
M = 5  # number of students
k = findMinDiff(A, N, M)
print(k)
