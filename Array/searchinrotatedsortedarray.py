def search(nums,target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = i + (j - i) // 2
        if nums[mid] == target:
            return mid
        elif nums[i] <= nums[mid]:

            if nums[i] <= target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        else:
            if nums[mid] < target <= nums[j]:
                i = mid + 1
            else:
                j = mid - 1
    return -1
nums = [4,5,6,7,0,1,2]
target=0
k=search(nums,target)
print(k)