#questions
#1. does the list only have positive numbers ?
#2. can we have repetitive pairs or all should be distinct ?
#3. is the inverse pair also valid ?
#4. How big is the array ?

def two_sum(nums,target):
    if not nums:
        return
    hash_table = {}
    for i in nums:
        if i not in hash_table:
            hash_table[target-i] = nums.index(i)
        else:
            return(nums.index(i),hash_table[i])
        

nums = [2,11,15,7]
target = 9
print(two_sum(nums,target))

#time complexity - O(n)
#space complexity - O(n)

#distinct pairs constraint
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            continue
        elif nums[i] + nums[j] == target:
            print(i,j)
#time complexity  - O(n2)
    
