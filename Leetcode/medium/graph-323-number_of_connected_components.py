from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = Graph()
        number_of_islands = 0
        visited = []

        for edge in edges:
            graph.adjacency_list[edge[0]].append(edge[1])
            graph.adjacency_list[edge[1]].append(edge[0])
            
        for node in graph.adjacency_list:
            if node not in visited:
                number_of_islands += 1
                self.bfs(graph,node,visited)
            
        print(number_of_islands)
        

    def bfs(self,graph,node,visited):
        custom_queue = deque()
        custom_queue.append(node)

        while custom_queue:
            deVertex = custom_queue.popleft()
            
            for edges in graph.adjacency_list[deVertex]:
                if edges not in visited:
                    visited.append(edges)
                    custom_queue.append(edges)



edges = [[0,1],[1,2],[3,4]]
sol = Solution()
sol.countComponents(5,edges)