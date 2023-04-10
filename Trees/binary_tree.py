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
    if not newTree: #Time and space complexity O(n) as we traverse the whole tree in recursion process
        return
    inorder_traversal(newTree.left)
    print(newTree.data)
    inorder_traversal(newTree.right)

def postorder_traversal(newTree):
    if not newTree: #Time and space complexity O(n) as we traverse the whole tree in recursion process
        return
    postorder_traversal(newTree.left)
    postorder_traversal(newTree.right)
    print(newTree.data)

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

#while searching we always use level order traversal because queues perform better than stacks and recursion
def searchnode_BT(newTree,value):
    if not newTree:
        return
    else:
        custom_queue = []
        custom_queue.append(newTree) 
        while custom_queue:
            root = custom_queue.pop(0)
            if root.data == value:
                return "We found the element"
            if root.left is not None:
                custom_queue.append(root.left)
            if root.right is not None:
                custom_queue.append(root.right)
        return "The element is not present"
    
def insertnode_BT(newTree,value):
    newnode = TreeNode(value)
    if not newTree:
        newTree = newnode
    else:
        custom_queue = []
        custom_queue.append(newTree)
        while custom_queue:
            root = custom_queue.pop(0)
            #we always start from the left child 
            if root.left is not None:
                custom_queue.append(root.left)
            else:
                root.left = newnode
                return 
            if root.right is not None:
                custom_queue.append(root.right)
            else:
                root.right = newnode
                return

#To delete a node in BT , find the deepest node and replace the node to delete with deepest node value
# then delete the deepest node
# In binary tree nodes get attached from left to right

def getdeepest_node(newTree):
    if not newTree:
        return
    else:
        custom_queue = []
        custom_queue.append(newTree)
        while custom_queue:
            root = custom_queue.pop(0)
            if root.left is not None:
                custom_queue.append(root.left)
            if root.right is not None:
                custom_queue.append(root.right)
        deepestnode = root.data
        return deepestnode
    
def deletedeepest_node(newTree):
    if not newTree:
        return
    
    deepest_node = getdeepest_node(newTree)
    custom_queue = []
    custom_queue.append(newTree)
    while custom_queue:
        root = custom_queue.pop(0)
        if root.data == deepest_node:
            root.data = None
            return
        else:
            if root.left is not None:
                if root.left.data == deepest_node:
                    root.left = None
                    return
                else:
                    custom_queue.append(root.left)
            if root.right is not None:
                if root.right .data == deepest_node:
                    root.right  = None
                    return
                else:
                    custom_queue.append(root.right)
    
def deletenode_BT(newTree,node):
    if not newTree:
        return
    deepest_node = getdeepest_node(newTree)
    deletedeepest_node(newTree)
    custom_queue = []
    custom_queue.append(newTree)
    while custom_queue:   #Time complexity O(n)
        root = custom_queue.pop(0)
        if root.data == node.data:
            node.data = deepest_node
            return
        else:
            if root.left is not None:
                if root.left.data == node.data:
                    root.left.data = deepest_node
                    return
                else:
                    custom_queue.append(root.left)
            if root.right is not None:
                if root.right.data == node.data:
                    root.right.data  = deepest_node
                    return
                else:
                    custom_queue.append(root.right)

def deleteentire_BT(newTree):
    newTree.data = None
    newTree.left = None
    newTree.right = None




            
    


     
 






        
    


newTree = TreeNode(3)
newTree.left = TreeNode(4)
newTree.left.left = TreeNode(7)
newTree.left.right = TreeNode(10)
newTree.right = TreeNode(5)
newTree.right.right = TreeNode(8)

print("Preorder traversal")
preorder_traversal(newTree)

print("Inorder traversal")
inorder_traversal(newTree)

print("Postorder traversal")
postorder_traversal(newTree)

print("Levelorder traversal")
levelorder_traversal(newTree)

print("Searching an element in BT")
print(searchnode_BT(newTree,11))

print("Insert a node")
insertnode_BT(newTree,11)
levelorder_traversal(newTree)

print("delete node")
node = TreeNode(4)
deletenode_BT(newTree,node)
levelorder_traversal(newTree)

print("delete entire tree")
deleteentire_BT(newTree)
levelorder_traversal(newTree)




#Two types of traversal in BT
#Depth first search - 
# preorder  - Root , Left , Right
# inorder  - Left , Root , Right
# postorder - Left , right , root
#Breadth first search - level order











newTree = TreeNode("Drinks")










