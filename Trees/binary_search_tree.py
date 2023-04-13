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
    
def minimum_value_node(newTree):
    #mimumum value of the BST tree is the left most node
    current = newTree
    while current.left:
        current = current.left
    return current

def deletenode(newTree,nodeValue):
    if not newTree:
        return
    if nodeValue < newTree.data:
        deletenode(newTree.left,nodeValue)
    elif nodeValue > newTree.data:
        deletenode(newTree.right,nodeValue)
    else:
        #delete node which has one child
        if newTree.left is None:
            newTree.data = newTree.right.data
            newTree.right = None
            return
        if newTree.right is None:
            newTree.data = newTree.left.data
            newTree.left = None
            return
        
        temp = minimum_value_node(newTree.right)
        newTree.data = temp.data
        temp = None
        return

def deleteentireBST(newTree):
    newTree.data = None
    newTree.right = None
    newTree.left = None
    print ("The entire tree is deleted")

##Time complexities
#Insert , search and delete is O(logN)
#Traverse is O(n)
        




newTree = TreeNode(10)
insertNode(newTree,20)
insertNode(newTree,30)
insertNode(newTree,40)
insertNode(newTree,50)
insertNode(newTree,60)
insertNode(newTree,70)
insertNode(newTree,80)
levelorder_traversal(newTree)
# print(searchNode(newTree,60))
# deletenode(newTree,70)
# levelorder_traversal(newTree)




