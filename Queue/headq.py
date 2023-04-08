import heapq

custom_heap = []

heapq.heappush(custom_heap,23)
heapq.heappush(custom_heap,0)
heapq.heappush(custom_heap,-1)


for i in custom_heap:
    print(i)

custom_list = [2,3,1,5,0,6,8]

heapq.heapify(custom_list)

#heapify the list 
print(custom_list)