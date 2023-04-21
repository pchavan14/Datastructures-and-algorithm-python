
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        visited = set()
        number_of_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    number_of_islands += 1      
                    path = self.recursive_dfs(grid,i,j,visited,"x",[])  
     
       

        return(number_of_islands)


    def recursive_dfs(self,grid,i,j,visited,direction,path):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0' or (i,j) in visited:
            return
        visited.add((i,j))
        self.recursive_dfs(grid,i+1,j,"r"visited)
        self.recursive_dfs(grid,i,j+1,"l"visited)
        self.recursive_dfs(grid,i-1,j,"d",visited)
        self.recursive_dfs(grid,i,j-1,"u",visited)
        
            

        

grid = [
  ["0","1","0","1","1"],
  ["1","1","1","0","0"],
  ["0","0","0","1","0"],
  ["0","0","1","1","1"]
]

#This can be implemented using dfs or bfs both of them
#Visit an isalnd and then keep on visited adjoining islands till we hit water
sol = Solution()
print(sol.numIslands(grid))