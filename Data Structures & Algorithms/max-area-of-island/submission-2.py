class Solution:
    def __init__(self):
        self.area = 0
        self.global_max = 0
    def dfs(self,i,j,grid):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 0
        if grid[i][j]==0:
            return 0
        grid[i][j]=0
        self.area+=1
        self.dfs(i,j-1,grid)
        self.dfs(i,j+1,grid)
        self.dfs(i-1,j,grid)
        self.dfs(i+1,j,grid)
        return 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.area = 0
                    self.dfs(i,j,grid)
                    self.global_max = max(self.global_max,self.area)
        return self.global_max