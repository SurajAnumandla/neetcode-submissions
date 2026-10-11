from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        q= deque()
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        while q and fresh:
            for a in range(len(q)):
                i,j = q.popleft()
                for x,y in ((-1,0),(1,0),(0,-1),(0,1)):
                    dx = i+x
                    dy = j+y
                    if (dx>=0 and dy>=0 and dx<m and dy<n and 
                    grid[dx][dy]==1):
                        grid[dx][dy]=2
                        fresh-=1
                        q.append((dx,dy))
            time+=1
        return time if fresh==0 else -1
