#operations on singly linked list

#1. create head and tail and assign NULL reference to it
#2. Create node with data and NULL reference
#3. Point head and tail to that node

#Node class
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

#SSL class
class singly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    def insertSLL(self,value,location):
        newNode = Node(value)

        #if the SLL is empty , reference head and tail to this node
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
             #beginning of sll
            if location == 0: #Time complexity O(1)
                newNode.next = self.head #head stores first node physical location
                self.head = newNode
            #insert node at the end of SLL
            elif location == -1: #Time complexity O(1)
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            #insert node between two nodes
            else:
                tempNode =  self.head
                index = 0
                while (index < location -1): #Time complexity O(n)
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traverseSSL(self):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            temp = self.head
            while temp is not None:  #Time complexity - O(n)
                print(temp.value)
                temp = temp.next

    def searchSSL(self,value):
        if self.head is None:
            return ("the list is empty")
        else:
            temp = self.head
            while temp is not None: #Time complexity - O(n)
                if temp.value == value:
                    return("the element exits in the linked list")
                temp = temp.next
            return ("The element does not exist in the linked list")
        
    #delete a node from the linked list
    def deletenodeSSL(self,location):
        if self.head is None:
            return ("The SSL does not exist")
        else:
            #delete the first node
            if location == 0:
                #check if it is the only node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            #delete last node
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    while temp.next.next is not None:
                        temp = temp.next
                    temp.next = None
                    self.tail = temp
            #delete a node in between
            else:
                temp = self.head
                index = 0
                while index < location - 1: #Time complexity - O(n)
                    temp = temp.next
                    index += 1
                #find the node before the one needs to be deleted
                nextnode = temp.next
                temp.next = nextnode.next
                nextnode.next = None

    def deleteentireSSL(self):
        if self.head is None:  #Time complexity - O(1)
            return "List does not exist"
        else:
            self.head = None
            self.tail = None
        


#create linked list and nodes
singly_ll = singly_linked_list()
singly_ll.insertSLL(1,0)
singly_ll.insertSLL(2,-1)
singly_ll.insertSLL(4,-1)
singly_ll.insertSLL(5,-1)
singly_ll.insertSLL(3,2)
singly_ll.traverseSSL()
singly_ll.deletenodeSSL(3)
singly_ll.traverseSSL()
singly_ll.deleteentireSSL()
singly_ll.traverseSSL()



