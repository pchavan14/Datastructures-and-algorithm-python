from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        visited = []
        graph = Graph()

        for edge in edges:
            graph.adjacency_list[edge[0]].append(edge[1])
            graph.adjacency_list[edge[1]].append(edge[0])

        parent = {0:-1}
        stack = [0]

        while stack:
            popVertex = stack.pop()

            for edges in graph.adjacency_list[popVertex]:
                if edges == parent[popVertex]:
                    continue
                if edges in parent:
                    return False
                parent[edges] = popVertex
                stack.append(edges)

        print(stack)

                
                


n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
sol = Solution()
sol.validTree(n,edges)