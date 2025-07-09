class Solution:
    def maxPrefixes(self, arr, leftIndex, rightIndex):
        # code here.
        l=[]
        n=len(arr)
        for i in range(len(leftIndex)):
            L=leftIndex[i]
            R=rightIndex[i]
            max_sum=float("-inf")
            current_sum=0
            for j in range(L,R+1):
                current_sum+=arr[j]
                max_sum=max(current_sum,max_sum)
            l.append(max_sum)
        return l