from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        graph = Graph()

        for a , b in edges:
            graph.adjacency_list[a].append(b)
            graph.adjacency_list[b].append(a)

        #can use BFS
        visited = []
        custom_queue = deque()

        #add the source elements in both of them
        visited.append(source)
        custom_queue.append(source)

        while custom_queue:
            deVertex = custom_queue.popleft()
            if deVertex == destination:
                return True
            for edges in graph.adjacency_list[deVertex]:
                if edges not in visited:
                    visited.append(edges)
                    custom_queue.append(edges)

        return False
        
        

        
        
            
        


n = 3
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
sol = Solution()
print(sol.validPath(n,edges,source,destination))

