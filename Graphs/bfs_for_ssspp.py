from collections import deque
#create graph with adjacency list
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list:
            #The adjacency list contains the list of connected vertices
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def bfs(self,start,end):
        custom_queue = deque()
        custom_queue.append([start])

        while custom_queue:
            deVertex = custom_queue.popleft()
            node = deVertex[-1]
            if node == end:
                return deVertex 
            for vertices in self.adjacency_list.get(node,[]):
                new_path = list(deVertex)
                new_path.append(vertices)
                custom_queue.append(new_path)
            print(new_path)
                

custom_graph = Graph()
custom_graph.add_vertex('A')
custom_graph.add_vertex('B')
custom_graph.add_vertex('C')
custom_graph.add_vertex('D')
custom_graph.add_vertex('E')
custom_graph.add_vertex('F')
custom_graph.add_vertex('G')
custom_graph.add_edge('A','B')
custom_graph.add_edge('A','C')
custom_graph.add_edge('B','D')
custom_graph.add_edge('B','G')
custom_graph.add_edge('C','D')
custom_graph.add_edge('C','E')
custom_graph.add_edge('D','F')
custom_graph.add_edge('E','F')
custom_graph.add_edge('F','G')
print(custom_graph.bfs('A','E'))

    
