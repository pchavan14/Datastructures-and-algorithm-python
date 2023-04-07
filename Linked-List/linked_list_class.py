class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traversal(self):
        temp = self.head
        set = {temp.value}
        while temp:
            print(temp.value)
            temp = temp.next


ll = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(1)
node4 = Node(3)


ll.head = node1
ll.tail = node4
node1.next = node2
node2.next = node3
node3.next = node4

ll.traversal()

    
         