class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        if p.val != q.val:
            return False
        return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))



sol_class = Solution()
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(1)
node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(1)
print(sol_class.isSameTree(node,node1))