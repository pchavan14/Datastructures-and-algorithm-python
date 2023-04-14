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
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
    
    def BFS(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacent_vertices in self.adjacency_list[deVertex]:
                if adjacent_vertices not in visited:
                    visited.append(adjacent_vertices)
                    queue.append(adjacent_vertices)


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
custom_graph.print_graph()
custom_graph.BFS('A')


