class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return None
        count_dict = {}

        for i in nums:
            if i not in count_dict:
                count_dict[i] = 0
            else:
                count_dict[i] += 1

        #The below statement returns the maximum number in the dictionary
        return(max(count_dict, key=count_dict.get))


nums = [3]
sol = Solution()
sol.majorityElement(nums)