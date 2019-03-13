class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.output = 0
        
        def dfs(row,col):
            if row<0 or col<0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
                return 0
                
            grid[row][col] = '#'
            down = dfs(row+1,col)
            up = dfs(row-1,col)
            right = dfs(row,col+1)
            left = dfs(row,col-1)
            
            self.output += 4 - left - right - up - down
            
            return 1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row,col)
                    break
                    
        return self.output

obj = Solution()
obj.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])