class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return
        else:
            custom_queue = []
            level_order_queue = []
            
            custom_queue.append(root)
            
            while custom_queue: #Time and space complexity is O(n)
                level = []
                for _ in range(len(custom_queue)):
                    root = custom_queue.pop(0)
                    level.append(root.val)
                    if root.left is not None:
                        custom_queue.append(root.left)
                        

                    if root.right is not None:
                        custom_queue.append(root.right)
                level_order_queue.append(level)
            print (level_order_queue)
                    
                
               

       

sol_class = Solution()
node = TreeNode(3)
node.left = TreeNode(9)
node.left.left = TreeNode(10)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
sol_class.levelOrder(node)

