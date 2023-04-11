#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        if root.left is None and root.right is None:
            return True
        
        
        def utilfunction(L,R):
            if L is None and R is None:
                return True
            if (L is None and R is not None) or (R is None and L is not None):
                return False
            if L.val == R.val:
                x = utilfunction(L.right,R.left)
                y = utilfunction(L.left,R.right)
                return ( x and y)

        return(utilfunction(root.left,root.right))
        

        








