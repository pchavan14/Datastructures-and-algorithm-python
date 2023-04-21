
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
                    visited.add((i,j))
                    number_of_islands += 1      
                    self.recursive_dfs(grid,i,j,visited)       
       

        return(number_of_islands)
    
    def bfs(self,grid,i,j,visited):
        stack = []
        stack.append((i,j))
        while stack:
            i,j = stack.pop(0) #bfs
            for x , y in [(0,1),(1,0),(-1,0),(0,-1)]:
                xi = x + i
                yj = y + j
                if 0<=xi<len(grid) and 0<=yj<len(grid[0]) and grid[xi][yj] == '1' and (xi,yj) not in visited:
                    stack.append((xi,yj))
                    visited.add((xi,yj))

    def recursive_dfs(self,grid,i,j,visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        visited.add((i,j))
        self.recursive_dfs(grid,i+1,j,visited)
        self.recursive_dfs(grid,i,j+1,visited)
        self.recursive_dfs(grid,i-1,j,visited)
        self.recursive_dfs(grid,i,j-1,visited)
        
            

        

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