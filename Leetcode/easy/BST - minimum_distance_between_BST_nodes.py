#Definition for a binary tree node.
import sys
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder_bst(root):
            nonlocal min_diff
            if root is None:
                return
            inorder_bst(root.left)
            if sorted_array:
                min_diff = min(min_diff,root.val - sorted_array[len(sorted_array) - 1])
            sorted_array.append(root.val)
            inorder_bst(root.right)

        min_diff = sys.maxsize
        sorted_array = []
        inorder_bst(root)

        print(min_diff)
        
        #infinite value
        
       

        # for i in range(1,len(sorted_array)):
        #     min_diff = min(min_diff,sorted_array[i] - sorted_array[i-1])
        # return(min_diff)



sol_class = Solution()
node = TreeNode(4)
node.left = TreeNode(2)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right = TreeNode(6)

sol_class.minDiffInBST(node)
