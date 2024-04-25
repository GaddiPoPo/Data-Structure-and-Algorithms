#reverse a string
def reverseastring(str,n):
    i=0
    j=n-1
    while i<=j:
        list1[i],list1[j]=list1[j],list1[i]
        i+=1
        j-=1
    return "".join(list1)
str="jagrat"
list1=list(str)
n=len(list1)
k=reverseastring(list1,n)
print(k)