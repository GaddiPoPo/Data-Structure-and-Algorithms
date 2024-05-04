def permutations(s):
    if len(s) == 1:
        return [s]

    res = []
    for i in range(len(s)):
        n = s[i]
        perms = permutations(s[:i] + s[i + 1:])
        for perm in perms:
            res.append(n + perm)
    return res


s = "abc"
k = permutations(s)
print(k)