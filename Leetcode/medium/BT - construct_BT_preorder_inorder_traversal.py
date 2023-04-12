class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):


        def bst(preorder,inorder):
            if preorder == [] or inorder == []:
                return None
          
            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            preorder.pop(0)
            
            
            root.left = bst(preorder,inorder[0:index])
            root.right = bst(preorder,inorder[index+1:])
            return root



        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
preorder = [3,9,15]
inorder = [9,3,15]
sol = Solution()
sol.buildTree(preorder, inorder)