#binary search tree
#insertion and deletion is faster in BST

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insertNode(newTree,val):
    newnode = TreeNode(val)
    if not newTree:
        newTree = newnode
    else:
        root = newTree
        while root: #Time complexity O(LogN) for inserting a node and space complexity is also O(LogN)
            if newnode.data <= root.data: #O(N/2)
                if root.left is None:
                    root.left = newnode
                    return
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = newnode
                    return
                else:
                    root = root.right

##Level order traversal using queue
def levelorder_traversal(newTree):
    if not newTree:
        return
    else:
        custom_queue = []
        custom_queue.append(newTree)
        while custom_queue: #Time and space complexity is O(n)
            root = custom_queue.pop(0)
            print(root.data)
            if root.left is not None:
                custom_queue.append(root.left)
            if root.right is not None:
                custom_queue.append(root.right)

                
##Search time complexity O(LogN) as we traverse only half
def searchNode(newTree,val):
    if not newTree:
        return "The tree is empty"
    else:
        root = newTree
        while root:
            if root.data == val:
                return "Found the element"
            elif root.data > val:
                root = root.left
            else:
                root = root.right
        return "Element not found"





newTree = TreeNode(70)
insertNode(newTree,50)
insertNode(newTree,30)
insertNode(newTree,90)
insertNode(newTree,60)
insertNode(newTree,80)
insertNode(newTree,100)
levelorder_traversal(newTree)
print(searchNode(newTree,60))




