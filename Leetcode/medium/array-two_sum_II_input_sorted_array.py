class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = 0 
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1,j+1]
        

nums = [0,0,3,4]
target = 0
sol = Solution()
print(sol.twoSum(nums,target))