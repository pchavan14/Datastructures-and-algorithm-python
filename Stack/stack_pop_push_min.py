class Stack:
    def __init__(self):
        self.list = []
        self.min = None

    def isempty(self):
        if len(self.list) == 0:
            return True
        return False
    
    def peek(self):
        if not self.isempty():
            return self.list[-1]
    
    def push(self,value):
        if not self.isempty():
            if value < self.peek():
                self.min = value
            else:
                self.min = self.peek()
        self.list.append(value)

    def pop(self):
        if not self.isempty():
            self.list.pop()

    def minimum(self):
        return self.min
    
    def traversal(self):
        for i in self.list:
            print(i)
    

stack = Stack()
print("Min element",stack.minimum())


