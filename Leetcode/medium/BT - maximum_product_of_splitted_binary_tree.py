# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
       

        def subtree_traversal(subroot): ##Time complexity - O(n) , space complexity as well
            nonlocal subtree_sums
            if not subroot:
                return 0
            total_sum = subroot.val + subtree_traversal(subroot.left) + subtree_traversal(subroot.right)
            print(total_sum)
            subtree_sums.append(total_sum)
            return total_sum

        subtree_sums = []   
        total_sum = subtree_traversal(root)
        print(total_sum)
        print(subtree_sums)
        
        maxProduct = 0
        for s in subtree_sums:
            maxProduct = max(maxProduct, s * (total_sum - s))
        return maxProduct % (10 ** 9 + 7) ## ** is raised to , to the power of 9









sol_class = Solution()
node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right = TreeNode(3)
node.right.left = TreeNode(6)

print(sol_class.maxProduct(node))

