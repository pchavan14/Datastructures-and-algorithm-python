
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class singly_LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def createCSLL(self,value): #Time complexity = 1
        newnode = Node(value)
        newnode.next = newnode
        self.head = newnode
        self.tail = newnode
        return "CSLL has been created"
    
    def insertCSLL(self,value,location):
        newnode = Node(value)
        if self.head is None:          
            newnode.next = newnode
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next = self.head
                self.tail.next = newnode
                self.head = newnode
            elif location == -1:
                newnode.next = self.tail.next
                self.tail.next = newnode
                self.tail = newnode
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                nextNode = temp.next
                temp.next = newnode
                newnode.next = nextNode
                if temp == self.tail:
                    newnode.next = self.tail.next
                    self.tail.next = newnode
                    self.tail = newnode
    #traversal of circular single linked list
    def printCSLL(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp == self.tail.next:
                break

    def searchCSLL(self,value):
        temp = self.head
        while temp:
            if temp.value == value:
                return("found the element")
            temp = temp.next
            if temp == self.tail.next:
                break
        return("the element is not found")
    
    def deletionCSLL(self,location):
        if self.head is None:
            print("The linked list is empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.head = None
                    self.head.next = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.head = None
                    self.head.next = None
                else:
                    temp = self.head
                    while temp.next.next is not self.head:
                        temp = temp.next
                    temp.next = self.tail.next
                    self.tail = temp
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                #find the node before the one needs to be deleted
                nextnode = temp.next
                temp.next = nextnode.next
                nextnode.next = None

    

                




singlell = singly_LL()
singlell.createCSLL(1)
singlell.insertCSLL(2,0)
singlell.insertCSLL(3,-1)
singlell.insertCSLL(4,2)
singlell.printCSLL()
print(singlell.searchCSLL(4))
singlell.deletionCSLL(2)
singlell.printCSLL()