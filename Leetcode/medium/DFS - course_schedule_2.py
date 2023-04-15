from collections import defaultdict
class Node:
    def __init__(self) -> None:
        self.dependent_courses = []
        self.indegree = 0



class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjacency_list = defaultdict(Node)
        total_dependencies = 0

        for course in prerequisites:
            curr_node = course[1]
            dependent_node = course[0]
            adjacency_list[curr_node].dependent_courses.append(dependent_node)
            adjacency_list[dependent_node].indegree += 1
            total_dependencies += 1

        no_dependency = []
       
        
        #add courses that are not a part of prerequisites
        for i in range(0,numCourses):
            if i not in adjacency_list:
                adjacency_list[i] = Node()

        #find 0 dependency course
        for course in adjacency_list:
           if adjacency_list[course].indegree == 0:
               no_dependency.append(course)
       
        #print the adjacency list
        # for i in adjacency_list:
        #     print(i, adjacency_list[i].dependent_courses,adjacency_list[i].indegree)
        
        
        removed_edges = 0
        topological_sort = []

        while no_dependency:
            node = no_dependency.pop()
            topological_sort.append(node)
            for i in adjacency_list[node].dependent_courses:
                adjacency_list[i].indegree -= 1
                removed_edges += 1
                if adjacency_list[i].indegree == 0:
                    no_dependency.append(i)

        if not removed_edges == total_dependencies:
            return []
        
        return topological_sort


      


sol = Solution()
numCourses = 5
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.findOrder(numCourses,prerequisites))
