# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        m = len(nums) // 2
        root = TreeNode(nums[m])          
        
        root.left = self.sortedArrayToBST(nums[0:m])
        root.right = self.sortedArrayToBST(nums[m+1:len(nums)])
        return root



        
        
        
        
            








sol = Solution()
nums = [-10,-3,0,5,9]
sol.sortedArrayToBST(nums)

        