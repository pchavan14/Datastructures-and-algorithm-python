# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.


class Node:
    def __init__(self):
        self.indegree = 0
        self.dependent_courses = []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        from collections import defaultdict
        dependency_list = defaultdict(Node)
        total_dependencies = 0

        for preq in prerequisites:
            current = preq[1]
            dependent = preq[0]
            dependency_list[current].dependent_courses.append(dependent)
            dependency_list[dependent].indegree += 1
            total_dependencies += 1


       #check for nodependency nodes by using DFS , if you want to check for BFS create queue
        no_dependecy = []
        for i in dependency_list:
            if dependency_list[i].indegree == 0:
                no_dependecy.append(i)

        #total number of edges removes
        removed_edges = 0
 
        while no_dependecy:
            popVertex = no_dependecy.pop() #for BFS pop(0)
            for adjacent_vertices in dependency_list[popVertex].dependent_courses:
                    dependency_list[adjacent_vertices].indegree -= 1
                    removed_edges += 1
                    if dependency_list[adjacent_vertices].indegree == 0:
                        no_dependecy.append(adjacent_vertices)
                       
            
        return (removed_edges == total_dependencies)

     



sol = Solution()
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(sol.canFinish(numCourses,prerequisites))








