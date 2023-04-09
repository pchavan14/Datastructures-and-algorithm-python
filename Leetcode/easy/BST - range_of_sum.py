#Given the root node of a binary search tree and two integers low and high, 
#return the sum of values of all nodes with a value in the inclusive range [low, high].

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        #works in python3 but not in python
        def bst(root):
            nonlocal total_sum # The nonlocal keyword is used in nested functions to reference a variable in the parent function. 
            if not root:
                return
            if root.val >= low and root.val <= high:       
                total_sum += root.val
            bst(root.left)
            bst(root.right)
            return total_sum


        total_sum = 0
        bst(root)
        return (total_sum)
    


        
    
        





newTree = TreeNode(10)
newTree.left = TreeNode(5)
newTree.left.left = TreeNode(3)
newTree.left.right = TreeNode(7)
newTree.right = TreeNode(15)
newTree.right.right = TreeNode(18)

sol = Solution()
total_sum = sol.rangeSumBST(newTree,7,15)

print(total_sum)
