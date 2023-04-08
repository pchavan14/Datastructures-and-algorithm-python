#enqueue - insert elements into the queue
#dequeue - remove elements from the queue
#is empty - method to check the queue
#peek - check the first element of the queue

class Queue:
    def __init__(self):
        self.queue = []

    def isempty(self):
        if len(self.queue) == 0:
            return True
        return False


    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        if not self.isempty():
            self.queue.pop(0)

    def peek(self):
        return self.queue[0]
    
    def traversal(self):
        for i in self.queue:
            print(i)


custom_queue = Queue()
custom_queue.enqueue(3)
custom_queue.enqueue(4)
custom_queue.enqueue(5)
custom_queue.traversal()
print("Dequeue the element")
custom_queue.dequeue()
custom_queue.traversal()
print("Peek the element")
print(custom_queue.peek())
print("After peeking the element")
custom_queue.traversal()


