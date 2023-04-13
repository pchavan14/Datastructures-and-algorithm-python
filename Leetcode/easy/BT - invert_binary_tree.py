class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.left)

        temp = root.left
        root.left = root.right
        root.right = temp
        return root.val



sol_class = Solution()
node = TreeNode(4)
node.left = TreeNode(2)
node.right = TreeNode(7)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right.left = TreeNode(6)
node.right.right = TreeNode(9)
print(sol_class.invertTree(node))