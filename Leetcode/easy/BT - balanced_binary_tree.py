##Need to implement two recursion calls in this questions
#First two find depth and then to find difference at each node with depth
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def depth(self,root):
        if not root:
            return 0
        
        left_subtree = self.depth(root.left)
        right_subtree = self.depth(root.right)

        return (max(left_subtree,right_subtree) + 1)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        
        #get depth of each subtree and then do the difference
        left_subtree = self.depth(root.left)
        right_subtree = self.depth(root.right)

        return (abs(left_subtree - right_subtree) <= 1 
                and self.isBalanced(root.left) and self.isBalanced(root.right))
            


        
            
        





sol_class = Solution()
node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
node.right.right.right = TreeNode(4)
print(sol_class.isBalanced(node))