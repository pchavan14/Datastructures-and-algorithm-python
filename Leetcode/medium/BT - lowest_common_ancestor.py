# Definition for a binary tree node.
#Lowest common ancestor of two nodes in BT
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        if (root.val == p or root.val == q):
            return root.val
        
        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        
        #if (left_res and right_res):
        return root.val
        # else:
        #     return left_res or right_res
       
        




sol_class = Solution()
node = TreeNode(2)
node.left = TreeNode(1)
node.left.left = TreeNode(10)
node.left.left.right = TreeNode(11)
node.left.right = TreeNode(5)
node.left.right.left = TreeNode(7)
node.left.right.right = TreeNode(6)
node.right = TreeNode(3)

print(sol_class.lowestCommonAncestor(node,11,7))

        