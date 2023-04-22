from collections import defaultdict
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        #flat list
        flat_list = []
        for sublist in rooms:
            for item in sublist:
                flat_list.append(item)

        print(flat_list)
        
        graph = defaultdict(list)
        for i in range(len(rooms)):
            graph[i] = rooms[i]

        print(graph)
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
        
        
        if flat_list == visited:
            return True
        return False










rooms =  [[1],[1]]
sol = Solution()
print(sol.canVisitAllRooms(rooms))