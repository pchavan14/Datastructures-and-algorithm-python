from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        end_row = len(grid) - 1
        end_column = len(grid[0]) - 1
        end = (end_row,end_column)

        if grid[0][0] != 0 or grid[end_row][end_column] != 0:
            return -1
    
        visited = set()
        

        visited.add((0,0))
        return(self.bfs(grid,0,0,visited,end))


    def bfs(self,grid,row,col,visited,end):
        custom_queue = deque()
        custom_queue.append([(row,col)])
        
        while custom_queue:
            
            path = custom_queue.popleft()
            print(path)
            node = path[-1]
            row = node[0]
            col = node[1]
            if node == end:
               return len(path)
            
            for x , y in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
                xi = row + x
                yj = col + y
    
                
                if 0<=xi<len(grid) and 0<=yj<len(grid[0]) and grid[xi][yj] == 0 and (xi,yj) not in visited:
                    #print(xi,yj)
                    new_path = list(path)
                    new_path.append((xi,yj))
                    custom_queue.append(new_path)
                    visited.add((xi,yj))
                   

        return -1
            
    




        


        
                







#grid = [[0,0],[1,0]]
grid = [[0,0,0],[1,1,0],[1,1,0]]
sol = Solution()
print(sol.shortestPathBinaryMatrix(grid))
