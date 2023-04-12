# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        ##trick here is root is at the end of the postorder and check both conditions for empty inorder and postorder
        if inorder == [] or postorder == []:
            return None

        root = TreeNode(postorder.pop())

        index = inorder.index(root.val)
        
        #we traverse through the right tree first
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        
        return root
       