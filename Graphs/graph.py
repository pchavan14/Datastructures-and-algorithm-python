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
       
    def remove_edge(self,vertex1,vertex2):
        #In remove method of list we can pass element , in pop method we can only pass index
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list:
            for edge in self.adjacency_list[vertex]:
                self.adjacency_list[edge].remove(vertex)
            del self.adjacency_list[vertex]
          
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])


custom_graph = Graph()
custom_graph.add_vertex('A')
custom_graph.add_vertex('B')
custom_graph.add_vertex('C')
custom_graph.add_vertex('D')
custom_graph.add_edge('A','B')
custom_graph.add_edge('A','C')
custom_graph.add_edge('B','C')
custom_graph.print_graph()    
# custom_graph.remove_edge('A','B')
# custom_graph.remove_edge('C','D')
# print("After removing edges")
# custom_graph.print_graph()  

print("After removing the vertex")
custom_graph.remove_vertex('C')
custom_graph.print_graph()  

        



