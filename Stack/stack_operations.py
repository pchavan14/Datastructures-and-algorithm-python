#stack creation using list
#remove from stack by using pop method
#always consider stack empty 
#peek - top peek on the top method but do not remove the element from stack
#isempty - to check element in  the stack

#implementing stack with dynamic list
class Stack:
    def __init__(self):
        self.list = []

    #empty method
    def isempty(self):
        if len(self.list) == 0: #Time complexity is O(1)
            return True
        return False
    
    def push(self,value):
        self.list.append(value)

    def pop(self):
        if not self.isempty(): #calling a function
            self.list.pop()

    def peek(self):
        return self.list[-1]

    def traverse(self):
        for i in self.list:
            print(i)

custom_stack = Stack()
custom_stack.push(3)
custom_stack.push(4)
custom_stack.push(5)
custom_stack.traverse()
print(custom_stack.isempty())
custom_stack.pop()
custom_stack.traverse()
print(custom_stack.peek())
custom_stack.traverse()

    






