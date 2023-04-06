class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def createdll(self,value):
        newnode = Node(value)
        newnode.prev = None
        newnode.next = None
        self.head = newnode
        self.tail = newnode
        print("The DLL is created")

    def insertdll(self,value,location):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                self.head.prev = newnode
                newnode.next = self.head
                self.head = newnode
            elif location == -1:
                self.tail.next = newnode
                newnode.prev = self.tail
                self.tail = newnode
            else:
                index = 0
                temp = self.head
                while index < location -1:
                    temp = temp.next
                    index += 1
                newnode.next = temp.next
                newnode.prev = temp
                temp.next.prev = newnode
                temp.next = newnode

    def traversedll(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def reversetraversedll(self):
        temp = self.tail
        while temp != None:
            print(temp.value)
            temp = temp.prev

    def searchdll(self,value):
        temp = self.head
        while temp != None:
            if temp.value == value:
                return "the element is present"
            temp = temp.next
        return "the element is not found"

doublyll = DLL()
doublyll.insertdll(1,0)
doublyll.insertdll(2,0)
doublyll.insertdll(3,1)
doublyll.insertdll(4,1)
#doublyll.traversedll()
doublyll.reversetraversedll()





