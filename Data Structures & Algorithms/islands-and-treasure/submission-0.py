from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return grid
        m = len(grid)
        n = len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
        dist = 1
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                for c,d in ((0,-1),(0,1),(1,0),(-1,0)):
                    nx,ny = x+c,y+d
                    if nx>=0 and ny>=0 and nx<m and ny<n:
                        if grid[nx][ny]==2147483647:
                            grid[nx][ny]=dist
                            q.append((nx,ny))
            dist+=1
