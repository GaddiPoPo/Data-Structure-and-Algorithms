def max_cuts(n, x, y, z):
    if n == 0:
        return 0
    if n < 0:
        return float('-inf')  # Return negative infinity as this is not a valid solution
    a = max_cuts(n - x, x, y, z) + 1
    b = max_cuts(n - y, x, y, z) + 1
    c = max_cuts(n - z, x, y, z) + 1
    d = max(a, b, c)
    return d

n = 11
x = 2
y = 3
z = 5
k = max_cuts(n, x, y, z)
print(k)
