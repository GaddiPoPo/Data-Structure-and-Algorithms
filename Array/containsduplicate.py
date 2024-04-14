def duplicate(arr):
    s = set()
    for i in arr:
        if i in s:
            return True
        s.add(i)
    return False
arr = [3, 9, 2, 5, 8]
n = len(arr)
result = duplicate(arr)
print(result)
# False for no duplicated and vice versa