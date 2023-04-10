#collections.deque class allows removing objects from either end in O(1) time complexity
#this is a double ended queue
#Best library to implement queue in python

#use the collections class to create a FIFO queue

from collections import deque

#create a queue with or without capacity
custom_queue = deque()


custom_queue.append(1)
custom_queue.append(2)

for i in custom_queue:
    print(i)

custom_queue.appendleft(3)

#when we specify the max length for the queue , the queue becomes a circular queue and start removing elements from the beginning
for i in custom_queue:
    print(i)




