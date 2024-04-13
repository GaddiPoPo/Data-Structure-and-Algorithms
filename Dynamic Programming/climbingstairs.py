def climbstairs(n):
    one,two=1,1
    for i in range(n-1):
        temp=one
        one=one+two
        two=temp
    return one
n=int(input("enter the stair you wanna climb "))
k=climbstairs(n)
print(k)