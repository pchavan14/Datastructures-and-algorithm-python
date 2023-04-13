class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        left_root = self.maxDepth(root.left)
        right_root = self.maxDepth(root.right)

        
        return max(left_root,right_root) + 1
    



sol_class = Solution()
node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
print(sol_class.maxDepth(node))