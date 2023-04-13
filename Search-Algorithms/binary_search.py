#Time complexity is O(LogN)
#Can only be used to search in a sorted array


def binary_search_rec(nums,value):
    if len(nums) == 0:
        return "The number is not found"
    m = len(nums) // 2
    if nums[m] == value:
        return "The number is found"
    elif value < nums[m]:
        return binary_search_rec(nums[0:m],value)
    else:
        return binary_search_rec(nums[m+1:],value)
    

def binary_search_iter(nums,value):
    l = 0
    r = len(nums) - 1
   

    while (l <= r):
        m = l + (r-l) // 2
        if nums[m] == value:
            return "The number is found"
        elif value < nums[m]:
            l = 0
            r = m
        else:
            l = m + 1
            r = len(nums) - 1
    return "The number is not found"


   
   





nums = [1,2,3,4,5,6,7,8]
print(binary_search_rec(nums,4))
print(binary_search_iter(nums,10))
