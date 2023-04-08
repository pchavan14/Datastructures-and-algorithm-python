#Use a single list to implement n stacks

class MultiStack:
    def __init__(self,stack_size,number_of_stacks):
        self.number_of_stacks = number_of_stacks
        self.stack_size = stack_size
        self.custom_list = [0] * (self.number_of_stacks * self.stack_size)
        self.sizes = [0] * self.number_of_stacks

    def isFull(self,stacknum):
        if self.sizes[stacknum] == self.stack_size:
            return True
        return False
    
    def isempty(self,stacknum):
        if self.sizes[stacknum] == 0:
            return True
        return False
    
    def indexOfTop(self,stacknum):
        offset = stacknum * self.stack_size
        print("Offset",offset)
        for i in self.sizes:
            print("Sizes of stack",i)
        print("Index of the top",offset + self.sizes[stacknum] - 1)
        return offset + self.sizes[stacknum] - 1
    
    def push(self,item,stacknum):
        if self.isFull(stacknum):
            return "The stack is full"
        else:
            self.sizes[stacknum] += 1
            self.custom_list[self.indexOfTop(stacknum)] = item

    def pop(self,stacknum):
        if self.isempty(stacknum):
            return "The stack is empty"
        else:
            value = self.custom_list[self.indexOfTop(stacknum)]
            self.custom_list[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -=1
            return value
        
    def peek(self,stacknum):
        if self.isempty(stacknum):
            return "the stack is empty"
        else:
            value = self.custom_list[self.indexOfTop(stacknum)]
            return value
        
    def traversestack(self):
        for i in self.custom_list:
            print(i)
        
customstack = MultiStack(4,3)
customstack.push(3,0)
customstack.push(4,1)
customstack.traversestack()


