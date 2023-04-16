# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
##Inorder traversal of a BST is a sorted array !!!!
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder_traversal = []

        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            inorder_traversal.append(root.val)
            inorder(root.right)

        inorder(root)
        
        for i in range(1,len(inorder_traversal)):
            if inorder_traversal[i-1] >= inorder_traversal[i]:
                return False

        return True
        
        
        
        




sol_class = Solution()
node = TreeNode(2)
node.left = TreeNode(1)
# node.left.left = TreeNode(1)
# node.left.right = TreeNode(3)
node.right = TreeNode(3)

print(sol_class.isValidBST(node))
