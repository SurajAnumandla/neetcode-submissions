from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m = len(grid)
        n = len(grid[0])

        fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        time = 0     
        best = 0
        while q and fresh:
            for _ in range(len(q)):
                i,j = q.popleft()
                for di,dj in ((0,-1),(0,1),(-1,0),(1,0)):
                    ni,nj = i+di,j+dj
                    if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1:
                        grid[ni][nj]=0
                        fresh-=1
                        q.append((ni,nj))
            time+=1
        return -1 if fresh!=0 else time            