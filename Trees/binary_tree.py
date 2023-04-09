#Binary tree - It has atmost two childrens

#Types of binary tree
#full binary tree  - each node has 0 or 2 children
#Perfect binary tree - all nodes in same level and have 2 childrens

#Linked list is used in BT creation

#Time complexity - O(1)
#Space complexity - O(1)
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder_traversal(newTree):
    if not newTree:  #Time and space complexity O(n) as we traverse the whole tree in recursion process
        return
    print(newTree.data)
    preorder_traversal(newTree.left)
    preorder_traversal(newTree.right)

def inorder_traversal(newTree):
    if not newTree:
        return
    inorder_traversal(newTree.left)
    print(newTree.data)
    inorder_traversal(newTree.right)

        
    


newTree = TreeNode(3)
newTree.left = TreeNode(4)
newTree.left.left = TreeNode(7)
newTree.right = TreeNode(5)
newTree.right.right = TreeNode(8)

print("Preorder traversal")
preorder_traversal(newTree)

print("Inorder traversal")
inorder_traversal(newTree)


#Two types of traversal in BT
#Depth first search - 
# preorder  - Root , Left , Right
# inorder  - Left , Root , Right
# postorder - Left , right , root
#Breadth first search - level order











newTree = TreeNode("Drinks")










