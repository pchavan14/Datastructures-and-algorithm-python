import heapq
#classes for edge
class edge:
    def __init__(self,weight,start,end):
        self.weight = weight
        self.start_vertex = start
        self.end_vertex = end

#Class for node
class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        #previous node that we come to this node
        self.predecessor = None
        #neighbors or nodes we can move to
        self.neighbors = []
        self.min_distance = float("inf")

    #Inbuilt function to check the minimum distance node
    def __lt__(self,other_node):
        return self.min_distance < other_node.min_distance
    
    def add_edge(self,weight,destination_vertex):
        edge = edge(weight,self,destination_vertex)
        self.neighbors.append(edge)

class dijsktra:
    def __init__(self):
        self.heap = []

    def calculate(self,start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap,start_vertex)
        while self.heap:
            #pop the minimum distance node from the heap
            actual_vertex = heapq.heappop(self.heap)

            #check all the neighbors for actual_vertex
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.end_vertex
                new_distance = start_vertex.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start

                    #update the heap
                    




