from collections import defaultdict
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        
        if len(connections) < n-1:
            return (-1)

        adjacency_list = defaultdict(list)
        visited = set()
        number_of_islands = 0
        
        for i in connections:
            adjacency_list[i[0]].append(i[1])
            adjacency_list[i[1]].append(i[0])
        
        
        for node in range(n):
            if node not in visited:
                self.bfs(adjacency_list,node,visited)             
                number_of_islands += 1
    

        return (number_of_islands - 1)



    def bfs(self,adjacency_list,node,visited):
        visited.add(node)
        custom_queue = []
        custom_queue.append(node)


        while custom_queue:
            deVertex = custom_queue.pop(0)
            for edge in adjacency_list[deVertex]:
                if edge not in visited:
                    visited.add(edge)
                    custom_queue.append(edge)
        






n = 6
connections =  [[0,1],[0,2],[0,3],[1,2]]
sol = Solution()
sol.makeConnected(n,connections)

