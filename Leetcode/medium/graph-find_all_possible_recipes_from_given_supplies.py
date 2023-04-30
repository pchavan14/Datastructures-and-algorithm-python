from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self):
        self.out_nodes = []
        self.indegree = 0


class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """

        adjacency_list = defaultdict(Graph)

        for i, value in enumerate(ingredients):
           for v in value:
               adjacency_list[v].out_nodes.append(recipes[i])
               adjacency_list[recipes[i]].indegree += 1

        no_dependency_nodes = deque()
        for key , node in adjacency_list.items():
            if key in supplies and node.indegree == 0:
                no_dependency_nodes.append(key)

        result = []
        while no_dependency_nodes:
            k = no_dependency_nodes.popleft()
            if k in recipes:
                result.append(k)
            for neighbor in adjacency_list[k].out_nodes:
                adjacency_list[neighbor].indegree -= 1
                if adjacency_list[neighbor].indegree == 0:
                    no_dependency_nodes.append(neighbor)

        print(result)
            

        
        
recipes = ["bread","sandwich"]
ingredients =[["yeast","flour"],["bread","meat"]]
supplies = ["yeast","flour","meat"]

sol = Solution()
sol.findAllRecipes(recipes,ingredients,supplies)