##Binary heap

#Binary heap is a binary tree with atmost two nodes
#Binary min heap and max heap , the key at root must be minimum of maximum among all keys present in the tree
#and the propoert is recursively true for all nodes
#binary heap is a complete tree (all levels are filled and the last level is left most) 
#Complete tree is suitable to be stored in an array
#Complete tree means all the levels of the trees should be filled first and then we move to the last level , because of this complete heap
#property the insertion into binary heap is O(LogN)


#Binary heap gives us the minimum or maxmium node is O(1) time complexity [peek] and extract is O(LogN) and insertion is O(LogN)

class Heap:
    def __init__(self,size):
        self.customList = (size + 1) * [None] #+1 because we are ignoring 0th index
        self.heapSize = 0 #O(1) time complexity and space complexity O(n)
        self.maxSize = size + 1

#peek method , return the min or max element
def peekofHeap(rootNode):
    if not rootNode:
        return None
    return rootNode.customList[1]

#size of heap - only the elements which are filled
def sizeofHeap(rootNode):
    if not rootNode:
        return None
    return rootNode.heapSize

#level order traversal
def levelorder(rootNode):
    if not rootNode:
        return
    else:
        ##the elements are in a list so we need to traverse the list
        for i in range(1,rootNode.heapSize + 1):
            print(rootNode.customList[i])
        

#heapfiy method for insertion
#index = index of the element which we want to heapify after addition , heap_type is min or max
def heapify_tree_insert(rootNode , index , heap_type):
    parent_index = index // 2 ##O(LogN) time complexity and space also will be O(LogN)
    if index <= 1:
        return
    if heap_type == "Min":
        if rootNode.customList[parent_index] > rootNode.customList[index]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parent_index]
            rootNode.customList[parent_index] = temp
        heapify_tree_insert(rootNode,parent_index,heap_type)
    elif heap_type == "Max":
        if rootNode.customList[parent_index] < rootNode.customList[index]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parent_index]
            rootNode.customList[parent_index] = temp
        heapify_tree_insert(rootNode,parent_index,heap_type)


def insertNode(rootNode,node_value,heap_type):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The heap is full"
    rootNode.customList[rootNode.heapSize + 1] = node_value
    rootNode.heapSize += 1
    heapify_tree_insert(rootNode,rootNode.heapSize,heap_type) #O(LogN) time complexity
    return "The value has been succesfull inserted"

#extract a node from binary heap
#only root can be extracted from heap
def heapify_tree_extract(rootNode,index,heap_type):
    left_child = 2 * index
    right_child = 2 * index + 1
    swap_child = 0

    #if the heap is empty
    if rootNode.heapSize < left_child:
        return
    #if last left node
    elif rootNode.heapSize == left_child:
        if heap_type == "Min":
            if rootNode.customList[index] > rootNode.customList[left_child]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[left_child]
                rootNode.customList[left_child] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[left_child]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[left_child]
                rootNode.customList[left_child] = temp
            return
    else:
        if heap_type == "Min":
            if rootNode.customList[right_child] > rootNode.customList[left_child]:
                swap_child = left_child
            else:
                swap_child = right_child
            if rootNode.customList[index] > rootNode.customList[swap_child]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swap_child]
                rootNode.customList[swap_child] = temp
        else:
            if rootNode.customList[right_child] > rootNode.customList[left_child]:
                swap_child = right_child
            else:
                swap_child = left_child
            if rootNode.customList[index] < rootNode.customList[swap_child]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swap_child]
                rootNode.customList[swap_child] = temp
        heapify_tree_extract(rootNode,swap_child,heap_type)

def extractNode(rootNode,heap_type):
    if rootNode.heapSize == 0:
        return None
    extractNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -=1
    heapify_tree_extract(rootNode,1,heap_type)
    return extractNode

new_heap = Heap(5)
insertNode(new_heap,20,"Min")
insertNode(new_heap,10,"Min")
insertNode(new_heap,30,"Min")
insertNode(new_heap,5,"Min")
levelorder(new_heap)

##heapQ module is python is used to create a binary heap or heapify an list when inserting and removing objects
print("Heap using heapq module")
import heapq

custom_list = []

#heappush pushes the element into the heap and maintain the heap invariant
#heappop returns the smallest element from the heap
heapq.heappush(custom_list,5)
heapq.heappush(custom_list,4)
print(heapq.heappushpop(custom_list,7))
print(custom_list[0])

#heapify method heapifies the given list
a = [10,4,2,3]
heapq.heapify(a)
print(a)




