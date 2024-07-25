def twoSum(nums,target):
    map={}
    for i,n in enumerate(nums):
        diff=target-n
        if diff in map:
            return [map[diff],i]
        map[n]=i
    return
nums=[1,4,7,6]
target=8
k=twoSum(nums,target)
print(k)