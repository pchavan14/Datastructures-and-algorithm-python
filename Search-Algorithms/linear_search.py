def LinearSearch(nums,value):
    for i in nums:
        if i == value:
            return nums.index(i)
    return -1


nums = [2,4,1,6,7]
print(LinearSearch(nums,1))