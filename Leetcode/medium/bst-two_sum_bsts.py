# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        #Duplicates in a binary search tree are not allowed
        #we can only use set if there are unique node values in a tree
        list1= set()
        list2 = set()
        list1 = self.inorder(root1,list1)  
        list2 = self.inorder(root2,list2)


        for i in list1:
            #The lookup in a set is O(1) , so its always better to store values in a set
            if (target - i) in list2:
                return True
        return False
     


    def inorder(self,root,list):
        if not root:
            return None
        self.inorder(root.left,list)
        list.add(root.val)
        self.inorder(root.right,list)
        return list