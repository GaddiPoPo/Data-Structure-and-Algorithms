# last occurenec of a character
def lastoccur(str, x, i, ans):
    if i >= len(str):
        return ans
    if str[i] == x:
        ans = i
    return lastoccur(str, x, i + 1, ans)


i = 0
str = "abcddedg"
ans = -1
x = 'd'
k = lastoccur(str, x, i, ans)
print(k)