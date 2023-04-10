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
            #nonlocal total_sum # The nonlocal keyword is used in nested functions to reference a variable in the parent function. 
            #alternative to nonlocal variable is creating a dictioanry and accessing it
            if not root:
                return
            if root.val >= low and root.val <= high:       
                d['total_sum'] += root.val
            bst(root.left)
            bst(root.right)
           

        d = {'total_sum' : 0}
        bst(root)
        return(d['total_sum'])
    
    #iterative approach by creating  a stack
    def rangeSumBST_iterative(self,root,low,high):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        
        return ans
    


        
    
        





newTree = TreeNode(10)
newTree.left = TreeNode(5)
newTree.left.left = TreeNode(3)
newTree.left.right = TreeNode(7)
newTree.right = TreeNode(15)
newTree.right.right = TreeNode(18)

sol = Solution()
total_sum = sol.rangeSumBST(newTree,7,15)

print(total_sum)

iterative_sum = sol.rangeSumBST_iterative(newTree,7,15)

print(iterative_sum)
