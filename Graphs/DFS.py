#create a graph using dictionary (adjacency graph)
class Graph:
    def __init__(self):
      self.adjacency_list = {}

    def add_vertex(self,vertex):
       #check if vertex is in the dictionary
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    #undirected and unweighted 
    def add_edge(self,vertex1,vertex2):
        #vertices must be present in a graph before adding an edge between them
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            #self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
    
    def DFS(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacent_vertices in self.adjacency_list[popVertex]:
                if adjacent_vertices not in visited:
                    stack.append(adjacent_vertices)
                    visited.append(adjacent_vertices)


custom_graph = Graph()
custom_graph.add_vertex('2')
custom_graph.add_vertex('1')
custom_graph.add_vertex('0')
custom_graph.add_vertex('3')
custom_graph.add_vertex('4')
custom_graph.add_edge('2','1')
custom_graph.add_edge('1','0')
custom_graph.add_edge('4','0')
custom_graph.add_edge('3','4')
custom_graph.print_graph()
custom_graph.DFS('2')
