from collections import defaultdict
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

       
        
        graph = defaultdict(list)
        for i in range(len(rooms)):
            graph[i] = rooms[i]

        
        custom_stack = []
        custom_stack.append(0)
        visited = []


        while custom_stack:
            popVertex = custom_stack.pop()
            visited.append(popVertex)

            for rooms in graph[popVertex]:
                if rooms not in visited:
                    visited.append(rooms)
                    custom_stack.append(rooms)
        
        
        return len(visited) == len(rooms)










rooms =  [[1],[1]]
sol = Solution()
print(sol.canVisitAllRooms(rooms))