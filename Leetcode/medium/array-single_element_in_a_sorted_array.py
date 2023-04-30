#solution must be in O(log n) and O(1) space
#from collections import Counter
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums)-1
        while left < right:
            mid = int((left + right)/2)
            print(left,right,mid)
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid

        print(nums[right])



nums = [1,1,2,3,3,4,4,8,8]
sol = Solution()
sol.singleNonDuplicate(nums)
