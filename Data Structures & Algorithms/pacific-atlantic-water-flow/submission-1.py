class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m = len(heights)
        n = len(heights[0])
        po = 0
        ao = 1
        visited = [[[False,False] for j in range(n)]for i in range(m)]

        def dfs(i,j,prev,ocean):
            if i<0 or j<0 or i>=m or j>=n:
                return
            if heights[i][j]<prev:
                return
            if visited[i][j][ocean]:
                return

            visited[i][j][ocean] = True
            
            dfs(i,j-1,heights[i][j],ocean)
            dfs(i,j+1,heights[i][j],ocean)
            dfs(i-1,j,heights[i][j],ocean)
            dfs(i+1,j,heights[i][j],ocean)

        for i in range(n):
            dfs(0,i,heights[0][i],po)
            dfs(m-1,i,heights[m-1][i],ao)
        
        for i in range(m):
            dfs(i,0,heights[i][0],po)
            dfs(i,n-1,heights[i][n-1],ao)

        return [[i,j] for i in range(m) for j in range(n) if visited[i][j][0] and visited[i][j][1]]