# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 or not root2:
            return False
        

        def postorder(root,key):
            if not root:
                return
            if root.left is None and root.right is None:
                postorder_dict[key].append(root.val)
            postorder(root.left,key)
            postorder(root.right,key)


        postorder_dict = defaultdict(list)
        
        postorder(root1,'root1')
        postorder(root2,'root2')
        
        
        

        if postorder_dict['root1'] == postorder_dict['root2']:
            return True
        else:
            return False