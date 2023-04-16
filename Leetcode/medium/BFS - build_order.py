# Build Order
# You are given a list of projects and a list of dependencies 
# (which is a list of pairs of projects, where the second project is dependent on the first project).
# All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

# projects a,b,c,d,e,f
# dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)

from collections import defaultdict
from collections import deque
class GraphNode:
   def __init__(self):
      self.dependent_nodes = []
      self.indegree = 0



def findBuildOrder(projects, dependencies):
    adjacency_list = defaultdict(GraphNode)
    total_dependencies = 0

    # create the adjacency list
    for project in dependencies:
       curr_project = project[0]
       dependent_project = project[1]
       adjacency_list[curr_project].dependent_nodes.append(dependent_project)
       adjacency_list[dependent_project].indegree += 1
       total_dependencies += 1

    no_dependency = deque()
    #add the nodes with no dependency
    for i in projects:
       if i not in adjacency_list:
          no_dependency.append(i)

    #find the nodes with 0 dependency
    for i in adjacency_list:
       if adjacency_list[i].indegree == 0:
          no_dependency.append(i)

    #variable to track the removed edges
    removed_edges = 0
    topological_sort = []

    while no_dependency:
       deVertex = no_dependency.popleft()
       topological_sort.append(deVertex)

       for i in adjacency_list[deVertex].dependent_nodes:
          adjacency_list[i].indegree -= 1
          removed_edges += 1
          if adjacency_list[i].indegree == 0:
             no_dependency.append(i)

    if removed_edges == total_dependencies:
       return topological_sort
    return False

        
       
    

    

       




    





project = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]
print(findBuildOrder(project,dependencies))
    








