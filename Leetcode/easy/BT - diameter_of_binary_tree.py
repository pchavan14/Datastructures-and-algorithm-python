class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diameter = 0
        def bst(root):
            nonlocal diameter
            if not root:
                return 0
            left_path = bst(root.left)
            right_path = bst(root.right)

            diameter = max(diameter,left_path + right_path)
            print(left_path , right_path , diameter)

            
            return max(left_path,right_path) + 1
        
        (bst(root))
        return (diameter)

       
        






sol_class = Solution()
node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right = TreeNode(3)
sol_class.diameterOfBinaryTree(node)