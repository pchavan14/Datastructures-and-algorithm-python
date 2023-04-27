#when any problem asks for maximum or minimum of anything consider DP
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1]) not in result:
                    result.append(sum(nums[i:j+1]))

        result.sort(key= lambda x: x, reverse=True)

        print(result[0])

        #optimized brute force
        max_subarray = 0
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i,len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray,current_subarray)
        
   






nums = [5,4,-1,7,8]
sol = Solution()
sol.maxSubArray(nums)