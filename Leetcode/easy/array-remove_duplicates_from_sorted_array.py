class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return nums

        i = 0
        j = i + 1

        while (j < len(nums)):
            if nums[i] == nums[j]:
                nums.remove(nums[j])
            else:
                i = i + 1
                j = j + 1

        print(nums)

sol = Solution()
sol.removeDuplicates([0,0,1,1,1,2,2,3,4])