# print all subsequences of string
def subseq(s,current='',i=0):
    if i==len(s):
        print(current)
        return

    subseq(s,current+s[i],i+1)
    subseq(s,current,i+1)
s='abc'
subseq(s)