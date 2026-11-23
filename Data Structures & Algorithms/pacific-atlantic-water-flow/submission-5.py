class Solution:
    def dfs(self,i,j,prev,ocean,grid,heights):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 
        if grid[i][j][ocean]:
            return
        if heights[i][j]< prev:
            return
        grid[i][j][ocean]=True
        self.dfs(i,j-1,heights[i][j],ocean,grid,heights)
        self.dfs(i,j+1,heights[i][j],ocean,grid,heights)
        self.dfs(i-1,j,heights[i][j],ocean,grid,heights)
        self.dfs(i+1,j,heights[i][j],ocean,grid,heights)
        return
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        grid = [[[False,False] for j in range(n)] for i in range(m)]

        for i in range(0,n):
            self.dfs(0,i,heights[0][i],0,grid,heights)
            self.dfs(m-1,i,heights[m-1][i],1,grid,heights)
        
        for i in range(0,m):
            self.dfs(i,0,heights[i][0],0,grid,heights)
            self.dfs(i,n-1,heights[i][n-1],1,grid,heights)
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j][0] and grid[i][j][1]:
                    res.append([i,j])
        return res
        # return [[[i,j] if grid[i][j][0] and grid[i][j][1]] for j in range(n)] for i in range(m)]